# AGENTS.md

Repositório da disciplina **ENE0046 — Laboratório de Eletrônica** (UnB, 2026/2).
Aluno: Gabriel de Sousa, matrícula 211056000, Turma 04.

**As regras completas de trabalho estão em [`CLAUDE.md`](./CLAUDE.md). Leia esse
arquivo antes de editar qualquer coisa.** Este arquivo existe só para agentes que não
carregam `CLAUDE.md` automaticamente, e repete o mínimo indispensável.

## O que se faz aqui

Simulações no **LTspice** (rodando sob wine) e relatórios em **LaTeX**. Cada roteiro
tem duas entregas: os arquivos `.asc`/`.asy` da simulação individual, e o relatório em
equipe.

## Mínimo indispensável

1. **LTspice pelo wrapper:** `/home/ia/.local/bin/ltspice` — `-b` para batch,
   `-netlist` para só gerar o `.net`. Fechar com
   `WINEPREFIX=$HOME/.wine-ltspice wineserver -k`, nunca com `pkill -f LTspice.exe`.
2. **Resistores só da série E12**, entre 1 kΩ e 82 kΩ, no máximo dois em série por
   perna. Valor E24 (16k, 20k, 24k…) perde ponto.
3. **A ordem de terminais do LM741 e do TL064 é diferente.** Trocar a ordem compila,
   simula sem reclamar e devolve resultado errado. Confira sempre a linha `X§U…` do
   netlist contra o cabeçalho do `.SUBCKT` em `ene0046.lib`.
4. **Uma única diretiva de análise ativa por arquivo.** Nós com nome descritivo. Nome e
   matrícula como Comment no desenho.
5. **Pinos do formato `.asc` têm offset:** `res` em `(16,16)` e `(16,96)`, `voltage` em
   `(0,16)` e `(0,96)`. Errar por 16 px cria nó solto que o LTspice não reporta.
6. **Validar sempre em dois níveis:** ler o `.net` gerado **e** abrir na interface e
   inspecionar a captura de tela. Netlist limpo não garante esquemático legível, e
   esquemático bonito não garante circuito certo.
7. **Trabalhe em cópia** num diretório temporário. `.net`, `.raw`, `.op.raw` e `.log`
   são artefatos de teste e não voltam para o diretório do projeto.

## Git

Nunca rode git por iniciativa própria — nem `commit` local. Cada operação exige pedido
explícito. Operação com o remoto exige confirmação separada, mesmo com o commit local
já autorizado. Commits por escopo, nunca tudo junto.
