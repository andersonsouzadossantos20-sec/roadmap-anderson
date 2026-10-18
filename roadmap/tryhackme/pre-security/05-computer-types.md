# TryHackMe — Computer Types

- **Roadmap:** Pre Security → Computer Fundamentals  
- **Data:** 18/10/2026  
- **Status:** Concluída  
- **Link:** [https://tryhackme.com/room/computertypes](https://tryhackme.com/room/computertypes)

---

## 📚 Resumo

Room introdutória que explora os diferentes tipos de computadores, desde laptops e desktops até chips embutidos em objetos do dia a dia (como cafeteiras e geladeiras inteligentes). Mostra que computadores estão em todo lugar e que cada tipo é projetado com trade-offs específicos para atender a um propósito.

---

## 🧠 Aprendizados

- Identificar os principais tipos de computadores e suas finalidades
- Diferenciar computadores com interface direta (laptop, desktop, workstation) dos que operam sem tela/teclado (servidores e embarcados)
- Compreender a diferença entre dispositivos IoT e sistemas embarcados (embedded)
- Entender os trade-offs de design (portabilidade × desempenho, especialização × custo, conectividade × simplicidade)
- Reconhecer que computadores críticos muitas vezes são os “invisíveis”

---

## 💻 Comandos / Ferramentas

| Ferramenta | Finalidade | Resultado |
|------------|------------|-----------|
| Site estático interativo (Task 4) | Identificar e classificar 8 tipos de computadores em cenários práticos | Flag obtida: `THM{8_computer_types}` |

---

## 📝 Anotações

### Tipos de computadores (Month 1)

| Tipo          | Características principais                          | Melhor para                          |
|---------------|-----------------------------------------------------|--------------------------------------|
| **Laptop**    | Portátil, alimentado por bateria, resfriamento limitado | Uso diário e mobilidade             |
| **Desktop**   | Fixo, melhor resfriamento, desempenho sustentado    | Trabalho contínuo e alto desempenho |
| **Workstation** | Componentes especializados, alta precisão e confiabilidade | Tarefas profissionais (3D, simulações, edição 4K) |
| **Server**    | Sem tela/teclado dedicados, roda 24/7, atende múltiplos usuários | Hospedagem de serviços e sites      |

### Tipos de computadores (Month 2)

- **Smartphone:** computador de bolso mais popular, otimizado para bateria e conectividade
- **Tablet:** experiência focada em toque
- **IoT (Internet of Things):** dispositivos conectados à rede com função específica (ex: smart doorbell, smart fridge)
- **Embedded (Embarcado):** computador embutido dentro de outro dispositivo, muitas vezes sem conexão à internet (ex: cafeteira, porta automática)

### Por que existem tipos diferentes?

Todo design de computador envolve **trade-offs**:
- Portabilidade × Desempenho sustentado
- Especialização × Custo
- Conectividade × Simplicidade / confiabilidade

O computador “certo” depende da tarefa que precisa ser realizada.

---

## ⚠️ Dificuldades

- [Registrar se houve dificuldade em distinguir IoT de Embedded ou em algum cenário do site interativo.]

---

## 🔗 Referências

- [Computer Types — TryHackMe](https://tryhackme.com/room/computertypes)

---

## ✅ Revisão

- [x] Room concluída
- [x] Consigo explicar a diferença entre Laptop, Desktop, Workstation e Server
- [x] Consigo distinguir Smartphone, Tablet, IoT e Embedded
- [x] Entendo os principais trade-offs de design de computadores
