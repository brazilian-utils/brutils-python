from itertools import chain
from secrets import randbelow


# FORMATTING
############

def sieve(dirty: str) -> str:
    """
    Filters out CNPJ formatting symbols. Symbols that are not used
    in the CNPJ formatting are left unfiltered on purpose so that
    if fails other tests, because their presence indicate that the
    input was somehow corrupted.
    """
    return ''.join(filter(lambda char: char not in './-', dirty))


def display(cnpj: str) -> str:
    """
    Will format an adequately formatted numbers-only CNPJ string,
    adding in standard formatting visual aid symbols for display.
    """
    if not cnpj.isdigit() or len(cnpj) != 14 or len(set(cnpj)) == 1: return None
    return '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])


# CALCULATORS
#############

def hashdigit(cnpj: str, position: int) -> int:
    """
    Will compute the given `position` checksum digit for the `cnpj`
    input. The input needs to contain all elements previous to
    `position` else computation will yield the wrong result.
    """
    weightgen = chain(range(position -8, 1, -1), range(9, 1, -1))
    val = sum(int(digit) * weight for digit, weight in zip(cnpj, weightgen)) % 11
    return 0 if val < 2 else 11 - val


def checksum(basenum: str) -> str:
    """
    Will compute the checksum digits for a given CNPJ base number.
    `basenum` needs to be a digit-string of adequate length.
    """
    verifying_digits = ''
    verifying_digits += str(hashdigit(basenum, 13))
    verifying_digits += str(hashdigit(basenum + verifying_digits, 14))
    return verifying_digits


# OPERATIONS
############

def validate(cnpj: str) -> bool:
    """
    Returns whether or not the verifying checksum digits of the
    given `cnpj` match it's base number. Input should be a digit
    string of proper length.
    """
    if not cnpj.isdigit() or len(cnpj) != 14 or len(set(cnpj)) == 1: return False
    return all(hashdigit(cnpj, i +13) == int(v) for i, v in enumerate(cnpj[12:]))


def generate(branch: int = 1) -> str:
    """
    Generates a random valid CNPJ digit string. An optional branch
    number parameter can be given, it defaults to 1.
    """
    base = str(randbelow(100000000)).zfill(8) + str(branch % 10000).zfill(4)
    return base + checksum(base)

