# Lab_Eletronica — ENE0046, Laboratório de Eletrônica (UnB, 2026/2)

Repositório de trabalho da disciplina: roteiros, simulações no LTspice, pré-relatórios
e relatórios em LaTeX.

Aluno: **Gabriel de Sousa** — matrícula **211056000** — Turma 04.

## Estrutura

```
LAB_1/                        Roteiro 1 — Simulação de circuitos (introdução ao LTspice)
  Gabriel/                    item_1..item_6 .asc + artefatos de simulação
  modelo-relatorio-ENE0046/   modelo LaTeX oficial da disciplina
  R1-simulacao-de-circuitos.pdf   roteiro
  relatorio1.pdf              relatório entregue
LAB_2/                        Roteiro 2 — Amplificador operacional
  item_1..item_5.asc          esquemáticos de entrega
  item_6.asy  item_7.asy      símbolos LM741 e TL064
  ene0046.lib                 macro-modelos SPICE fornecidos pela disciplina
  R2-amplificador-operacional.pdf   roteiro
  Imagens/                    capturas para o relatório
Lab.Eletronica_marina/        material da colega de equipe (roteiros 2 a 7, modelos)
```

Cada roteiro tem duas entregas: **simulação individual** (os `.asc`/`.asy`) e
**relatório em equipe** (LaTeX, uma ou duas semanas depois).

## Ferramentas

LTspice roda sob wine. Nunca chame `wine` direto, use o wrapper:

```bash
/home/ia/.local/bin/ltspice arquivo.asc      # abre na interface gráfica
/home/ia/.local/bin/ltspice -b arquivo.asc   # roda em batch, gera .raw e .log
/home/ia/.local/bin/ltspice -netlist a.asc   # só gera o .net, sem simular
```

Para fechar o LTspice use `WINEPREFIX=$HOME/.wine-ltspice wineserver -k`.
**Não** use `pkill -f LTspice.exe`: o padrão casa com a própria linha de comando do
shell e mata a sessão que executou o comando.

Os `.asy` e o `.lib` precisam estar na mesma pasta do `.asc` para o LTspice resolvê-los.

## Especificação por matrícula

Matrícula na forma `ABCDEFGHI`. Se `EF` ou `GH` der `00`, adote `80`.
Para 211056000: `EF = 56`, `GH = 00 → 80`, `I = 0`.

| grandeza | fórmula | valor |
|---|---|---|
| Ganho não inversor `G` | `4 + ((7·EF + 3·GH) mod 81)/10` | **10,5** |
| Pesos do somador | `k1 = 2 + (EF mod 4)`, `k2 = 6 + (GH mod 4)` | **k1 = 2, k2 = 6** |
| Ganho diferencial `Ad` | `2 + ((3·GH + 7·I) mod 90)/10` | **8** |

Restrições de componentes, verificadas em todo esquemático:

- resistores da **série E12** (1,0 1,2 1,5 1,8 2,2 2,7 3,3 3,9 4,7 5,6 6,8 8,2 ×10ⁿ)
- faixa **1 kΩ a 82 kΩ**
- no máximo **dois resistores em série por perna** da rede de realimentação
- alimentação simétrica de **±15 V** em todas as seções

Antes de entregar, rode a auditoria: extraia todo `SYMATTR Value` de símbolo `res` e
confira contra a lista E12. Valor E24 (16k, 20k, 24k, 30k…) reprova no critério.

## Regras de correção — o que a disciplina avalia

Critérios do roteiro, na ordem em que costumam custar ponto:

1. **Símbolo com atributos corretos e terminais na ordem do subcircuito.**
   `Prefix = X`, `ModelFile = ene0046.lib`, `Value = LM741` ou `TL064`.
   `SpiceModel` **não** serve. Ordem trocada compila, simula sem reclamar e devolve
   resultado errado — é o erro que mais reprova.
2. **Componentes E12** que realizam a especificação da matrícula.
3. **Nós nomeados de forma descritiva** (`vout_diferencial`, `no_soma`), nunca `N001`.
4. **Diretivas gravadas como SPICE directive**, não como comentário.
5. **Nome e matrícula anotados no esquemático como Comment.**
6. **Uma única diretiva de análise ativa por arquivo.** Mesmo circuito em dois arquivos:
   copie, troque a diretiva, salve com o novo nome.
7. **Saturação prevista analiticamente e confirmada** em simulação e em bancada.
8. **Cada divergência entre projeto, simulação e medição recebe causa apontada.**
   Não basta relatar o desvio, tem que dizer de onde veio.

Ordem de terminais das duas peças de `ene0046.lib` — elas **não** são iguais:

| terminal | LM741 (`item_6.asy`) | TL064 (`item_7.asy`) |
|---|---|---|
| entrada não inversora | SpiceOrder 1 | SpiceOrder 3 |
| entrada inversora | 2 | 1 |
| V+ | 3 | 4 |
| V− | 4 | 5 |
| saída | 5 | 2 |

## Padrão visual dos esquemáticos

Padrão estabelecido nos itens 1 a 5 do LAB_2. Reproduza em qualquer arquivo novo.

- Comentário com **nome, matrícula e descrição do item no topo** (`TEXT 64 -48`).
- **Diretivas na faixa inferior esquerda**, sem encostar em componente.
- Realimentação desenhada como **laço retangular acima do amplificador**, nunca
  passando por cima ou por baixo dele.
- **VCC e VEE em fios horizontais curtos** saindo dos pinos de alimentação, com o
  rótulo na ponta. Fio vertical longo com texto girado 90° polui e cruza a
  realimentação.
- `InstName` e `Value` do amplificador **acima do símbolo**
  (`WINDOW 0 -8 -16 Left 2` / `WINDOW 3 -8 8 Left 2`). Na posição padrão eles caem
  exatamente na altura dos rótulos VCC/VEE.
- Resistores horizontais usam `WINDOW 0 0 56 VBottom 2` e `WINDOW 3 58 59 VCenter 2`,
  que põem a referência acima e o valor abaixo do corpo.
- `InstName` das fontes deslocado para baixo-direita (`WINDOW 0 48 48 Left 2`), senão
  encosta no nome do nó de entrada.
- Alimentação simétrica **agrupada numa região separada**, com legenda própria.
- Vários circuitos no mesmo arquivo: **empilhe em linhas**, uma descrição `;(a)`,
  `;(b)` acima de cada bloco. Comprimir tudo na horizontal reduz o zoom-to-fit e faz
  os textos colidirem.
- Deixe **pelo menos 96 px** entre o rótulo de uma fonte e o valor do resistor vizinho.

### Alimentação negativa

Não existe fonte de −15 V: use uma fonte de `15` **invertida**, com o terminal `+`
no terra e o `−` no nó VEE.

```
SYMBOL voltage 1424 720 R0
SYMATTR InstName Vneg
SYMATTR Value 15
FLAG 1424 736 0        <- pino + (Y+16)
FLAG 1424 816 VEE      <- pino - (Y+96)
```

## Geometria do formato .asc — as armadilhas

Coordenadas de pino são **relativas ao ponto de colocação** do `SYMBOL`. Errar por
16 px gera nó solto que o LTspice **não reporta como erro**.

| símbolo | pinos (offset a partir do ponto de colocação, rotação R0) |
|---|---|
| `res` | `(16, 16)` e `(16, 96)` — **não** `(16, 0)` |
| `voltage` | `(0, 16)` = `+` e `(0, 96)` = `−` |
| `item_6` / `item_7` | In+ `(-32, 80)`, In− `(-32, 48)`, V+ `(0, 32)`, V− `(0, 96)`, OUT `(32, 64)` |

Rotação `R90` mapeia `(x, y) → (−y, x)`. Um `res` em `R90` colocado em `(X, Y)` fica
com pinos em `(X−16, Y+16)` e `(X−96, Y+16)`.

Três modos de falha silenciosa:

1. **Fio curto demais.** Se o fio termina 16 px antes do pino, o netlist mostra
   `R4d NC_01 0 12k` — nó desconectado, simulação roda e o resultado é errado.
2. **Fio vertical atravessando outro pino.** Um fio de x=768 descendo até y=320 toca
   a entrada não inversora do amplificador e curto-circuita as entradas, sem erro.
   Sempre pare o fio no pino de destino, nunca depois dele.
3. **Pino sobre fio conecta.** Um pino que cai no meio de um segmento de fio fica
   ligado nele. Útil de propósito, perigoso por acidente — confira o `.net`.

## Processo de verificação obrigatório

Netlist limpo **não** significa esquemático bom, e esquemático bonito não significa
circuito certo. Sempre os dois:

```bash
cd /tmp/…/scratchpad          # trabalhe numa cópia, não suje o diretório do projeto
/home/ia/.local/bin/ltspice -netlist item_N.asc && cat item_N.net
/home/ia/.local/bin/ltspice -b       item_N.asc && tail item_N.log
```

No `.net`, confira nesta ordem:

- nenhum nó `NC_xx`
- a linha `X§U…` com os nós na ordem do `.SUBCKT` da peça
- valores dos resistores e as somas em série
- nós com nome descritivo, sem `N00x` em ponto importante

Depois abra na interface e **olhe a captura**:

```bash
/home/ia/.local/bin/ltspice item_N.asc &
xwininfo -root -tree | grep "LTspice -"        # pega geometria da janela
ffmpeg -y -f x11grab -video_size LxA -i :0.0+X,Y -frames:v 1 saida.png
```

`xwd -silent -id <ID>` devolve imagem em branco sob o compositor do GNOME; capture a
região da tela pelo `x11grab` usando a geometria que o `xwininfo` informou.
Para esperar a janela abrir sem `sleep`, use `ffmpeg -re -f lavfi -i "nullsrc=d=15" -f null -`.

Se houver qualquer colisão de texto, corrija e **repita o ciclo**. Duas ou três
rodadas por arquivo é o normal.

### Lendo o `.raw` sem abrir a GUI

Cabeçalho pode vir em UTF-16LE. Em transiente, a primeira variável (tempo) é `float64`
e as demais são `float32`; em `.op` e `.dc` costuma ser tudo `float64`. Com `.step`,
as rodadas vêm concatenadas — separe onde o tempo decresce.

## Relatório em LaTeX

Modelo oficial em `LAB_1/modelo-relatorio-ENE0046/modelo-relatorio/`.
Compile sempre `modelo-relatorio.tex` (o `estilo-relatorio.tex` é um pedaço dele e não
compila sozinho). Os três arquivos, mais `logo-unb.png`, ficam na mesma pasta.

```bash
latexmk -pdf modelo-relatorio.tex
```

O relatório traz a simulação de projeto **de cada integrante**, a montagem em bancada
com os valores medidos dos componentes, a simulação da montagem e a medição.
Use `relatorio1.pdf` (LAB_1) como referência de estrutura, profundidade e tom.

Instrumentos da bancada: fonte E3631A, gerador 33220A, osciloscópio DSO1002A,
multímetro 34401A.

## Git

- **Nunca** rode comando git por iniciativa própria. Exige pedido explícito, a cada vez.
- Isso inclui `commit` local.
- Operação com o remoto (`fetch`, `pull`, `push`) exige confirmação separada e explícita,
  mesmo quando o commit local já foi autorizado.
- Commits por escopo, nunca tudo junto.
