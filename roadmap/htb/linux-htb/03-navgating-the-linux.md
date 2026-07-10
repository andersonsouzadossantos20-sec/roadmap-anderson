# Navigating the Linux Operating System

> **Módulo:** Linux Fundamentals  
> **Plataforma:** Hack The Box Academy  
> **Status:** ✅ Concluído

---

# Objetivo

Aprender a navegar pelo sistema de arquivos Linux utilizando o terminal, compreendendo a estrutura de diretórios e os principais comandos utilizados no dia a dia.

---

# Introdução

Grande parte da administração de sistemas Linux é realizada através do terminal. Saber localizar diretórios, navegar entre eles e visualizar seu conteúdo é uma habilidade essencial para administradores de sistemas e profissionais de Cybersecurity.

---

# Estrutura de Caminhos

Existem dois tipos de caminhos no Linux.

## Caminho Absoluto

Sempre começa pelo diretório raiz (`/`).

Exemplo:

```bash
/home/kali/Documents
```

Não importa onde você esteja, esse caminho sempre apontará para o mesmo local.

---

## Caminho Relativo

É baseado no diretório atual.

Exemplo:

```bash
Documents
```

ou

```bash
../Downloads
```

---

# Diretórios Especiais

| Símbolo | Significado |
|----------|-------------|
| `/` | Diretório raiz |
| `.` | Diretório atual |
| `..` | Diretório anterior |
| `~` | Diretório HOME do usuário |

Exemplos:

```bash
cd ~

cd ..

cd .
```

---

# Principais comandos

## pwd

Mostra o diretório atual.

```bash
pwd
```

---

## ls

Lista arquivos e diretórios.

```bash
ls
```

Opções comuns:

```bash
ls -l
```

Lista detalhada.

```bash
ls -la
```

Mostra arquivos ocultos.

---

## cd

Altera o diretório atual.

```bash
cd /home/kali

cd ..

cd ~

cd /
```

---

## tree

Exibe a estrutura de diretórios em formato de árvore.

```bash
tree
```

Caso não esteja instalado:

```bash
sudo apt install tree
```

---

# Arquivos Ocultos

Arquivos iniciados com "." ficam ocultos.

Exemplo:

```text
.bashrc
.profile
```

Para visualizá-los:

```bash
ls -la
```

---

# Navegação eficiente

Alguns atalhos úteis:

```text
Tab → Auto completar

↑ ↓ → Histórico

Ctrl + L → Limpar terminal
```

---

# Aplicação em Cybersecurity

Durante atividades de Pentest é comum navegar rapidamente entre diretórios contendo ferramentas, exploits, wordlists e evidências coletadas durante um teste.

Dominar a navegação no Linux aumenta significativamente a produtividade.

---

# Anotações Pessoais

- Entender caminhos absolutos e relativos facilitou bastante a navegação.
- Os comandos `pwd`, `ls` e `cd` acabam sendo utilizados praticamente o tempo todo.
- Pequenos atalhos como `Tab` ajudam muito durante o uso do terminal.

---

# Resumo

Neste tópico aprendi como navegar pelo sistema de arquivos Linux utilizando caminhos absolutos e relativos, além de utilizar comandos fundamentais para localizar diretórios e visualizar seu conteúdo.
