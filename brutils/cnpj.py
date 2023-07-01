from itertools import chain
from random import randint


# FORMATTING
############


def sieve(dirty):  # type: (str) -> str
    """
    Filters out CNPJ formatting symbols. Symbols that are not used
    in the CNPJ formatting are left unfiltered on purpose so that
    if fails other tests, because their presence indicate that the
    input was somehow corrupted.
    """
    return "".join(filter(lambda char: char not in "./-", dirty))


def remove_symbols(dirty):  # type: (str) -> str
    """Alias to the function `sieve`. Better naming."""
    return sieve(dirty)


def display(cnpj):  # type: (str) -> str
    """
    Will format an adequately formatted numbers-only CNPJ string,
    adding in standard formatting visual aid symbols for display.
    """
    if not cnpj.isdigit() or len(cnpj) != 14 or len(set(cnpj)) == 1:
        return None
    return "{}.{}.{}/{}-{}".format(
        cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:]
    )


def format_cnpj(cnpj):  # type: (str) -> str
    """
    Will format an adequately formatted numbers-only CNPJ string,
    adding in standard formatting visual aid symbols for display.
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
    Returns whether or not the verifying checksum digits of the
    given `cnpj` match it's base number. Input should be a digit
    string of proper length.
    """
    if not cnpj.isdigit() or len(cnpj) != 14 or len(set(cnpj)) == 1:
        return False
    return all(
        _hashdigit(cnpj, i + 13) == int(v) for i, v in enumerate(cnpj[12:])
    )


def is_valid(cnpj):  # type: (str) -> bool
    """
    Returns whether or not the verifying checksum digits of the
    given `cnpj` match it's base number. Input should be a digit
    string of proper length.
    Using this method name to match with the js library  api.
    Using the same method to ensure backwards compatibility.
    """
    return isinstance(cnpj, str) and validate(cnpj)


def generate(branch=1):  # type: (int) -> str
    """
    Generates a random valid CNPJ digit string. An optional branch
    number parameter can be given, it defaults to 1.
    """
    branch %= 10000
    branch += int(branch == 0)
    branch = str(branch).zfill(4)
    base = str(randint(0, 99999999)).zfill(8) + branch

    return base + _checksum(base)


def _hashdigit(cnpj, position):  # type: (str, int) -> int
    """
    Will compute the given `position` checksum digit for the `cnpj`
    input. The input needs to contain all elements previous to
    `position` else computation will yield the wrong result.
    """
    weightgen = chain(range(position - 8, 1, -1), range(9, 1, -1))
    val = (
        sum(int(digit) * weight for digit, weight in zip(cnpj, weightgen)) % 11
    )
    return 0 if val < 2 else 11 - val


def _checksum(basenum):  # type: (str) -> str
    """
    Will compute the checksum digits for a given CNPJ base number.
    `basenum` needs to be a digit-string of adequate length.
    """
    verifying_digits = str(_hashdigit(basenum, 13))
    verifying_digits += str(_hashdigit(basenum + verifying_digits, 14))
    return verifying_digits
