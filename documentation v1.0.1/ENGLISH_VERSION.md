# brutils

### [Procurando pela versão em português?](PORTUGUESE_VERSION.md)

_Compatible with Python 2.7 and 3.x_

`brutils` is a library for validating brazilian document numbers, and might
eventually evolve to deal with other validations related to brazilian bureaucracy.

It's main functionality is the validation of CPF and CNPJ numbers, but suggestions
for other (preferrably deterministic) things to validate are welcome.


## Installation

```
pip install brutils
```


## Utilization

### Importing:
```
>>> from brutils import cpf, cnpj, phone
```

### How do I validate a CPF or CNPJ?
```
# numbers only, formatted as strings

>>> cpf.validate('00011122233')
False
>>> cnpj.validate('00111222000133')
False
```

### What if my string has formatting symbols in it?
```
>>> cpf.sieve('000.111.222-33')
'00011122233'
>>> cnpj.sieve('00.111.222/0001-00')
'00111222000100'

# The `sieve` function only filters out the symbols used for CPF or CNPJ validation.
# It purposefully doesn't remove other symbols, as those may be indicators of data
# corruption, or a possible lack of input filters.
```

### What if I want to format a numbers only string?
```
>>> cpf.display('00011122233')
'000.111.222-33'
>>> cnpj.display('00111222000100')
'00.111.222/0001-00'
```

### What if I want to generate random, but numerically valid CPF or CNPJ numbers?
```
>>> cpf.generate()
'17433964657'
>>> cnpj.generate()
'34665388000161'
```

### What if I want to remove symbols from number phone?
```
>>> phone.remove_symbols_phone()
'(21) 2569-6969'
```

## Testing

```
python2.7 -m unittest discover tests/
python3 -m unittest discover tests/
```
