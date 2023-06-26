<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Utils library for Brazilian-specific businesses.</p>

[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypi.org/project/brutils/)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)
### [Procurando pela versão em português?](README.md)
### [Looking for 1.0.1 version documentation?](/documentation%20v1.0.1/ENGLISH_VERSION.md)

</div>

# Getting Started

Brazilian Utils is a library focused on solving problems that we face daily in
the development of applications for the Brazilian business.

## Installation

```
pip install brutils
```

## Usage

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

## CPF

### is_valid_cpf

Check if CPF is valid.

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

Check if CNPJ is valid. Numbers only, formatted as strings.

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
