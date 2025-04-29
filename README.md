<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Biblioteca de utilitários para empresas específicas do Brasil.</p>

[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypistats.org/packages/brutils)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)

### [Looking for the english version?](README_EN.md)

</div>

# Introdução

Brazilian Utils é uma biblioteca com foco na resolução de problemas que enfrentamos diariamente no
desenvolvimento de aplicações para o business Brasileiro.

- [Instalação](#instalação)
- [Utilização](#utilização)
- [Utilitários](#utilitários)
- [Novos Utilitários e Reportar Bugs](#novos-utilitários-e-reportar-bugs)
- [Dúvidas? Ideias?](#dúvidas-ideias)
- [Contribuindo com o Código do Projeto](#contribuindo-com-o-código-do-projeto)

# Instalação

```bash
pip install brutils
```

# Utilização

Para usar um de nossos utilitários, basta importar a função necessária, como no exemplo abaixo:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```

# Utilitários


- [TIN Venezuela](#tin_venezuela)
  - [remove\_symbols](#remove_symbols)
  - [is\_valid](#is_valid)
  - [\_calculate\_digit](#_calculate_digit)
  - [format\_tin](#format_tin)
  - [generate\_ein](#generate_ein)
  - [example\_usage](#example_usage)

## NIF Venezuela

### remove_symbols

Remove espaços, pontos e hifens da sequência de entrada (input) dado pelo usuário.

Argumentos:

- tin (str): O TIN (NIF) a ser validado, uma string que começa com uma letra, seguida por 8 números e um dígito verificador.

Retorna:

- bool: Verdadeiro se os dígitos de verificação corresponderem ao número base,
          Falso caso contrário.


### is_valid

Valida o TIN para garantir que esteja dentro das especificações do país passadas como parâmetros!

Argumentos:

- tin (str): Uma string com 10 dígitos.

Retorna:

- str: Se o input passado pelo usuário conter qualquer coisa diferente do argumento acima, retorna uma mensagem de "inválido", como erro.

Exemplo:

```python
>>> from tin_venezuela import is_valid
>>> is_valid("V-12345678-9") => 'Valid Venezuela TIN'
>>> is_valid("A-12345678-9") => 'Invalid Venezuela TIN'
```


### format_tin

Formata um TIN para exibição.

Args:

- tin (str): Adiciona os separados corretos conforme os parâmetros do país.

Retorna:

- str: Um TIN formatado com os separadores no lugar certo!

Exemplo:

```python
>>> from tin_venezuela import format_tin
>>> format_tin("V123456789") => ("V-12345678-9")
```


### generate

Gera um TIN válido.

Args:

- tin (str): Gera um TIN válido.

Retorna:

- str: Gera um número válido dados os parâmetros corretos.

Exemplo:

```python
>>> from tin_venezuela import generate
>>> generate("V-12345678-9") => 'Valid Venezuela TIN'
>>> generate("A-12345678-9") => 'Invalid Venezuela TIN'
```


### example_usage

Gera TIN válido aleatoriamente como exemplo, analisa o input do usuário, além de formatá-los.

Argumentos:

- str: Um TIN válido gerado aleatoriamente como exemplo, input do usuário.

Retorna:

- str: Um TIN válido gerado aleatoriamente como exemplo, input do usuário analisado e formatado com símbolos visuais se for válido, None se não for válido.

Exemplo:

```python
>>> from tin_venezuela import example_usage
>>> tin("E784532186") => 'Valid Venezuela TIN'

>>> is_valid(tin) => 'Valid Venezuela TIN'

>>> is_valid(user_input)("E784532186") => 'Valid input - Venezuela TIN'

>>> formatted_input = format_tin(user_input) => ("E-78453218-6")
```

---

# Novos Utilitários e Reportar Bugs

Caso queira sugerir novas funcionalidades ou reportar bugs, basta criar
uma nova [issue][github-issues] e iremos lhe responder por lá!

(Para saber mais sobre github issues, confira a [documentação oficial do GitHub][github-issues-doc]).

# Dúvidas? Ideias?

Dúvidas de como utilizar a biblioteca? Novas ideias para o projeto?
Quer compartilhar algo com a gente? Fique à vontade para criar um tópico no nosso
[Discussions][github-discussions] que iremos interagir por lá!

(Para saber mais sobre github discussions, confira a
[documentação oficial do GitHub][github-discussions-doc]).

# Contribuindo com o Código do Projeto

Sua colaboração é sempre muito bem-vinda! Preparamos o arquivo [CONTRIBUTING.md][contributing] para
te ajudar nos primeiros passos. Lá você encontrará toda a informação necessária para contribuir com
o projeto. Não hesite em nos perguntar utilizando o [GitHub Discussions][github-discussions] caso
haja qualquer dificuldade ou dúvida. Toda ajuda conta!

Vamos construir juntos! 🚀🚀

[contributing]: CONTRIBUTING.md
[github-discussions-doc]: https://docs.github.com/pt/discussions
[github-discussions]: https://github.com/brazilian-utils/brutils-python/discussions
[github-issues-doc]: https://docs.github.com/pt/issues/tracking-your-work-with-issues/creating-an-issue
[github-issues]: https://github.com/brazilian-utils/brutils-python/issues

## ❤️ Quem já Contribuiu

<a href="https://github.com/brazilian-utils/brutils-python/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=brazilian-utils/brutils-python" />
</a></br></br>

_Feito por [contrib.rocks](https://contrib.rocks)._
