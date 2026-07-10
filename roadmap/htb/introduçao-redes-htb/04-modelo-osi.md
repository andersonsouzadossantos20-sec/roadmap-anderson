# Modelo OSI

> **Módulo:** Introduction to Networking  
> **Plataforma:** Hack The Box Academy  
> **Status:** ✅ Concluído

---

# Introdução

Durante esse estudo finalmente entendi por que o modelo OSI aparece em praticamente todo material sobre redes.

No começo ele parece apenas um monte de camadas para decorar, mas depois fica claro que o objetivo dele é muito mais simples: organizar a comunicação da rede em etapas.

Isso facilita entender onde cada protocolo atua, como os dados são transmitidos e até onde determinados problemas ou ataques podem acontecer.

Mesmo que a Internet utilize o modelo TCP/IP, estudar o OSI ajuda bastante a visualizar todo o processo.

---

# O que é o Modelo OSI?

O **OSI (Open Systems Interconnection)** é um modelo de referência criado para dividir a comunicação de rede em sete camadas.

Cada camada possui uma responsabilidade específica e trabalha em conjunto com as demais.

```text
+---------------------------+
| 7 - Application           |
| 6 - Presentation          |
| 5 - Session               |
| 4 - Transport             |
| 3 - Network               |
| 2 - Data Link             |
| 1 - Physical              |
+---------------------------+
```

A ideia principal é separar responsabilidades, tornando a comunicação mais organizada e padronizada.

---

# Camada Física (Physical)

É a camada responsável pela transmissão física dos dados.

Aqui não existe preocupação com IP ou protocolos, apenas com sinais elétricos, ópticos ou ondas de rádio.

Exemplos:

- Cabos de rede
- Fibra óptica
- Conectores
- Wi-Fi

---

# Camada de Enlace (Data Link)

Responsável pela comunicação entre dispositivos da mesma rede.

É nessa camada que aparecem os endereços MAC.

Alguns protocolos:

- Ethernet
- Wi-Fi (802.11)

Equipamentos comuns:

- Switches

---

# Camada de Rede (Network)

Essa camada permite que os dados atravessem diferentes redes até chegar ao destino.

É aqui que entra o endereço IP.

Protocolos importantes:

- IPv4
- IPv6
- ICMP

Equipamento mais conhecido:

- Roteador

---

# Camada de Transporte (Transport)

Responsável por garantir que a comunicação aconteça corretamente.

Ela controla:

- Entrega dos dados.
- Ordem dos pacotes.
- Controle de erros.

Protocolos:

- TCP
- UDP

---

# Camada de Sessão (Session)

Gerencia a comunicação entre duas aplicações.

Ela cria, mantém e encerra sessões durante uma comunicação.

Embora nem sempre seja perceptível para o usuário, ela faz parte do processo de comunicação.

---

# Camada de Apresentação (Presentation)

Responsável por preparar os dados para que a aplicação consiga interpretá-los.

Algumas funções:

- Criptografia.
- Compressão.
- Conversão de formatos.

Um exemplo comum é o uso de criptografia em conexões HTTPS.

---

# Camada de Aplicação (Application)

É a camada mais próxima do usuário.

Tudo aquilo que utilizamos diariamente funciona aqui.

Exemplos:

- HTTP
- HTTPS
- FTP
- SMTP
- DNS

Sempre que acessamos um site ou enviamos um e-mail, estamos utilizando protocolos dessa camada.

---

# O que isso muda na Cybersecurity?

Antes desse estudo eu enxergava a comunicação da rede como uma única coisa.

Agora ficou muito mais fácil visualizar em qual camada determinado protocolo atua e onde um problema pode acontecer.

Isso ajuda bastante durante:

- Análise de tráfego.
- Troubleshooting.
- Pentest.
- Captura de pacotes no Wireshark.

---

# O que ficou de aprendizado

Depois desse estudo consegui entender:

- O objetivo do modelo OSI.
- A função de cada uma das sete camadas.
- Onde protocolos como HTTP, TCP e IP atuam.
- Como esse modelo ajuda a compreender melhor a comunicação de rede.

Mesmo sabendo que a Internet utiliza o TCP/IP, estudar o OSI tornou muito mais fácil entender como tudo funciona por trás.
