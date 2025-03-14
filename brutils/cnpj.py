from itertools import chain
from json import loads
from random import randint
from urllib.error import HTTPError
from urllib.request import urlopen

from brutils.exceptions import CNPJNotFound, InvalidCNPJ
from brutils.types import CnpjData

# FORMATTING
############


def sieve(dirty):  # type: (str) -> str
    """
    Removes specific symbols from a CNPJ (Brazilian Company Registration
    Number) string.

    This function takes a CNPJ string as input and removes all occurrences of
    the '.', '/' and '-' characters from it.

    Args:
        cnpj (str): The CNPJ string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.

    Example:
        >>> sieve("12.345/6789-01")
        "12345678901"
        >>> sieve("98/76.543-2101")
        "98765432101"

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """

    return "".join(filter(lambda char: char not in "./-", dirty))


def remove_symbols(dirty):  # type: (str) -> str
    """
    This function is an alias for the `sieve` function, offering a more
    descriptive name.

    Args:
        dirty (str): The dirty string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.

    Example:
        >>> remove_symbols("12.345/6789-01")
        "12345678901"
        >>> remove_symbols("98/76.543-2101")
        "98765432101"
    """

    return sieve(dirty)


def display(cnpj):  # type: (str) -> str
    """
    Will format an adequately formatted numbers-only CNPJ string,
    adding in standard formatting visual aid symbols for display.

    Formats a CNPJ (Brazilian Company Registration Number) string for
    visual display.

    This function takes a CNPJ string as input, validates its format, and
    formats it with standard visual aid symbols for display purposes.

    Args:
        cnpj (str): The CNPJ string to be formatted for display.

    Returns:
        str: The formatted CNPJ with visual aid symbols if it's valid,
             None if it's not valid.

    Example:
        >>> display("12345678901234")
        "12.345.678/9012-34"
        >>> display("98765432100100")
        "98.765.432/1001-00"

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """

    if not cnpj.isdigit() or len(cnpj) != 14 or len(set(cnpj)) == 1:
        return None
    return "{}.{}.{}/{}-{}".format(
        cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:]
    )


def format_cnpj(cnpj):  # type: (str) -> str
    """
    Formats a CNPJ (Brazilian Company Registration Number) string for visual
    display.

    This function takes a CNPJ string as input, validates its format, and
    formats it with standard visual aid symbols for display purposes.

    Args:
        cnpj (str): The CNPJ string to be formatted for display.

    Returns:
        str: The formatted CNPJ with visual aid symbols if it's valid,
             None if it's not valid.

    Example:
        >>> format_cnpj("03560714000142")
        '03.560.714/0001-42'
        >>> format_cnpj("98765432100100")
        None
    """

    if not is_valid(cnpj):
        return None

    return "{}.{}.{}/{}-{}".format(
        cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14]
    )


# OPERATIONS
############


def validate(cnpj):  # type: (str) -> bool
    """
    Validates a CNPJ (Brazilian Company Registration Number) by comparing its
    verifying checksum digits to its base number.

    This function checks the validity of a CNPJ by comparing its verifying
    checksum digits to its base number. The input should be a string of digits
    with the appropriate length.

    Args:
        cnpj (str): The CNPJ to be validated.

    Returns:
        bool: True if the checksum digits match the base number,
              False otherwise.

    Example:
        >>> validate("03560714000142")
        True
        >>> validate("00111222000133")
        False

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """

    if not cnpj.isdigit() or len(cnpj) != 14 or len(set(cnpj)) == 1:
        return False
    return all(
        _hashdigit(cnpj, i + 13) == int(v) for i, v in enumerate(cnpj[12:])
    )


def is_valid(cnpj):  # type: (str) -> bool
    """
    Returns whether or not the verifying checksum digits of the given `cnpj`
    match its base number.

    This function does not verify the existence of the CNPJ; it only
    validates the format of the string.

    Args:
        cnpj (str): The CNPJ to be validated, a 14-digit string

    Returns:
        bool: True if the checksum digits match the base number,
              False otherwise.

    Example:
        >>> is_valid("03560714000142")
        True
        >>> is_valid("00111222000133")
        False
    """

    return isinstance(cnpj, str) and validate(cnpj)


def generate(branch=1):  # type: (int) -> str
    """
    Generates a random valid CNPJ digit string. An optional branch number
    parameter can be given; it defaults to 1.

    Args:
        branch (int): An optional branch number to be included in the CNPJ.

    Returns:
        str: A randomly generated valid CNPJ string.

    Example:
        >>> generate()
        "30180536000105"
        >>> generate(1234)
        "01745284123455"
    """

    branch %= 10000
    branch += int(branch == 0)
    branch = str(branch).zfill(4)
    base = str(randint(0, 99999999)).zfill(8) + branch

    return base + _checksum(base)


def _hashdigit(cnpj, position):  # type: (str, int) -> int
    """
    Calculates the checksum digit at the given `position` for the provided
    `cnpj`. The input must contain all elements before `position`.

    Args:
        cnpj (str): The CNPJ for which the checksum digit is calculated.
        position (int): The position of the checksum digit to be calculated.

    Returns:
        int: The calculated checksum digit.

    Example:
        >>> _hashdigit("12345678901234", 13)
        3
        >>> _hashdigit("98765432100100", 14)
        9
    """

    weightgen = chain(range(position - 8, 1, -1), range(9, 1, -1))
    val = (
        sum(int(digit) * weight for digit, weight in zip(cnpj, weightgen)) % 11
    )
    return 0 if val < 2 else 11 - val


def _checksum(basenum):  # type: (str) -> str
    """
    Calculates the verifying checksum digits for a given CNPJ base number.

    This function computes the verifying checksum digits for a provided CNPJ
    base number. The `basenum` should be a digit-string of the appropriate
    length.

    Args:
        basenum (str): The base number of the CNPJ for which verifying checksum
                       digits are calculated.

    Returns:
        str: The verifying checksum digits.

    Example:
        >>> _checksum("123456789012")
        "30"
        >>> _checksum("987654321001")
        "41"
    """

    verifying_digits = str(_hashdigit(basenum, 13))
    verifying_digits += str(_hashdigit(basenum + verifying_digits, 14))
    return verifying_digits

def get_cnpj_information(cnpj, raise_exceptions=False):  # type: (str, bool) -> CnpjData | None
    """
    Fetches company information from a given CNPJ (Brazilian Company
    Registration Number) using the CNPJws API.

    Args:
        cnpj (str): The CNPJ to be checked.
        raise_exceptions (bool, optional): Whether to raise exceptions when the CNPJ is invalid or not found. Defaults to False.
        
    Raises:
        InvalidCNPJ: When the given CNPJ is not valid.
        CNPJNotFound: When the given CNPJ is not found in the database.

    Returns:
        CnpjData: A dictionary containing the company information fetched from the
              ReceitaWS API.
              
    Example:
        >>> get_cnpj_information("42.064.856/0001-70")
        {
            'cnpj_raiz': '42064856',
            'razao_social': 'C D TIRABASSI JUNIOR TECNOLOGIA DA INFORMACAO LTDA',
            'capital_social': '1000.00',
            'responsavel_federativo': '',
            'atualizado_em': '2025-02-08T03:00:00.000Z',
            'porte': {
                'id': '01',
                'descricao': 'Micro Empresa'
            },
            'natureza_juridica': {
                'id': '2062',
                'descricao': 'Sociedade Empresária Limitada'
            },
            'qualificacao_do_responsavel': {
                'id': 49,
                'descricao': 'Sócio-Administrador '
            },
            'socios': [
                {
                'cpf_cnpj_socio': '***529958**',
                'nome': 'CARLOS DONIZETE TIRABASSI JUNIOR',
                'tipo': 'Pessoa Física',
                'data_entrada': '2021-05-24',
                'cpf_representante_legal': '***000000**',
                'nome_representante': None,
                'faixa_etaria': '31 a 40 anos',
                'atualizado_em': '2025-02-08T03:00:00.000Z',
                'pais_id': '1058',
                'qualificacao_socio': {
                    'id': 49,
                    'descricao': 'Sócio-Administrador '
                },
                'qualificacao_representante': None,
                'pais': {
                    'id': '1058',
                    'iso2': 'BR',
                    'iso3': 'BRA',
                    'nome': 'Brasil',
                    'comex_id': '105'
                }
                }
            ],
            'simples': {
                'simples': 'Sim',
                'data_opcao_simples': '2021-05-24',
                'data_exclusao_simples': None,
                'mei': 'Não',
                'data_opcao_mei': None,
                'data_exclusao_mei': None,
                'atualizado_em': '2025-02-08T03:00:00.000Z'
            },
            'estabelecimento': {
                'cnpj': '42064856000170',
                'atividades_secundarias': [
                {
                    'id': '6201501',
                    'secao': 'J',
                    'divisao': '62',
                    'grupo': '62.0',
                    'classe': '62.01-5',
                    'subclasse': '6201-5/01',
                    'descricao': 'Desenvolvimento de programas de computador sob encomenda'
                },
                {
                    'id': '6201502',
                    'secao': 'J',
                    'divisao': '62',
                    'grupo': '62.0',
                    'classe': '62.01-5',
                    'subclasse': '6201-5/02',
                    'descricao': 'Web desing'
                },
                {
                    'id': '6202300',
                    'secao': 'J',
                    'divisao': '62',
                    'grupo': '62.0',
                    'classe': '62.02-3',
                    'subclasse': '6202-3/00',
                    'descricao': 'Desenvolvimento e licenciamento de programas de computador customizáveis'
                },
                {
                    'id': '6204000',
                    'secao': 'J',
                    'divisao': '62',
                    'grupo': '62.0',
                    'classe': '62.04-0',
                    'subclasse': '6204-0/00',
                    'descricao': 'Consultoria em tecnologia da informação'
                },
                {
                    'id': '6209100',
                    'secao': 'J',
                    'divisao': '62',
                    'grupo': '62.0',
                    'classe': '62.09-1',
                    'subclasse': '6209-1/00',
                    'descricao': 'Suporte técnico, manutenção e outros serviços em tecnologia da informação'
                },
                {
                    'id': '6311900',
                    'secao': 'J',
                    'divisao': '63',
                    'grupo': '63.1',
                    'classe': '63.11-9',
                    'subclasse': '6311-9/00',
                    'descricao': 'Tratamento de dados, provedores de serviços de aplicação e serviços de hospedagem na Internet'
                },
                {
                    'id': '6319400',
                    'secao': 'J',
                    'divisao': '63',
                    'grupo': '63.1',
                    'classe': '63.19-4',
                    'subclasse': '6319-4/00',
                    'descricao': 'Portais, provedores de conteúdo e outros serviços de informação na Internet'
                },
                {
                    'id': '8599603',
                    'secao': 'P',
                    'divisao': '85',
                    'grupo': '85.9',
                    'classe': '85.99-6',
                    'subclasse': '8599-6/03',
                    'descricao': 'Treinamento em informática'
                }
                ],
                'cnpj_raiz': '42064856',
                'cnpj_ordem': '0001',
                'cnpj_digito_verificador': '70',
                'tipo': 'Matriz',
                'nome_fantasia': 'BITIZE',
                'situacao_cadastral': 'Ativa',
                'data_situacao_cadastral': '2021-05-24',
                'data_inicio_atividade': '2021-05-24',
                'nome_cidade_exterior': None,
                'tipo_logradouro': 'RUA',
                'logradouro': 'EUGENIO RABELLO',
                'numero': '98',
                'complemento': None,
                'bairro': 'JARDIM EMBAIXADOR',
                'cep': '18040436',
                'ddd1': '41',
                'telefone1': '96869828',
                'ddd2': None,
                'telefone2': None,
                'ddd_fax': None,
                'fax': None,
                'email': 'meucnpj@contabilizei.com.br',
                'situacao_especial': None,
                'data_situacao_especial': None,
                'atualizado_em': '2025-02-08T03:00:00.000Z',
                'atividade_principal': {
                'id': '6203100',
                'secao': 'J',
                'divisao': '62',
                'grupo': '62.0',
                'classe': '62.03-1',
                'subclasse': '6203-1/00',
                'descricao': 'Desenvolvimento e licenciamento de programas de computador não customizáveis'
                },
                'pais': {
                'id': '1058',
                'iso2': 'BR',
                'iso3': 'BRA',
                'nome': 'Brasil',
                'comex_id': '105'
                },
                'estado': {
                'id': 26,
                'nome': 'São Paulo',
                'sigla': 'SP',
                'ibge_id': 35
                },
                'cidade': {
                'id': 3851,
                'nome': 'Sorocaba',
                'ibge_id': 3552205,
                'siafi_id': '7145'
                },
                'motivo_situacao_cadastral': None,
                'inscricoes_estaduais': [
                
                ]
            }
            }
    """
    base_api_url = "https://publica.cnpj.ws/cnpj/{}"
    
    clean_cnpj = remove_symbols(cnpj)
    cnpj_is_valid = is_valid(clean_cnpj)
    
    if not cnpj_is_valid:
        if raise_exceptions:
            raise InvalidCNPJ(cnpj)

        return None
    
    try:
        with urlopen(base_api_url.format(clean_cnpj)) as f:
            response = f.read()
            data = loads(response)

            return CnpjData(**data)
        
    except HTTPError as e:
        if raise_exceptions:
            if e.code == 400:
                raise InvalidCNPJ(cnpj) from e

            elif e.code == 404:
                raise CNPJNotFound(cnpj) from e
            
            raise e

        return None

    except Exception as e:
        if raise_exceptions:
            raise CNPJNotFound(cnpj) from e

        return None