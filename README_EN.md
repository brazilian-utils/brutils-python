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
  - [format_phone](#format_phone)
  - [is_valid_phone](#is_valid_phone)
  - [is_valid_mobile_phone](#is_valid_mobile_phone)
  - [is_valid_landline_phone](#is_valid_landline_phone)
  - [remove_symbols_phone](#remove_symbols_phone)
  - [generate_mobile_phone](#generate_mobile_phone)
  - [generate_landline_phone](#generate_landline_phone)
- [Email](#email)
  - [is_valid_email](#is_valid_email)
- [License_Plate](#license_plate)
  - [is_valid_license_plate](#is_valid_license_plate)
  - [is_valid_license_plate_old_format](#is_valid_license_plate_old_format)
  - [is_valid_license_plate_mercosul](#is_valid_license_plate_mercosul)
  - [convert_license_plate_to_mercosul](#convert_license_plate_to_mercosul)
  - [format_license_plate](#format_license_plate)
  - [remove\_symbols\_license\_plate](#remove_symbols_license_plate)
  - [get_license_plate_format](#get_license_plate_format)
  - [generate_license_plate](#generate_license_plate)
- [PIS](#pis)
  - [is_valid_pis](#is_valid_pis)
  - [generate_pis](#generate_pis)
  - [remove_symbols_pis](#remove_symbols_pis)
  - [format_pis](#format_pis)
- [Legal Process](#legal-process)
  - [format_processo_juridico](#format_processo_juridico)
  - [remove\_symbols\_processo\_juridico](#remove_symbols_processo_juridico)
  - [generate_processo_juridico](#generate_processo_juridico)
  - [is_valid_processo_juridico](#is_valid_processo_juridico)
- [Título Eleitoral](#titulo-eleitoral)
  - [is_valid_titulo_eleitoral](#is_valid_titulo_eleitoral)

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

### format_phone
Formats a given phone number to a human-presentable format. If it is not a valid number, returns `None`
***Example: 11994029275 will be formatted to (11)99402-9275***


```python
>>> format_phone("11994029275")
'(11)99402-9275'
>>> format_phone("1635014415")
'(16)3501-4415'
>>> format_phone("333333")
>>>
```

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

### generate_mobile_phone

Generates a valid and random mobile phone number

```python
>>> from brutils import generate_mobile_phone
>>> generate_mobile_phone()
'63996408441'
>>> generate_mobile_phone()
'78964850019'
>>> generate_mobile_phone() 
'53924997638'
```

### generate_landline_phone

Generates a valid landline phone number

```python
>>> from brutils import generate_landline_phone
>>> generate_landline_phone()
5929797740
>>> generate_landline_phone()
9345561355
>>> generate_landline_phone()
1145081947
>>> generate_landline_phone()
3138577807
>>>
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

## License Plate

### is_valid_license_plate

Checks whether a Brazilian license plate is valid. It supports the old format as well as the Mercosul one.

```python
>>> from brutils import is_valid_license_plate
>>> is_valid_license_plate('ABC1234')
True
>>> is_valid_license_plate('def5678')
True
>>> is_valid_license_plate('ABC4E67')
True
>>> is_valid_license_plate('GHI-4567')
False
```

### is_valid_license_plate_old_format

Checks if it is a License Plate in the old format used in Brazil. Receives as a parameter a string that should contain only alphanumeric characters (letters and numbers) and returns a boolean value. ***Example: 'abc1234' results in True.***
This function only validates plates in the old format and does not verify if it actually exists.

```python
>>> from brutils import is_valid_license_plate_old_format
>>> is_valid_license_plate_old_format('ABC1234')
True
>>> is_valid_license_plate_old_format('def5678')
True
>>> is_valid_license_plate_old_format('GHI-4567')
False
```

### is_valid_license_plate_mercosul

Checks if the provided string representing a license place is valid, according to the new
Mercosul standards, in other words, if it follows the pattern LLLNLNN.
***Example: ABC4E67.***

```python
>>> from brutils import is_valid_license_plate_mercosul
>>> is_valid_license_plate_mercosul('ABC4E67')
True
```

### convert_license_plate_to_mercosul

Converts the provided string representing a license plate in the old format to the new
format, according to the new Mercosul standards (following the pattern LLLNLNN). In case
the provided license plate is invalid it will return the value `None`.
***Example: ABC4567 -> ABC4F67.***

```python
>>> from brutils import convert_license_plate_to_mercosul
>>> convert_license_plate_to_mercosul("ABC123")
"ABC1C34"
>>> convert_license_plate_to_mercosul("abc123")
"ABC1C34"
>>> convert_license_plate_to_mercosul("ABC1D23")
None
```

### format_license_plate

Given a String corresponding to valid license plate, whether following the old Brazilian
pattern (LLLNNNN) or the new Mercosul pattern (LLLNLNN), return a new String corresponding
to the formatted license plate with a dash (-) for the old format or in upper case for the
Mercosul format.
***Exemplo: ABC1234 -> ABC-1234.***
            ABC1E34 -> ABC1E34.***

```python
>>> format_license_plate("ABC1234")
"ABC-1234"
>>> format_license_plate("abc1234")
"ABC-1234"
>>> format_license_plate("ABC1D23")
"ABC1D23"
>>> format_license_plate("abc1d23")
"ABC1D23"
>>> format_license_plate("ABCD123")
None
```

### remove_symbols_license_plate

Removes the dash ("-") formatting symbol from a license plate number and returns only the number. Purposefully doesn't remove other symbols.

```python
from brutils import remove_symbols_license_plate

>>> remove_symbols_license_plate("ABC-123")
"ABC123"
>>> remove_symbols_license_plate("abc123")
"abc123"
>>> remove_symbols_license_plate("ABCD123")
"ABCD123"
>>> remove_symbols_license_plate("@abc#-#123@")
"@abc##123@"
```

### get_license_plate_format

Infers the format of a license plate, returning `LLLNNNN` for the old pattern, `LLLNLNN` for the Mercosul one and `None` for invalid license plates.

```python
from brutils import get_license_plate_format

>>> get_license_plate_format("ABC123")
"LLLNNNN"
>>> get_license_plate_format("abc123")
"LLLNNNN"
>>> get_license_plate_format("ABC1D23")
"LLLNLNN"
>>> get_license_plate_format("abc1d23")
"LLLNLNN"
>>> get_license_plate_format("ABCD123")
None
```
### generate_license_plate

Generate random valid license plates using a provided pattern (LLLNLNN or LLLNNNN), having
as default the Mercosul pattern. When provided an invalid pattern `None` is returned.

```python
from brutils import generate_license_plate

>>> generate_license_plate()
"ABC1D23"
>>> generate_license_plate(format="LLLNLNN")
"ABC4D56"
>>> generate_license_plate(format="LLLNNNN")
"ABC123"
>>> generate_license_plate(format="invalid")

## PIS

### is_valid_pis

Check if PIS/PASEP number is valid. Numbers only, formatted as strings. Does not check if PIS/PASEP exists.
More details about the validation can be found here: https://www.macoratti.net/alg_pis.htm.

```python
from brutils import is_valid_pis

>>> is_valid_pis("12038619494")
True
>>> is_valid_pis("11111111111")
False
>>> is_valid_pis("123456")
False
```

### generate_pis

Generates a valid random PIS/PASEP number.

```python
from brutils import generate_pis

>>> generate_pis()
'12038619494'
>>> generate_pis()
'57817700092'
>>> generate_pis()
'49850211630'
```

### remove_symbols_pis

Removes the formatting symbols ("-" and ".") from a PIS/PASEP number. It doesn't remove other symbols on purpose.

```python
from brutils import remove_symbols_pis

>>> remove_symbols_pis('170.33259.50-4')
'17033259504'
>>> remove_symbols_pis('/._')
'/_'
```

### format_pis

Format the PIS number. Returns None if the PIS is invalid.

```python
>>> from brutils import format_pis
>>> format_pis('12038619494')
'120.38619.49-4'
```

## Legal Process

### format_processo_juridico

Formats to the legal process pattern a 20 length string containing only digits.

```python
>>> from brutils import format_processo_juridico
>>> format_processo_juridico('23141945820055070079')
'2314194-58.2005.5.07.0079'
>>> format_processo_juridico('00000000000000000000')
'0000000-00.0000.0.00.0000'
>>>
```

### remove_symbols_processo_juridico

Removes common symbols from a legal process number string.
The standard symbols removed are "." and "-". It purposefully doesn't remove other symbols.

```python
from brutils import remove_symbols_processo_juridico

>>> remove_symbols_processo_juridico("6439067-89.2023.4.04.5902")
"64390678920234045902"
>>> remove_symbols_processo_juridico("4976023-82.2012.7.00.2263")
"49760238220127002263"
>>> remove_symbols_processo_juridico("4976023-82.2012.7.00.2263*!*&#")
"49760238220127002263*!*&#"
```

### generate_processo_juridico

Generates a valid legal process number according to the arguments of _ano_ which receives a year and _orgao_  which receives the legal entity id. The arguments have default values for _ano_ as the default year and _orgao_ a number between 1 and 9.


```python
>>> from brutils import generate_processo_juridico
>>> print(generate_processo_juridico())
45676401020238170592
>>> print(generate_processo_juridico(ano=2025))
32110268020258121130
>>> print(generate_processo_juridico(orgao=5))
37573041520235090313
>>> print(generate_processo_juridico(ano=2024, orgao=4))
33158248820244017105
>>>
```

## is_valid_processo_juridico

Checks if a string containing a legal process number is valid or not.

```python
>>> from brutils import is_valid_processo_juridico
>>> is_valid_processo_juridico('10188748220234018200')
True
>>> is_valid_processo_juridico('45532346920234025107')
True
>>> is_valid_processo_juridico('00000000000000000000')
False
>>> is_valid_processo_juridico('455323423QQWEQWSsasd&*(()')
False
>>>
```

## Titulo Eleitoral

### is_valid_titulo_eleitoral

Checks whether the Brazilian Voter ID number is valid. Accepts only numbers, formatted as a string. It does not verify whether the ID actually exists.

```python
>>> from brutils import is_valid_titulo_eleitoral
>>> is_valid_titulo_eleitoral('123456789011')
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