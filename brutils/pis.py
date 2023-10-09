from random import randint


WEIGHTS = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

# FORMATTING
############

# to do: remover este comentário e adicionar a implementação da formatação do PIS.

# OPERATIONS
############


def validate(pis: str) -> bool:
    """
    Validate a Brazilian PIS number.

    The PIS is valid if:
    - It has 11 digits
    - All characters are digits
    - It passes the weight calculation check

    Args:
        pis[str]: PIS number as a string.

    Returns:
        value[bool]: True if PIS is valid, False otherwise.
    """
    if len(pis) != 11 or not pis.isdigit():
        return False

    return pis[-1] == str(_checksum(pis[:-1]))


def is_valid(pis: str) -> bool:
    """
    Returns whether or not the verifying checksum digit of the
    given `pis` match its base number.

    Args:
        pis[str]: PIS number as a string of proper length.

    Returns:
        value[bool]: True if PIS is valid, False otherwise.
    """
    return isinstance(pis, str) and validate(pis)


def generate() -> str:
    """
    Generates a random valid Brazilian PIS number.

    Args:
        None

    Returns:
        value[str]: PIS number as a string.
    """
    base = str(randint(0, 9999999999)).zfill(10)

    return base + str(_checksum(base))


def _checksum(base_pis: str) -> int:
    """
    Calculates the checksum digit of the given `base_pis` string.

    Args:
        base_pis [str]: 10 first digits of PIS number as a string.

    Returns:
        value [int]: Checksum digit.
    """
    pis_digits = list(map(int, base_pis))
    pis_sum = sum(digit * weight for digit, weight in zip(pis_digits, WEIGHTS))
    check_digit = 11 - (pis_sum % 11)

    return 0 if check_digit in [10, 11] else check_digit


def format_pis(pis: str) -> str:
    """
    Format an adequately formatted numbers-only PIS string,
    Returns a PIS formatted with standard visual aid symbols.
    Returns :
        value [str]: PIS formatted
    """

    if not is_valid(pis):
        return None

    return "{}.{}.{}-{}".format(pis[:3], pis[3:8], pis[8:10], pis[10:11])
