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
  - [remove_symbols_phone](#remove_symbols_phone)
  - [generate_mobile_phone](#generate_mobile_phone)
  - [generate_landline_phone](#generate_landline_phone)
  - [remove_international_code_phone](#remove_international_code_phone)
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
  - [format_legal_process](#format_legal_process_processo_juridico)
  - [remove\_symbols\_processo\_juridico](#remove_symbols_legal_process)
  - [generate_legal_process](#generate_legal_process_processo_juridico)
  - [is_valid_legal_process](#is_valid_legal_process_processo_juridico)
- [Título Eleitoral](#titulo-eleitoral)
  - [is_valid_titulo_eleitoral](#is_valid_titulo_eleitoral)

## CPF

### is_valid_cpf

Returns whether or not the verifying checksum digits of the given CPF
(Brazilian Individual Taxpayer Number) match its base number.
This function does not verify the existence of the CPF; it only
validates the format of the string.

Args:
  * cpf (str): The CPF to be validated, a 11-digit string

Returns:
  * bool: True if the checksum digits match the base number,
          False otherwise.

Example:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf("82178537464")
True
>>> is_valid_cpf('00011122233')
False
```

### format_cpf

Format a CPF (Brazilian Individual Taxpayer Number) for display with visual
aid symbols. This function takes a numbers-only CPF string as input and adds
standard formatting visual aid symbols for display.

Args:
  * cpf (str): A numbers-only CPF string.

Returns:
  * str: A formatted CPF string with standard visual aid symbols or
         None if the input is invalid.

Example:

```python
>>> from brutils import format_cpf
>>> format_cpf('82178537464')
'821.785.374-64'
>>> format_cpf("55550207753")
'555.502.077-53'
```

### remove_symbols_cpf

Removes specific symbols from a CPF (Brazilian Individual Taxpayer Number)
string. This function takes a CPF string as input and removes all occurrences of
the '.', '-' characters from it.

Args:
  * cpf (str): The CPF string containing symbols to be removed.

Returns:
  * str: A new string with the specified symbols removed.

Example:

```python
>>> from brutils import remove_symbols_cpf
>>> remove_symbols_cpf('000.111.222-33')
'00011122233'
```

### generate_cpf

Generate a random valid CPF (Brazilian Individual Taxpayer Number) digit string.

Returns:
  * str: A random valid CPF string.

Example:

```python
>>> from brutils import generate_cpf
>>> generate_cpf()
'17433964657'
>>> generate_cpf()
"10895948109"
```

## CNPJ

### is_valid_cnpj

Returns whether or not the verifying checksum digits of the given CNPJ
(Brazilian Company Registration Number) match its base number.
Input should be a digit string of proper length.
This function does not verify the existence of the CNPJ; it only
validates the format of the string.

Args:
  * cnpj (str): The CNPJ to be validated.

Returns:
  * bool: True if the checksum digits match the base number,
          False otherwise.

Example:

```python
>>> from brutils import is_valid_cnpj
>>> is_valid_cnpj('03560714000142')
True
>>> is_valid_cnpj('00111222000133')
False
```

### format_cnpj

Formats a CNPJ (Brazilian Company Registration Number) string for visual
display.
This function takes a CNPJ string as input, validates its format, and
formats it with standard visual aid symbols for display purposes.

Args:
  * cnpj (str): The CNPJ string to be formatted for display.

Returns:
  * str: The formatted CNPJ with visual aid symbols if it's valid,
         None if it's not valid.

Example:

```python
>>> from brutils import format_cnpj
>>> format_cnpj("03560714000142")
'03.560.714/0001-42'
>>> format_cnpj("98765432100100")
None
```

### remove_symbols_cnpj

Removes specific symbols from a CNPJ (Brazilian Company Registration Number)
string.
This function takes a CNPJ string as input and removes all occurrences of
the '.', '/' and '-' characters from it.

Args:
  * cnpj (str): The CNPJ string containing symbols to be removed.

Returns:
  * str: A new string with the specified symbols removed.

Example:

```python
>>> from brutils import remove_symbols_cnpj
>>> remove_symbols_cnpj('00.111.222/0001-00')
'00111222000100'
```

### generate_cnpj

Generates a random valid CNPJ (Brazilian Company Registration Number) digit
string. An optional branch number parameter can be given; it defaults to 1.

Args:
  * branch (int): An optional branch number to be included in the CNPJ.

Returns:
  * str: A randomly generated valid CNPJ string.

Example:

```python
>>> from brutils import generate_cnpj
>>> generate_cnpj()
'34665388000161'
>>> generate(1234)
"01745284123455"
```

## CEP

### is_valid_cep

Checks if a Brazilian CEP (Postal Code) is valid.
To be considered valid, the input must be a string containing exactly 8 digits.
This function does not verify if the CEP is a real postal code; it only
validates the format of the string.

Args:
  * cep (str): The string containing the CEP to be checked.

Returns:
  * bool: True if the CEP is valid (8 digits), False otherwise.

Example:

```python
>>> from brutils import is_valid_cep
>>> is_valid_cep('01310200')
True
```

### format_cep

This function takes a CEP (Postal Code) as input and, if it is a valid
8-digit CEP, formats it into the standard "12345-678" format.

Args:
  * cep (str): The input CEP (Postal Code) to be formatted.

Returns:
  * str: The formatted CEP in the "12345-678" format if it's valid,
         None if it's not valid.

Example:

```python
>>> from brutils import format_cep
>>> format_cep('01310200')
'01310-200'
>>> format_cep("12345678")
"12345-678"
>>> format_cep("12345")
None
```

### remove_symbols_cep

This function takes a CEP (Postal Code) as input and removes all occurrences of
the '.' and '-' characters from it.

Args:
  * cep (str): The input CEP (Postal Code) containing symbols to be removed.

Returns:
  * str: A new string with the specified symbols removed.

Example:

```python
>>> from brutils import remove_symbols_cep
>>> remove_symbols_cep('01310-200')
'01310200'
>>> remove_symbols_cep("123-45.678.9")
"123456789"
>>> remove_symbols_cep("abc.xyz")
"abcxyz"
```

### generate_cep

Generates a random 8-digit CEP (Postal Code) number as a string.

Returns:
  * str: A randomly generated 8-digit number.

Example:

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

Return whether a Brazilian phone number is valid.
It does not verify if the number actually exists.

```
is_valid_phone(phone_number, type)
```

Args
  - phone_number:
    * the phone number to be validated
    * mandatory
    * digits only, no symbols
    * without the country code
    * should include the area code (DDD) with two digits
    * example: '+55 48 9999 9999' should be used as '4899999999'

  - type:
    * 'mobile' to validate only mobile numbers
    * 'landline' to validate only landline phone numbers
    * if not specified, it validates for either.
    * optional

Return
  - bool: True if the phone number is valid. False otherwise.

Example

```python
>>> from brutils import is_valid_phone
>>> is_valid_phone('11994029275')
True
>>> is_valid_mobile_phone('11994029275', 'mobile')
True
>>> is_valid_landline_phone('1938814933', 'landline')
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

### remove_international_code_phone

Remove the international code (+55) from a string that contains a Brazilian phone number.

```python
>>> from brutils import remove_international_code_phone
>>> remove_international_code_phone("5521994029275")
"21994029275"
>>> remove_international_code_phone("+5521994029275")
"+21994029275"
>>> remove_international_code_phone("5555994029275")
"55994029275"
>>> remove_international_code_phone("21994029275")
"21994029275"
>>>
```

## Email

### is_valid_email

Check if a string corresponds to a valid email address.

Args:
  * email (str): The input string to be checked.

Returns:
  * bool: True if email is a valid email address, False otherwise.

Example:

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

Check if a license plate is valid.
This function does not verify if the license plate is a real license plate;
it only validates the format of the string.

Args:
  * license_plate (str): A license plate string.

Returns:
  * bool: True if the license plate is valid, False otherwise.

Example:

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

Checks whether a string matches the old format of Brazilian license plate
(LLLNNNN).
This function does not verify if the license plate is a real license plate;
it only validates the format of the string.

Args:
  * license_plate (str): A license plate string.

Returns:
  * bool: True if the string corresponds to a license plate in the old
          pattern format, False otherwise.

Example:

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

Checks whether a string matches the Mercosul license plate format (LLLNNNN).
This function does not verify if the license plate is a real license plate;
it only validates the format of the string.

Args:
  * license_plate (str): A license plate string.

Returns:
  * bool: True if the string corresponds to a license plate in the Mercosul
          pattern format, False otherwise.

Example:

```python
>>> from brutils import is_valid_license_plate_mercosul
>>> is_valid_license_plate_mercosul('ABC4E67')
True
>>> is_valid_license_plate_mercosul('abc167')
False
```

### convert_license_plate_to_mercosul

Converts an old pattern license plate (LLLNNNN) to a Mercosul format
(LLLNLNN).

Args:
  * license_plate (str): A string of proper length representing the
                         old pattern license plate.

Returns:
  * str: The converted Mercosul license plate (LLLNLNN) or
         'None' if the input is invalid.

Example:

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

Formats a license plate into the correct pattern.
This function receives a license plate in any pattern (LLLNNNN or LLLNLNN)
and returns a formatted version.

Args:
  * license_plate (str): A license plate string.

Returns:
  * str: The formatted license plate string or
         'None' if the input is invalid.

Example:

```python
>>> format_license_plate("ABC1234") # old format (contains a dash)
"ABC-1234"
>>> format_license_plate("abc1234") # old format (contains a dash)
"ABC-1234"
>>> format_license_plate("ABC1D23") # mercosul format
"ABC1D23"
>>> format_license_plate("abc1d23") # mercosul format
"ABC1D23"
>>> format_license_plate("ABCD123")
None
```

### remove_symbols_license_plate

Removes the dash (-) symbol from a license plate string.

Args:
  * license_plate_number (str): A license plate number containing symbols to
                                be removed.

Returns:
  * str: The license plate number with the specified symbols removed.

Example:

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

Return the format of a license plate. 'LLLNNNN' for the old pattern and
'LLLNLNN' for the Mercosul one.

Args:
  * license_plate (str): A license plate string without symbols.

Returns:
  * str: The format of the license plate (LLLNNNN, LLLNLNN) or
          'None' if the format is invalid.

Example:

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

Generate a valid license plate in the given format. In case no format is
provided, it will return a license plate in the Mercosul format.

Args:
  * format (str): The desired format for the license plate.
                  'LLLNNNN' for the old pattern or 'LLLNLNN' for the
                   Mercosul one. Default is 'LLLNLNN'

Returns:
  * str: A randomly generated license plate number or
         'None' if the format is invalid.

Example:

```python
from brutils import generate_license_plate

>>> generate_license_plate()
"ABC1D23"
>>> generate_license_plate(format="LLLNLNN")
"ABC4D56"
>>> generate_license_plate(format="LLLNNNN")
"ABC123"
>>> generate_license_plate(format="invalid")
None
```

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

### format_legal_process

Format a legal process ID into a standard format.

Args:
  * legal_process_id (str): A 20-digits string representing the legal
                            process ID.

Returns:
  * str: The formatted legal process ID or None if the input is invalid.

Example:

```python
>>> from brutils import format_legal_process
>>> format_legal_process('23141945820055070079')
'2314194-58.2005.5.07.0079'
>>> format_legal_process('00000000000000000000')
'0000000-00.0000.0.00.0000'
>>> format_legal_process("123")
None
```

### remove_symbols_legal_process

Removes specific symbols from a given legal process.

This function takes a legal process as input and removes all occurrences
of the '.' and '-' characters from it.

Args:
  * legal_process (str): A legal process containing symbols to be removed.

Returns:
  * str: The legal process string with the specified symbols removed.

Example:

```python
from brutils import remove_symbols_legal_process

>>> remove_symbols_legal_process("6439067-89.2023.4.04.5902")
"64390678920234045902"
>>> remove_symbols_legal_process("4976023-82.2012.7.00.2263")
"49760238220127002263"
>>> remove_symbols_legal_process("4976023-82.2012.7.00.2263*!*&#")
"49760238220127002263*!*&#"
```

### generate_legal_process

Generate a random legal process ID number.

Args:
  * year (int): The year for the legal process ID (default is the current
                year).
                The year should not be in the past
  * orgao (int): The organization code (1-9) for the legal process ID
                 (default is random).

Returns:
    str: A randomly generated legal process ID.
         None if one of the arguments is invalid.

Example:

```python
>>> from brutils import generate_legal_process
>>> generate_legal_process()
"45676401020238170592"
>>> generate_legal_process(year=2025)
"32110268020258121130"
>>> generate_legal_process(orgao=5)
"37573041520235090313"
>>> generate_legal_process(year=2024, orgao=4)
"33158248820244017105"
```

## is_valid_legal_process

Check if a legal process ID is valid.

This function does not verify if the legal process ID is a real legal
process ID; it only validates the format of the string.

Args:
  * legal_process_id (str): A digit-only string representing the legal
                            process ID.

Returns:
  * bool: True if the legal process ID is valid, False otherwise.

Example:

```python
>>> from brutils import is_valid_legal_process
>>> is_valid_legal_process('10188748220234018200')
True
>>> is_valid_legal_process('45532346920234025107')
True
>>> is_valid_legal_process('00000000000000000000')
False
>>> is_valid_legal_process('455323423QQWEQWSsasd&*(()')
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
