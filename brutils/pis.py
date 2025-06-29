from random import randint

WEIGHTS = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

# FORMATTING
############


def remove_symbols(pis: str) -> str:
    """
    Remove formatting symbols from a PIS.

    This function takes a PIS (Programa de Integração Social) string with
    formatting symbols and returns a cleaned version with no symbols.

    Args:
        pis (str): A PIS string that may contain formatting symbols.

    Returns:
        str: A cleaned PIS string with no formatting symbols.

    Example:
        >>> remove_symbols("123.456.789-09")
        '12345678909'
        >>> remove_symbols("98765432100")
        '98765432100'
    """
    return pis.replace(".", "").replace("-", "")


def format_pis(pis: str) -> str:
    """
    Format a valid PIS (Programa de Integração Social) string with
    standard visual aid symbols.

    This function takes a valid numbers-only PIS string as input
    and adds standard formatting visual aid symbols for display.

    Args:
        pis (str): A valid numbers-only PIS string.

    Returns:
        str: A formatted PIS string with standard visual aid symbols
        or None if the input is invalid.

    Example:
        >>> format_pis("12345678909")
        '123.45678.90-9'
        >>> format_pis("98765432100")
        '987.65432.10-0'
    """

    if not is_valid(pis):
        return None

    return "{}.{}.{}-{}".format(pis[:3], pis[3:8], pis[8:10], pis[10:11])


# OPERATIONS
############


def is_valid_pis_pasep(pis_pasep: str) -> bool: # Renomeada de is_valid
    """
    Validates a given PIS/Pasep number.

    This function checks if the provided PIS/Pasep number is valid according to the official
    validation rules. It returns True if the number is valid, and False otherwise.

    Args:
        pis_pasep (str): The PIS/Pasep number to be validated.

    Returns:
        bool: True if the PIS/Pasep number is valid, False otherwise.

    Example:
        >>> is_valid_pis_pasep('123.45678.90-1')
        True
        >>> is_valid_pis_pasep('12345678901')
        True
        >>> is_valid_pis_pasep('PIS inválido')
        False
        >>> is_valid_pis_pasep('123.45678.90-0')
        False
    """
    if not isinstance(pis_pasep, str):
        return False

    cleaned_pis = remove_symbols(pis_pasep)

    if not (len(cleaned_pis) == 11 and cleaned_pis.isdigit()):
        return False

    base_pis = cleaned_pis[:-1]
    check_digit_given = int(cleaned_pis[-1])
    
    calculated_check_digit = _checksum(base_pis)

    return check_digit_given == calculated_check_digit


def generate() -> str:
    """
    Generate a random valid Brazilian PIS number.

    This function generates a random PIS number with the following characteristics:
    - It has 11 digits
    - It passes the weight calculation check

    Args:
        None

    Returns:
        str: A randomly generated valid PIS number as a string.

    Example:
        >>> generate()
        '12345678909'
        >>> generate()
        '98765432100'
    """
    base = str(randint(0, 9999999999)).zfill(10)

    return base + str(_checksum(base))


def _checksum(base_pis: str) -> int:
    """
    Calculate the checksum digit of the given `base_pis` string.

    Args:
        base_pis (str): The first 10 digits of a PIS number as a string.

    Returns:
        int: The checksum digit.
    """
    pis_digits = list(map(int, base_pis))
    pis_sum = sum(digit * weight for digit, weight in zip(pis_digits, WEIGHTS))
    check_digit = 11 - (pis_sum % 11)

    return 0 if check_digit in [10, 11] else check_digit
