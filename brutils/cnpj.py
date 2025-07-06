from itertools import chain
from random import randint

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

    Aceita tanto o formato antigo (14 dígitos) quanto o novo (12 alfanuméricos + 2 dígitos).

    Returns:
        str: The formatted CNPJ with visual aid symbols if it's valid,
             None if it's not valid.
    """
    if not isinstance(cnpj, str) or len(cnpj) != 14:
        return None
    # Formato antigo: só números
    if cnpj.isdigit():
        if not is_valid(cnpj):
            return None
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
    # Novo formato: 12 alfanuméricos + 2 dígitos
    if cnpj[:12].isalnum() and cnpj[-2:].isdigit() and is_valid_cnpj(cnpj):
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
    return None


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


def _mod11_alfanumerico(cnpj_base: str) -> str:
    """
    Calcula os dois dígitos verificadores para o novo CNPJ alfanumérico.
    Cada caractere é convertido para valor numérico: ord(CHAR) - 48.
    """
    def char_to_num(c):
        return ord(c) - 48

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1
    nums = [char_to_num(c) for c in cnpj_base]
    # Primeiro DV
    soma1 = sum(n * p for n, p in zip(nums, pesos1))
    dv1 = 11 - (soma1 % 11)
    if dv1 >= 10:
        dv1 = 0
    # Segundo DV
    nums2 = nums + [dv1]
    soma2 = sum(n * p for n, p in zip(nums2, pesos2))
    dv2 = 11 - (soma2 % 11)
    if dv2 >= 10:
        dv2 = 0
    return f"{dv1}{dv2}"


def is_valid_cnpj(cnpj: str) -> bool:
    """
    Valida CNPJ nos dois formatos:
    - Antigo: 14 dígitos numéricos
    - Novo: 12 alfanuméricos (A-Z, 0-9) + 2 dígitos
    """
    if not isinstance(cnpj, str):
        return False
    cnpj = cnpj.strip()
    if len(cnpj) != 14:
        return False
    # Formato antigo: só números
    if cnpj.isdigit():
        return is_valid(cnpj)
    # Novo formato: 12 alfanuméricos + 2 dígitos
    if not (cnpj[:12].isalnum() and cnpj[-2:].isdigit()):
        return False
    cnpj_base = cnpj[:12]
    dv = cnpj[-2:]
    dv_calc = _mod11_alfanumerico(cnpj_base)
    return dv == dv_calc


def remove_symbols_cnpj(cnpj: str) -> str:
    """
    Remove símbolos de um CNPJ em qualquer formato.
    """
    return ''.join(c for c in cnpj if c.isalnum())


def generate_cnpj(new_format=False) -> str:
    """
    Gera CNPJ válido no formato antigo (apenas números) ou novo (alfanumérico).
    """
    from random import choice
    import string
    if not new_format:
        # Geração padrão já existente
        return generate()
    # Novo formato: 12 alfanuméricos + 2 dígitos
    alfanum = string.ascii_uppercase + string.digits
    cnpj_base = ''.join(choice(alfanum) for _ in range(12))
    dv = _mod11_alfanumerico(cnpj_base)
    return cnpj_base + dv
