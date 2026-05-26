# 🛡️ Registro de Estudo: Defesa de Sistemas e de Rede

**Data:** 26/05/2026  
**Curso:** Cisco Networking Academy — Defesa de Rede  
**Módulo 2:** Defesa do Sistema e da Rede  

---

## 🎯 Objetivo do Módulo
Dominar as táticas operacionais e técnicas de blindagem (*hardening*) aplicadas a hosts, redes, aplicações e sistemas especializados, visando mitigar superfícies de ataque e garantir a resiliência da infraestrutura contra incidentes.

---

## 📐 1. Proteção de Ativos e Aplicações
Implementação de barreiras de segurança focadas na infraestrutura física, nos softwares e nos protocolos de rede essenciais.

* **Segurança Física:** Proteção dos ativos tangíveis por meio de barreiras mecânicas, controle de acesso a salas de servidores, monitoramento por imagem e blindagem contra desastres ou intrusões locais.
* **Segurança de Aplicações:** Práticas voltadas a eliminar vulnerabilidades no código e nas plataformas. Envolve validação de dados, atualizações de patches de segurança e o uso de Web Application Firewalls (WAF) para conter ameaças na camada de aplicação.
* **Network Hardening (Serviços e Protocolos):** Processo de desativação de serviços desnecessários, fechamento de portas vulneráveis e substituição de protocolos inseguros (como HTTP ou Telnet) por alternativas criptografadas (como HTTPS e SSH).

---

## 🚨 2. Blindagem de Infraestrutura e Redes Sem Fio
Estratégias de isolamento lógico e proteção de perímetros dinâmicos, incluindo dispositivos móveis e redes corporativas Wi-Fi.

* **Blindagem de Rede (Segmentação):** Divisão da rede corporativa em sub-redes ou zonas isoladas (VLANs, DMZs). A segmentação impede que um atacante se mova lateralmente pela rede caso consiga comprometer um único dispositivo.
* **Blindagem e Codificação de Dispositivos Sem Fio e Móveis:** Implementação de protocolos robustos de criptografia (como WPA3) e gerenciamento centralizado de dispositivos via MDM (*Mobile Device Management*), garantindo conformidade mesmo fora do perímetro tradicional de TI.

---

## 📋 3. Resiliência e Sistemas Especializados
A capacidade de adaptação e continuidade do negócio frente a incidentes, além da proteção de ecossistemas não tradicionais de tecnologia.

* **Resiliência da Segurança Digital:** Abordagem voltada para a alta disponibilidade, redundância de sistemas e capacidade de recuperação rápida. O foco é garantir que o ecossistema de segurança consiga continuar operando ou se restabeleça em tempo mínimo após sofrer um impacto.
* **Sistemas Integrados e Especializados:** Aplicação de conceitos de segurança em ambientes de IoT (Internet das Coisas), sistemas industriais (SCADA/ICS) e dispositivos embarcados, que possuem restrições de hardware e exigem abordagens personalizadas de proteção.

---

## 🔬 Observação Prática (Defesa de Sistemas e Rede)
Enquanto o Módulo 1 focou na parte estratégica (SOC, Políticas e Governança), o Módulo 2 foca na execução técnica. A segmentação de rede e o *hardening* de serviços são as ações práticas que dão sustentação às diretrizes de Defesa em Profundidade. Sem essa redução ativa da superfície de ataque nos hosts e roteadores, o monitoramento do SOC se torna sobrecarregado e ineficiente.

---

## 📚 Termos Chave

| Termo | Definição |
| :--- | :--- |
| **Hardening** | Processo de mapear e remover funções, protocolos e portas desnecessárias para reduzir vulnerabilidades. |
| **Segmentação** | Prática de dividir uma rede de computadores em sub-redes menores para melhorar o desempenho e a segurança. |
| **Resiliência** | A capacidade de uma infraestrutura de resistir, absorver e se recuperar de ataques ou falhas operacionais. |
| **Sistemas Embarcados** | Sistemas de computação dedicados a funções específicas dentro de um produto maior (ex: dispositivos IoT). |

---

## 🧩 Insight do Dia
> "A segurança de sistemas não é definida pelo que você adiciona à sua rede, mas frequentemente pelo que você remove ou desativa. Portas abertas sem uso, serviços legados ativos e redes totalmente planas são os maiores convites para movimentos laterais de invasores. Simplificar e blindar são os primeiros passos da defesa real."

---

**Próximo Passo:** Módulo 3: Controle de Acesso / Implementação de Políticas de Identidade e Autenticação.
