# TryHackMe — Data Encoding

- **Roadmap:** Pre Security → Computer Fundamentals
- **Data:** 27/10/2026
- **Status:** Concluída
- **Link:** [Data Encoding](https://tryhackme.com/room/dataencoding)

---

## 📚 Resumo

Sala introdutória sobre a codificação de dados e a maneira como os computadores representam caracteres e símbolos.

O conteúdo aborda ASCII e Unicode, incluindo os padrões UTF-8, UTF-16 e UTF-32. Esses padrões permitem representar letras, números, símbolos e caracteres de diferentes idiomas em formato digital.

---

## 🧠 Aprendizados

- Compreender o conceito de codificação de caracteres.
- Conhecer o padrão ASCII e suas limitações.
- Entender a finalidade do Unicode.
- Diferenciar UTF-8, UTF-16 e UTF-32.
- Compreender como computadores representam caracteres por meio de valores numéricos.
- Reconhecer a importância da codificação correta para evitar problemas na exibição de textos.

---

## 💻 Conceitos principais

| Conceito | Finalidade |
|----------|------------|
| ASCII | Representar um conjunto básico de caracteres |
| Unicode | Definir códigos para caracteres de diversos idiomas e sistemas de escrita |
| UTF-8 | Codificação Unicode de tamanho variável, de 1 a 4 bytes por ponto de código |
| UTF-16 | Codificação Unicode que utiliza unidades de 16 bits |
| UTF-32 | Codificação Unicode que utiliza unidades de 32 bits |

---

## 📝 Anotações

### ASCII

O ASCII é um padrão tradicional de codificação que representa caracteres básicos, incluindo letras inglesas, números e símbolos de controle.

Sua versão original utiliza 7 bits por caractere.

### Unicode

O Unicode permite representar caracteres de diversos idiomas, além de símbolos e emojis.

Ele ajuda a resolver limitações de padrões mais antigos, que não conseguem representar todos os sistemas de escrita.

### UTF-8, UTF-16 e UTF-32

São formas de codificar caracteres Unicode em bytes.

- **UTF-8:** utiliza de 1 a 4 bytes por ponto de código e é amplamente utilizado na web.
- **UTF-16:** utiliza unidades de 16 bits, podendo precisar de duas unidades para determinados caracteres.
- **UTF-32:** utiliza uma unidade de 32 bits por ponto de código.

É importante diferenciar o código de um caractere da forma como ele é codificado em bytes.

### Relação com a computação

A codificação correta permite que textos sejam armazenados, transmitidos e exibidos adequadamente em diferentes sistemas.

---

## 🔗 Referências

- [Data Encoding — TryHackMe](https://tryhackme.com/room/dataencoding)

---

## ✅ Revisão

- [x] Sala concluída.
- [x] Entendo o conceito de codificação de caracteres.
- [x] Conheço ASCII e Unicode.
- [x] Sei diferenciar UTF-8, UTF-16 e UTF-32.
- [x] Compreendo a importância da codificação para o processamento de textos.
