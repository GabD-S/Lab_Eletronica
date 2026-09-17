# Estado após revisão final dos arquivos — 17/09/2026

Os seis `.asc` revisados estão em `Simulacoes/`. Todos foram executados em cópia temporária, sem erros ou avisos, e seus desenhos foram inspecionados no LTspice. Os netlists não contêm nós automáticos nem pinos desconectados. Símbolos e biblioteca originais foram preservados.

- Itens 1, 2, 3 e 5: nós automáticos substituídos por nomes descritivos.
- Item 4: Gear, passo máximo T/1000, cshunt=0.01f, sem compressão. Saída senoidal limpa a 5 kHz e triangular a 100 kHz. Inclinações centrais próximas de ±0,325 V/µs.
- Item 6: Gear, passo máximo T/1000, sem cshunt e sem compressão. Saída senoidal a 50 kHz e aproximadamente triangular a 500 kHz. Inclinações centrais próximas de ±3,493 V/µs.
- Item 5: mantido conforme o roteiro; comentário explicita a corrente DC praticamente nula do macromodelo fornecido.

O LM741 fornecido tem slew rate diferente do típico de 0,5 V/µs do datasheet. Uma estimativa a partir do estágio interno é G1 × R3 × I1 / C3 = 2,1 mS × 517 Ω × 100 µA / 333,33 pF ≈ 0,326 V/µs, coerente com a simulação. Variar a capacitância numérica entre 0,01 fF, 0,1 fF e 1 fF manteve a rampa em aproximadamente 0,325 V/µs. Não se alterou o modelo para forçar o valor típico. Essa diferença foi anotada no próprio item 4 e deve ser explicada na análise posterior.

As pendências de montagem, ondulação e assimetria descritas na auditoria inicial abaixo foram tratadas. Permanecem as limitações do modelo LM741 quanto ao típico de datasheet e do TL064 quanto à corrente DC, explicitadas nos arquivos. A aprovação e a interpretação da tolerância pelo professor não podem ser garantidas. A entrega atual consiste nos arquivos; bancada e relatório são etapas posteriores.

Veja [ENTREGA.md](ENTREGA.md) para os campos do portal. O ZIP contém somente os seis `.asc`, os dois `.asy` e `ene0046.lib`.

---

# Histórico: auditoria anterior às correções

Os resultados e pendências abaixo descrevem a versão anterior, não os arquivos finais revisados.

# Verificação do Roteiro 3 — 17/09/2026

Fonte: [R3-nao-idealidades.pdf](R3-nao-idealidades.pdf), seções 2 a 5. Escopo: os arquivos atuais de `Simulacoes/`. Os esquemáticos e modelos não foram alterados nesta auditoria. Simulações e ensaios auxiliares ficaram em `/tmp/lab3-auditoria` e `/tmp/lab3-layout`.

**Conclusão: a estrutura dos seis circuitos está correta, mas ainda não é possível declarar todos os requisitos cumpridos.** Há nós sem nomes descritivos, resultados analíticos sem registro prévio, problemas na demonstração de slew rate e uma limitação do modelo TL064 para corrente de polarização. Não há registros de bancada nem relatório no LAB_3.

## Especificação individual e requisitos comuns

Matrícula 211056000: EF = 56, GH = 00 → 80, I = 0. Portanto:

- G1 = 20 + (56 mod 21) = 34.
- G2 = 80 + (80 mod 41) = 119.
- Vp = 2 + I/2 = 2 V.

| Requisito | Verificação |
|---|---|
| Seis arquivos, item_1.asc a item_6.asc | Cumprido |
| Uma análise ativa por arquivo | Cumprido: .op, .op, .ac, .tran, .op, .tran |
| .step nos dois ensaios de slew rate | Cumprido; .step e .options não são análises adicionais |
| Nome e matrícula como comentários; análises como diretivas | Cumprido |
| Alimentação simétrica ±15 V | Cumprido, inclusive polaridade de Vneg |
| Resistores E12 de 1 kΩ a 100 kΩ | Cumprido. Este é o limite específico do R3, apesar do limite antigo de 82 kΩ em CLAUDE.md |
| No máximo dois resistores em série por perna | Cumprido |
| Símbolos do Roteiro 2 | Cumprido: LM741.asy e TL064.asy são idênticos aos respectivos símbolos de LAB_2 |
| Biblioteca local, referenciada sem caminho absoluto | Cumprido |
| Ordem de terminais dos subcircuitos | Cumprido para ambos os modelos |
| Sem pinos desconectados | Nenhum NC_xx nos netlists verificados |
| Nós com nomes descritivos | **Pendente:** nó inversor N001 nos itens 1, 2 e 5; junção entre Rf2a e Rf2b no item 3 também recebe N001 |
| Legibilidade dos esquemáticos | Conferida pelas capturas do LTspice; itens 2–6 reorganizados na tarefa anterior |
| Simulações executáveis | As seis análises originais concluíram; isso não garante, por si só, adequação dos resultados |

## Verificação por item

### Item 1 — seção 2.1: offset do LM741

Circuito correto: Rf = 100 kΩ, Rg = 1 kΩ, entrada não inversora aterrada, ganho nominal 101 e análise .op.

Resultado extraído: Vo = 0,111131 V; pela expressão do roteiro, Vos = Vo/101 = **1,1003 mV**. É próximo do valor típico de 1 mV e inferior ao máximo de 5 mV da tabela do LM741 a 25 °C. A simulação usa 27 °C por padrão. Fonte: [datasheet TI LM741, tabela 6.5](https://www.ti.com/lit/ds/symlink/lm741.pdf).

O resultado e a comparação não estavam registrados no LAB_3; ficam registrados nesta auditoria. A medida Vo/101 inclui o efeito da corrente na entrada inversora através de Rf; deve ser identificada como a estimativa prescrita pelo roteiro, não como uma extração isolada do offset intrínseco.

### Item 2 — seção 2.2: corrente de polarização do LM741

Circuito correto: mesmo ganho, com Rs = 100 kΩ na entrada não inversora, análise .op.

Vo = −0,472875 V; ΔVo = −0,584006 V. Pela convenção ΔVo = Vo_com_Rs − Vo_sem_Rs, ΔVo/(101 Rs) = **−57,82 nA**. A magnitude é 57,82 nA; a corrente física entra no terminal não inversor, produzindo tensão negativa sobre Rs. A corrente diretamente extraída do terminal é aproximadamente 57,85 nA.

A comparação com o típico de 80 nA do datasheet requer cuidado: o procedimento estima a corrente da entrada não inversora, enquanto o parâmetro usual Ib representa a média das correntes nas duas entradas. O modelo fornece aproximadamente 101,87 nA na inversora, resultando em média de 79,86 nA. Não é correto reprovar a corrente de 57,82 nA apenas por compará-la diretamente com 80 nA.

Pendente: nome descritivo no nó inversor; incorporar cálculo, sinal e comparação à documentação final.

### Item 3 — seção 2.3: resposta em frequência

Cumpre: dois amplificadores no mesmo arquivo, mesma fonte AC 1, resistores E12, ganhos nominais 34 e 119, varredura `.ac dec 50 10 10meg`.

Resultados extraídos com interpolação logarítmica no ponto de queda de 1/√2 em relação ao ganho a 10 Hz:

| Estágio | Ganho a 10 Hz | Corte | Produto ganho × corte |
|---|---:|---:|---:|
| G1 | 33,995 | 29,58 kHz | 1,006 MHz |
| G2 | 118,933 | 8,402 kHz | 0,999 MHz |

Os ganhos diferem dos nominais em menos de 0,1%; os produtos diferem entre si em aproximadamente 0,63%. São coerentes com um produto ganho-banda de aproximadamente 1 MHz.

Pendente: nomear a junção dos dois resistores em série e registrar as curvas/resultados para a documentação final.

### Item 4 — seção 2.4: slew rate do LM741

Configuração correta: seguidor, Vp = 2 V, frequências de 5 kHz e 100 kHz, dez períodos em cada passo. O limite calculado com SR típico de 0,5 V/µs é **39,79 kHz**; o comentário existente está correto. Fonte: [datasheet TI LM741](https://www.ti.com/lit/ds/symlink/lm741.pdf).

**Resultado ainda não aprovado:** em 5 kHz, a saída apresenta ondulações rápidas sobre a senoide e alcança cerca de −2,297 a +2,336 V nos últimos cinco períodos. Em 100 kHz, a saída fica arredondada, com inclinação máxima de aproximadamente 0,317 V/µs; nos trechos centrais, aproximadamente ±0,302 V/µs. Isso não demonstra de forma convincente a rampa triangular pedida, nem concorda em 15% com o típico de 0,5 V/µs.

É necessário investigar o comportamento do modelo e das opções numéricas antes de fechar a entrega. O arquivo usa `trtol=20`. Um ensaio auxiliar com Gear, trtol=1 e passo menor não eliminou totalmente a ondulação; portanto, não se atribui aqui uma causa conclusiva nem se afirma que trocar uma opção resolve o problema.

### Item 5 — seção 2.2: corrente de polarização do TL064

Circuito e .op corretos. **A extração pedida está limitada pelo modelo fornecido.**

Foi simulado, somente em cópia temporária, o circuito de referência sem Rs usando também TL064. Não se deve subtrair o offset do LM741 do resultado com TL064.

As duas saídas do TL064 foram aproximadamente 2,702600 mV e indistinguíveis na precisão dos dados gravados. A corrente diretamente extraída da entrada é da ordem de 1,5×10⁻²³ A, numericamente desprezível. O modelo recebe os sinais de entrada através de fontes controladas e capacitores, sem reproduzir uma corrente DC de polarização realista nesses terminais.

Consequência: a subtração fornece zero na resolução disponível e não permite uma razão finita e fisicamente útil entre as correntes dos dois amplificadores. Isso deve ser documentado como limitação do macromodelo; não representa uma medida da corrente real do componente. Não se deve alterar a biblioteca fornecida para forçar concordância.

Pendente também: nome descritivo no nó inversor.

### Item 6 — seção 2.4: slew rate do TL064

Configuração correta: seguidor, Vp = 2 V, frequências diferentes das do LM741 (50 e 500 kHz), dez períodos, método Gear. O limite calculado com SR típico de 3,5 V/µs é **278,52 kHz**. Fonte: [datasheet TI TL06xx](https://www.ti.com/lit/ds/symlink/tl064.pdf).

Em 50 kHz, a saída acompanha a senoide com amplitude próxima de 2 V. Em 500 kHz, apresenta trechos aproximadamente lineares e assimetria entre subida e descida.

**Comparação quantitativa pendente:** nos trechos próximos de zero dos últimos dois períodos, as medianas das inclinações são aproximadamente +4,25 e −3,07 V/µs. A subida fica cerca de 21% acima de 3,5 V/µs. Esses números são estimativas locais extraídas das amostras, não uma medição final por cursores; é necessário selecionar trechos representativos, registrar ambos os sentidos e explicar a assimetria antes de declarar conformidade com a tolerância do roteiro. O critério também cita concordância com o modelo, não apenas com um típico de datasheet.

## Bancada — seções 3.1 a 3.8

**Não verificável pelos arquivos atuais:** não há registros de medições de bancada no LAB_3. Isso significa ausência de evidência no repositório, não prova de que os ensaios não foram realizados.

| Seção | O que deve existir para considerar cumprida |
|---|---|
| 3.1 — equipe e componentes | Número da equipe; ganho baixo e Vp da tabela correspondente; ganho alto 101; um resistor por perna, dentre os valores disponíveis; valores medidos antes de montar |
| 3.2 — montagem | Pinagem física correta, ±15 V, desacoplamento de 100 nF em cada alimentação, terra comum, gerador configurado para alta impedância |
| 3.3 — offset | Vo e Vos; comparação com datasheet; ajuste por potenciômetro de 10 kΩ entre pinos 1 e 5 do LM741 com cursor em V−; tensão residual; repetição com outro amplificador sem ajuste |
| 3.4 — polarização | Duas leituras para cada componente, com e sem Rs; ΔVo, corrente e sentido; comparação LM741/TL064 e explicação da diferença |
| 3.5 — frequência | Referência a 100 Hz; saída de 200 mV de pico no ganho baixo e 1 V no ganho 101; 6–8 frequências por ganho, 3–4 perto do corte e outras até uma década acima; gráfico com eixo logarítmico, dois cortes e dois produtos ganho-banda; justificar amplitudes baixas |
| 3.6 — slew rate | Começar a 1 kHz com Vp da equipe; encontrar transição para triângulo; capturar entrada e saída para cada peça; medir rampa com cursores; comparar SR, frequência limite e razão entre velocidades; responder sobre dependência do corte com amplitude |
| 3.7 — sequência | Alimentação/offset/polarização → resposta em frequência → seguidor/slew rate → repetições com TL064 |
| 3.8 — registro | Tabelas previsto versus obtido, gráfico de frequência e capturas do triângulo |

Turma 04 não identifica automaticamente a equipe 4. Os ganhos 34/119 e Vp = 2 V são da simulação individual; a bancada usa os valores da equipe e ganho alto 101.

## Entregas e critérios — seções 4 e 5

- Simulação: seis .asc, símbolos e biblioteca estão presentes. O envio conjunto pelo portal, previsto para 17/09, não pode ser verificado localmente.
- Relatório em equipe, previsto para 01/10: não localizado no LAB_3. Deve usar o modelo oficial e incluir projeto de cada integrante, valores medidos, simulação da montagem real, medições, gráficos, respostas às questões e causas das divergências.
- Tolerâncias: até 15% nos resultados e 5% nas condições de ensaio. As amplitudes/frequências prescritas estão configuradas corretamente; os resultados de slew rate exigem a revisão descrita acima.
- O roteiro limita a pontuação de itens com resultados fora da tolerância e de arquivos que não simulam. Não é possível garantir aprovação integral com as pendências encontradas.

Prioridades: revisar resultados dos itens 4 e 6; documentar a limitação do item 5; nomear os nós automáticos; consolidar os cálculos e comparações; realizar/registrar bancada e relatório quando chegar essa etapa.
