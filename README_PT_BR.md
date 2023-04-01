<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Utils library for Brazilian-specific businesses.</p>
</div>

[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypi.org/project/brutils/)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)

### [Looking for the english version?](README.md)

`brutils` é uma biblioteca para tratar de validações de documentos brasileiros,
e que eventualmente pode evoluir para tratar de outras coisas dentro do escopo
de validações relacionadas a burocracias brasileiras.

Sua principal funcionalidade é a validação de CPFs e CNPJs, mas sugestões sobre
outras coisas a se validar (preferencialmente de maneira determinística) são bem
vindas.


## Instalação

```
pip install brutils
```


## Utilização

### Como faço para validar um CPF ou CNPJ?
```
# somente numeros, em formato string

>>> from brutils import is_valid_cpf, is_valid_cnpj
>>> is_valid_cpf('00011122233')
False
>>> is_valid_cnpj('00111222000133')
False
```

### E se a minha string estiver formatada com simbolos?
```
>>> from brutils import parse_cpf, parse_cnpj
>>> parse_cpf('000.111.222-33')
'00011122233'
>>> parse_cnpj('00.111.222/0001-00')
'00111222000100'

# A função `sieve` limpa apenas os simbolos de formatação de CPF ou CNPJ, e de
# whitespace nas pontas. Ela não remove outros caractéres propositalmente, pois
# estes seriam indicativos de uma possível corrupção no dado ou de uma falta de
# filtros de input.
```

### E se eu quiser formatar uma string numérica?
```
>>> from brutils import format_cpf, format_cnpj
>>> format_cpf('00011122233')
'000.111.222-33'
>>> format_cnpj('00111222000100')
'00.111.222/0001-00'
```

### E se eu quiser gerar CPFs ou CNPJs validos aleatórios?
```
>>> cpf.generate()
'17433964657'
>>> cnpj.generate()
'34665388000161'
```


## Testes

```
python3 -m unittest discover tests/
```
