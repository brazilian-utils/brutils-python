<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Utils library for Brazilian-specific businesses.</p>


[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypi.org/project/brutils/)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)

### [Looking for the english version?](README_EN.md)
### [Procurando a documentação da versão 1.0.1?](/documentation%20v1.0.1/PORTUGUESE_VERSION.md)
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

## CPF

### is_valid_cpf

Verifica se o CPF é valido. Apenas números, formatados como string. Não verifica se o CPF existe.

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```

### format_cpf

Formata o CPF. Retorna None se o CPF for inválido.

```python
>>> from brutils import format_cpf
>>> format_cpf('11144477735')
'111.444.777-35'
```

### remove_symbols_cpf

Remove os símbolos de formatação do CPF e retorna somente números. Filtra apenas os símbolos utilizados para a validação do CPF. Propositalmente não remove outros símbolos.

```python
>>> from brutils import remove_symbols_cpf
>>> remove_symbols_cpf('000.111.222-33')
'00011122233'
```

### generate_cpf

Gera um CPF válido aleatório.

```python
>>> from brutils import generate_cpf
>>> generate_cpf()
'17433964657'
```

## CNPJ

### is_valid_cnpj

Verifica se o CNPJ é valido. Apenas números, formatados como string. Não verifica se o CNPJ existe.

```python
>>> from brutils import is_valid_cnpj
>>> is_valid_cnpj('00111222000133')
False
```

### format_cnpj

Formata o CNPJ.

```python
>>> from brutils import format_cnpj
>>> format_cnpj('00111222000100')
'00.111.222/0001-00'
```

### remove_symbols_cnpj

Remove os símbolos de formatação do CPF e retorna somente números. Filtra apenas os símbolos utilizados para a validação do CPF. Propositalmente não remove outros símbolos.

```python
>>> from brutils import remove_symbols_cnpj
>>> remove_symbols_cnpj('00.111.222/0001-00')
'00111222000100'
```

### generate_cnpj

Gera um CNPJ válido aleatório.

```python
>>> from brutils import generate_cnpj
>>> generate_cnpj()
'34665388000161'
```

## CEP

### is_valid_cep

Verifica se o CEP é valido. Apenas números, formatados como string. Não verifica se o CEP existe.

```python
>>> from brutils import is_valid_cep
>>> is_valid_cep('01310200')
True
```

### format_cep

Formata o CEP. Retorna None se o CEP for inválido.

```python
>>> from brutils import format_cep
>>> format_cep('01310200')
'01310-200'
```

### remove_symbols_cep

Remove os símbolos de formatação do CEP e retorna somente números. Filtra apenas os símbolos utilizados para a validação do CEP. Propositalmente não remove outros símbolos.

```python
>>> from brutils import remove_symbols_cep
>>> remove_symbols_cep('01310-200')
'01310200'
```

### generate_cep

Gera um CEP válido aleatório.

```python
>>> from brutils import generate_cep
>>> generate_cep()
'77520503'
```


## Contributing

Sua colaboração é sempre bem-vinda! Preparamos o [arquivo contributing][contributing] pra te ajudar nos primeiros passos. Toda ajuda conta! Sinta-se livre para criar novas [GitHub issues][github-issues] e interagir aqui.

Vamos construir juntos! 🚀🚀

[github-issues]: https://github.com/brazilian-utils/brutils-python/issues
[contributing]: CONTRIBUTING.md
