from random import randint


# FORMATTING
############


def remove_symbols(dirty):  # type: (str) -> str
    """
    Filters out CEP formatting symbols. Symbols that are not used
    in the CEP formatting are left unfiltered on purpose so that
    if fails other tests, because their presence indicate that the
    input was somehow corrupted.
    """
    return "".join(filter(lambda char: char not in ".-", dirty))


def format_cep(cep):  # type: (str) -> str
    """
    Will format an adequately formatted numbers-only CEP string,
    adding in standard formatting visual aid symbols for display.
    """

    if not is_valid(cep):
        return None

    return "{}-{}".format(cep[:5], cep[5:8])


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


def generate():  # type: () -> str
    """
    Generates a random valid CEP digit string. An optional branch
    number parameter can be given, it defaults to 1.
    """
    generated_number = ""

    for _ in range(0, 8):
        generated_number = generated_number + str(randint(0, 9))

    return generated_number
