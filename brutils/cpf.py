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
    Will format an adequately formatted numbers-only CPF string,
    adding in standard formatting visual aid symbols for display.
    """
    return display(cpf)


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


# source: https://www.geradorcpf.com/algoritmo_do_cpf.htm
def is_valid(cpf):  # type: (str) -> bool
    """
    Returns whether or not the verifying checksum digits of the
    given `cpf` match it's base number. Input should be a digit
    string of proper length.
    Using this method name to match with the js library  api.
    Using the same method to ensure backwards compatibility.
    """
    print("\n### cpf ###\n")
    print(cpf)
    is_valid = isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit()

    if not is_valid:
        print("not string or not len 11 or not only digits")
        return

    ### 10th Digit Verification ###

    nine_first_digits = cpf[0:9]
    constants_tenth_digit = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    nine_first_digits = list(nine_first_digits)
    nine_first_digits_int = []

    for digit in nine_first_digits:
        nine_first_digits_int.append(int(digit))

    sum = 0

    for index in range(0, 9):
        sum += nine_first_digits_int[index] * constants_tenth_digit[index]

    rest = sum % 11

    tenth_digit_int = int(cpf[9])

    print("10th digit verification")
    print("sum", sum)
    print("rest", rest)

    if rest < 2 and tenth_digit_int != 0:
        print("tenth digit not valid")
        return False

    if rest >= 2 and tenth_digit_int != (11 - rest):
        print("tenth digit not valid")
        return False

    ### 11th Digit Verification ###

    x = nine_first_digits_int + [tenth_digit_int]
    constants_eleventh_digit = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    sum_2 = 0

    for index in range(0, 10):
        sum_2 += x[index] * constants_eleventh_digit[index]

    rest_2 = sum_2 % 11

    print("11th digit verification")
    print("sum_2", sum_2)
    print("rest_2", rest_2)

    eleventh_digit_int = int(cpf[10])

    if rest_2 < 2 and eleventh_digit_int != 0:
        print("eleventh digit not valid")
        return False

    if rest_2 >= 2 and eleventh_digit_int != (11 - rest_2):
        print("eleventh digit not valid")
        return False

    return True


def generate():  # type: () -> str
    """Generates a random valid CPF digit string."""
    base = str(randint(1, 999999998)).zfill(9)
    while len(set(base)) == 1:
        base = str(randint(1, 999999998)).zfill(9)
    return base + checksum(base)
