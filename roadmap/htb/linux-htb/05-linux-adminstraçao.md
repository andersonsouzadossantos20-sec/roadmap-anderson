# Working with Files and Directories

> **Módulo:** Linux Fundamentals  
> **Plataforma:** Hack The Box Academy  
> **Status:** ✅ Concluído

---

# Objetivo

Aprender a criar, copiar, mover, remover e visualizar arquivos e diretórios utilizando os comandos do Linux.

---

# Introdução

Grande parte da administração de sistemas envolve manipulação de arquivos.

O Linux disponibiliza diversas ferramentas que permitem realizar essas tarefas diretamente pelo terminal.

---

# Criando diretórios

Utilizando:

```bash
mkdir
```

Exemplo:

```bash
mkdir projetos
```

Criando vários diretórios:

```bash
mkdir pentest scripts wordlists
```

---

# Criando arquivos

Comando:

```bash
touch
```

Exemplo:

```bash
touch notas.txt
```

---

# Copiando arquivos

Utilizando:

```bash
cp
```

Exemplo:

```bash
cp arquivo.txt backup.txt
```

Copiando diretórios:

```bash
cp -r pasta backup
```

---

# Movendo arquivos

Comando:

```bash
mv
```

Exemplo:

```bash
mv arquivo.txt Documentos/
```

Também pode ser utilizado para renomear arquivos.

```bash
mv teste.txt notas.txt
```

---

# Removendo arquivos

```bash
rm arquivo.txt
```

Removendo diretórios:

```bash
rm -r pasta
```

Para remover sem confirmação:

```bash
rm -rf pasta
```

⚠️ Deve ser utilizado com cuidado.

---

# Localizando arquivos

Comando:

```bash
find
```

Exemplo:

```bash
find /home -name "*.txt"
```

---

# Visualizando arquivos

## cat

Mostra todo o conteúdo.

```bash
cat arquivo.txt
```

---

## less

Permite navegar pelo conteúdo.

```bash
less arquivo.txt
```

---

## head

Mostra as primeiras linhas.

```bash
head arquivo.txt
```

---

## tail

Mostra as últimas linhas.

```bash
tail arquivo.txt
```

Também pode acompanhar arquivos em tempo real.

```bash
tail -f log.txt
```

---

# Compactação

Criando um arquivo compactado:

```bash
tar -czvf backup.tar.gz pasta/
```

Extraindo:

```bash
tar -xzvf backup.tar.gz
```

---

# Aplicação em Cybersecurity

Manipular arquivos é uma atividade constante durante um Pentest.

Alguns exemplos:

- Organizar evidências.
- Copiar logs.
- Baixar exploits.
- Compactar resultados.
- Localizar arquivos sensíveis.
- Analisar configurações.

---

# Anotações Pessoais

- Os comandos `cp`, `mv` e `rm` possuem sintaxe simples, mas devem ser utilizados com atenção.
- O comando `find` mostrou-se extremamente útil para localizar arquivos rapidamente.
- O `tail -f` é bastante interessante para acompanhar logs em tempo real.

---

# Resumo

Neste tópico aprendi os principais comandos utilizados para manipular arquivos e diretórios no Linux, incluindo criação, cópia, movimentação, remoção, busca e visualização de conteúdo.
