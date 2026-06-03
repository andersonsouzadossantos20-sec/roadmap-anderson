# 🌐 Registro de Estudo: Endereçamento IPv6

**Data:** 03/06/2026  
**Curso:** Cisco Networking Academy — Endereçamento de Rede e Solução Básica de Problemas  
**Módulo 4:** Endereçamento IPv6

---

# 🎯 Objetivo do Módulo
Compreender a estrutura do IPv6, seus diferentes tipos de endereços, métodos de configuração automática e os mecanismos utilizados para comunicação em redes modernas.

---

# 📌 1. Tipos de Endereço IPv6

O IPv6 utiliza endereços de 128 bits, oferecendo um espaço praticamente inesgotável de endereçamento.

## 🔹 Global Unicast Address (GUA)

- Equivalente ao endereço público do IPv4.
- Roteável pela Internet.
- Identifica unicamente um dispositivo.

Exemplo:

```text
2001:db8::1
```

---

## 🔹 Link-Local Address (LLA)

- Utilizado apenas dentro da rede local.
- Não é roteável pela Internet.
- Todo dispositivo IPv6 possui um endereço Link-Local.

Prefixo:

```text
FE80::/10
```

---

## 🔹 Unique Local Address (ULA)

- Similar aos endereços privados IPv4.
- Utilizado em redes internas.

Prefixo:

```text
FC00::/7
```

---

# ⚙️ 2. Configuração Estática do GUA e LLA

Os endereços IPv6 podem ser configurados manualmente.

## Vantagens

- Controle total do endereçamento.
- Facilidade para servidores e equipamentos críticos.
- Endereços previsíveis.

Exemplo:

```text
2001:db8:acad:1::10/64
```

---

# 🔄 3. Endereçamento Dinâmico para GUAs

O IPv6 suporta configuração automática sem necessidade obrigatória de DHCP.

## 🔹 SLAAC (Stateless Address Autoconfiguration)

Permite que o dispositivo:

1. Receba informações do roteador.
2. Gere automaticamente seu endereço IPv6.
3. Configure gateway padrão.

Vantagem:

- Simplicidade.
- Menor necessidade de administração.

---

## 🔹 DHCPv6

Fornece:

- Endereço IPv6.
- DNS.
- Informações adicionais da rede.

Pode operar junto com SLAAC.

---

# 🔗 4. Endereçamento Dinâmico para LLAs

Os endereços Link-Local podem ser gerados automaticamente de duas formas:

## Método EUI-64

Utiliza o endereço MAC para gerar parte do IPv6.

Exemplo:

```text
MAC:
00:1A:2B:3C:4D:5E

IPv6:
FE80::021A:2BFF:FE3C:4D5E
```

---

## Endereço Aleatório

O sistema operacional gera identificadores aleatórios para aumentar a privacidade do usuário.

---

# 📢 5. Endereços IPv6 Multicast

O IPv6 substitui o broadcast pelo multicast.

Em vez de enviar para todos os dispositivos, envia apenas para os dispositivos interessados.

Prefixo:

```text
FF00::/8
```

---

## Multicasts Importantes

### All-Nodes

```text
FF02::1
```

Todos os dispositivos IPv6 da rede local.

---

### All-Routers

```text
FF02::2
```

Todos os roteadores IPv6 da rede local.

---

# 🧪 Observação Prática (Cibersegurança)

O IPv6 é frequentemente negligenciado em auditorias de segurança.

Ataques comuns relacionados:

- Rogue Router Advertisement
- IPv6 Spoofing
- SLAAC Abuse
- Neighbor Discovery Attacks
- Dual Stack Exploitation

Muitas empresas desativam apenas o IPv4 durante testes e esquecem que o IPv6 continua ativo, criando uma superfície de ataque invisível.

---

# 📚 Termos Chave

| Termo | Definição |
|---------|---------|
| IPv6 | Protocolo de Internet de 128 bits |
| GUA | Global Unicast Address |
| LLA | Link-Local Address |
| ULA | Unique Local Address |
| SLAAC | Stateless Address Autoconfiguration |
| DHCPv6 | Dynamic Host Configuration Protocol for IPv6 |
| EUI-64 | Método de geração automática baseado em MAC |
| Multicast | Comunicação para múltiplos dispositivos específicos |

---

# 🧩 Insight do Dia

> "O IPv6 não é apenas um IPv4 maior. Ele foi projetado para simplificar a configuração, eliminar limitações de endereçamento e preparar a Internet para bilhões de novos dispositivos."

---

## 🚀 Próximos Passos

- Estudar Descoberta de Vizinhos IPv6 (NDP).
- Entender ICMPv6.
- Aprender Router Advertisement (RA).
- Explorar ataques e defesas em ambientes IPv6.
- Avançar para Switches e Roteadores Cisco.

#Cisco #Networking #IPv6 #CCNA #CyberSecurity #Redes #NDP #SLAAC #DHCPv6
