# Camada de Rede e Endereçamento IP

> Módulo: Introduction to Networking
> Plataforma: Hack The Box Academy

---

# Introdução

Neste estudo aprofundei meus conhecimentos sobre a Camada de Rede (Layer 3) do modelo OSI, responsável por permitir que os dados encontrem o caminho correto entre a origem e o destino.

Também estudei como funciona o endereçamento IPv4, representação em binário, máscaras de sub-rede, CIDR e alguns dos principais protocolos utilizados nessa camada.

---

# Camada de Rede (Network Layer)

A Camada de Rede é responsável por permitir que pacotes atravessem diferentes redes até chegarem ao destino.

Enquanto as camadas inferiores cuidam da comunicação dentro de uma mesma rede física, a Camada 3 permite que dispositivos localizados em redes completamente diferentes consigam se comunicar.

Suas principais funções são:

- Endereçamento lógico (IP)
- Roteamento de pacotes
- Escolha do melhor caminho até o destino
- Encaminhamento entre roteadores

Em outras palavras, é essa camada que faz a Internet funcionar em grande escala.

---

# Protocolos da Camada 3

Durante o módulo conheci alguns protocolos importantes:

## IPv4 / IPv6

Responsáveis pelo endereçamento lógico dos dispositivos.

Cada equipamento conectado à rede recebe um endereço IP que permite sua identificação.

---

## ICMP

Utilizado para diagnóstico e controle da rede.

É o protocolo utilizado por ferramentas como:

- ping
- traceroute

---

## IPsec

Conjunto de protocolos responsável por adicionar segurança às comunicações IP através de autenticação e criptografia.

Muito utilizado em VPNs.

---

## RIP

Protocolo de roteamento dinâmico simples.

Os roteadores trocam informações para descobrir caminhos até outras redes.

---

## OSPF

Também é um protocolo de roteamento, porém muito mais eficiente e utilizado em redes corporativas.

Calcula automaticamente o melhor caminho para o envio dos pacotes.

---

## IGMP

Responsável pelo gerenciamento de grupos Multicast.

Permite que dispositivos participem ou saiam de grupos de comunicação.

---

# Endereço IP

Aprendi que um endereço IP funciona como o endereço de uma residência.

Enquanto o endereço MAC identifica fisicamente um equipamento dentro da rede local, o endereço IP identifica sua localização lógica na rede.

Sem um endereço IP seria impossível localizar corretamente um dispositivo na Internet.

---

# Estrutura do IPv4

O IPv4 possui:

- 32 bits
- dividido em 4 octetos
- cada octeto possui 8 bits
- valores entre 0 e 255

Exemplo:

192.168.10.39

Cada número representa um octeto.

---

# Sistema Binário

Também estudei como um endereço IPv4 é representado em binário.

Cada octeto possui oito bits.

Exemplo:

Decimal

192

Binário

11000000

Essa representação é utilizada pelos dispositivos durante o processamento dos pacotes.

---

# Máscara de Sub-rede

A máscara de sub-rede determina qual parte do endereço IP representa:

- Rede (Network)
- Host

Exemplo:

IP

192.168.10.39

Máscara

255.255.255.0

Assim é possível identificar quais dispositivos pertencem à mesma rede.

---

# CIDR

O CIDR é uma forma mais simples de representar a máscara de sub-rede.

Em vez de escrever:

255.255.255.0

escrevemos:

192.168.10.39/24

O número após a barra indica quantos bits pertencem à parte da rede.

---

# Network Address

É o endereço que identifica toda a rede.

Não pode ser atribuído a um dispositivo.

---

# Broadcast Address

É utilizado para enviar um pacote para todos os dispositivos daquela rede ao mesmo tempo.

---

# Default Gateway

É o endereço do roteador responsável por encaminhar os pacotes para outras redes.

Sempre que o destino não pertence à rede local, o computador envia o pacote primeiro para o gateway.

---

# O que aprendi

Após esse estudo passei a entender melhor:

- Como um dispositivo é identificado na Internet.
- Como os roteadores encaminham pacotes.
- A diferença entre endereço IP, máscara e gateway.
- Como funciona a divisão entre rede e host.
- Como um endereço IPv4 é representado em binário.
- O papel dos principais protocolos da Camada de Rede.

Esse conhecimento é a base para entender roteamento, subnetting, VPNs, análise de tráfego e diversas atividades relacionadas ao Pentest e à Segurança da Informação.
