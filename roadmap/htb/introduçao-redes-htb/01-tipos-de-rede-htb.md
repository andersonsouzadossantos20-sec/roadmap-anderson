# Tipos de Redes

> **Módulo:** Introduction to Networking  
> **Plataforma:** Hack The Box Academy  
> **Status:** ✅ Concluído

---

# Introdução

Depois de terminar os módulos de Linux e Windows, comecei a estudar um dos assuntos mais importantes para quem quer trabalhar com Cybersecurity: **Redes**.

Antes desse módulo eu sabia, por exemplo, o que era uma LAN ou uma VPN, mas nunca tinha parado para entender onde cada tipo de rede realmente se encaixa ou por que elas existem.

Foi um daqueles assuntos que parecem simples à primeira vista, mas que fazem bastante diferença quando você entende o contexto.

---

# Por que existem diferentes tipos de redes?

Nem toda rede possui o mesmo objetivo.

Uma rede dentro da minha casa é completamente diferente da estrutura utilizada por um provedor de Internet.

Conforme a quantidade de dispositivos aumenta e a distância entre eles também cresce, surgem diferentes tecnologias para resolver esses problemas.

Foi exatamente isso que esse tópico mostrou.

---

# LAN (Local Area Network)

A LAN é provavelmente a rede que mais utilizamos no dia a dia.

Ela conecta dispositivos dentro de uma área relativamente pequena.

Exemplos:

- Minha rede doméstica.
- Laboratórios.
- Empresas.
- Escolas.

Características:

- Alta velocidade.
- Baixa latência.
- Administração local.

Sempre que meu computador conversa com outro dispositivo conectado ao mesmo roteador, normalmente essa comunicação acontece dentro de uma LAN.

---

# WAN (Wide Area Network)

Quando precisamos conectar redes que estão em locais diferentes, entramos no conceito de WAN.

Ela cobre distâncias muito maiores do que uma LAN.

Exemplos:

- Filiais de uma empresa.
- Diferentes cidades.
- Diferentes países.
- A própria Internet.

Enquanto uma LAN conecta dispositivos próximos, uma WAN conecta redes inteiras.

---

# WLAN (Wireless Local Area Network)

A WLAN nada mais é do que uma LAN utilizando comunicação sem fio.

Na prática, é o Wi-Fi que utilizamos diariamente.

Vantagens:

- Mobilidade.
- Facilidade de instalação.

Desvantagens:

- Mais interferência.
- Alcance limitado.
- Necessidade de proteger a comunicação utilizando criptografia.

---

# VPN (Virtual Private Network)

Esse foi um conceito que fez bastante sentido porque eu já utilizava na Hack The Box sem entender exatamente o que estava acontecendo.

Sempre que inicio a VPN da HTB no Kali Linux, minha máquina passa a fazer parte da rede privada da plataforma.

Isso permite acessar laboratórios que normalmente não estariam disponíveis pela Internet.

A VPN cria um túnel criptografado entre dois pontos, protegendo a comunicação mesmo utilizando uma rede pública.

Ela é muito utilizada para:

- Trabalho remoto.
- Acesso seguro.
- Proteção da comunicação.
- Conectar diferentes redes privadas.

---

# BGP (Border Gateway Protocol)

Esse foi um dos conceitos mais interessantes do módulo.

O BGP é o protocolo responsável por permitir que diferentes provedores de Internet troquem informações de roteamento.

Em outras palavras, ele ajuda a Internet a descobrir qual o melhor caminho para que um pacote saia da minha rede e chegue ao destino.

Sem esse protocolo seria praticamente impossível manter a Internet funcionando da forma que conhecemos hoje.

---

# MAN (Metropolitan Area Network)

A MAN fica entre uma LAN e uma WAN.

Seu objetivo é conectar diferentes locais dentro de uma mesma cidade.

Exemplos:

- Universidades.
- Hospitais.
- Órgãos públicos.
- Empresas com vários prédios.

---

# PAN (Personal Area Network)

A PAN é uma rede extremamente pequena.

Ela conecta dispositivos pessoais próximos ao usuário.

Exemplos:

- Notebook + Smartphone.
- Smartphone + Tablet.

---

# WPAN (Wireless Personal Area Network)

A WPAN funciona da mesma forma que a PAN, porém utilizando comunicação sem fio.

Tecnologias bastante utilizadas:

- Bluetooth.
- ZigBee.
- NFC.

É esse tipo de rede que permite conectar um fone Bluetooth ao celular, por exemplo.

---

# O que isso muda na Cybersecurity?

Antes eu enxergava "rede" como praticamente a mesma coisa em qualquer ambiente.

Depois desse estudo ficou mais claro que existem diversos cenários diferentes.

Cada tipo de rede possui características próprias, tecnologias diferentes e desafios específicos de segurança.

Isso influencia diretamente a forma como um profissional realiza:

- Reconhecimento.
- Análise de tráfego.
- Segmentação de redes.
- Testes de invasão.
- Monitoramento.

Quanto melhor entendemos a infraestrutura, mais fácil fica compreender onde determinados ataques podem acontecer.

---

# O que ficou de aprendizado

Depois desse estudo consegui entender melhor:

- A diferença entre LAN, WAN, WLAN e VPN.
- Onde cada tipo de rede é utilizado.
- Como a própria Hack The Box utiliza uma VPN para conectar os laboratórios.
- A importância do BGP para o funcionamento da Internet.
- Que redes diferentes exigem abordagens diferentes durante uma análise de segurança.

Esse foi um ótimo começo para entender redes de forma mais estruturada, algo que certamente vai fazer diferença nos próximos módulos.
