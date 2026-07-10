# Proxies

> **Módulo:** Introduction to Networking
> **Plataforma:** Hack The Box Academy
> **Status:** ✅ Concluído

---

# Introdução

Esse foi um dos tópicos que mais gostei até agora.

Antes eu pensava que um proxy servia apenas para esconder o endereço IP, mas durante o módulo percebi que ele pode desempenhar diversas funções dentro de uma rede.

Além disso, ficou muito mais fácil entender por que ferramentas como o Burp Suite são chamadas de **Intercepting Proxy**.

---

# O que é um Proxy?

Um proxy funciona como um intermediário entre o cliente e o servidor.

Ao invés de o cliente enviar uma requisição diretamente para um servidor, ela passa primeiro pelo proxy.

```text
Cliente
   │
   ▼
Proxy
   │
   ▼
Servidor
```

O servidor responde ao proxy, que então encaminha a resposta para o cliente.

---

# Por que utilizar um Proxy?

Dependendo do ambiente, um proxy pode ser utilizado para:

- Controlar acesso à Internet.
- Filtrar conteúdo.
- Registrar atividades dos usuários.
- Armazenar páginas em cache.
- Melhorar desempenho.
- Aumentar a privacidade.

Tudo depende da forma como ele é configurado.

---

# Forward Proxy

O Forward Proxy atua em nome do cliente.

```text
Cliente
   │
   ▼
Forward Proxy
   │
   ▼
Internet
```

É bastante utilizado em empresas para controlar o acesso dos funcionários à Internet.

Também pode ocultar o endereço IP real do cliente.

---

# Reverse Proxy

O Reverse Proxy trabalha do lado do servidor.

```text
Internet
    │
    ▼
Reverse Proxy
    │
    ▼
Servidor Web
```

Nesse caso, quem acessa o site nem percebe que existe um proxy entre ele e o servidor.

Esse tipo de proxy é muito utilizado para:

- Balanceamento de carga.
- Proteção contra ataques.
- Cache.
- SSL/TLS.
- Alta disponibilidade.

---

# Proxy Transparente

O usuário normalmente nem percebe que está utilizando um proxy.

É bastante comum em:

- Escolas.
- Empresas.
- Hotéis.
- Redes públicas.

Seu principal objetivo costuma ser controlar ou monitorar o tráfego.

---

# Intercepting Proxy

Esse foi o conceito que mais fez sentido para quem pretende trabalhar com Segurança Web.

O Burp Suite funciona exatamente dessa maneira.

```text
Navegador
      │
      ▼
Burp Suite
      │
      ▼
Servidor
```

Antes que uma requisição chegue ao servidor, ela pode ser:

- Visualizada.
- Modificada.
- Reenviada.
- Repetida.
- Analisada.

Praticamente todo Pentest Web utiliza esse conceito.

---

# Onde vejo isso no dia a dia?

Mesmo sem perceber, utilizamos proxies com frequência.

Alguns exemplos:

- Empresas controlando acesso à Internet.
- Cloudflare protegendo sites.
- Burp Suite interceptando requisições HTTP.
- Balanceadores de carga distribuindo acessos.

Depois desse módulo ficou muito mais fácil entender essas tecnologias.

---

# O que isso muda na Cybersecurity?

Para quem pretende trabalhar com Pentest Web, entender proxies é praticamente obrigatório.

Grande parte dos testes realizados em aplicações web depende da capacidade de interceptar e modificar requisições HTTP.

Ferramentas como Burp Suite, OWASP ZAP e diversos scanners funcionam utilizando esse princípio.

---

# O que ficou de aprendizado

Depois desse estudo consegui entender:

- O que realmente é um proxy.
- A diferença entre Forward Proxy e Reverse Proxy.
- Como funciona um Intercepting Proxy.
- Por que o Burp Suite é uma ferramenta tão importante durante um Pentest.

Esse foi um dos assuntos que mais conectou teoria com algo que já utilizo nos laboratórios, tornando o aprendizado muito mais fácil de visualizar.
