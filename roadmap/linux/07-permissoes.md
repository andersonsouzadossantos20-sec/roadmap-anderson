# Permissions Management

> **Módulo:** Linux Fundamentals
> **Plataforma:** Hack The Box Academy
> **Status:** ✅ Concluído

---

# Objetivo

Entender como o Linux controla o acesso a arquivos e diretórios através do sistema de permissões.

---

# Introdução

Um dos principais mecanismos de segurança do Linux é o sistema de permissões.

Cada arquivo ou diretório possui permissões que determinam quem pode visualizar, modificar ou executar determinado recurso.

---

# Estrutura das Permissões

Exemplo:

```text
-rwxr-xr--
```

Essa sequência representa:

```text
Tipo

Usuário

Grupo

Outros
```

---

# Tipos de Permissão

| Permissão | Significado |
|-----------|-------------|
| r | Read (Leitura) |
| w | Write (Escrita) |
| x | Execute (Execução) |

---

# Usuário, Grupo e Outros

As permissões são divididas em três categorias:

- Owner (Usuário)
- Group (Grupo)
- Others (Outros)

---

# chmod

Altera permissões.

Modo simbólico:

```bash
chmod u+x script.sh
```

Modo numérico:

```bash
chmod 755 script.sh
```

---

# Sistema Octal

| Valor | Permissão |
|-------:|-----------|
| 7 | rwx |
| 6 | rw- |
| 5 | r-x |
| 4 | r-- |
| 0 | --- |

Exemplo:

```bash
chmod 644 arquivo.txt
```

---

# chown

Altera o proprietário.

```bash
sudo chown kali arquivo.txt
```

---

# chgrp

Altera o grupo.

```bash
sudo chgrp developers projeto
```

---

# ls -l

Visualizar permissões.

```bash
ls -l
```

Exemplo:

```text
-rwxr-xr-x
```

---

# Permissões Especiais

Durante os estudos também conheci permissões especiais importantes.

## SUID

Permite executar um programa com os privilégios do proprietário.

---

## SGID

Arquivos executam com o grupo do proprietário.

Diretórios fazem novos arquivos herdarem o grupo.

---

## Sticky Bit

Muito utilizado em diretórios compartilhados.

Mesmo que todos possuam escrita, apenas o proprietário pode remover seus próprios arquivos.

Exemplo clássico:

```text
/tmp
```

---

# Aplicação em Cybersecurity

Permissões incorretas podem permitir:

- Escalonamento de privilégios.
- Execução indevida de programas.
- Vazamento de informações.
- Alteração de arquivos críticos.

Durante um Pentest, verificar permissões é uma das primeiras atividades realizadas após obter acesso ao sistema.

---

# Anotações Pessoais

- O sistema de permissões é uma das principais camadas de segurança do Linux.
- Entender o significado do `rwx` facilita muito a administração do sistema.
- Permissões especiais como SUID aparecem frequentemente em laboratórios de privilege escalation.

---

# Resumo

Neste tópico aprendi como o Linux controla o acesso aos arquivos através do sistema de permissões, utilizando comandos como `chmod`, `chown` e `chgrp`, além de compreender permissões especiais importantes para administração e segurança do sistema.
