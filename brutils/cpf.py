from secrets import randbelow


# FORMATTING
############

def sieve(dirty: str) -> str:
    """
    Filters out CPF formatting symbols. Symbols that are not used
    in the CPF formatting are left unfiltered on purpose so that
    if fails other tests, because their presence indicate that the
    input was somehow corrupted.
    """
    return ''.join(filter(lambda char: char not in '.-', dirty))


def display(cpf: str) -> str:
    """
    Will format an adequately formatted numbers-only CPF string,
    adding in standard formatting visual aid symbols for display.
    """
    if not cpf.isdigit() or len(cpf) != 11 or len(set(cpf)) == 1: return None
    return '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])


# CALCULATORS
#############

def hashdigit(cpf: str, position: int) -> int:
    """
    Will compute the given `position` checksum digit for the `cpf`
    input. The input needs to contain all elements previous to
    `position` else computation will yield the wrong result.
    """
    val = sum(int(digit) * weight for digit, weight in zip(cpf, range(position, 1, -1))) % 11
    return 0 if val < 2 else 11 - val


def checksum(basenum: str) -> str:
    """
    Will compute the checksum digits for a given CPF base number.
    `basenum` needs to be a digit-string of adequate length.
    """
    verifying_digits = ''
    verifying_digits += str(hashdigit(basenum, 10))
    verifying_digits += str(hashdigit(basenum + verifying_digits, 11))
    return verifying_digits


# OPERATIONS
############

def validate(cpf: str) -> bool:
    """
    Returns whether or not the verifying checksum digits of the
    given `cpf` match it's base number. Input should be a digit
    string of proper length.
    """
    if not cpf.isdigit() or len(cpf) != 11 or len(set(cpf)) == 1: return False
    return all(hashdigit(cpf, i +10) == int(v) for i, v in enumerate(cpf[9:]))


def generate() -> str:
    """Generates a random valid CPF digit string."""
    base = str(randbelow(1000000000)).zfill(9)
    return base + checksum(base)

