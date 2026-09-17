# Entrega dos arquivos do LAB_3

Use os arquivos da pasta [Simulacoes](Simulacoes/), mantendo seus nomes.

| Campo no portal | Arquivo |
|---|---|
| Item 1 | [item_1.asc](Simulacoes/item_1.asc) |
| Item 2 | [item_2.asc](Simulacoes/item_2.asc) |
| Item 3 | [item_3.asc](Simulacoes/item_3.asc) |
| Item 4 | [item_4.asc](Simulacoes/item_4.asc) |
| Item 5 | [item_5.asc](Simulacoes/item_5.asc) |
| Item 6 | [item_6.asc](Simulacoes/item_6.asc) |
| Item 7 — opcional, símbolo | [LM741.asy](Simulacoes/LM741.asy) |
| Item 8 — opcional, símbolo | [TL064.asy](Simulacoes/TL064.asy) |

O `.asc` contém o circuito: componentes, fios, valores e comando de análise.
O `.asy` contém o símbolo: desenho do amplificador, pinos e correspondência dos terminais com o modelo. Não é outra simulação. Os dois símbolos são os mesmos construídos no LAB_2; seus nomes correspondem às referências usadas pelos circuitos do LAB_3. Recomenda-se enviar ambos nos campos opcionais, sem renomeá-los.

A biblioteca [ene0046.lib](Simulacoes/ene0046.lib) contém os modelos elétricos fornecidos pela disciplina. Para abrir e simular em outro computador, mantenha os seis `.asc`, os dois `.asy` e a biblioteca na mesma pasta. A captura do portal não mostra campo próprio para `.lib`; não a envie no lugar de um `.asy`. O professor precisa ter a biblioteca fornecida pela disciplina disponível.

O [ZIP completo](LAB_3_arquivos_entrega.zip) reúne esses nove arquivos para transporte. Nos campos que pedem `.asc` ou `.asy`, envie os arquivos individuais correspondentes, não o ZIP.

As seis simulações finais foram verificadas no LTspice, com netlists e inspeção visual. Os itens 4 e 6 mostram senoide na frequência baixa e limitação aproximadamente triangular na alta. Os comentários dos itens 4 e 5 registram particularidades dos modelos fornecidos: slew rate do LM741 de aproximadamente 0,326 V/µs e corrente DC de entrada praticamente nula no TL064. A biblioteca original não foi modificada.

O documento de verificação e este guia são auxiliares locais; não são necessários nos oito campos mostrados. O envio no portal deve ser feito pelo aluno.
