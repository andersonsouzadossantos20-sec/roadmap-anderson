# 📚 Registro de Estudo — Cibersegurança

**Data:** 09/09/2026  
**Tema:** Network Fundamentals  
**Área:** Redes de Computadores  
**Plataforma:** Hackviser

---

# 🎯 Objetivo do Estudo

Compreender os fundamentos necessários para entender como computadores e dispositivos se comunicam através de redes.

O estudo abordou desde os conceitos básicos de redes, tipos e topologias, até modelos de comunicação, protocolos, endereçamento IP/MAC e subnetting.

O objetivo principal foi construir uma base sólida de redes que possa ser utilizada posteriormente em análise de tráfego, exploração de serviços, reconhecimento e testes de segurança.

---

# 📖 Conceitos Fundamentais

- Conceito e importância de uma rede de computadores.
- Tipos de redes.
- Dispositivos de rede.
- Topologias de rede.
- Modos e tipos de comunicação.
- Modelos de redes.
- Modelo OSI.
- Modelo TCP/IP.
- Protocolos e portas.
- Endereços IP e MAC.
- Subnetting e segmentação de redes.

---

# 🧠 Explicação Técnica

## 1. Redes de Computadores

Uma rede de computadores permite que dispositivos troquem dados utilizando meios físicos ou sem fio e protocolos de comunicação.

Uma rede pode variar bastante em tamanho e finalidade, desde uma pequena rede doméstica até grandes infraestruturas que interligam diferentes regiões do mundo.

---

## 2. Tipos de Redes

Alguns dos principais tipos de redes são:

- **LAN (Local Area Network):** rede utilizada em uma área limitada, como uma residência, empresa ou laboratório.
- **WAN (Wide Area Network):** conecta redes geograficamente distantes.
- **WLAN:** rede local utilizando comunicação sem fio.
- **Internet:** grande conjunto de redes interconectadas.

A diferença entre esses tipos está principalmente na escala, alcance e finalidade da infraestrutura.

---

## 3. Dispositivos de Rede

Os dispositivos de rede possuem funções diferentes dentro da comunicação.

Exemplos:

- **Switch:** conecta dispositivos dentro de uma rede local e encaminha quadros utilizando endereços MAC.
- **Router:** conecta redes diferentes e encaminha pacotes utilizando endereços IP.
- **Access Point:** fornece conectividade wireless para dispositivos.
- **Firewall:** controla e filtra tráfego de acordo com regras de segurança.

Compreender a função de cada dispositivo é importante para entender o caminho percorrido pelo tráfego.

---

## 4. Topologias de Rede

A topologia representa a forma como os dispositivos estão organizados e conectados.

Exemplos:

- Estrela
- Barramento
- Anel
- Malha
- Híbrida

Em redes modernas, a topologia lógica e a topologia física podem ser diferentes.

---

## 5. Modos de Comunicação

A comunicação pode ocorrer de diferentes formas.

### Simplex

A comunicação ocorre em apenas uma direção.

### Half-Duplex

Os dois lados podem transmitir, mas não simultaneamente.

### Full-Duplex

Os dois lados conseguem transmitir simultaneamente.

Também existem diferentes formas de comunicação quanto ao número de participantes, como:

- Unicast
- Broadcast
- Multicast

---

# 🌐 Modelos de Rede

## Modelo OSI

O modelo OSI divide a comunicação em sete camadas:

1. Física
2. Enlace de Dados
3. Rede
4. Transporte
5. Sessão
6. Apresentação
7. Aplicação

Cada camada possui responsabilidades específicas dentro do processo de comunicação.

---

## Modelo TCP/IP

O modelo TCP/IP é utilizado como referência prática para as comunicações em redes modernas.

Suas camadas são normalmente representadas como:

1. Acesso à Rede
2. Internet
3. Transporte
4. Aplicação

O modelo TCP/IP possui relação direta com protocolos utilizados na Internet, como IP, TCP, UDP, HTTP e DNS.

---

# 🔌 Protocolos e Portas

Protocolos definem regras utilizadas para comunicação entre dispositivos.

Alguns exemplos importantes:

| Protocolo | Função | Porta comum |
|-----------|--------|-------------|
| HTTP | Comunicação web | 80 |
| HTTPS | Comunicação web com TLS | 443 |
| DNS | Resolução de nomes | 53 |
| SSH | Acesso remoto seguro | 22 |
| FTP | Transferência de arquivos | 21 |
| SMTP | Envio de e-mails | 25 |
| TCP | Transporte orientado à conexão | — |
| UDP | Transporte sem conexão | — |

Uma porta identifica um ponto lógico associado a um serviço dentro de um host.

Em um pentest, descobrir quais portas estão abertas pode ajudar a identificar os serviços disponíveis e possíveis superfícies de ataque.

---

# 🖥️ IP e MAC

## Endereço IP

O endereço IP identifica logicamente um dispositivo dentro de uma rede.

Exemplo de IPv4:

```text
192.168.1.10
```

## Endereço MAC

O endereço MAC está associado à interface de rede e é utilizado principalmente na comunicação da camada de enlace.

Exemplo:
```
00:1A:2B:3C:4D:5E
```

Enquanto o IP é utilizado no roteamento entre redes, o MAC possui papel importante na comunicação dentro do segmento de rede local.

## 🧮 IP Subnetting

Subnetting é o processo de dividir uma rede IP em redes menores.

Isso permite:

Melhor organização da infraestrutura.
Separação de segmentos.
Redução do domínio de broadcast.
Melhor utilização dos endereços IP.
Segmentação de redes.

Exemplo:
```
192.168.1.0/24
```
Uma rede /24 possui 256 endereços no espaço IPv4, sendo normalmente 254 utilizáveis em uma rede tradicional.

Ao aplicar subnetting, essa rede pode ser dividida em redes menores, como:
```
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```
Esse conhecimento é fundamental para compreender roteamento, segmentação e alcance de hosts durante um pentest.
