# TryHackMe — Windows Command Line

- **Roadmap:** Pre Security → Computer Fundamentals
- **Data:** 25/10/2026
- **Status:** Concluída
- **Link:** [Windows Command Line](https://tryhackme.com/room/windowbasics)

---

## 📚 Resumo

Sala introdutória sobre a utilização da linha de comando do Windows por meio do Prompt de Comando (CMD). O conteúdo demonstra como interagir com o sistema operacional utilizando comandos de texto, sem depender exclusivamente da interface gráfica.

Durante as atividades, foram exploradas tarefas como navegar por arquivos e pastas, localizar arquivos, visualizar diretórios ocultos, ler conteúdos diretamente pelo terminal e coletar informações básicas sobre o sistema e a rede.

Essas habilidades são importantes para a administração de sistemas, a resolução de problemas e diversas atividades relacionadas à cibersegurança.

---

## 🧠 Aprendizados

- Entender como interagir com o Windows utilizando o Prompt de Comando (CMD).
- Navegar por arquivos e diretórios sem utilizar o mouse.
- Localizar arquivos mesmo quando não se conhece sua localização exata.
- Identificar arquivos e diretórios ocultos.
- Ler o conteúdo de arquivos diretamente pelo terminal.
- Coletar informações básicas sobre o sistema operacional.
- Consultar informações relacionadas à rede.
- Compreender a importância da linha de comando para administração de sistemas e cibersegurança.

---

## 💻 Comandos / Ferramentas

| Comando | Finalidade | Resultado |
|---------|------------|-----------|
| `dir` | Listar arquivos e diretórios | Conceito estudado |
| `cd` | Navegar entre diretórios | Conceito estudado |
| `cd ..` | Voltar ao diretório anterior na hierarquia | Conceito estudado |
| `type` | Exibir o conteúdo de um arquivo de texto | Conceito estudado |
| `where` | Localizar arquivos executáveis nos caminhos pesquisados | Conceito estudado |
| `ipconfig` | Consultar informações de configuração de rede | Conceito estudado |
| `systeminfo` | Exibir informações detalhadas sobre o sistema | Conceito estudado |
| Prompt de Comando (CMD) | Administrar e investigar o Windows por comandos | Sala concluída |

---

## 📝 Anotações

### O que é a linha de comando do Windows?

A linha de comando permite interagir com o sistema operacional por meio de instruções textuais.

No Windows, uma das principais ferramentas para isso é o Prompt de Comando, conhecido como CMD.

Por meio dele, é possível navegar pelo sistema de arquivos, consultar informações, executar programas e realizar tarefas administrativas.

### Navegação pelo sistema de arquivos

O CMD permite explorar diretórios e arquivos utilizando comandos.

Exemplos:

- `dir`: lista os arquivos e diretórios do local atual.
- `cd nome_da_pasta`: acessa uma pasta.
- `cd ..`: volta um nível na hierarquia de diretórios.
- `cd \`: acessa a raiz da unidade atual.

### Localização e leitura de arquivos

A linha de comando facilita a localização e a leitura de arquivos sem precisar navegar manualmente pelas pastas.

- `where notepad`: procura o executável do Notepad nos locais pesquisados pelo Windows.
- `type arquivo.txt`: exibe o conteúdo de um arquivo de texto.
- `dir /a`: lista arquivos e diretórios, incluindo itens com atributos ocultos.

É importante lembrar que o comando `where` não pesquisa automaticamente todos os diretórios do disco; ele utiliza os caminhos e critérios definidos para a pesquisa.

### Coleta de informações do sistema

Durante uma investigação ou atividade de suporte, é importante conhecer o sistema operacional em execução.

- `systeminfo`: apresenta informações sobre o sistema, como versão do Windows, memória e detalhes do computador.
- `hostname`: exibe o nome do computador.
- `whoami`: informa o usuário e o contexto de identidade atual.
- `tasklist`: lista os processos em execução.

Esses comandos ajudam a identificar o ambiente e a compreender o estado do sistema.

### Informações de rede

A linha de comando também permite consultar informações básicas sobre a conectividade e a configuração de rede.

- `ipconfig`: mostra informações das interfaces de rede, incluindo endereços IP.
- `ipconfig /all`: apresenta informações adicionais sobre as interfaces e sua configuração.

Esses dados ajudam na identificação de problemas de conectividade e na compreensão da configuração de rede do computador.

### Por que a linha de comando é importante na cibersegurança?

A linha de comando é utilizada em diferentes áreas da segurança da informação porque permite executar tarefas de maneira rápida e precisa.

Entre suas aplicações estão:

- Investigar arquivos e diretórios.
- Consultar informações do sistema.
- Identificar processos em execução.
- Verificar configurações de rede.
- Automatizar tarefas administrativas.
- Apoiar análises de segurança e investigações de incidentes.

Nem todas as informações são visíveis pela interface gráfica, e o terminal pode oferecer acesso mais direto a determinados recursos do sistema.

---

## ⚠️ Dificuldades

- [ ] Registrar os comandos que apresentaram maior dificuldade.
- [ ] Praticar a navegação entre diretórios.
- [ ] Treinar a localização e leitura de arquivos.
- [ ] Revisar os comandos para consultar informações do sistema e da rede.

---

## 🔗 Referências

- [Windows Command Line — TryHackMe](https://tryhackme.com/room/windowbasics)

---

## ✅ Revisão

- [x] Sala concluída.
- [x] Entendo a finalidade do Prompt de Comando.
- [x] Sei navegar por arquivos e diretórios utilizando comandos.
- [x] Conheço formas de localizar e ler arquivos.
- [x] Entendo como consultar informações básicas do sistema.
- [x] Conheço comandos para consultar informações de rede.
- [x] Compreendo a importância da linha de comando para a cibersegurança.

---

**Conclusão:** sala concluída no TryHackMe, fortalecendo meus conhecimentos sobre a linha de comando do Windows, navegação por arquivos, coleta de informações e administração básica do sistema.
