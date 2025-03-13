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

- [TIN Anguilla](#tin_anguilla)
  - [remove\_symbols](#remove_symbols)
  - [is\_valid\_individual](#is_valid_individual)
  - [is\_valid\_company](#is_valid_company)
  - [is\_valid](#is_valid)
  - [format\_tin](#generate)
  - [generate](#generate)
  - [example\_usage](#example_usage)

## NIF Anguilla

### remove_symbols

Remove espaços, pontos e hifens da sequência de entrada (input) dado pelo usuário.

Argumentos:

- tin (str): O TIN (NIF) a ser validado, uma string de 10 a 12 dígitos (letras e números). 

Retorna:

- bool: Verdadeiro se os dígitos de verificação corresponderem ao número base,
          Falso caso contrário.

### is_valid_individual

Valida o TIN da pessoa física (cidadão / indivíduo) para garantir que esteja dentro das especificações do país passadas como parâmetros!

Argumentos:

- tin (str): Um string com 10 caracteres, sendo os 2 primeiros letras e os demais dígitos.

Retorna:

- str: Se o input passado pelo usuário conter qualquer coisa diferente do argumento acima, retorna uma mensagem de "inválido", como erro.

Exemplo:

```python
>>> from tin_anguilla import is_valid_individual
>>> is_valid_individual("AB12345678") => 'Valid Anguilla TIN'
>>> is_valid_individual("XYZ1234567") => 'Invalid Anguilla TIN: Must start with two letters.'
```

### is_valid_company

Valida o TIN da pessoa jurírica (empresa) para garantir que esteja dentro das especificações do país passadas como parâmetros!

Argumentos:

- tin (str): Um string entre 10 e 12 caracteres, com letras e dígitos.

Retorna:

- str: Se o input passado pelo usuário conter qualquer coisa diferente do argumento acima, retorna uma mensagem de "inválido", como erro.

Exemplo:

```python
>>> from tin_anguilla import is_valid_company
>>> is_valid_company("ABC12345678") => 'Valid Anguilla TIN'
>>> is_valid_company("XY1234567") => 'Invalid Anguilla TIN: Must start with three letters.'
```

### is_valid

Determina se o TIN é válido para pessoas físicas ou jurídicas.

Retorna:

- str: Se o input for igual a 10 dígitos, é individual. Se for maior de 10 (até 12) é de empresa.

Exemplo:

```python
>>> from tin_anguilla import is_valid
>>> is_valid("AB12345678") => 'Valid Anguilla TIN Individual'
>>> is_valid("XYZ12345678") => 'Valid Anguilla TIN Company'
```


### format_tin

Formata um TIN para exibição.

Args:

- tin (str): Adiciona os separados corretos conforme os parâmetros do país.

Retorna:

- str: Um TIN formatado com os separadores no lugar certo!

Exemplo:

```python
>>> from tin_anguilla import format_tin
>>> format_tin("GEH15998436") => ("GEH-15998436")
```


### generate

Gera um TIN de Anguilla válido.

Args:

- tin (str): Gera um TIN de Anguilla válido.

Retorna:

- str: Gera um número válido dados os parâmetros corretos.

Exemplo:

```python
>>> from tin_anguilla import generate
>>> generate("AB12345678") => 'Valid Anguilla TIN Individual'
>>> generate("XYZ12345678") => 'Valid Anguilla TIN Company'
```

### example_usage

Gera TIN válido aleatoriamente como exemplo para pessoas físicas e jurídicas, analisa o input do usuário, além de formatá-los.

Argumentos:

- str: Um TIN válido gerado aleatoriamente como exemplo para pessoas físicas e jurídicas, input do usuário.

Retorna:

- str: Um TIN válido gerado aleatoriamente como exemplo para pessoas físicas e jurídicas, input do usuário analisado e formatado com símbolos visuais se for válido, None se não for válido.

Exemplo:

```python
>>> from tin_anguilla import example_usage
>>> tin_individual("AB12345678") => 'Valid Anguilla TIN Individual'
>>> tin_company("XYZ12345678") => 'Valid Anguilla TIN Company'

>>> is_valid(tin_individual) => 'Valid Anguilla TIN Company'
>>> is_valid(tin_company) => 'Valid Anguilla TIN Company'

>>> is_valid(user_input)("GEH15998436") => 'Valid input - Anguilla TIN Company'

>>> formatted_input = format_tin(user_input) => ("GEH-15998436")
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
