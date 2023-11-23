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
  - [remove_international_code_phone](#remove_international_code_phone)
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
  - [format_legal_process](#format_legal_process)
  - [remove\_symbols\_processo\_juridico](#remove_symbols_legal_process)
  - [generate_legal_process](#generate_legal_process)
  - [is_valid_legal_process](#is_valid_legal_process)
- [Título Eleitoral](#titulo-eleitoral)
  - [is_valid_titulo_eleitoral](#is_valid_titulo_eleitoral)

## CPF

### is_valid_cpf

Retorna se os dígitos de verificação do CPF fornecido
correspondem ao seu número base. Esta função não verifica a existência do CPF;
ela apenas valida o formato da string.

Argumentos:
  * cpf (str): O CPF a ser validado, uma string de 11 dígitos

Retorna:
  * bool: Verdadeiro se os dígitos de verificação corresponderem ao número base,
          Falso caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf("82178537464")
True
>>> is_valid_cpf('00011122233')
False
```

### format_cpf

Formate um CPF (Cadastro de Pessoa Física brasileiro) para exibição visual.
Esta função recebe uma string de CPF contendo apenas números como entrada e
adiciona símbolos de formatação padrão para exibição.

Argumentos:
  * cpf (str): Uma string de CPF contendo apenas números.

Retorna:
  * str: O CPF formatado com símbolos visuais se for válido,
         None se não for válido.

Exemplo:

```python
>>> from brutils import format_cpf
>>> format_cpf('82178537464')
'821.785.374-64'
>>> format_cpf("55550207753")
'555.502.077-53'
```

### remove_symbols_cpf

Remove símbolos específicos de uma string de CPF (Cadastro de Pessoa Física
brasileiro). Esta função recebe como entrada uma string de CPF e remove todas as
ocorrências dos caracteres '.', '-' dela.

Argumentos:
  * cpf (str): A string de CPF contendo os símbolos a serem removidos.

Retorna:
  * str: Uma nova string com os símbolos especificados removidos.

Exemplo:

```python
>>> from brutils import remove_symbols_cpf
>>> remove_symbols_cpf('000.111.222-33')
'00011122233'
```

### generate_cpf

Gerar uma string de dígitos de CPF válida aleatória.

Retorna:
  * str: Um CPF válido gerado aleatoriamente.

Exemplo:

```python
>>> from brutils import generate_cpf
>>> generate_cpf()
'17433964657'
>>> generate_cpf()
"10895948109"
```

## CNPJ

### is_valid_cnpj

Verifica se os dígitos de verificação do CNPJ (Cadastro Nacional da Pessoa
Jurídica) fornecido correspondem ao seu número base. A entrada deve ser uma
string de dígitos com o comprimento apropriado. Esta função não verifica a
existência do CNPJ; ela só valida o formato da string.

Argumentos:
  * cnpj (str): O CNPJ a ser validado.

Retorna:
  * bool: True se os dígitos de verificação corresponderem ao número base,
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
  * cnpj (str): A string de CNPJ a ser formatada para exibição.

Retorna:
  * str: O CNPJ formatado com símbolos visuais se for válido,
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
  * cnpj (str): A string de CNPJ que contém os símbolos a serem removidos.

Retorna:
  * str: Uma nova string com os símbolos especificados removidos.

Exemplo:

```python
>>> from brutils import remove_symbols_cnpj
>>> remove_symbols_cnpj('00.111.222/0001-00')
'00111222000100'
```

### generate_cnpj

Gera uma string de dígitos CNPJ válida aleatória. Um número de filial
opcional pode ser fornecido; o padrão é 1.

Argumentos:
  * branch (int): Um número de filial opcional a ser incluído no CNPJ.

Retorna:
  * str: Um CNPJ válido gerado aleatoriamente.

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
  * cep (str): A string contendo o CEP a ser verificado.

Retorno:
  * bool: True se o CEP for válido (8 dígitos), False caso contrário.

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
Esta função recebe um CEP como entrada e, se for um CEP válido com 8 dígitos,
o formata no padrão "12345-678".

Argumentos:
  * cep (str): O CEP (Código de Endereçamento Postal) de entrada a ser
              formatado.

Retorna:
  * str: O CEP formatado no formato "12345-678" se for válido, None se não for
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
fornecido. Esta função recebe um CEP como entrada e remove todas as ocorrências
dos caracteres '.' e '-' dele.

Argumentos:
  * cep (str): O CEP (Código de Endereçamento Postal) de entrada que contém os
               símbolos a serem removidos.

Retorna:
  * str: Uma nova string com os símbolos especificados removidos.

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
  * str: Um número de 8 dígitos gerado aleatoriamente.

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
```

### remove_international_code_phone

Remove o código internacional (+55) de uma string que contém um número de telefone brasileiro.

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

Verificar se uma string corresponde a um endereço de e-mail válido.

Argumentos:
  * email (str): A string de entrada a ser verificada.

Retorna:
  * bool: Verdadeiro se o email for um endereço de e-mail válido, Falso
          caso contrário.

Exemplo:

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

Verifica se uma placa de carro é válida.
Esta função não verifica se a placa de carro é uma placa de carro real;
ela apenas valida o formato da string.

Args:
  * license_plate (str): Uma string representando uma placa de carro.

Retorna:
  * bool: Verdadeiro se a placa de carro for válida, Falso caso contrário.

Exemplo:

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

Verifica se uma string corresponde ao formato antigo da placa de carro brasileira
(LLLNNNN).
Esta função não verifica se a placa de carro é uma placa de carro real;
ela apenas valida o formato da string.

Args:
  * license_plate (str): Uma string representando uma placa de carro.

Retorna:
  * bool: Verdadeiro se a string corresponder a uma placa de carro no formato
          antigo, Falso caso contrário.

Exemplo:

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

Verifica se uma string corresponde ao formato de placa Mercosul (LLLNNNN).
Esta função não verifica se a placa de carro é uma placa de carro real;
ela apenas valida o formato da string.

Args:
  * license_plate (str): Uma string representando uma placa de carro.

Retorna:
  * bool: Verdadeiro se a string corresponder a uma placa de carro no formato Mercosul,
          Falso caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_license_plate_mercosul
>>> is_valid_license_plate_mercosul('ABC4E67')
True
```

### convert_license_plate_to_mercosul

Converte uma placa de carro no formato antigo (LLLNNNN) para o formato Mercosul
(LLLNLNN).

Args:
  * license_plate (str): Uma string com o tamanho adequado que representa a
                         placa no formato antigo.

Retorna:
  * str: A placa Mercosul convertida (LLLNLNN) ou
         'None' se a entrada for inválida.

Exemplo:

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

Formata uma placa de carro no padrão correto.
Esta função recebe uma placa de carro em qualquer formato (LLLNNNN ou LLLNLNN)
e retorna uma versão formatada.

Args:
  * license_plate (str): Uma string representando uma placa de carro.

Retorna:
  * str: A string da placa de carro formatada ou
         'None' se a entrada for inválida.

Exemplo:


```python
>>> format_license_plate("ABC1234") # formato antigo (contém traço)
"ABC-1234"
>>> format_license_plate("abc1234") # formato antigo (contém traço)
"ABC-1234"
>>> format_license_plate("ABC1D23") # formato mercosul
"ABC1D23"
>>> format_license_plate("abc1d23") # formato mercosul
"ABC1D23"
>>> format_license_plate("ABCD123")
None
```

### remove_symbols_license_plate

Remove o símbolo de hífen (-) de uma string de placa de carro.

Args:
  * license_plate_number (str): Uma string de placa de carro contendo símbolos a
                              serem removidos.

Retorna:
  * str: A string da placa de carro com os símbolos especificados removidos.

Exemplo:

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

Retorna o formato de uma placa de carro. 'LLLNNNN' para o formato antigo e
'LLLNLNN' para o formato Mercosul.

Args:
  * license_plate (str): Uma string de placa de carro sem símbolos.

Retorna:
  * str: O formato da placa de carro (LLLNNNN, LLLNLNN) ou
         'None' se o formato for inválido.

Exemplo:

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

Gere uma placa de carro válida no formato especificado. Caso nenhum formato seja
fornecido, ele retornará uma placa de carro no formato Mercosul.

Args:
  * format (str): O formato desejado para a placa de carro. 'LLLNNNN' para o
  formato antigo ou 'LLLNLNN' para o formato Mercosul. O padrão é 'LLLNLNN'.

Retorna:
  * str: Um número de placa de carro gerado aleatoriamente ou
         'None' se o formato for inválido.

Exemplo:

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
````

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

### format_legal_process

Formata um ID de processo jurídico em um formato padrão.

Args:
  * legal_process_id (str): Uma string de 20 dígitos que representa o ID do
                            processo jurídico.

Returna:
  * str: O ID do processo jurídico formatado ou None se a entrada for inválida.

Exemplo:

```python
>>> from brutils import format_legal_process
>>> format_legal_process('23141945820055070079')
'2314194-58.2005.5.07.0079'
>>> format_legal_process('00000000000000000000')
'0000000-00.0000.0.00.0000'
>>>
```

### remove_symbols_legal_process

Remove símbolos específicos de um processo jurídico fornecido.

Esta função recebe um processo jurídico como entrada e remove todas as
ocorrências dos caracteres '.' e '-' dele.

Args:
  * legal_process (str): Um processo jurídico contendo símbolos a serem
                         removidos.

Returna:
  * str: A string do processo jurídico com os símbolos especificados removidos.

Exemplo:

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

Gere um número aleatório de ID de processo jurídico.

Args:
  * year (int): O ano para o ID do processo jurídico (o padrão é o ano atual).
                Não pode ser um ano do passado.
  * orgao (int): O órgão (1-9) para o ID do processo jurídico
                 (o padrão é aleatório).

Returna:
  * str: Um ID de processo jurídico gerado aleatoriamente.
         None caso algum dos argumento seja inválido.

Exemplo:

```python
>>> from brutils import generate_legal_process
>>> generate_legal_process()
"45676401020238170592"
>>> generate_legal_process(ano=2025)
"32110268020258121130"
>>> generate_legal_process(orgao=5)
"37573041520235090313"
>>> generate_legal_process(ano=2024, orgao=4)
"33158248820244017105"
```

## is_valid_legal_process

Verifique se um ID de processo jurídico é válido.

Esta função não verifica se o ID de processo jurídico é um ID de processo
jurídico real; ela apenas valida o formato da string.

Args:
  * legal_process_id (str): Uma string contendo apenas dígitos que representa
                            o ID do processo jurídico.

Returna:
  * bool: Verdadeiro se o ID do processo jurídico for válido, Falso caso
          contrário.

Examplo:

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
