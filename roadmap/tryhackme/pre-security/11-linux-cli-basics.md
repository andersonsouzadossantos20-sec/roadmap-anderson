# TryHackMe — Linux Basics

- **Roadmap:** Pre Security → Computer Fundamentals
- **Data:** 23/10/2026
- **Status:** Em progresso
- **Link:** [Linux Basics](https://tryhackme.com/room/linuxclibasics)

---

## 📚 Resumo

Sala introdutória sobre os fundamentos da linha de comando do Linux. O conteúdo apresenta como navegar pelo sistema de arquivos, localizar arquivos, investigar informações do sistema operacional e consultar arquivos de configuração importantes.

Por meio de tarefas práticas, a sala simula atividades de uma equipe de suporte a operações cibernéticas, permitindo desenvolver familiaridade com o terminal Linux e compreender como essas habilidades são utilizadas na administração de sistemas e na segurança da informação.

---

## 🧠 Aprendizados

- Compreender a navegação pelo sistema de arquivos do Linux.
- Aprender a localizar arquivos e diretórios.
- Investigar informações sobre o sistema operacional.
- Conhecer arquivos de configuração importantes.
- Utilizar pistas para resolver tarefas práticas no terminal.
- Entender a importância da linha de comando na administração de sistemas.
- Construir uma base para estudar permissões, usuários, grupos, processos e gerenciamento de pacotes.

---

## 💻 Comandos / Ferramentas

| Comando / Ferramenta | Finalidade | Resultado |
|----------------------|------------|-----------|
| `pwd` | Exibir o diretório atual | Conceito para revisão |
| `ls` | Listar arquivos e diretórios | Conceito para revisão |
| `cd` | Navegar entre diretórios | Conceito para revisão |
| `find` | Localizar arquivos e diretórios | Conceito para revisão |
| `cat` | Exibir o conteúdo de arquivos de texto | Conceito para revisão |
| `grep` | Pesquisar padrões de texto em arquivos | Conceito para revisão |
| Terminal Linux | Interagir com o sistema por meio de comandos | Laboratório em andamento |

---

## 📝 Anotações

### Navegação pelo sistema de arquivos

No Linux, o terminal permite navegar pelos diretórios e interagir com arquivos sem depender de uma interface gráfica.

Comandos importantes:

- `pwd`: mostra o caminho do diretório atual.
- `ls`: lista os arquivos e diretórios.
- `cd`: permite mudar de diretório.
- `ls -la`: lista também arquivos ocultos e apresenta informações adicionais.

### Localização de arquivos

Encontrar arquivos rapidamente é uma habilidade importante para administração de sistemas e investigação de problemas.

Exemplos:

- `find /home -name "arquivo.txt"`: procura um arquivo com esse nome dentro de `/home`.
- `find . -type f`: lista arquivos regulares a partir do diretório atual.

A pesquisa pode depender das permissões de acesso e do diretório escolhido.

### Investigação do sistema

Conhecer o sistema operacional ajuda a identificar o ambiente em que estamos trabalhando.

Comandos úteis para praticar:

- `whoami`: mostra o usuário atual.
- `uname -a`: apresenta informações sobre o kernel e o sistema.
- `cat /etc/os-release`: exibe informações sobre a distribuição Linux.
- `ps aux`: lista processos em execução.

### Arquivos de configuração

O Linux utiliza arquivos de configuração para armazenar informações importantes sobre o sistema e seus serviços.

Exemplo:

- `/etc/os-release`: informações sobre a distribuição Linux.
- `/etc/hostname`: nome configurado para o sistema.
- `/etc/passwd`: informações das contas de usuários, sem armazenar suas senhas em texto puro.

É importante compreender a finalidade desses arquivos e ter cuidado ao modificá-los.

### Importância para a cibersegurança

A linha de comando é utilizada em diversas atividades de segurança da informação, como:

- Investigar processos e atividades do sistema.
- Localizar arquivos relevantes durante uma análise.
- Consultar configurações do sistema operacional.
- Verificar usuários e permissões.
- Automatizar tarefas administrativas.
- Apoiar atividades de defesa e testes de segurança autorizados.


---

## 🔗 Referências

- [Linux Basics — TryHackMe](https://tryhackme.com/room/linuxclibasics)

---

## ✅ Revisão

- [x] Tarefa 1 — Introdução.
- [x] Tarefa 2 — Missão de Navegação: "Encontre as Anotações Perdidas".
- [x] Tarefa 3 — Investigando o Sistema.
- [x] Tarefa 4 — Conclusão.
- [x] Sala concluída.
- [x] Consigo navegar pelo sistema de arquivos usando o terminal.
- [x] Sei localizar arquivos e consultar informações do sistema.
- [x] Entendo a importância dos arquivos de configuração.

---

**Conclusão:** estudo dos fundamentos da linha de comando do Linux, desenvolvendo habilidades essenciais para a administração de sistemas e para os próximos módulos de cibersegurança.
