# 📚 Registro de Estudo — Cibersegurança

**Data:** 07/10/2026  
**Tema:** OWASP Top 10 (2025)  
**Área:** Segurança de Aplicações Web  
**Plataforma:** Hackviser

---

# 🎯 Objetivo do Estudo

Compreender os principais riscos de segurança em aplicações web segundo a classificação **OWASP Top 10 (2025)**.

O estudo teve como objetivo entender não apenas quais são as categorias de risco, mas também suas causas, o ponto de vista do atacante, o comportamento das requisições e respostas HTTP, as evidências que podem ser coletadas durante um teste e os controles utilizados para reduzir os riscos.

---

# 📖 Conceitos Fundamentais

- OWASP
- OWASP Top 10
- Segurança de aplicações web
- Controle de acesso
- Configuração de segurança
- Cadeia de suprimentos de software
- Criptografia
- Injeção
- Design seguro
- Autenticação
- Integridade de software e dados
- Logging e alertas de segurança
- Tratamento de condições excepcionais
- Requisições HTTP
- Respostas HTTP
- Causa raiz
- Evidências de vulnerabilidade
- Controles defensivos

---

# 🧠 Explicação Técnica

## 1. OWASP

A **OWASP (Open Worldwide Application Security Project)** é uma organização dedicada à melhoria da segurança de aplicações e desenvolvimento de recursos, metodologias e materiais relacionados à segurança de software.

Um dos projetos mais conhecidos da organização é o **OWASP Top 10**.

O Top 10 organiza riscos relevantes de segurança em aplicações web em categorias que ajudam desenvolvedores, profissionais de segurança e pentesters a identificar problemas recorrentes.

---

# 🔐 OWASP Top 10 — 2025

A versão 2025 organiza os principais riscos em dez categorias.

> As categorias representam **famílias de riscos**, e não necessariamente uma única vulnerabilidade específica.

---

## A01 — Broken Access Control

### Controle de Acesso Inseguro

Ocorre quando uma aplicação não verifica corretamente se um usuário possui autorização para executar determinada ação ou acessar determinado recurso.

Exemplo:

```http
GET /api/users/1001

Um usuário autenticado pode tentar alterar o identificador:

GET /api/users/1002

Se a aplicação retornar informações pertencentes a outro usuário sem verificar a autorização, existe uma falha de controle de acesso.

Esse tipo de problema pode aparecer em:

IDOR/BOLA
Acesso a funções administrativas
Manipulação de parâmetros
APIs
Recursos pertencentes a outros usuários
⚙️ A02 — Security Misconfiguration
Configuração de Segurança Incorreta

Acontece quando sistemas, servidores, frameworks ou aplicações são configurados de maneira insegura.

Exemplos:

Serviços desnecessários habilitados.
Configurações padrão mantidas.
Mensagens de erro excessivamente detalhadas.
Headers de segurança ausentes.
Interfaces administrativas expostas.
Permissões incorretas.

Durante um pentest, informações de configuração podem ser identificadas através de:

HTTP Headers
Mensagens de erro
Arquivos expostos
Endpoints administrativos
Configurações do servidor
📦 A03 — Software Supply Chain Failures
Falhas na Cadeia de Suprimentos de Software

Aplicações modernas dependem de componentes externos, bibliotecas, pacotes, frameworks, imagens de containers e outros recursos.

Uma vulnerabilidade ou comprometimento em uma dessas dependências pode afetar a aplicação que utiliza o componente.

Exemplos:

Aplicação
   │
   ├── Framework
   ├── Biblioteca
   ├── Pacote externo
   └── Dependência transitiva

A segurança da aplicação depende também da segurança de seus componentes e do processo utilizado para obtê-los, atualizá-los e distribuí-los.

🔑 A04 — Cryptographic Failures
Falhas Criptográficas

Essa categoria envolve problemas relacionados à proteção inadequada de informações por mecanismos criptográficos.

Exemplos de problemas:

Dados sensíveis transmitidos sem proteção adequada.
Armazenamento inseguro de informações sensíveis.
Algoritmos criptográficos inadequados.
Gerenciamento incorreto de chaves.
Senhas armazenadas de maneira insegura.

O problema não é simplesmente "não utilizar criptografia".

É necessário utilizar mecanismos criptográficos apropriados para o tipo de informação e para o contexto da aplicação.

💉 A05 — Injection
Injeção

Ocorre quando dados controlados pelo usuário são interpretados como parte de uma instrução ou comando.

Exemplos conhecidos:

SQL Injection
Command Injection
LDAP Injection
NoSQL Injection

Exemplo conceitual:

Entrada do usuário
       ↓
Aplicação
       ↓
Concatenação insegura
       ↓
Comando/consulta
       ↓
Interpretador

O problema ocorre quando a aplicação não separa adequadamente dados de instruções.

Em Web Pentest, essa categoria é especialmente importante porque pode envolver manipulação direta de parâmetros enviados através de requisições HTTP.

🏗️ A06 — Insecure Design
Design Inseguro

Essa categoria está relacionada a falhas originadas no próprio desenho da aplicação ou do fluxo de negócio.

Diferentemente de uma simples configuração incorreta ou implementação isolada, o problema pode estar na forma como o sistema foi projetado.

Exemplo conceitual:

Usuário
   ↓
Solicita operação sensível
   ↓
Sistema não possui mecanismo adequado
   ↓
Operação realizada

Mesmo que o código esteja funcionando conforme foi implementado, o sistema pode possuir um fluxo de negócio inseguro.

Por isso, segurança precisa ser considerada durante o design da aplicação, e não apenas depois da implementação.

🔐 A07 — Authentication Failures
Falhas de Autenticação

Essa categoria envolve problemas relacionados à confirmação da identidade de usuários.

Exemplos:

Mecanismos de login fracos.
Recuperação de senha insegura.
Proteções inadequadas contra ataques automatizados.
Sessões mal protegidas.
Falhas em mecanismos de autenticação multifator.

Durante um teste de segurança, o pentester pode analisar:

Login
↓
Sessão
↓
Cookies
↓
Autenticação
↓
Recuperação de conta

O objetivo é verificar se o mecanismo realmente impede que um atacante obtenha ou abuse da identidade de outro usuário.

🧾 A08 — Software or Data Integrity Failures
Falhas de Integridade de Software ou Dados

Essa categoria envolve situações nas quais a aplicação confia em software, componentes ou dados sem verificar adequadamente sua integridade.

Exemplos conceituais:

Atualizações não verificadas.
Dependências obtidas de fontes não confiáveis.
Dados críticos manipuláveis sem validação adequada.
Processos de atualização inseguros.

A integridade garante que determinado software ou dado não tenha sido alterado de maneira não autorizada.

📝 A09 — Security Logging and Alerting Failures
Falhas no Registro e Alerta de Segurança

Uma aplicação pode possuir vulnerabilidades, mas se não registrar eventos relevantes ou não gerar alertas adequados, a detecção e resposta podem ser prejudicadas.

Exemplos:

Falhas de autenticação não registradas.
Eventos de segurança sem contexto suficiente.
Ausência de alertas.
Logs insuficientes.
Falta de monitoramento de atividades suspeitas.

Exemplo:

Ataque
  ↓
Aplicação
  ↓
Evento de segurança
  ↓
Log
  ↓
Monitoramento
  ↓
Alerta
  ↓
Resposta

Quando uma dessas etapas falha, a capacidade de detectar e investigar ataques pode ser reduzida.

⚠️ A10 — Mishandling of Exceptional Conditions
Manipulação Inadequada de Condições Excepcionais

Essa categoria está relacionada ao tratamento incorreto de situações inesperadas ou excepcionais durante a execução da aplicação.

Exemplos conceituais:

Erros tratados de maneira insegura.
Estados inesperados que permitem comportamento indevido.
Falhas que deixam a aplicação em um estado inseguro.
Tratamento inconsistente de exceções.

Uma aplicação deve possuir mecanismos seguros para lidar com condições inesperadas sem expor informações sensíveis ou permitir que o sistema entre em um estado explorável.

🌐 Análise HTTP no Contexto do OWASP Top 10

Uma parte importante do estudo foi observar vulnerabilidades através do comportamento de requisições e respostas HTTP.

Exemplo:

POST /login HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

username=admin&password=test

Durante um Web Pentest, o profissional pode modificar elementos como:

Método HTTP
Headers
Cookies
Parâmetros
Corpo da requisição
IDs
Tokens
Valores enviados pelo usuário

E então observar a resposta:

HTTP/1.1 200 OK
Content-Type: application/json

ou:

HTTP/1.1 403 Forbidden

ou:

HTTP/1.1 500 Internal Server Error

A diferença entre essas respostas pode fornecer evidências importantes sobre o comportamento da aplicação.

🔧 Tecnologias / Ferramentas Relacionadas
OWASP
HTTP/HTTPS
Burp Suite
OWASP ZAP
Nmap
Wireshark
APIs REST
Cookies
Sessões HTTP
Headers HTTP
Web Applications
SIEM
Sistemas de Logging
💻 Comandos / Sintaxe Importante

O treinamento foi predominantemente conceitual e não apresentou um conjunto específico de comandos obrigatórios.

Mesmo assim, alguns comandos são úteis para complementar a prática dos conceitos estudados.

Observar headers HTTP
curl -I https://example.com
Realizar uma requisição HTTP
curl -i https://example.com
Especificar um método HTTP
curl -X POST https://example.com/login

Em um ambiente autorizado de laboratório, ferramentas como Burp Suite permitem interceptar e modificar essas requisições de maneira muito mais prática.

🔬 Experimento / Prática

Para relacionar o conteúdo com Web Pentest:

Analisar uma aplicação web de laboratório.
Interceptar uma requisição HTTP utilizando Burp Suite.
Identificar parâmetros controlados pelo usuário.
Observar cookies e mecanismos de sessão.
Alterar parâmetros dentro do ambiente autorizado.
Comparar diferentes respostas HTTP.
Procurar indícios de problemas de controle de acesso.
Analisar mensagens de erro.
Identificar configurações potencialmente inseguras.
Relacionar cada comportamento encontrado com uma categoria do OWASP Top 10.
📊 Resultados Observados

O treinamento foi concluído com:

Progresso: 100%
Status: Concluído
Pontuação: 10 pontos

Foram estudadas as dez categorias do OWASP Top 10 (2025):

A01 - Broken Access Control
A02 - Security Misconfiguration
A03 - Software Supply Chain Failures
A04 - Cryptographic Failures
A05 - Injection
A06 - Insecure Design
A07 - Authentication Failures
A08 - Software or Data Integrity Failures
A09 - Security Logging and Alerting Failures
A10 - Mishandling of Exceptional Conditions
⚠️ Problemas Encontrados

Nenhum problema técnico relevante durante o treinamento.

O principal desafio conceitual foi compreender que o OWASP Top 10 representa categorias de riscos, e não simplesmente uma lista de dez vulnerabilidades individuais.

🛠️ Solução

A melhor forma de interpretar o Top 10 é relacionar cada categoria com:

Causa raiz
     ↓
Comportamento da aplicação
     ↓
Possível impacto
     ↓
Evidências observáveis
     ↓
Exploração
     ↓
Mitigação

Isso evita transformar o estudo em uma simples memorização das categorias.

🔐 Relação com Cibersegurança

O OWASP Top 10 é especialmente relevante para Web Pentest porque fornece uma referência para classificar e investigar problemas comuns em aplicações web.

Durante um pentest, o profissional pode utilizar as categorias como uma referência para direcionar testes.

Por exemplo:

Aplicação Web
     │
     ├── Autenticação
     │      └── A07
     │
     ├── Autorização
     │      └── A01
     │
     ├── Entrada de dados
     │      └── A05
     │
     ├── Configuração
     │      └── A02
     │
     └── Logs/Monitoramento
            └── A09

O OWASP Top 10 não substitui uma metodologia completa de pentest, mas fornece uma referência importante para identificar e classificar riscos de aplicações web.

📚 Termos Importantes Aprendidos
Termo	Significado
OWASP	Organização voltada à segurança de aplicações
OWASP Top 10	Classificação de riscos importantes em aplicações web
Broken Access Control	Falhas na aplicação de autorização e controle de acesso
Security Misconfiguration	Configurações inseguras em sistemas ou aplicações
Supply Chain	Cadeia de componentes e dependências utilizados pelo software
Cryptographic Failures	Problemas relacionados à proteção criptográfica de dados
Injection	Inserção de dados que são interpretados como comandos ou instruções
Insecure Design	Falhas originadas no projeto ou arquitetura da aplicação
Authentication	Processo de verificar a identidade de um usuário
Integrity	Garantia de que software ou dados não foram alterados indevidamente
Logging	Registro de eventos ocorridos em um sistema
Alerting	Geração de alertas a partir de eventos relevantes
Exception	Condição inesperada durante a execução do software
HTTP	Protocolo utilizado na comunicação entre clientes e servidores web
Pentest	Teste autorizado para identificar e validar vulnerabilidades
🧩 Insight do Dia

OWASP Top 10 não é uma checklist de "dez exploits".

Ele funciona melhor como um mapa de riscos para entender onde uma aplicação pode falhar, por que ela falha, como essa falha pode ser observada e qual impacto ela pode causar.

Para Web Pentest, o conhecimento realmente útil começa quando uma categoria deixa de ser apenas um nome e passa a ser relacionada com uma requisição HTTP real.
