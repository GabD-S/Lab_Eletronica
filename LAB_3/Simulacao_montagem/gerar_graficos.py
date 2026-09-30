from pathlib import Path
import re,json,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
parser=argparse.ArgumentParser(description="Gera gráficos da montagem a partir dos .raw do LTspice.")
parser.add_argument("dados",type=Path,help="Pasta temporária com os resultados dos sete circuitos")
parser.add_argument("saida",type=Path,help="Pasta de destino dos gráficos")
args=parser.parse_args()
BASE=args.dados
OUT=args.saida
OUT.mkdir(parents=True,exist_ok=True)
def raw(name):
 b=(BASE/(name+'.raw')).read_bytes();enc='utf-16-le' if b[1]==0 else 'utf-8';mark='Binary:\n'.encode(enc);p=b.index(mark);h=b[:p].decode(enc);buf=b[p+len(mark):]
 names=re.findall(r'^\s*\d+\s+(\S+)\s+\S+',h,re.M);n=len(names);count=int(re.search(r'No. Points:\s+(\d+)',h)[1])
 if 'complex' in h:a=np.frombuffer(buf,dtype='<c16').reshape(count,n)
 elif len(buf)==count*(8+4*(n-1)):
  dt=np.dtype([('t','<f8'),('v','<f4',(n-1,))]);v=np.frombuffer(buf,dtype=dt);a=np.column_stack([v['t'],v['v']])
 else:a=np.frombuffer(buf,dtype='<f8').reshape(count,n)
 return dict(zip(names,a.T))
m={}
for file,node in [('montagem_offset','vout_offset'),('montagem_bias_lm741','vout_bias'),('montagem_offset_tl064','vout_offset'),('montagem_bias_tl064','vout_bias_tl064')]:m[file]=float(raw(file)[f'V({node})'][0])
m['Gcalc_baixo']=1+9.98/1.03;m['Gcalc_alto']=1+99.97/1.03;m['vos_sim']=m['montagem_offset']/m['Gcalc_alto'];m['ib_sim']=(m['montagem_bias_lm741']-m['montagem_offset'])/(m['Gcalc_alto']*98.9e3)
a=raw('montagem_frequencia');f=a['frequency'].real
plt.rcParams.update({'font.size':11,'figure.dpi':180,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(9,4.8),layout='constrained')
for k,col,n in [(1,'#1365a5','baixo'),(2,'#c45c16','alto')]:
 g=np.abs(a[f'V(vout_g{k})']/a['V(vin_ac)']);db=20*np.log10(g);target=db[0]-20*np.log10(np.sqrt(2));i=np.flatnonzero(db<=target)[0];fc=10**np.interp(target,db[i-1:i+1][::-1],np.log10(f[i-1:i+1])[::-1]);m['G_'+n]=float(g[0]);m['fc_'+n]=float(fc);m['gbw_'+n]=float(fc*g[0]);ax.semilogx(f,db,color=col,label=f'Simulação: ganho {n}, fc = {fc/1e3:.2f} kHz');ax.plot(fc,target,'s',color=col)
fb=np.array([100,1e4,4e4,6e4,7e4,91e3,110e3,300e3]);gb=np.array([2.05,2.03,1.89,1.58,1.64,1.48,1.32,.59])/np.array([.18103,.1808,.1821,.18267,.1826,.1829,.1821,.181])
fa=np.array([100,2000,5000,9900,50000]);ga=np.array([1.95,1.93,1.86,1.48,.57])/np.array([.01983,.01982,.01989,.0178,.01972])
ax.semilogx(fb[:3],20*np.log10(gb[:3]),'o',color='#1365a5',label='Bancada: ganho baixo, senoide');ax.semilogx(fb[3:],20*np.log10(gb[3:]),'^',mfc='none',color='#1365a5',label='Bancada: ganho baixo, triangular');ax.semilogx(fa,20*np.log10(ga),'o',color='#c45c16',label='Bancada: ganho alto')
# Ajuste ao módulo normalizado; Gref fixado pela medida de 100 Hz.
candidates=np.linspace(10000,20000,100001);err=((ga[1:,None]/ga[0]-1/np.sqrt(1+(fa[1:,None]/candidates)**2))**2).sum(axis=0);fit=float(candidates[err.argmin()]);m['fc_ajuste_alto']=fit;m['gbw_ajuste_alto']=float(fit*ga[0]);m['cortes_ponto_alto']=(fa[1:]/np.sqrt((ga[0]/ga[1:])**2-1)).tolist();m['ganhos_bancada_baixo']=gb.tolist();m['ganhos_bancada_alto']=ga.tolist()
xf=np.geomspace(100,3e5,200);ax.semilogx(xf,20*np.log10(ga[0]/np.sqrt(1+(xf/fit)**2)),':',color='#c45c16',label=f'Ajuste de um polo à bancada: fc ≈ {fit/1e3:.2f} kHz')
ax.set(xlabel='Frequência (Hz)',ylabel='Ganho (dB)',xlim=(80,1e6),ylim=(-3,45),title='Montagem: simulação com resistores medidos e dados de bancada');ax.grid(True,which='both',alpha=.2);ax.legend(fontsize=8,loc='lower left');fig.savefig(OUT/'montagem_frequencia.png');plt.close(fig)
fig,axes=plt.subplots(2,1,figsize=(9,6.4),layout='constrained')
for ax,part,freq,suffix in zip(axes,['lm741','tl064'],[39700,447000],['','_tl064']):
 a=raw('montagem_slew_'+part);t=a['time'];cut=np.where(np.diff(t)<0)[0][0]+1;t=t[cut:];v=a[f'V(vout_seguidor{suffix})'][cut:];vi=a[f'V(vin_seguidor{suffix})'][cut:];mask=t>=8/freq;ax.plot(t[mask]*1e6,vi[mask],'--',color='#777777',label='Entrada');ax.plot(t[mask]*1e6,v[mask],color='#1365a5',label='Saída simulada')
 for sign,label in [(1,'subida'),(-1,'descida')]:
  ix=np.flatnonzero((t>9/freq)&(t<10/freq)&(abs(v)<.2)&(np.gradient(v,t)*sign>0));groups=np.split(ix,np.where(np.diff(ix)>1)[0]+1);ix=max(groups,key=len);slope,intercept=np.polyfit(t[ix],v[ix],1);m['sr_'+part+'_'+label]=float(slope/1e6);ax.plot(t[ix]*1e6,v[ix],color='#c45c16',lw=3)
 ax.set(xlabel='Tempo (µs)',ylabel='Tensão (V)',title=f'{part.upper()} — {freq/1000:g} kHz; Vp = 2 V');ax.grid(alpha=.2);ax.legend(loc='lower right',fontsize=9)
fig.suptitle('Simulação nas frequências registradas no ensaio de slew rate');fig.savefig(OUT/'montagem_slew.png');plt.close(fig)
print(json.dumps(m,indent=2))
