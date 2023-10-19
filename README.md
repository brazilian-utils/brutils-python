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
  - [format_phone](#format_phone)
  - [is_valid_phone](#is_valid_phone)
  - [remove_symbols_phone](#remove_symbols_phone)
  - [generate_mobile_phone](#generate_mobile_phone)
  - [generate_landline_phone](#generate_landline_phone)
- [Email](#email)
  - [is_valid_email](#is_valid_email)
- [License Plate](#license_plate)
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
- [Processo Jurídico](#processo-jurídico)
  - [format_processo_juridico](#format_processo_juridico)
  - [remove\_symbols\_processo\_juridico](#remove_symbols_processo_juridico)
  - [generate_processo_juridico](#generate_processo_juridico)
  - [is_valid_processo_juridico](#is_valid_processo_juridico)
- [Título Eleitoral](#titulo-eleitoral)
  - [is_valid_titulo_eleitoral](#is_valid_titulo_eleitoral)

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

Verifica se os dígitos de verificação do CNPJ (Cadastro Nacional da Pessoa
Jurídica) fornecido correspondem ao seu número base.
A entrada deve ser uma string de dígitos com o comprimento apropriado.

Esta função não verifica a existência do CNPJ; ela só valida o formato da
string.

Argumentos:
    cnpj (str): O CNPJ a ser validado.

Retorna:
    bool: True se os dígitos de verificação corresponderem ao número base,
          False caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_cnpj
>>> is_valid_cnpj('03560714000142')
True
>>> is_valid_cnpj('00111222000133')
False
```

### format_cnpj

Formata uma string de CNPJ (Cadastro Nacional da Pessoa Jurídica) para exibição
visual.

Esta função recebe uma string de CNPJ como entrada, valida seu formato e a
formata com símbolos visuais padrão para fins de exibição.

Argumentos:
    cnpj (str): A string de CNPJ a ser formatada para exibição.

Retorna:
    str: O CNPJ formatado com símbolos visuais se for válido,
         None se não for válido.

Exemplo:

```python
>>> from brutils import format_cnpj
>>> format_cnpj("03560714000142")
'03.560.714/0001-42'
>>> format_cnpj("98765432100100")
None
```

### remove_symbols_cnpj

Remove símbolos específicos de uma string de CNPJ (Cadastro Nacional da Pessoa
Jurídica).

Esta função recebe uma string de CNPJ como entrada e remove todas as
ocorrências dos caracteres '.', '/' e '-' dela.

Argumentos:
    cnpj (str): A string de CNPJ que contém os símbolos a serem removidos.

Retorna:
    str: Uma nova string com os símbolos especificados removidos.

Exemplo:

```python
>>> from brutils import remove_symbols_cnpj
>>> remove_symbols_cnpj('00.111.222/0001-00')
'00111222000100'
```

### generate_cnpj

Gera uma sequência de dígitos CNPJ válida aleatória. Um número de filial
opcional pode ser fornecido; o padrão é 1.

Argumentos:
    branch (int): Um número de filial opcional a ser incluído no CNPJ.

Retorna:
    str: Uma sequência CNPJ válida gerada aleatoriamente.

Exemplo:

```python
>>> from brutils import generate_cnpj
>>> generate_cnpj()
'34665388000161'
>>> generate(1234)
"01745284123455"
```

## CEP

### is_valid_cep

Verifica se um CEP (Código de Endereçamento Postal) brasileiro é válido.

Para que um CEP seja considerado válido, a entrada deve ser uma string contendo
exatamente 8 dígitos. Esta função não verifica se o CEP é um CEP real, pois
valida apenas o formato da string.

Args:
    cep (str): A string contendo o CEP a ser verificado.

Retorno:
    bool: True se o CEP for válido (8 dígitos), False caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_cep
>>> is_valid_cep('01310200')
True
>>> is_valid_cep("12345")
False
>>> is_valid_cep("abcdefgh")
False
```

### format_cep

Formata um CEP (Código de Endereçamento Postal) brasileiro em um formato padrão.

Esta função recebe um CEP (Código de Endereçamento Postal) como entrada e, se
for um CEP válido com 8 dígitos, o formata no formato padrão "12345-678".

Argumentos:
    cep (str): O CEP (Código de Endereçamento Postal) de entrada a ser
               formatado.

Retorna:
    str: O CEP formatado no formato "12345-678" se for válido, None se não for
         válido.

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

Remove símbolos específicos de um CEP (Código de Endereçamento Postal)
fornecido.

Esta função recebe um CEP (Código de Endereçamento Postal) como entrada e remove
todas as ocorrências dos caracteres '.' e '-' dele.

Argumentos:
    cep (str): O CEP (Código de Endereçamento Postal) de entrada que contém os
    símbolos a serem removidos.

Retorna:
    str: Uma nova string com os símbolos especificados removidos.

Exemplo:

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

Gera um número de CEP (Código de Endereçamento Postal) aleatório de 8 dígitos
como uma string.

Retorna:
    str: Um número de 8 dígitos gerado aleatoriamente.

Exemplo:

```python
>>> from brutils import generate_cep
>>> generate_cep()
'77520503'
```

## Phone

### format_phone
Formata um numero de telefone recebido para um formato apresentavel humanamente. Caso não seja um numero válido, retorna `None`
***Exemplo: 11994029275 será formatado para (11)99402-9275***

```python
>>> format_phone("11994029275")
'(11)99402-9275'
>>> format_phone("1635014415")
'(16)3501-4415'
>>> format_phone("333333")
>>>
```

### is_valid_phone

Retornar se um número de telefone brasileiro é valido.
Não verifica se o número realmente existe.

```
is_valid_phone(phone_number, type)
```

Argumentos
  - phone_number (str):
    * o número de telefone a ser validado
    * obrigatório
    * apenas dígitos, sem símbolos
    * sem o código do país
    * deve incluir o número de DDD com dois dígitos
    * exemplo: '+55 48 9999 9999' deve ser utilizado como '4899999999'

  - type (str):
    * 'mobile' para validar apenas números de celular
    * 'landline' para validar apenas números de telefone fixo
    * caso não especificado, valida para um para o outro.
    * opcional

Retorno
  - bool: True se o número é válido, False caso contrário.

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

### generate_landline_phone

Gera um número de telefone fixo válido

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

## Placa de Carro

### is_valid_license_plate

Verifica se uma placa veicular é válida. Suporta padrão antigo e padrão Mercosul.

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

### remove_symbols_license_plate

Remove símbolos "-" de formatação de um número de placa e retorna apenas o número. Propositalmente não remove outros símbolos.

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

Infere o formato de uma placa, `LLLNNNN` para o padrão antigo, `LLLNLNN` para o padrão Mercosul e `None` para placas inválidas.

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

Gera placas válidas de carro utilizando como parâmetro um dos formatos válidos (LLLNLNN ou
LLLNNNN), tendo como formato padrão o padrão Mercosul. Caso seja fornecido um formato
inválido, é retornado o valor `None`.

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

### remove_symbols_pis

Remove símbolos "-" e "." de formatação de um número PIS/PASEP. Propositalmente não remove outros símbolos.

```python
from brutils import remove_symbols_pis

>>> remove_symbols_pis('170.33259.50-4')
'17033259504'
>>> remove_symbols_pis('/._')
'/_'
```

### format_pis

Formata o número PIS. Retorna None se o PIS for inválido.

```python
>>> from brutils import format_pis
>>> format_pis('12038619494')
'120.38619.49-4'
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

### generate_processo_juridico

Gera um número de processo válido de acordo com o ano informado e o órgão. Por padrão o argumento de _ano_ recebe sempre o ano atual e o _orgao_ recebe um valor aleatório de 1 à 9.

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

Verifica se o número de um processo informado por string é válido ou não.

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

Verifica se o número do Título Eleitoral brasileiro é valido. Apenas números, formatados como string. Não verifica se o Título realmente existe.

```python
>>> from brutils import is_valid_titulo_eleitoral
>>> is_valid_titulo_eleitoral('123456789011')
False
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
