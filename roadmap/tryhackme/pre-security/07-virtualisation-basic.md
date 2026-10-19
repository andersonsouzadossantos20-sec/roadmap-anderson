# TryHackMe — Virtualisation Basics

- **Roadmap:** Pre Security → Computer Fundamentals  
- **Data:** 19/10/2026  
- **Status:** Concluída  
- **Link:** [https://tryhackme.com/room/virtualisationbasics](https://tryhackme.com/room/virtualisationbasics)

---

## 📚 Resumo

Room que explica por que a virtualização é fundamental no IT moderno. Mostra como um único servidor físico pode rodar várias máquinas virtuais, melhorando o aproveitamento de hardware, reduzindo custos e permitindo isolamento seguro de ambientes. Também introduz o conceito de containers.

---

## 🧠 Aprendizados

- Entender por que “um servidor físico = um aplicativo” é ineficiente
- Compreender como a virtualização resolve problemas de utilização e escalabilidade
- Conhecer os componentes de uma máquina virtual e o papel do hypervisor
- Diferenciar hypervisor Type 1 e Type 2
- Entender a diferença entre Máquinas Virtuais e Containers

---

## 💻 Comandos / Ferramentas

| Ferramenta / Conceito | Finalidade | Resultado |
|-----------------------|------------|-----------|
| Lab interativo de gerenciamento de VMs | Reiniciar servidor, criar nova VM e analisar recursos | Atividade prática concluída |

---

## 📝 Anotações

### Por que virtualizar?

Antes da virtualização:
- Cada aplicação precisava de um servidor físico próprio
- Hardware ficava subutilizado
- Custos altos e escalabilidade difícil

Com virtualização:
- Várias VMs compartilham o mesmo servidor físico
- Melhor aproveitamento de CPU, RAM e armazenamento
- Isolamento entre ambientes

### Componentes principais

| Componente | Função |
|------------|--------|
| **Hypervisor** | Software que cria e gerencia as máquinas virtuais (o “síndico” do prédio) |
| **Máquina Virtual (VM)** | Computador virtual completo (próprio SO, CPU, RAM, disco) |
| **Host** | Servidor físico que roda o hypervisor |
| **Guest** | Sistema operacional dentro da VM |

### Tipos de Hypervisor

- **Type 1 (Bare-metal):** roda diretamente no hardware (usado em datacenters)
- **Type 2 (Hosted):** roda em cima de um sistema operacional existente (ex: VirtualBox, VMware Workstation) — ideal para labs pessoais

### Containers vs VMs

- **Máquina Virtual:** virtualiza o hardware completo + sistema operacional
- **Container:** ambiente leve e isolado que compartilha o kernel do host e roda apenas a aplicação + dependências (mais eficiente para múltiplas aplicações pequenas)

### Lab prático (Task 4)

- Reiniciar o **Mail-SERVER** que estava com erro
- Criar a **Marketing-VM** com recursos específicos
- Identificar a VM que estava rodando há mais tempo: **Monitoring-SYS**

---

## ⚠️ Dificuldades

- [Registrar se houve dificuldade em diferenciar Type 1 / Type 2 ou Containers x VMs.]

---

## 🔗 Referências

- [Virtualisation Basics — TryHackMe](https://tryhackme.com/room/virtualisationbasics)

---

## ✅ Revisão

- [x] Room concluída
- [x] Consigo explicar por que a virtualização é importante
- [x] Entendo o papel do hypervisor
- [x] Consigo diferenciar Type 1 e Type 2
- [x] Sei a diferença entre Máquina Virtual e Container
