# brutils

### [Looking for the english version?](ENGLISH_VERSION.md)

_Compatível com Python 2.7 e 3.x_

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

### Importando a Biblioteca:
```
>>> from brutils import cpf, cnpj
```

### Como faço para validar um CPF ou CNPJ?
```
# somente numeros, em formato string

>>> cpf.validate('00011122233')
False
>>> cnpj.validate('00111222000133')
False
```

### E se a minha string estiver formatada com simbolos?
```
>>> cpf.sieve('000.111.222-33')
'00011122233'
>>> cnpj.sieve('00.111.222/0001-00')
'00111222000100'

# A função `sieve` limpa apenas os simbolos de formatação de CPF ou CNPJ, e de
# whitespace nas pontas. Ela não remove outros caractéres propositalmente, pois
# estes seriam indicativos de uma possível corrupção no dado ou de uma falta de
# filtros de input.
```

### E se eu quiser formatar uma string numérica?
```
>>> cpf.display('00011122233')
'000.111.222-33'
>>> cnpj.display('00111222000100')
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
python2.7 -m unittest discover tests/
python3 -m unittest discover tests/
```
