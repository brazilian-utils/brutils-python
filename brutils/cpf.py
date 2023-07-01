from random import randint


# FORMATTING
############


def sieve(dirty):  # type: (str) -> str
    """
    Filters out CPF formatting symbols.

    Symbols that are not used in the CPF formatting are left
    unfiltered on purpose so that if fails other tests,
    because their presence indicate that the input was somehow corrupted.
    """

    return "".join(filter(lambda char: char not in ".-", dirty))


def remove_symbols(dirty):  # type: (str) -> str
    """Alias to the function `sieve`. Better naming."""
    return sieve(dirty)


def display(cpf):  # type: (str) -> str
    """
    Format an adequately formatted numbers-only CPF string,
    adding in standard formatting visual aid symbols for display.
    Backcompatibility for Version 1.0.1.
    """

    if not cpf.isdigit() or len(cpf) != 11 or len(set(cpf)) == 1:
        return None

    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])


def format_cpf(cpf):  # type: (str) -> str
    """
    Format an adequately formatted numbers-only CPF string,
    Returns a cpf formatted with standard visual aid symbols.
    Returns None if cpf is invalid.
    """

    if not is_valid(cpf):
        return None

    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:11])


# OPERATIONS
############


def validate(cpf):  # type: (str) -> bool
    """
    Returns whether or not the verifying checksum digits of the
    given `cpf` match it's base number. Input should be a digit
    string of proper length.

    Source: https://www.geradorcpf.com/algoritmo_do_cpf.htm
    Backcompatibility for Version 1.0.1.
    """

    if not cpf.isdigit() or len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    return all(_hashdigit(cpf, i + 10) == int(v) for i, v in enumerate(cpf[9:]))


def is_valid(cpf):  # type: (str) -> bool
    """
    Evaluates that cpf is String and calls validate.
    """

    return isinstance(cpf, str) and validate(cpf)


def generate():  # type: () -> str
    """Generates a random valid CPF digit string."""

    base = str(randint(1, 999999998)).zfill(9)

    return base + _checksum(base)


def _hashdigit(cpf, position):  # type: (str, int) -> int
    """
    Will compute the given `position` checksum digit for the `cpf`
    input. The input needs to contain all elements previous to
    `position` else computation will yield the wrong result.
    """

    val = (
        sum(
            int(digit) * weight
            for digit, weight in zip(cpf, range(position, 1, -1))
        )
        % 11
    )

    return 0 if val < 2 else 11 - val


def _checksum(basenum):  # type: (str) -> str
    """
    Will compute the checksum digits for a given CPF base number.
    `basenum` needs to be a digit-string of adequate length.
    """

    verifying_digits = str(_hashdigit(basenum, 10))
    verifying_digits += str(_hashdigit(basenum + verifying_digits, 11))

    return verifying_digits
