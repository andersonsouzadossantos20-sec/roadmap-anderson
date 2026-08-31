# Modelo TCP/IP

> **Módulo:** Introduction to Networking  
> **Plataforma:** Hack The Box Academy  
> **Status:** ✅ Concluído

---

# Introdução

Depois de estudar o modelo OSI, fez muito sentido aprender o TCP/IP.

Foi nesse momento que percebi uma diferença importante: enquanto o OSI serve como um modelo de referência para facilitar o entendimento da comunicação, o TCP/IP é o conjunto de protocolos que realmente faz a Internet funcionar.

Praticamente toda comunicação que acontece hoje passa, de alguma forma, por esse modelo.

---

# O que é o Modelo TCP/IP?

O modelo TCP/IP organiza a comunicação em quatro camadas.

```text
+---------------------------+
| Application               |
| Transport                 |
| Internet                  |
| Network Access            |
+---------------------------+
```

Ele é mais simples que o OSI, mas representa muito melhor a forma como a Internet funciona atualmente.

---

# Camada de Aplicação

É onde ficam os protocolos utilizados diretamente pelas aplicações.

Exemplos:

- HTTP
- HTTPS
- DNS
- FTP
- SMTP
- SSH

Sempre que abrimos um navegador ou utilizamos algum serviço na Internet, normalmente estamos trabalhando nessa camada.

---

# Camada de Transporte

Responsável por entregar os dados entre origem e destino.

Os principais protocolos são:

## TCP

- Orientado à conexão.
- Mais confiável.
- Garante entrega dos dados.
- Reorganiza pacotes quando necessário.

Muito utilizado por:

- HTTP
- HTTPS
- SSH

---

## UDP

- Não estabelece conexão.
- Mais rápido.
- Não garante entrega.

Muito utilizado por:

- Streaming.
- Jogos online.
- VoIP.

---

# Camada Internet

Responsável pelo endereçamento e roteamento dos pacotes.

Protocolos:

- IPv4
- IPv6
- ICMP

É aqui que os pacotes descobrem o caminho até o destino.

---

# Camada de Acesso à Rede

É a camada responsável pela comunicação física com a rede.

Inclui tecnologias como:

- Ethernet.
- Wi-Fi.
- Cabos.
- Interfaces de rede.

Ela faz a ligação entre o computador e o meio físico de transmissão.

---

# Comparando com o Modelo OSI

Uma coisa interessante foi perceber que os dois modelos possuem objetivos parecidos.

O OSI divide a comunicação em sete camadas.

Já o TCP/IP simplifica tudo em apenas quatro.

Mesmo assim, vários conceitos continuam equivalentes.

Foi justamente essa comparação que me ajudou a entender melhor os dois modelos.

---

# O que isso muda na Cybersecurity?

Grande parte das ferramentas utilizadas em segurança trabalham diretamente sobre o TCP/IP.

Quando usamos:

- Wireshark.
- Burp Suite.
- Nmap.
- tcpdump.

Estamos analisando protocolos que pertencem ao modelo TCP/IP.

Quanto melhor entendermos esse modelo, mais fácil fica interpretar o comportamento da rede.

---

# O que ficou de aprendizado

Depois desse estudo consegui entender:

- A diferença entre o modelo OSI e o TCP/IP.
- Por que o TCP/IP é utilizado na Internet.
- As funções de cada camada.
- A diferença entre TCP e UDP.

Esse foi um dos tópicos mais importantes até agora, porque praticamente tudo que envolve redes depende desses protocolos.
