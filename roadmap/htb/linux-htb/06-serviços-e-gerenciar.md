# Service Management

> **Módulo:** Linux Fundamentals
> **Plataforma:** Hack The Box Academy
> **Status:** ✅ Concluído

---

# Objetivo

Compreender como os serviços são gerenciados no Linux utilizando o systemd e o comando systemctl.

---

# Introdução

Grande parte das aplicações executadas em um servidor Linux funcionam como serviços.

Exemplos:

- SSH
- Apache
- Nginx
- MySQL
- Docker

Gerenciar corretamente esses serviços é uma atividade comum na administração de sistemas.

---

# O que é um serviço?

Um serviço é um programa executado em segundo plano (background), normalmente iniciado automaticamente durante a inicialização do sistema.

---

# Systemd

A maioria das distribuições Linux modernas utiliza o **systemd** como sistema de inicialização.

Ele é responsável por:

- Inicializar o sistema.
- Gerenciar serviços.
- Controlar dependências.
- Registrar eventos.

---

# Systemctl

O principal comando para gerenciamento de serviços é:

```bash
systemctl
```

---

## Verificar status

```bash
systemctl status ssh
```

---

## Iniciar

```bash
sudo systemctl start ssh
```

---

## Parar

```bash
sudo systemctl stop ssh
```

---

## Reiniciar

```bash
sudo systemctl restart ssh
```

---

## Habilitar inicialização automática

```bash
sudo systemctl enable ssh
```

---

## Desabilitar

```bash
sudo systemctl disable ssh
```

---

## Listar serviços

```bash
systemctl list-units --type=service
```

---

# Aplicação em Cybersecurity

Durante testes de invasão é comum identificar quais serviços estão ativos em um servidor.

Esses serviços representam possíveis pontos de entrada para exploração de vulnerabilidades.

Também é importante compreender como iniciar ou interromper serviços durante laboratórios e ambientes de testes.

---

# Anotações Pessoais

- O `systemctl` concentra praticamente todo o gerenciamento de serviços.
- O comando `status` fornece informações úteis para troubleshooting.
- Saber identificar serviços ativos facilita a enumeração de um alvo.

---

# Resumo

Neste tópico aprendi como o Linux gerencia serviços utilizando o systemd e o systemctl, realizando operações como iniciar, parar, reiniciar e verificar o estado dos serviços.
