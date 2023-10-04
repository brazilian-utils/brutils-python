<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Utils library for Brazilian-specific businesses.</p>

[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypistats.org/packages/brutils)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)
### [Procurando pela versão em português?](README.md)

</div>

# Getting Started

Brazilian Utils is a library focused on solving problems that we face daily in
the development of applications for the Brazilian business.

- [Installation](#installation)
- [Usage](#usage)
- [Utilities](#utilities)
- [Contributing with Source Code](#contributing-with-source-code)
- [Feature Request and Bug Report](#feature-request-and-bug-report)
- [Questions? Ideas?](#questions-ideas)
- [Code Contribution](#code-contribution)


# Installation

```
pip install brutils
```

# Usage

To use one of our utilities you just need to import the required function as in the example below:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```

# Utilities

- [CPF](#cpf)
  - [is_valid_cpf](#is_valid_cpf)
  - [format_cpf](#format_cpf)
  - [remove_symbols_cpf](#remove_symbols_cpf)
  - [generate_cpf](#generate_cpf)
- [CNPJ](#cnpj)
  - [is_valid_cnpj](#is_valid_cnpj)
  - [format_cnpj](#format_cnpj)
  - [remove_symbols_cnpj](#remove_symbols_cnpj)
  - [generate_cnpj](#generate_cnpj)
- [CEP](#cep)
  - [is_valid_cep](#is_valid_cep)
  - [format_cep](#format_cep)
  - [remove_symbols_cep](#remove_symbols_cep)
  - [generate_cep](#generate_cep)
- [Phone](#phone)
  - [is_valid_phone](#is_valid_phone)
  - [is_valid_mobile_phone](#is_valid_mobile_phone)
  - [is_valid_landline_phone](#is_valid_landline_phone)
  - [remove_symbols_phone](#remove_symbols_phone)
- [Email](#email)
  - [is_valid_email](#is_valid_email)


## CPF

### is_valid_cpf

Check if CPF is valid. Numbers only, formatted as strings. Does not check if CPF exists.

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```

### format_cpf

Format CPF. Returns None if CPF is invalid.

```python
>>> from brutils import format_cpf
>>> format_cpf('11144477735')
'111.444.777-35'
```

### remove_symbols_cpf

Remove formatting symbols from CPF and return only digits.
It only filters out the symbols used for CPF validation.
It purposefully doesn't remove other symbols.

```python
>>> from brutils import remove_symbols_cpf
>>> remove_symbols_cpf('000.111.222-33')
'00011122233'
```

### generate_cpf

Generate a valid random CPF.

```python
>>> from brutils import generate_cpf
>>> generate_cpf()
'17433964657'
```

## CNPJ

### is_valid_cnpj

Check if CNPJ is valid. Numbers only, formatted as strings. Does not check if CNPJ exists.

```python
>>> from brutils import is_valid_cnpj
>>> is_valid_cnpj('00111222000133')
False
```

### format_cnpj

Format CNPJ.

```python
>>> from brutils import format_cnpj
>>> format_cnpj('00111222000100')
'00.111.222/0001-00'
```

### remove_symbols_cnpj

Remove formatting symbols from CNPJ and return only digits.
It only filters out the symbols used for CNPJ validation.
It purposefully doesn't remove other symbols.

```python
>>> from brutils import remove_symbols_cnpj
>>> remove_symbols_cnpj('00.111.222/0001-00')
'00111222000100'
```

### generate_cnpj

Generate a valid random CNPJ.

```python
>>> from brutils import generate_cnpj
>>> generate_cnpj()
'34665388000161'
```

## CEP

### is_valid_cep

Check if CEP is valid. Numbers only, formatted as strings. Does not check if CEP exists.

```python
>>> from brutils import is_valid_cep
>>> is_valid_cep('01310200')
True
```

### format_cep

Format CEP. Returns None if CEP is invalid.

```python
>>> from brutils import format_cep
>>> format_cpf('01310200')
'01310-200'
```

### remove_symbols_cep

Remove formatting symbols from CEP and return only digits.
It only filters out the symbols used for CEP validation.
It purposefully doesn't remove other symbols.

```python
>>> from brutils import remove_symbols_cep
>>> remove_symbols_cep('01310-200')
'01310200'
```

### generate_cep

Generate a valid random CEP.

```python
>>> from brutils import generate_cep
>>> generate_cep()
'77520503'
```

## Phone

### is_valid_phone

Check if phone number is valid, can be landline or mobile phone. Numbers only, with area code (DDD) and without the international prefix, formatted as a string. ***For example: +55 48 9999 9999 would become '4899999999'*** This function validates only Brazilian phone numbers and does not verify if the number actually exists.

```python
>>> from brutils import is_valid_phone
>>> is_valid_phone('11994029275')
True
```

### is_valid_mobile_phone

Check if mobile phone number is valid. Numbers only, with area code (DDD) and without the international prefix, formatted as a string. ***For example: +55 48 9999 9999 would become '4899999999'*** This function validates only Brazilian phone numbers and does not verify if the number actually exists.

```python
>>> from brutils import is_valid_mobile_phone
>>> is_valid_mobile_phone('11994029275')
True
```

### is_valid_landline_phone

Check if landline phone number is valid. Numbers only, with area code (DDD) and without the international prefix, formatted as a string. ***For example: +55 48 3333 3333 would become '4833333333'.*** This function validates only Brazilian phone numbers and does not verify if the number actually exists.

```python
>>> from brutils import is_valid_landline_phone
>>> is_valid_landline_phone('1938814933')
True
```

### remove_symbols_phone

Remove symbols from phone number. ***Example: +55 (21) 2569-6969 will return '552125696969'.***

```python
>>> from brutils import remove_symbols_phone
>>> remove_symbols_phone('+55 (21) 2569-6969')
'552125696969'
```
## Email

### is_valid_email

Check if a string corresponds to a valid email. The rules for validating an email address generally follow the specifications defined by RFC 5322 (updated by RFC 5322bis), which is the widely accepted standard for email address formats.

```python
from brutils import is_valid_email

>>> is_valid_email("joao.ninguem@gmail.com")
True
>>> is_valid_email(".joao.ninguem@gmail.com")
False
>>> is_valid_email("joao.ninguem@gmail.")
False
>>> is_valid_email("joao ninguem@gmail.com")
False
```

# Feature Request and Bug Report

If you want to suggest new features or report bugs, simply create
a new [issue][github-issues], and we will respond to you there!

(To learn more about GitHub issues, check out the [official GitHub documentation][github-issues-doc]).

# Questions? Ideas?

Questions on how to use the library? New ideas for the project?
Want to share something with us? Feel free to start a thread in our
[Discussions][github-discussions], and we'll interact with you there!

(To learn more about GitHub discussions, refer to the
[official GitHub documentation][github-discussions-doc]).

# Code Contribution

Your collaboration is always very welcome! We've prepared the [CONTRIBUTING.md][contributing] file
to assist you in getting started. There, you'll find all the information you need to contribute to
the project. Please, don't hesitate to ask us using [GitHub Discussions][github-discussions] if
you encounter any difficulties or have any questions. Every bit of help counts!

Let's build it together 🚀🚀

[contributing]: CONTRIBUTING_EN.md
[github-discussions-doc]: https://docs.github.com/en/discussions
[github-discussions]: https://github.com/brazilian-utils/brutils-python/discussions
[github-issues-doc]: https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue
[github-issues]: https://github.com/brazilian-utils/brutils-python/issues
