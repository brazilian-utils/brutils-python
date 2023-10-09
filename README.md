<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Utils library for Brazilian-specific businesses.</p>


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

```
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
  - [generate_mobile_phone](#generate_mobile_phone)
- [Email](#email)
  - [is_valid_email](#is_valid_email)
- [Processo Jurídico](#processo-juridico)
  - [format_processo_juridico](#format_processo_juridico)
- [License Plate](#license_plate)
  - [is_valid_license_plate_old_format](#is_valid_license_plate_old_format)
  - [is_valid_license_plate_mercosul](#is_valid_license_plate_mercosul)
  - [convert_license_plate_to_mercosul](#convert_license_plate_to_mercosul)
  - [format_license_plate](#format_license_plate)
- [PIS](#pis)
  - [is_valid_pis](#is_valid_pis)
  - [generate_pis](#generate_pis)
- [Processo Jurídico](#processo-jurídico)
  - [remove\_symbols\_processo\_juridico](#remove_symbols_processo_juridico)

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

Remove os símbolos de formatação do CPF e retorna somente números. Filtra apenas os símbolos
utilizados para a validação do CPF. Propositalmente não remove outros símbolos.

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

Remove os símbolos de formatação do CPF e retorna somente números. Filtra apenas os símbolos
utilizados para a validação do CPF. Propositalmente não remove outros símbolos.

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

Remove os símbolos de formatação do CEP e retorna somente números. Filtra apenas os símbolos
utilizados para a validação do CEP. Propositalmente não remove outros símbolos.

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

## Phone

### is_valid_phone

Verifica se o número de telefone é valido, podendo ser telefone fixo ou celular. Apenas números,
com DDD e sem o prefixo internacional, formatados como string.
***Exemplo: +55 48 9999 9999 deve ser chamado como is_valid_phone('4899999999').*** Esta função
valida apenas números de telefone brasileiros e não verifica se o número realmente existe.

```python
>>> from brutils import is_valid_phone
>>> is_valid_phone('11994029275')
True
```

### is_valid_mobile_phone

Verifica se o número de celular é valido. Apenas números, com DDD e sem o prefixo internacional,
formatados como string.***Exemplo: +55 48 9999 9999 ficaria '4899999999'.*** Esta função valida
apenas números de celular brasileiros e não verifica se o número realmente existe.

```python
>>> from brutils import is_valid_mobile_phone
>>> is_valid_mobile_phone('11994029275')
True
```

### is_valid_landline_phone

Verifica se o número de telefone fixo é valido. Apenas números, com DDD e sem o prefixo
internacional, formatados como string. ***Exemplo: +55 48 3333 3333 ficaria '4833333333'.***
Esta função valida apenas números de telefones fixos brasileiros e não verifica se o número
realmente existe.

```python
>>> from brutils import is_valid_landline_phone
>>> is_valid_landline_phone('1938814933')
True
```

### remove_symbols_phone

Remove símbolos do número de telefone. ***Exemplo: (21)2569-6969 ficaria '2125696969'.***

```python
>>> from brutils import remove_symbols_phone
>>> remove_symbols_phone('(21)2569-6969')
'2125696969'
```

### generate_mobile_phone

Gera um número de telefone móvel válido e aleatório

```python
>>> from brutils import generate_mobile_phone
>>> generate_mobile_phone()
'63996408441'
>>> generate_mobile_phone()
'78964850019'
>>> generate_mobile_phone() 
'53924997638'
```

## Email

### is_valid_email

Verificar se uma string corresponde a um e-mail válido. As regras para validar um endereço de e-mail geralmente seguem as especificações definidas pelo RFC 5322 (atualizado pelo RFC 5322bis), que é o padrão amplamente aceito para formatos de endereços de e-mail. 

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

## Processo Jurídico

### format_processo_juridico

Formata qualquer string de dígitos com tamanho de 20 caracteres no padrão de processo jurídico.

```python
>>> from brutils import format_processo_juridico
>>> format_processo_juridico('23141945820055070079')
'2314194-58.2005.5.07.0079'
>>> format_processo_juridico('00000000000000000000')
'0000000-00.0000.0.00.0000'
>>>
```


## License_Plate

### is_valid_license_plate_old_format

Verifica se é uma Placa de Veículo no antigo padrão utilizado no Brasil. Recebe como parâmetro uma string devendo conter somente caracteres alfanuméricos(letras e números) e retorna um valor booleano. ***Exemplo: 'abc1234' resulta em True.***
Esta função valida somente placas no antigo padrão e não verifica se a mesma realmente existe.

```python
>>> from brutils import is_valid_license_plate_old_format
>>> is_valid_license_plate_old_format('ABC1234')
True
>>> is_valid_license_plate_old_format('def5678')
True
>>> is_valid_license_plate_old_format('GHI-4567')
False
```

## License_Plate

### is_valid_license_plate_mercosul

Verifica se uma string correspondente a um número da placa é válido, conforme as novas
normas do Mercosul, isto é, seguindo o padrão LLLNLNN. 
***Exemplo: ABC4E67.***

```python
>>> from brutils import is_valid_license_plate_mercosul
>>> is_valid_license_plate_mercosul('ABC4E67')
True
```

### convert_license_plate_to_mercosul

Converte uma string correspondente a um número da placa é válido no formato antigo,
para o novo formato, conforme as novas normas do Mercosul (seguindo o padrão LLLNLNN).
Caso a placa informada seja inválida será retornado o valor `None`.
***Exemplo: ABC4567 -> ABC4F67.***

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

Dada uma String correspondente a uma placa de carro válida, seja no formato da placa
é o antigo (LLLNNNN) ou o novo Formato Mercosul (LLLNLNN), retornar uma String
correspondendo a esta placa formatada com o traço para o formato antigo e sem mudança para
o formato Mercosul.
***Exemplo: ABC4567 -> ABC4F67.***

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

## PIS

### is_valid_pis

Verifica se o número PIS/PASEP é valido. Apenas números, formatados como string. Não verifica se o PIS/PASEP existe.
Mais detalhes sobre a validação estão disponíveis em https://www.macoratti.net/alg_pis.htm.

### generate_pis

Gera um PIS/PASEP válido aleatório.

```python
from brutils import generate_pis

>>> generate_pis()
'12038619494'
>>> generate_pis()
'57817700092'
>>> generate_pis()
'49850211630'
```

## Processo Jurídico

### remove_symbols_processo_juridico

Remove os símbolos "." e "-" de formatação de um número de processo jurídico e retorna apenas o número. Propositalmente não remove outros símbolos.

```python
from brutils import remove_symbols_processo_juridico

>>> remove_symbols_processo_juridico("6439067-89.2023.4.04.5902")
"64390678920234045902"
>>> remove_symbols_processo_juridico("4976023-82.2012.7.00.2263")
"49760238220127002263"
>>> remove_symbols_processo_juridico("4976023-82.2012.7.00.2263*!*&#")
"49760238220127002263*!*&#"
```

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
