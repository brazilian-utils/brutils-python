from random import randint

# FORMATTING
############


def remove_symbols(dirty):  # type: (str) -> str
    """
    Removes specific symbols from a given CEP (Postal Code).

    This function takes a CEP (Postal Code) as input and removes all occurrences
    of the '.' and '-' characters from it.

    Args:
        cep (str): The input CEP (Postal Code) containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.

    Example:
        >>> remove_symbols("123-45.678.9")
        "123456789"
        >>> remove_symbols("abc.xyz")
        "abcxyz"
    """

    return "".join(filter(lambda char: char not in ".-", dirty))


def format_cep(cep):  # type: (str) -> str
    """
    Formats a Brazilian CEP (Postal Code) into a standard format.

    This function takes a CEP (Postal Code) as input and, if it is a valid
    8-digit CEP, formats it into the standard "12345-678" format.

    Args:
        cep (str): The input CEP (Postal Code) to be formatted.

    Returns:
        str: The formatted CEP in the "12345-678" format if it's valid,
             None if it's not valid.

    Example:
        >>> format_cep("12345678")
        "12345-678"
        >>> format_cep("12345")
        None
    """

    if not is_valid(cep):
        return None

    return "{}-{}".format(cep[:5], cep[5:8])


# OPERATIONS
############


def is_valid(cep):  # type: (str) -> bool
    """
    Checks if a CEP (Postal Code) is valid.

    To be considered valid, the input must be a string containing exactly 8
    digits.
    This function does not verify if the CEP is a real postal code; it only
    validates the format of the string.

    Args:
        cep (str): The string containing the CEP to be checked.

    Returns:
        bool: True if the CEP is valid (8 digits), False otherwise.

    Example:
        >>> is_valid("12345678")
        True
        >>> is_valid("12345")
        False
        >>> is_valid("abcdefgh")
        False

    Source:
        https://en.wikipedia.org/wiki/Código_de_Endereçamento_Postal
    """

    return isinstance(cep, str) and len(cep) == 8 and cep.isdigit()


def generate():  # type: () -> str
    """
    Generates a random 8-digit CEP (Postal Code) number as a string.

    Returns:
        str: A randomly generated 8-digit number.

    Example:
        >>> generate()
        "12345678"
    """

    generated_number = ""

    for _ in range(0, 8):
        generated_number = generated_number + str(randint(0, 9))

    return generated_number
