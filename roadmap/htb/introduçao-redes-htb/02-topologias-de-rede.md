# Topologias de Rede

> **Módulo:** Introduction to Networking
> **Plataforma:** Hack The Box Academy
> **Status:** ✅ Concluído

---

# Introdução

Depois de entender os diferentes tipos de redes, o próximo passo foi aprender como os dispositivos podem ser organizados dentro delas.

Antes desse estudo eu nunca tinha parado para pensar que a forma como computadores, switches e roteadores são conectados influencia diretamente no desempenho, na disponibilidade e até na segurança da rede.

Foi interessante perceber que uma mesma rede pode funcionar de maneiras completamente diferentes dependendo da topologia utilizada.

---

# O que é uma topologia de rede?

Topologia é a forma como os dispositivos são conectados entre si.

Ela define o caminho que os dados percorrem dentro da rede e como a comunicação acontece entre os equipamentos.

Cada topologia possui vantagens, desvantagens e cenários onde faz mais sentido ser utilizada.

---

# Topologia em Barramento (Bus)

Na topologia Bus, todos os dispositivos compartilham um único cabo principal.

```text
PC ─── PC ─── PC ─── PC
```

### Vantagens

- Estrutura simples.
- Baixo custo.
- Fácil de implementar em redes pequenas.

### Desvantagens

- Se o cabo principal apresentar problemas, toda a rede é afetada.
- Dificuldade para identificar falhas.
- Não escala bem para ambientes maiores.

Hoje praticamente não é utilizada em novas implementações.

---

# Topologia em Estrela (Star)

Foi a topologia que mais me chamou atenção porque é exatamente a mais utilizada atualmente.

Todos os dispositivos ficam conectados a um equipamento central, normalmente um switch.

```text
       PC
        |
PC --- Switch --- PC
        |
       PC
```

### Vantagens

- Fácil administração.
- Boa performance.
- Problemas em um computador normalmente não afetam os demais.

### Desvantagens

Se o switch central falhar, toda a comunicação é interrompida.

---

# Topologia em Anel (Ring)

Na topologia Ring cada dispositivo é conectado ao próximo, formando um círculo.

```text
PC ----- PC
|         |
|         |
PC ----- PC
```

Os dados percorrem o anel até chegar ao destino.

Hoje seu uso é bem menos comum, mas foi importante para entender como diferentes arquiteturas podem funcionar.

---

# Topologia Mesh

Na topologia Mesh os dispositivos possuem múltiplas conexões entre si.

```text
PC ------ PC
|\        /|
| \      / |
|  \    /  |
|   \  /   |
PC------PC
```

É uma estrutura muito mais resistente a falhas.

Mesmo que um caminho deixe de funcionar, normalmente existe outra rota disponível.

Essa característica faz com que seja utilizada em ambientes onde alta disponibilidade é essencial.

---

# Topologia Híbrida

Como o próprio nome sugere, combina duas ou mais topologias diferentes.

É bastante comum em empresas, onde diferentes setores possuem necessidades específicas.

Por exemplo:

- Escritórios utilizando Star.
- Backbone utilizando Mesh.

---

# O que isso muda na Cybersecurity?

Antes desse estudo eu enxergava a rede apenas como um conjunto de computadores conectados.

Agora ficou mais claro que a própria organização física e lógica da rede influencia diretamente na comunicação.

Isso faz diferença durante atividades como:

- Mapeamento da infraestrutura.
- Identificação de pontos únicos de falha.
- Segmentação da rede.
- Reconhecimento de ambientes corporativos.

Entender a topologia também facilita interpretar diagramas de rede durante um Pentest.

---

# O que ficou de aprendizado

Depois desse estudo consegui entender:

- O que é uma topologia de rede.
- Como cada estrutura organiza os dispositivos.
- Por que a topologia Star é tão utilizada atualmente.
- Que diferentes cenários exigem arquiteturas diferentes.

Foi um daqueles assuntos que parecem simples, mas ajudam bastante a visualizar como uma rede realmente é construída.
