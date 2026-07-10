# Using the Shell

> **Módulo:** Linux Fundamentals  
> **Plataforma:** Hack The Box Academy  
> **Status:** ✅ Concluído

---

# Objetivo

Neste tópico, o objetivo foi aprender a utilizar o Shell do Linux, entendendo como interagir com o sistema operacional através do terminal e executando comandos básicos para navegação, manipulação de arquivos e obtenção de informações do sistema.

---

# O que é o Shell?

O Shell é um interpretador de comandos responsável por fazer a comunicação entre o usuário e o sistema operacional.

Sempre que um comando é digitado no terminal, o Shell interpreta esse comando e solicita ao Kernel que execute a ação correspondente.

Fluxo simplificado:

```text
Usuário
   │
   ▼
Terminal
   │
   ▼
Shell (Bash)
   │
   ▼
Kernel
   │
   ▼
Hardware
```

O Shell é uma das ferramentas mais importantes para administradores de sistemas e profissionais de Cybersecurity.

---

# Bash

Durante os laboratórios da Hack The Box, o Shell utilizado foi o **Bash (Bourne Again Shell)**.

Ele é o interpretador de comandos padrão de diversas distribuições Linux e oferece recursos como:

- Histórico de comandos
- Auto complete
- Variáveis
- Pipes
- Redirecionamentos
- Scripts em Bash

Esses recursos tornam a administração do sistema muito mais rápida e eficiente.

---

# Terminal

O terminal é a interface onde o usuário interage com o Shell.

Através dele é possível executar comandos, administrar serviços, visualizar arquivos, criar scripts e realizar praticamente qualquer tarefa no sistema operacional.

Grande parte das ferramentas utilizadas em Pentest também é executada diretamente pelo terminal.

---

# Estrutura de um comando

A maioria dos comandos segue uma estrutura semelhante:

```bash
comando [opções] [argumentos]
```

Exemplo:

```bash
ls -la /home
```

Neste exemplo:

- `ls` → comando
- `-la` → opções
- `/home` → argumento

---

# Comandos básicos

## pwd

Exibe o diretório atual.

```bash
pwd
```

Saída:

```text
/home/kali
```

---

## whoami

Mostra qual usuário está utilizando o sistema.

```bash
whoami
```

Saída:

```text
kali
```

---

## hostname

Exibe o nome da máquina.

```bash
hostname
```

---

## clear

Limpa a tela do terminal.

```bash
clear
```

Atalho:

```text
Ctrl + L
```

---

## man

Exibe o manual de um comando.

```bash
man ls
```

É uma das ferramentas mais importantes para aprender novos comandos.

---

## help

Alguns comandos possuem ajuda integrada.

```bash
ls --help
```

---

# Auto Complete

Uma das funcionalidades mais úteis do Bash é o autocompletar utilizando a tecla **TAB**.

Exemplo:

```bash
cd Doc
```

Pressionando **TAB**, o Bash completa automaticamente o nome do diretório caso ele exista.

Isso reduz erros de digitação e aumenta a produtividade.

---

# Histórico de comandos

O Bash mantém um histórico dos comandos executados.

É possível navegar utilizando:

```text
↑
↓

```

Ou visualizar todo o histórico:

```bash
history
```

Também é possível executar novamente um comando utilizando seu número:

```bash
!25
```

---

# Variáveis de ambiente

O Shell possui diversas variáveis que armazenam informações importantes.

Para visualizar uma variável:

```bash
echo $HOME
```

Outros exemplos:

```bash
echo $USER

echo $PATH

echo $SHELL
```

Essas variáveis são utilizadas constantemente por programas e scripts.

---

# Curingas (Wildcards)

Os wildcards permitem trabalhar com vários arquivos ao mesmo tempo.

## *

Representa qualquer sequência de caracteres.

```bash
ls *.txt
```

Lista todos os arquivos com extensão `.txt`.

---

## ?

Representa exatamente um caractere.

```bash
ls file?.txt
```

Pode encontrar:

```text
file1.txt
file2.txt
```

---

# Atalhos úteis

| Atalho | Função |
|---------|--------|
| Ctrl + C | Interrompe um processo |
| Ctrl + L | Limpa o terminal |
| Ctrl + A | Início da linha |
| Ctrl + E | Final da linha |
| Tab | Auto complete |
| ↑ ↓ | Histórico de comandos |

---

# Por que aprender o Shell?

Embora existam interfaces gráficas para praticamente todas as tarefas, o Shell continua sendo a forma mais poderosa de administrar um sistema Linux.

Na área de Cybersecurity, praticamente todas as ferramentas são executadas através do terminal.

Conhecer bem o Shell facilita atividades como:

- Enumeração
- Administração de servidores
- Execução de scripts
- Automação
- Manipulação de arquivos
- Uso de ferramentas de Pentest

---

# Conclusão

Neste tópico aprendi como o Shell funciona e como ele atua como intermediário entre o usuário e o Kernel.

Também conheci comandos básicos, estrutura dos comandos, uso do histórico, variáveis de ambiente, auto complete e wildcards.

Esses conceitos servem como base para praticamente todas as atividades realizadas em ambientes Linux e serão utilizados durante todo o restante dos estudos.

---

# Principais conceitos estudados

- O que é um Shell
- Bash
- Terminal
- Estrutura de comandos
- Comandos básicos
- Histórico de comandos
- Variáveis de ambiente
- Auto complete
- Wildcards
- Atalhos do terminal
