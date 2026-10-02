# Lab 4 — manual de bancada: eletrocardiograma

**Equipe 1 · Turma 04.** Conferido com a versão do roteiro de **01/10/2026**, seções **4.1–4.8** (pp. 4–6). Os números abaixo são cálculos com os valores escritos nos componentes, **não medições reais**.

| O que você verá | Valor esperado para a Equipe 1 |
|---|---:|
| INA118 pino 6, ensaio 4.3 a 10 Hz | **4,00 Vpp** |
| TL064 pino 1, ensaio 4.4 a 10 Hz | **aproximadamente 4,00 Vpp** |
| TL064 pino 7, ensaio 4.5 a 10 Hz | **10,0 Vpp** |
| Junção do resistor de 1 kΩ com o capacitor de 2,2 µF, ensaio 4.6 a 10 Hz | **4,00 Vpp** |
| Frequência em que a saída cai a 0,707 do valor máximo, no lado das frequências baixas | cerca de 0,482 Hz |
| Frequência em que a saída cai a 0,707 do valor máximo, no lado das frequências altas | cerca de 72,3 Hz |

`Vpp` é a diferença entre o ponto mais alto e o mais baixo da onda mostrada no osciloscópio.

## 0. Roteiro §4.1 — o que pegar antes de montar

### Circuitos integrados, montagem e instrumentos

| Quantidade | Item |
|---:|---|
| 1 | **INA118 DIP-8**: peça preta com **4 pinos metálicos de cada lado** |
| 1 | **TL064 DIP-14**: peça preta com **7 pinos metálicos de cada lado** |
| 1 | Protoboard e fios para três trilhos: +15 V, GND/COM e −15 V |
| 1 | Fonte **Agilent E3631A** e cabos |
| 1 | Gerador **Agilent 33220A** e cabo BNC |
| 1 | Osciloscópio **Agilent DSO1002A** e duas pontas |
| 1 | Multímetro **Agilent 34410A** e pontas |
| 3 | Eletrodos e cabos, **somente para a etapa com pessoa autorizada pelo docente** |

### Resistores: quantidade, uso e cores

Cores abaixo para peças de **quatro faixas e tolerância dourada de 5%**. Se a peça tiver cinco faixas ou outra tolerância, identificar pelo código correspondente e confirmar no multímetro.

| Quantidade | Valor | Onde usar | Faixas de cor |
|---:|---:|---|---|
| 2 | 820 Ω | Um entre a entrada do INA e GND; outro entre TL064 pino 6 e GND | cinza · vermelho · marrom · dourado |
| 1 | 1 kΩ | Entre TL064 pino 7 e a saída final | marrom · preto · vermelho · dourado |
| 1 | 2,2 kΩ | Entre INA118 pinos 1 e 8 | vermelho · vermelho · vermelho · dourado |
| 1 | 33 kΩ | Entre TL064 pinos 7 e 6 | laranja · laranja · laranja · dourado |
| 1 | 100 kΩ | Entre o centro do BNC e a junção com um resistor de 820 Ω | marrom · preto · amarelo · dourado |
| 1 | 330 kΩ | Entre TL064 pino 3 e GND | laranja · laranja · amarelo · dourado |

### Capacitores cerâmicos

| Quantidade | Valor | Onde usar | Código comum |
|---:|---:|---|---|
| 5 | 1 µF | 1 entre INA pino 6 e TL064 pino 3; 4 junto aos pinos de alimentação | `105` |
| 1 | 2,2 µF | Entre a saída final e GND | `225` |

- Usar peças cerâmicas **não polarizadas**; a cor do corpo não identifica o valor.
- Confirmar tensão nominal **acima de 15 V** nos quatro capacitores ligados aos pinos de alimentação.

### Medir antes de inserir na placa

1. Deixar fonte e gerador **desligados**.
2. No 34410A, antes de conectar as pontas, apertar **Front/Rear** para usar os bornes da frente. Ponta preta em **Input LO**; vermelha em **Input HI**. Não usar os bornes de corrente.
3. Para cada resistor **fora do circuito**, apertar a tecla **Ω 2W**, encostar uma ponta em cada extremo e anotar a leitura.
4. Para cada capacitor **fora do circuito**, apertar **Shift** e depois **Freq** (função de capacitância); encostar uma ponta em cada terminal e anotar a leitura e o código da peça.
5. A leitura de **0,032 mV DC da foto** do multímetro não é resultado deste experimento.

## 1. Roteiro §4.2 — montar a alimentação e conferir os pinos

### Reconhecer e colocar as duas peças pretas

**DIP** é só o formato da peça: corpo preto retangular, com **duas fileiras de pinos metálicos**. O INA118 tem **8 pinos ao todo**; o TL064 tem **14**.

1. Deixar a fonte **desligada**.
2. Virar o protoboard para que a **fenda central fique na vertical** diante de você.
3. Procurar uma **meia-lua recortada ou um ponto** em uma ponta de cada peça preta. Colocar essa marca **voltada para a parte de cima** do protoboard.
4. Encaixar cada peça **sobre a fenda central**: uma fileira de pinos nos furos à esquerda, outra nos furos à direita.
   Nenhum pino entra na fenda. A fenda mantém separados os pinos dos dois lados.
5. Deixar espaço entre INA118 e TL064 para colocar os resistores e fios.

**Numeração olhando a peça de cima, com a marca em cima:**

```text
INA118 (8 pinos)             TL064 (14 pinos)
     marca                        marca
   1 ┌─────┐ 8                  1 ┌─────┐ 14
   2 │     │ 7                  2 │     │ 13
   3 │     │ 6                  3 │     │ 12
   4 └─────┘ 5                  4 │     │ 11
                                 5 │     │ 10
                                 6 │     │ 9
                                 7 └─────┘ 8
```

### Entender `COM` e preparar três linhas do protoboard

`COM` é o **borne da frente da fonte E3631A**, situado entre os bornes ajustáveis **+25 V** e **−25 V**. Ele será o **zero volt** da montagem.

Neste manual, **GND** é a linha do protoboard ligada por fio ao borne **COM** da fonte.

| Borne da E3631A | Ajuste na fonte | Ligar a uma linha do protoboard identificada como |
|---|---:|---|
| **+25 V** ajustável | +15,0 V em relação a `COM` | **+15 V** |
| **COM** | 0 V | **GND** |
| **−25 V** ajustável | −15,0 V em relação a `COM` | **−15 V** |

1. Escolher **três linhas/trilhos separados** no protoboard e identificá-los com `+15 V`, `GND` e `−15 V`.
2. Conferir se algum trilho lateral tem uma **interrupção no meio**. Se tiver, os furos dos dois lados da interrupção não estão ligados; usar um fio para uni-los somente quando forem o **mesmo** trilho.
3. Com a saída da fonte ainda desligada, levar **um fio de cada borne da tabela** para o trilho correspondente.

O borne com o **símbolo de terra de proteção** no painel da fonte é outra conexão; **não é o `COM`**. Não unir os trilhos `+15 V` e `−15 V` nem usar a saída `0–6 V` neste ensaio.

### Ligar INA118 e TL064 com a fonte desligada

| Ligação | Origem | Destino |
|---|---|---|
| Alimentação positiva do INA | INA pino **7** | +15 V |
| Alimentação negativa do INA | INA pino **4** | −15 V |
| Pino de referência do INA | INA pino **5 REF** | GND |
| Resistor de 2,2 kΩ | INA pino **1** | **2,2 kΩ** → INA pino **8** |
| Alimentação positiva do TL064 | TL064 pino **4** | +15 V |
| Alimentação negativa do TL064 | TL064 pino **11** | −15 V |
| Capacitor junto ao INA | INA pino **7** | **1 µF** → GND, perto do CI |
| Capacitor junto ao INA | INA pino **4** | **1 µF** → GND, perto do CI |
| Capacitor junto ao TL064 | TL064 pino **4** | **1 µF** → GND, perto do CI |
| Capacitor junto ao TL064 | TL064 pino **11** | **1 µF** → GND, perto do CI |

**Canais 3 e 4 do TL064 não usados:**

| Canal | Entrada não inversora | Unir saída à entrada inversora |
|---|---|---|
| 3 | pino **10** → GND | pinos **8–9** |
| 4 | pino **12** → GND | pinos **14–13** |

### Ajustar fonte e conferir com multímetro

1. Na **E3631A**, confirmar `OFF` no visor. Se as saídas estiverem ligadas, apertar **Output On/Off** para desligá-las.
2. Apertar **+25 V** para selecionar essa saída. Apertar **Display Limit**; selecionar ajuste de **tensão** na tecla de seleção tensão/corrente; girar o botão grande até **15,0 V**. As setas movem o dígito que pisca.
3. Segurar **Track** por pelo menos **1 segundo**. Conferir no visor, alternando **+25 V** e **−25 V**, que ambas as magnitudes estão em **15,0 V**. O borne negativo ficará em **−15 V relativo a COM**.
4. Ajustar os **limites de corrente das duas saídas** conforme a orientação do laboratório; o roteiro não fornece valor.
5. Apertar **Output On/Off** para ligar as saídas. Conferir **CV** e ausência de **CC** no visor, tanto ao selecionar **+25 V** quanto **−25 V**.
6. No **34410A**, apertar **Front/Rear** antes de conectar pontas, até usar os bornes frontais. Colocar ponta preta em **Input LO** e vermelha em **Input HI**, apertar **DC V**. Ponta preta no GND do protoboard.
7. Com a ponta vermelha, medir e conferir:

   | Ponto (`HI`) | Leitura esperada |
   |---|---:|
   | INA pino **7** | +15 V |
   | INA pino **4** | −15 V |
   | INA pino **5** | 0 V |
   | TL064 pino **4** | +15 V |
   | TL064 pino **11** | −15 V |

Corrigir qualquer inversão **antes** de aplicar sinal. Medir resistência apenas com a fonte desligada.

## 2. Roteiro §4.2 — controles usados em todas as medidas

### Gerador Agilent 33220A

1. Deixar a tecla **Output** apagada enquanto troca os fios. O BNC de sinal é o conector frontal **Output**, não o conector `Sync`.
2. Apertar **Sine** para selecionar a onda senoidal.
3. Apertar **Utility → Output Setup → Load**; apertar **Load** novamente até aparecer **High Z**. Fazer isso **antes** de ajustar a amplitude; mudar a carga depois pode mudar o número de Vpp exibido.
4. Apertar a tecla de tela **Freq**, digitar o valor e escolher **Hz**.
5. Apertar **Ampl**, digitar a tensão e escolher **Vpp**. Os valores mudam em cada seção abaixo; **14,60 Vpp da foto não é um ajuste deste roteiro**.
6. Apertar **Offset**, ajustar **0 V**. Apertar **Output** para acender e liberar o sinal **somente depois** de ligar o cabo.

**Vpp** é a tensão entre o topo e o fundo da onda. **Tensão de pico = Vpp ÷ 2.** Assim, pedir **2 V de pico** significa ajustar até ler **4 Vpp** no osciloscópio.

### Osciloscópio Agilent DSO1002A

1. Encaixar a ponta no conector frontal **CH1** ou **CH2**. Prender o jacaré de terra da ponta no **GND do protoboard**, nunca em +15 V ou −15 V.
2. Apertar a tecla física **CH1** ou **CH2**. No menu desse canal, deixar **Acoplamento = CC**. Não selecionar `CA`: essa opção remove parte das ondas lentas que serão medidas.
3. Conferir a chave **1×/10× da própria ponta**. No menu **Ponta prova**, escolher o mesmo número. Para o ensaio da seção 4.3 com as duas entradas unidas, usar **1× na ponta e 1× no menu**.
4. Para ler Vpp automaticamente, apertar **MEASURE → Fonte → CH1 ou CH2 → Tensão → Vpp**. Escolher o canal onde está a ponta.
5. Se o visor não der a leitura, girar **VOLTS/DIV** do canal e **SEC/DIV** até aparecerem ondas completas.
6. Para 10 Hz, começar em **20 ms/div**; para 60 Hz, em **5 ms/div**. Para medir perto de 0,5 Hz, usar **1 s/div**, como pede o roteiro. Para o ECG, usar **0,2 s/div**.
7. O menu **Limite Banda** pode ficar ligado para reduzir ruído. Anotar o canal, a posição 1×/10× e o ajuste de VOLTS/DIV em cada captura.

### Multímetro Agilent 34410A

- **Resistores fora da placa:** **Ω 2W**, pontas nos dois extremos.
- **Capacitores fora da placa:** **Shift → Freq** (capacitância), pontas nos dois terminais.
- **Tensões nos pinos da placa:** **DC V**, ponta preta no **GND**, ponta vermelha no pino indicado.
- Selecionar os bornes **frontais Input HI/LO** com **Front/Rear** antes de conectar as pontas.

## 3. Roteiro §4.3 — medir o INA118 sozinho

### §4.3, primeira medida: uma entrada recebe o gerador

**Ligar com `Output` apagado:**

- Centro do BNC **diretamente ao INA pino 3**; malha do BNC ao GND.
- INA pino **2 ao GND**; resistor de **2,2 kΩ entre INA pinos 1 e 8**.
- Ainda não ligar o capacitor de 1 µF ao INA pino 6.

1. Colocar **CH1** no INA pino **3** e **CH2** no INA pino **6**. Jacarés de terra no mesmo GND.
2. No gerador, apertar **Sine**, **Freq → 10 Hz**, **Offset → 0 V**, confirmar **High Z**. Em **Ampl**, começar perto de **0,169 Vpp**.
3. Apertar **Output**. No osciloscópio, usar **MEASURE → Fonte CH2 → Tensão → Vpp**. Ajustar **Ampl** do gerador até o CH2 indicar **4,00 Vpp** (isto é, 2,00 V de pico).
4. No osciloscópio, mudar a fonte da medida para **CH1** e anotar a tensão realmente aplicada ao INA pino 3. Voltar a medir CH2 e anotar o valor no INA pino 6.

| Anotar | Valor nominal aproximado |
|---|---:|
| Gerador / INA pino 3 | **0,169 Vpp** |
| INA pino 6 | **4,00 Vpp** |
| Leitura do pino 6 ÷ leitura do pino 3 | **23,73** |

O número exato da última linha depende do **resistor de 2,2 kΩ medido**: `1 + 50.000 Ω ÷ R_medido`.

### §4.3, segunda medida: a mesma onda nos pinos 2 e 3

1. Apertar **Output** para apagar a saída do gerador.
2. Soltar o INA pino **2** do GND; unir **INA pinos 2 e 3** com um fio. Ligar a união ao centro do BNC. Malha do BNC no GND.
3. No gerador, apertar **Freq → 60 Hz** e **Ampl → 10,0 Vpp** (= 5,0 V de pico); manter **Offset 0 V** e **High Z**.
4. Mover a chave física da ponta do CH2 para **1×**. Apertar **CH2 → Ponta prova → 1×**. Ponta CH2 no INA pino **6** e jacaré no GND.
5. Apertar **Output**. No CH2, deixar **Acoplamento = CC**; girar **VOLTS/DIV** até a menor escala que ainda mostre uma onda estável. Ajustar **SEC/DIV** perto de **5 ms/div**.
6. Apertar **MEASURE → Fonte CH2 → Tensão → Vpp** e anotar a onda de 60 Hz no pino 6. Se a tela mostrar somente ruído, anotar a **menor tensão Vpp que seria distinguível** nessa escala; não escrever zero.

| Comparar | Esperado |
|---|---|
| Entrada nos pinos 2 e 3 | **10,0 Vpp** em ambos |
| INA pino 6 | Onda de 60 Hz muito pequena; o roteiro **não fixa um valor numérico** |
| Leitura ou limite em Vpp do pino 6 ÷ **10,0 Vpp** | Registrar esse quociente; equivale à razão das amplitudes de pico, que o roteiro pede dividir por **5,0 V** |

Para a questão do roteiro, comparar esse resultado com a simulação do item 2, na qual um resistor foi alterado para 12 kΩ.

## 4. Roteiro §4.4 — ligar 1 µF, 330 kΩ e o primeiro canal do TL064

### §4.4, montar com `Output` apagado

1. Desfazer a união dos pinos 2 e 3 do INA. Ligar **INA pino 2 ao GND** e **centro do BNC ao INA pino 3**, como na primeira medida do §4.3.
2. Ligar o **capacitor de 1 µF** entre **INA pino 6** e uma junção livre do protoboard. Chamar essa junção de `PONTO_A`.
3. Ligar o **resistor de 330 kΩ** entre `PONTO_A` e GND.
4. Ligar `PONTO_A` diretamente ao **TL064 pino 3**.
5. Unir **TL064 pinos 2 e 1** com um fio. **Não** colocar resistor entre esses pinos; medir na saída **TL064 pino 1**.

### §4.4, medir em 10 Hz e depois baixar a frequência

1. No gerador, ajustar **Sine, 10 Hz, Offset 0 V, High Z**. Recuperar a amplitude usada na primeira medida do §4.3. Colocar CH2 no INA pino **6** e conferir **4,00 Vpp**. Não usar os 10,0 Vpp do ensaio de 60 Hz.
2. Mover a chave física da ponta CH2 para **10×** e selecionar **CH2 → Ponta prova → 10×**.
3. Colocar a ponta no **TL064 pino 1** e o jacaré no GND. Apertar **CH2 → Acoplamento → CC** e **MEASURE → Fonte CH2 → Tensão → Vpp**. Esperar perto de **4,00 Vpp**.
4. No gerador, apertar **Freq** e baixar a frequência sem mudar **Ampl**. No osciloscópio, girar **SEC/DIV** para **1 s/div** e aguardar algumas ondas a cada ajuste.
5. Anotar a frequência quando CH2 indicar **0,707 × leitura a 10 Hz**. Se a leitura inicial foi 4,00 Vpp, procurar **2,83 Vpp**.

| Anotar | Valor nominal |
|---|---:|
| INA pino 6 a 10 Hz | **4,00 Vpp** |
| TL064 pino 1 a 10 Hz | **aproximadamente 4,00 Vpp** |
| Frequência em que TL064 pino 1 chega perto de 2,83 Vpp | **0,482 Hz** |

## 5. Roteiro §4.5 — usar outro canal do TL064 e ajustar a saída para 10,0 Vpp

### §4.5, montar com `Output` apagado

1. Manter o fio entre **TL064 pinos 1 e 2** e o circuito da seção anterior.
2. Ligar **TL064 pino 1 → pino 5** com um fio.
3. Ligar **820 Ω entre TL064 pino 6 e GND**.
4. Ligar **33 kΩ entre TL064 pinos 7 e 6**. Medir a nova saída no **TL064 pino 7**.
5. Retirar o centro do BNC de **INA pino 3**. Montar: **centro do BNC → 100 kΩ → junção `PONTO_B` → 820 Ω → GND**. Ligar `PONTO_B` ao **INA pino 3**. Manter **INA pino 2 no GND**.
6. Ligar **CH1 ao centro do BNC, antes dos 100 kΩ**, e **CH2 ao TL064 pino 7**. Jacarés de terra no GND.

`PONTO_B` é a **junção dos resistores de 100 kΩ e 820 Ω**. Sua tensão é a leitura de CH1 multiplicada por `R_820 ÷ (R_100k + R_820)`, usando os valores reais medidos dos resistores.

### §4.5, medir em 10 Hz

1. No gerador, apertar **Freq → 10 Hz**, manter **Sine, Offset 0 V, High Z**; em **Ampl**, começar perto de **1,26 Vpp**.
2. Deixar a ponta CH2 em **10×** e o menu **Ponta prova = 10×**. Apertar **Output**.
3. No osciloscópio, usar **MEASURE → Fonte CH2 → Tensão → Vpp**. Ajustar **Ampl** até **TL064 pino 7 = 10,0 Vpp** (= 5,0 V de pico).
4. Se a onda ficar achatada, verificar ligações e alimentação.
5. Sem alterar o gerador, medir `Vpp` no **TL064 pino 1** e no **pino 7**. Medir também CH1 no gerador. A onda pode estar deslocada verticalmente; medir **Vpp**, não a altura do pico acima do zero.

| Anotar | Valor nominal aproximado |
|---|---:|
| Gerador no CH1 | **1,26 Vpp** |
| `PONTO_B`, calculado com os resistores medidos | **0,0102 Vpp** |
| TL064 pino 1 | **0,242 Vpp** |
| TL064 pino 7 | **10,0 Vpp** |
| Leitura do pino 7 ÷ leitura do pino 1 | **41,24** |
| Leitura do pino 7 ÷ tensão calculada em `PONTO_B` | **978,6** |

Calcular a primeira razão com os resistores medidos: `1 + R_33k ÷ R_820`.
Para estimar a saída de um sinal cardíaco ideal de **1 mV de pico**, o resultado nominal no pino 7 é perto de **0,98 V de pico**. A medida numa pessoa varia.

## 6. Roteiro §4.6 — ligar 1 kΩ e 2,2 µF na saída e medir 10 frequências

### §4.6, montar com `Output` apagado

| De | Componente | Para |
|---|---|---|
| TL064 pino **7** | Resistor **1 kΩ** | Junção `SAIDA_FINAL` |
| Junção `SAIDA_FINAL` | Capacitor cerâmico **2,2 µF** | GND |
| Junção `SAIDA_FINAL` | Ponta CH2 do osciloscópio | Jacaré CH2 no GND |

`SAIDA_FINAL` é a **junção entre o resistor de 1 kΩ, o capacitor de 2,2 µF e a ponta CH2**. Não medir no TL064 pino 7 achando que já é a saída final.

### §4.6, ajustar em 10 Hz e varrer

1. Deixar **CH1 no gerador antes dos 100 kΩ**; mover **CH2 para `SAIDA_FINAL`**. Confirmar **Acoplamento = CC** e o fator **Ponta prova** dos dois canais.
2. No gerador, usar **Sine, 10 Hz, Offset 0 V, High Z**. Reduzir **Ampl**, começando perto de **0,508 Vpp**, até CH2 indicar **4,00 Vpp** (= 2,00 V de pico).
3. Anotar o Vpp do gerador em CH1. **Não mudar mais `Ampl`**. Apertar **Freq** e usar cada frequência da tabela. Em cada linha, apertar **MEASURE → Fonte CH2 → Tensão → Vpp** e anotar a leitura.
4. Perto de **0,5 Hz**, ajustar **SEC/DIV para 1 s/div** e esperar algumas ondas antes de anotar. Para outras frequências, ajustar SEC/DIV para mostrar duas ou três ondas completas.

| Ajustar gerador (Hz) | Esperado em `SAIDA_FINAL` (Vpp) | Medido (Vpp) | Medido ÷ tensão calculada em `PONTO_B` |
|---:|---:|---:|---:|
| 0,20 | 1,55 |  |  |
| 0,35 | 2,37 |  |  |
| 0,48 | 2,85 |  |  |
| 0,70 | 3,33 |  |  |
| 3 | 3,99 |  |  |
| 10 | 4,00 |  |  |
| 50 | 3,33 |  |  |
| 72 | 2,87 |  |  |
| 100 | 2,37 |  |  |
| 720 | 0,40 |  |  |

**Os valores esperados pressupõem 4,00 Vpp na saída final a 10 Hz e peças com seus valores nominais.** Com peças reais, a tabela pode diferir.

As duas leituras perto de **2,83 Vpp** devem ocorrer aproximadamente a **0,482 Hz** e **72,3 Hz**. Traçar o gráfico da última coluna contra frequência em escala horizontal logarítmica, como pede §4.6.

Em **60 Hz**, o resistor de 1 kΩ e o capacitor de 2,2 µF deixam na `SAIDA_FINAL` cerca de **0,77 vez** a onda presente no TL064 pino 7 (**−2,27 dB**). Essa redução, sozinha, é pequena.

## 7. Roteiro §4.7 — medir o eletrocardiograma

### Informação que ainda falta no PDF novo

O roteiro **ainda não define a posição dos três eletrodos nem um arranjo de isolamento para ligar uma pessoa**. A fonte E3631A e o osciloscópio são alimentados pela rede. As malhas do BNC e da ponta estão ligadas ao GND do circuito.

**Não ligar eletrodos à pessoa até o docente fornecer e verificar o arranjo de isolamento e indicar as posições e ligações dos eletrodos.**

Não improvisar o terceiro eletrodo no GND nem remover o terra de proteção dos aparelhos. A [Analog Devices](https://wiki.analog.com/resources/eval/ad8232-evaluation-guide/a03321a) também exige isolamento da rede ao conectar eletrodos a uma pessoa.

### Quando o docente liberar o arranjo isolado

1. Apertar **Output** no gerador para desligá-lo; tirar o BNC e os resistores de 100 kΩ e 820 Ω das entradas do INA118.
2. Conectar os eletrodos **exatamente como indicado pelo docente** no arranjo isolado. O PDF não fornece pinos/posições suficientes para especificar essa ligação.
3. Ponta CH2 na junção `SAIDA_FINAL`; jacaré CH2 no GND. Apertar **CH2 → Acoplamento → CC** e ajustar **SEC/DIV = 0,2 s/div**.
4. Fotografar a tela em repouso. Identificar P, QRS e T.
5. Para o tempo entre picos R, apertar **CURSORS → Mode → Track**. Escolher CH2 para os dois cursores, posicioná-los nos dois picos R com o botão e ler **ΔX** em segundos.
6. Para a altura do QRS, posicionar um cursor na linha de base e outro no pico do QRS; ler **ΔY** em volts. Se o menu variar, contar as divisões da grade e multiplicar pelo ajuste **VOLTS/DIV**.
7. Calcular batimentos por minuto: **60 ÷ tempo entre dois picos R**. Registrar outra tela com o eletrodo de referência retirado **pelo docente** e outra durante contração do braço.

Não existe Vpp ou frequência cardíaca fixa prevista para uma pessoa. Para um sinal ideal de **1 mV de pico** perto de 10 Hz, a conta do circuito prevê perto de **0,97 V de pico** na saída. Usar a leitura real da pessoa no registro.

## 8. Roteiro §4.8 — conferência antes de sair da bancada

- [ ] Equipe **1**, data, foto da montagem e valores **medidos** dos resistores e capacitores.
- [ ] Tensões dos pinos de alimentação medidas com o 34410A antes do gerador.
- [ ] **§4.3:** Vpp no INA pino 3 e pino 6 a 10 Hz; Vpp residual no pino 6 com pinos 2 e 3 unidos a 60 Hz, ou limite de leitura.
- [ ] **§4.4:** Vpp no TL064 pino 1 a 10 Hz; frequência em que caiu para 0,707 desse valor.
- [ ] **§4.5:** Vpp no gerador antes dos 100 kΩ, no TL064 pino 1 e pino 7; cálculo da tensão em `PONTO_B`.
- [ ] **§4.6:** 10 linhas da tabela, gráfico e frequências em que a saída cai perto de 2,83 Vpp.
- [ ] **§4.7:** telas do ECG em repouso, sem referência e com contração; altura do QRS e tempo entre dois picos R.

Manter a montagem entre os dois encontros, se possível. Se precisar desmontar, fotografar cada ligação e guardar os valores medidos.

No relatório, comparar os resultados previstos, a simulação com as peças medidas e as leituras reais; explicar cada diferença.

### Referências dos aparelhos e pinos

- Pinagens físicas DIP: roteiro, p. 4; folhas de dados [INA118](https://www.ti.com/lit/ds/symlink/ina118.pdf) e [TL064](https://www.ti.com/lit/gpn/tl064).
- A ordem `.SUBCKT` da biblioteca é **ordem de nós de simulação**, não a numeração física do DIP.
- Gerador: [manual 33220A](https://www.keysight.com/no/en/assets/9018-04437/user-manuals/9018-04437.pdf).
- Fonte: [manual E3631A](https://www.keysight.com/us/en/assets/9018-01308/user-manuals/9018-01308.pdf).
- Osciloscópio: [manual DSO1002A/1000 Series](https://www.keysight.com/dz/en/assets/9018-02481/user-manuals/9018-02481.pdf).
- Multímetro: [manual 34410A](https://www.keysight.com/qa/en/assets/9018-05586/user-manuals/9018-05586.pdf).
