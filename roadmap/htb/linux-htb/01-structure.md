# Linux Structure

> **Módulo:** Linux Fundamentals  
> **Plataforma:** Hack The Box Academy  
> **Status:** ✅ Concluído

---

# Objetivo

Neste tópico, o objetivo foi compreender a estrutura básica do sistema operacional Linux, conhecer seus principais componentes e entender como eles trabalham juntos. Antes de aprender comandos e administração do sistema, é importante saber como o Linux é organizado internamente.

---

# O que é o Linux?

Linux é um sistema operacional de código aberto inspirado no Unix. Ele é amplamente utilizado em servidores, ambientes de desenvolvimento, computação em nuvem e distribuições voltadas para segurança ofensiva, como Kali Linux e Parrot OS.

Sua popularidade está relacionada à estabilidade, segurança, flexibilidade e à possibilidade de personalização.

---

# Arquitetura do Linux

O Linux é composto por diferentes camadas, onde cada uma possui uma função específica.

```text
               Usuário
                  │
        Aplicações e Programas
                  │
              Shell (Bash)
                  │
               Kernel
                  │
              Hardware
```

Cada camada possui um papel importante para o funcionamento do sistema.

---

## Hardware

O hardware corresponde à parte física do computador.

Exemplos:

- Processador (CPU)
- Memória RAM
- Disco (HD/SSD)
- Placa de Rede
- Monitor
- Teclado

O hardware não é acessado diretamente pelos programas. Toda comunicação passa pelo Kernel.

---

## Kernel

O Kernel é considerado o núcleo do sistema operacional.

Ele é responsável por controlar praticamente todos os recursos do computador.

Principais responsabilidades:

- Gerenciamento de memória
- Gerenciamento de processos
- Controle de dispositivos
- Comunicação com o hardware
- Gerenciamento do sistema de arquivos
- Controle de rede

Sempre que um programa precisa acessar algum recurso do computador, essa solicitação é feita ao Kernel.

---

## Shell

O Shell é a interface entre o usuário e o sistema operacional.

Sua principal função é interpretar comandos digitados no terminal e enviá-los ao Kernel para execução.

Exemplo:

```bash
pwd
ls
cd
mkdir
```

Durante os estudos, o Shell utilizado foi o **Bash (Bourne Again Shell)**, um dos interpretadores de comandos mais utilizados nas distribuições Linux.

---

## Aplicações

As aplicações são os programas executados pelo usuário.

Exemplos:

- Firefox
- Python
- Nmap
- Wireshark
- Burp Suite
- VS Code

Esses programas utilizam chamadas ao sistema (System Calls) para solicitar serviços ao Kernel.

---

# Estrutura de Diretórios

Diferente do Windows, onde existem unidades como `C:\` e `D:\`, o Linux organiza todos os arquivos a partir de um único diretório chamado **Root** (`/`).

Exemplo da estrutura:

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── media
├── opt
├── proc
├── root
├── run
├── srv
├── sys
├── tmp
├── usr
└── var
```

---

## Principais diretórios

| Diretório | Função |
|-----------|---------|
| `/` | Diretório raiz do sistema |
| `/home` | Arquivos pessoais dos usuários |
| `/root` | Diretório do usuário administrador |
| `/etc` | Arquivos de configuração |
| `/var` | Logs e arquivos variáveis |
| `/tmp` | Arquivos temporários |
| `/usr` | Programas e bibliotecas |
| `/bin` | Comandos essenciais |
| `/opt` | Softwares opcionais |
| `/dev` | Arquivos que representam dispositivos |

Conhecer essa estrutura facilita a localização de arquivos e a administração do sistema.

---

# Distribuições Linux

O Linux possui diversas distribuições (distros), desenvolvidas para diferentes objetivos.

Algumas das mais conhecidas são:

- Ubuntu
- Debian
- Fedora
- Arch Linux
- Kali Linux
- Parrot OS

Embora compartilhem o mesmo Kernel, cada distribuição possui suas próprias ferramentas, gerenciadores de pacotes e filosofias de uso.

---

# Linux na Cybersecurity

O Linux é amplamente utilizado na área de Segurança da Informação.

Grande parte das ferramentas utilizadas por profissionais de Pentest e Red Team foi desenvolvida para esse sistema operacional.

Além disso, muitos servidores que hospedam aplicações web utilizam Linux, tornando seu conhecimento essencial para atividades como:

- Enumeração
- Administração de servidores
- Análise de logs
- Automação
- Desenvolvimento de scripts
- Testes de invasão

---

# Conclusão

Entender a estrutura do Linux é o primeiro passo para trabalhar com esse sistema operacional de forma eficiente.

Conhecer conceitos como Kernel, Shell, sistema de arquivos e organização dos diretórios facilita o aprendizado dos próximos tópicos, como navegação, gerenciamento de arquivos, permissões e administração do sistema.

Essa base também é indispensável para quem deseja atuar na área de Cybersecurity, já que o Linux está presente na maior parte dos ambientes utilizados por profissionais de segurança.

---

# Principais conceitos estudados

- O que é Linux
- Arquitetura do sistema
- Hardware
- Kernel
- Shell
- Aplicações
- Estrutura de diretórios
- Distribuições Linux
- Importância do Linux para Cybersecurity
