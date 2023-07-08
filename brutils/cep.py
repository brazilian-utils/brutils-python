from random import randint


# FORMATTING
############


# OPERATIONS
############


def is_valid(cep):  # type: (str) -> bool
    """
    Returns when CEP is valid, input should be a digit
    string of proper length. Doesn't validate if it's real,
    'cause only the "Correios" Base does.

    Source: https://en.wikipedia.org/wiki/C%C3%B3digo_de_Endere%C3%A7amento_Postal

    """

    return isinstance(cep, str) and len(cep) == 8 and cep.isdigit()
