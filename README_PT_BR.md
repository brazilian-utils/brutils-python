<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Utils library for Brazilian-specific businesses.</p>


[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypi.org/project/brutils/)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)

### [Looking for the english version?](README.md)
</div>

# Introdução

Brazilian Utils é uma biblioteca com foco na resolução de problemas que enfrentamos diariamente no desenvolvimento de aplicações para o business Brasileiro.

## Instalação

```
pip install brutils
```

## Utilização

Para usar um de nossos utilitários, basta importar a função necessária, como no exemplo abaixo:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```

# Utilitários

## is_valid_cpf

Verifica se o CPF é valido. Apenas números, formatados como string.

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```

## format_cpf

Formata o CPF.

```python
>>> from brutils import format_cpf
>>> format_cpf('00011122233')
'000.111.222-33'
```

## parse_cpf

Remove os símbolos de formatação do CPF e retorna somente números. Filtra apenas os símbolos utilizados para a validação do CPF. Propositalmente não remove outros símbolos.


```python
>>> from brutils import parse_cpf
>>> parse_cpf('000.111.222-33')
'00011122233'
```
## generate_cpf

Gera um CPF válido aleatório.

```python
>>> cpf.generate()
'17433964657'
```

## is_valid_cnpj

Verifica se o CNPJ é valido. Apenas números, formatados como string.

```python
>>> from brutils import is_valid_cnpj
>>> is_valid_cnpj('00111222000133')
False
```

## format_cnpj

Formata o CNPJ.

```python
>>> from brutils import format_cnpj
>>> format_cnpj('00111222000100')
'00.111.222/0001-00'
```

## parse_cnpj

Remove os símbolos de formatação do CPF e retorna somente números. Filtra apenas os símbolos utilizados para a validação do CPF. Propositalmente não remove outros símbolos.

```python
>>> from brutils import parse_cnpj
>>> parse_cnpj('00.111.222/0001-00')
'00111222000100'
```

## generate_cnpj

Gera um CPF válido aleatório.

```python
>>> cnpj.generate()
'34665388000161'
```
