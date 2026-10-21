# TryHackMe — Operating Systems: Introduction

- **Roadmap:** Pre Security → Operating Systems Basics  
- **Data:** 21/10/2026  
- **Status:** Concluída  
- **Link:** [https://tryhackme.com/room/operatingsystemsintroduction](https://tryhackme.com/room/operatingsystemsintroduction)

---

## 📚 Resumo

Room introdutória sobre o que é um sistema operacional (SO), suas responsabilidades principais e como ele atua como o “gerente invisível” entre o hardware e os aplicativos. Explora conceitos como Kernel Space, User Space, gerenciamento de processos, memória, arquivos e usuários. Inclui prática em uma máquina Ubuntu MATE para coletar informações do sistema e encontrar uma flag.

---

## 🧠 Aprendizados

- Compreender o que é um sistema operacional e seu papel
- Diferenciar Kernel Space e User Space
- Conhecer as principais responsabilidades do SO (processos, memória, arquivos, usuários e dispositivos)
- Identificar tipos comuns de SO (Desktop, Server, Mobile, Embedded, Virtual/Cloud)
- Distinguir Interface Gráfica (GUI) e Interface de Linha de Comando (CLI)
- Praticar a coleta de informações do sistema em um ambiente real

---

## 💻 Comandos / Ferramentas

| Ferramenta / Ação | Finalidade | Resultado |
|-------------------|------------|-----------|
| About This Computer / System Monitor | Verificar especificações do sistema (versão, memória, disco) | Informações coletadas |
| Navegação no Home e Documents | Localizar arquivos de usuário e a flag | Flag encontrada |

---

## 📝 Anotações

### O que é um Sistema Operacional?

O **SO** é o software principal que gerencia o hardware, os aplicativos e todos os recursos do sistema. Ele atua como intermediário entre o usuário e o hardware.

### Espaços de execução

| Espaço | Características |
|--------|-----------------|
| **Kernel Space** | Área altamente privilegiada com acesso direto ao hardware. Onde o kernel é executado e gerencia os recursos do sistema. |
| **User Space** | Área onde os aplicativos comuns rodam com permissões limitadas, por segurança e estabilidade. |

### Principais responsabilidades do SO

- **Process Management** → cria, agenda, prioriza e finaliza programas
- **Memory Management** → aloca RAM e isola a memória de cada processo
- **File System Management** → organiza arquivos, diretórios, permissões e metadados
- **User Management** → gerencia contas, autenticação e permissões
- **Device Management** → carrega drivers e gerencia dispositivos conectados

### Interfaces de interação

- **GUI (Graphical User Interface)** → janelas, ícones e menus (interação por cliques)
- **CLI (Command Line Interface)** → interface baseada em texto, onde se digitam comandos com precisão e rapidez

### Tipos de Sistemas Operacionais

| Tipo | Uso principal | Características |
|------|---------------|-----------------|
| **Desktop** | Computadores pessoais, trabalho e jogos | Interface gráfica rica, multitarefa |
| **Server** | Hospedagem, bancos de dados, nuvem | Sem GUI (headless), alta disponibilidade |
| **Mobile** | Smartphones e tablets | Touch, eficiente em energia, sandboxed |
| **Embedded** | IoT, carros, eletrodomésticos | Pegada pequena, hardware limitado |
| **Virtual/Cloud** | VMs e containers | Leve, escalável, rápida implantação |

### Lab prático (Ubuntu MATE)

- Versão do Ubuntu MATE: **1.26.2**
- Memória alocada: **1.9 GiB**
- Sistema de arquivos raiz (`/dev/root`): **ext4**
- Diretórios de usuário em Home: **3**
- Flag encontrada em `/home/alex/Documents/note.txt`:  

---

## 🔗 Referências

- [Operating Systems: Introduction — TryHackMe](https://tryhackme.com/room/operatingsystemsintroduction)

---

## ✅ Revisão

- [x] Room concluída
- [x] Consigo explicar o que é um sistema operacional
- [x] Entendo a diferença entre Kernel Space e User Space
- [x] Conheço as principais responsabilidades do SO
- [x] Consigo distinguir GUI e CLI
- [x] Identifico os principais tipos de SO
