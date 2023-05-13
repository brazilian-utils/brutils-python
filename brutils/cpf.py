from random import randint


# FORMATTING
############


def sieve(dirty):  # type: (str) -> str
    """
    Filters out CPF formatting symbols. Symbols that are not used
    in the CPF formatting are left unfiltered on purpose so that
    if fails other tests, because their presence indicate that the
    input was somehow corrupted.
    """

    return "".join(filter(lambda char: char not in ".-", dirty))


def parse(dirty):  # type: (str) -> str
    """
    Filters out CPF formatting symbols. Symbols that are not used
    in the CPF formatting are left unfiltered on purpose so that
    if fails other tests, because their presence indicate that the
    input was somehow corrupted.
    """

    return sieve(dirty)


def display(cpf):  # type: (str) -> str
    """
    Will format an adequately formatted numbers-only CPF string,
    adding in standard formatting visual aid symbols for display.
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
    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])


# CALCULATORS
#############


def hashdigit(cpf, position):  # type: (str, int) -> int
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


def checksum(basenum):  # type: (str) -> str
    """
    Will compute the checksum digits for a given CPF base number.
    `basenum` needs to be a digit-string of adequate length.
    """
    verifying_digits = str(hashdigit(basenum, 10))
    verifying_digits += str(hashdigit(basenum + verifying_digits, 11))
    return verifying_digits


# OPERATIONS
############


def validate(cpf):  # type: (str) -> bool
    """
    Returns whether or not the verifying checksum digits of the
    given `cpf` match it's base number. Input should be a digit
    string of proper length.
    """
    if not cpf.isdigit() or len(cpf) != 11 or len(set(cpf)) == 1:
        return False
    return all(hashdigit(cpf, i + 10) == int(v) for i, v in enumerate(cpf[9:]))


def generate():  # type: () -> str
    """Generates a random valid CPF digit string."""
    base = str(randint(1, 999999998)).zfill(9)
    while len(set(base)) == 1:
        base = str(randint(1, 999999998)).zfill(9)
    return base + checksum(base)


def is_valid(cpf):  # type: (str) -> bool
    """
    Returns whether or not a cpf is_valid.
    Source: https://www.geradorcpf.com/algoritmo_do_cpf.htm
    """
    is_syntax_valid = isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit()

    return is_syntax_valid and _is_semantic_valid(cpf)


def _is_semantic_valid(cpf):
    cpf = [int(digit) for digit in cpf]

    constants_tenth_digit = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    is_tenth_digit_valid = _is_digit_valid(cpf, constants_tenth_digit, 9)

    constants_eleventh_digit = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    is_eleventh_digit_valid = _is_digit_valid(cpf, constants_eleventh_digit, 10)

    return is_tenth_digit_valid and is_eleventh_digit_valid


def _is_digit_valid(cpf, constants, digit_index):
    sum = _multiply_and_sum_lists(cpf, constants, digit_index)
    rest = sum % 11
    digit = cpf[digit_index]

    return (rest <= 2 and digit == 0) or (rest > 2 and digit == (11 - rest))


def _multiply_and_sum_lists(list_1, list_2, max_index):
    sum = 0

    for index in range(0, max_index):
        sum += list_1[index] * list_2[index]

    return sum
