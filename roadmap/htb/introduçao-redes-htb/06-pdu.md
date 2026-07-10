# Unidades de Dados (PDU)

> **Módulo:** Introduction to Networking  
> **Plataforma:** Hack The Box Academy  
> **Status:** ✅ Concluído

---

# Introdução

Esse foi um daqueles assuntos que, à primeira vista, parece ter um nome complicado, mas depois de entender a ideia ficou bem simples.

Durante a comunicação entre dois dispositivos, os dados não permanecem sempre no mesmo formato. Conforme passam pelas diferentes camadas da rede, eles vão recebendo novas informações para que consigam chegar corretamente ao destino.

Essas diferentes representações dos dados são chamadas de **PDU (Protocol Data Unit)**.

---

# O que é uma PDU?

Uma **Protocol Data Unit (PDU)** é o nome dado aos dados em cada etapa da comunicação de rede.

Cada camada adiciona suas próprias informações antes de encaminhar os dados para a próxima camada.

Esse processo é conhecido como **encapsulamento**.

Quando os dados chegam ao destino, acontece o processo inverso, chamado de **desencapsulamento**, onde cada camada remove as informações adicionadas anteriormente até que a mensagem original seja entregue à aplicação.

---

# As PDUs em cada camada

Cada camada utiliza uma PDU diferente.

| Camada | PDU |
|---------|-----|
| Aplicação | Data |
| Transporte | Segment (TCP) / Datagram (UDP) |
| Rede | Packet |
| Enlace | Frame |
| Física | Bits |

Embora o modelo OSI possua sete camadas, normalmente as PDUs são associadas apenas às camadas onde ocorre alteração no formato dos dados.

---

# Como acontece o encapsulamento?

Imagine que eu acesso um site pelo navegador.

Antes da requisição chegar ao servidor, ela passa por várias etapas.

```text
Aplicação
    │
    ▼
Data
    │
    ▼
Transporte
    │
    ▼
Segment
    │
    ▼
Rede
    │
    ▼
Packet
    │
    ▼
Enlace
    │
    ▼
Frame
    │
    ▼
Física
    │
    ▼
Bits
```

Cada camada adiciona informações importantes para que a comunicação aconteça corretamente.

Depois que os dados chegam ao servidor, todo esse processo acontece ao contrário.

---

# Por que isso é importante?

Antes desse estudo eu imaginava que um pacote simplesmente "saía" do computador e chegava ao destino.

Agora ficou mais claro que cada camada participa da comunicação e adiciona suas próprias informações.

Isso explica por que ferramentas como o Wireshark mostram tantos detalhes em um único pacote.

Na verdade, o que estamos vendo é o resultado de todas essas camadas trabalhando juntas.

---

# Relação com o Wireshark

Mesmo ainda estando nos fundamentos, esse assunto já fez bastante sentido pensando nas ferramentas que vou utilizar mais para frente.

Quando abrimos um pacote no Wireshark, conseguimos visualizar exatamente essas informações adicionadas durante o encapsulamento.

Por exemplo:

- Endereço MAC → Camada de Enlace.
- Endereço IP → Camada de Rede.
- Porta TCP ou UDP → Camada de Transporte.
- Dados HTTP → Camada de Aplicação.

Entender as PDUs facilita bastante interpretar uma captura de rede.

---

# O que isso muda na Cybersecurity?

Grande parte do trabalho em Cybersecurity envolve analisar como os dados trafegam pela rede.

Durante um Pentest ou uma análise de tráfego, é comum precisar identificar:

- De onde um pacote veio.
- Para onde ele está indo.
- Qual protocolo está sendo utilizado.
- Em qual camada ocorreu determinado problema.

Conhecer as PDUs ajuda justamente a entender esse caminho.

É um conhecimento que será utilizado constantemente em ferramentas como:

- Wireshark
- tcpdump
- Burp Suite
- Nmap

---

# O que ficou de aprendizado

Depois desse estudo consegui entender que os dados não atravessam a rede sempre da mesma forma.

Conforme passam pelas camadas, eles recebem novas informações que permitem sua identificação, roteamento e entrega ao destino.

Também aprendi os conceitos de **encapsulamento** e **desencapsulamento**, que ajudam a explicar como uma simples requisição consegue sair do meu computador e chegar corretamente a outro dispositivo.

Foi um ótimo fechamento para esse módulo, porque conectou vários conceitos estudados anteriormente, como o modelo OSI, o TCP/IP e o funcionamento da comunicação em redes.
