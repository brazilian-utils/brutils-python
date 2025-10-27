from itertools import chain
from random import randint, choice
import string


# =============================================================================
# 27-10-2025
# Estou seguindo o que foi explicitado aqui para as mudanças sugeridas:
# https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/141102
# Especificamente no Anexo Único
# =============================================================================

# =============================================================================
# FORMATTING
# =============================================================================


def sieve(dirty):  # type: (str) -> str
    """
    Removes specific symbols from a CNPJ (Brazilian Company Registration
    Number) string.

    This function takes a CNPJ string as input and removes all occurrences of
    the '.', '/' and '-' characters from it.

    Args:
        cnpj (str): The CNPJ string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.

    Example:
        >>> sieve("12.345/6789-01")
        "12345678901"
        >>> sieve("98/76.543-2101")
        "98765432101"

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """

    return "".join(filter(lambda char: char not in "./-", dirty))


def remove_symbols(dirty):  # type: (str) -> str
    """
    This function is an alias for the `sieve` function, offering a more
    descriptive name.

    Args:
        dirty (str): The dirty string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.

    Example:
        >>> remove_symbols("12.345/6789-01")
        "12345678901"
        >>> remove_symbols("98/76.543-2101")
        "98765432101"
    """

    return sieve(dirty)


def display(cnpj):  # type: (str) -> str
    """
    Formats a CNPJ (Brazilian Company Registration Number) string for
    visual display, adding standard separators.

    Supports both numeric and alphanumeric formats, following the
    2026 specification.

    Args:
        cnpj (str): The CNPJ string (numeric or alphanumeric).

    Returns:
        str: The formatted CNPJ string, or None if invalid.

    Example:
        >>> display("12345678000195")
        "12.345.678/0001-95"
        >>> display("12ABC34501DE35")
        "12.ABC.345/01DE-35"

    Notes:
        - Prior to 2026, only numeric CNPJs are expected.
        - From 2026 onwards, alphanumeric roots and orders are allowed.
    """
    clean = sieve(cnpj)

    # Must have exactly 14 characters (including letters/numbers)
    if len(clean) != 14 or len(set(clean)) == 1:
        return None

    # Split parts (root, order, DV)
    root = clean[:8]
    order = clean[8:12]
    dv = clean[12:]

    # Compose visually formatted CNPJ
    return "{}.{}.{}/{}-{}".format(root[:2], root[2:5], root[5:8], order, dv)




def format_cnpj(cnpj):  # type: (str) -> str
    """
    Validates and formats a CNPJ (Brazilian Company Registration Number)
    for visual display.

    Supports both numeric and alphanumeric formats (post-2026).

    Args:
        cnpj (str): The CNPJ string to be formatted.

    Returns:
        str: A formatted version of the CNPJ if valid, or None if invalid.

    Example:
        >>> format_cnpj("03560714000142")
        '03.560.714/0001-42'
        >>> format_cnpj("12ABC34501DE35")
        '12.ABC.345/01DE-35'
    """
    if not is_valid(cnpj):
        return None
    return display(sieve(cnpj))


# =============================================================================
# VALIDATION HELPERS
# =============================================================================


def is_alphanumeric_cnpj(cnpj):  # type: (str) -> bool
    """
    Detects whether a given CNPJ contains letters, indicating
    the new alphanumeric format valid from 2026 onwards.

    Args:
        cnpj (str): The CNPJ string to analyze.

    Returns:
        bool: True if the CNPJ includes alphabetic characters.
    """
    return any(ch.isalpha() for ch in cnpj)


def ascii_value(ch):  # type: (str) -> int
    """
    Converts a single alphanumeric character into its numeric value
    used in the alphanumeric CNPJ checksum calculation.
    """
    if not ch.isalnum():
        raise ValueError(f"Invalid CNPJ character: {ch}")
    return ord(ch.upper()) - 48



# =============================================================================
# CORE VALIDATION AND CHECKSUM LOGIC
# =============================================================================


def validate(cnpj):  # type: (str) -> bool
    """
    Validates both traditional numeric CNPJs and the new
    alphanumeric format introduced in 2026.

    The validation rule used depends on whether the CNPJ contains
    alphabetic characters.

    Args:
        cnpj (str): The CNPJ string (numeric or alphanumeric).

    Returns:
        bool: True if the CNPJ is valid according to its format.
    """
    clean = sieve(cnpj)
    if len(clean) != 14:
        return False

    # Detect which version of the CNPJ is being used
    if is_alphanumeric_cnpj(clean):
        base, dv = clean[:12], clean[12:]
        expected = _checksum_alphanumeric(base)
    else:
        base, dv = clean[:12], clean[12:]
        expected = _checksum(base)

    return dv == expected


def is_valid(cnpj):  # type: (str) -> bool
    """
    Checks whether the given CNPJ string (numeric or alphanumeric)
    is valid by verifying its checksum digits.

    Args:
        cnpj (str): The CNPJ to be validated.

    Returns:
        bool: True if the CNPJ is valid, False otherwise.

    Example:
        >>> is_valid("34665388000161")
        True
        >>> is_valid("12ABC34501DE35")
        True
        >>> is_valid("00000000000000")
        False
    """

    return isinstance(cnpj, str) and validate(cnpj)


# =============================================================================
# CHECKSUM GENERATION (NUMERIC)
# =============================================================================


def _hashdigit(cnpj, position):  # type: (str, int) -> int
    """
    Calculates the checksum digit at the given `position` for the provided
    `cnpj`. The input must contain all elements before `position`.

    Args:
        cnpj (str): The CNPJ for which the checksum digit is calculated.
        position (int): The position of the checksum digit to be calculated.

    Returns:
        int: The calculated checksum digit.
    """
    weightgen = chain(range(position - 8, 1, -1), range(9, 1, -1))
    val = (
        sum(int(digit) * weight for digit, weight in zip(cnpj, weightgen)) % 11
    )
    return 0 if val < 2 else 11 - val


def _checksum(basenum):  # type: (str) -> str
    """
    Calculates the verifying checksum digits for a given numeric CNPJ base.

    Args:
        basenum (str): The 12-digit numeric CNPJ base.

    Returns:
        str: The 2 verifying digits.
    """
    verifying_digits = str(_hashdigit(basenum, 13))
    verifying_digits += str(_hashdigit(basenum + verifying_digits, 14))
    return verifying_digits


# =============================================================================
# CHECKSUM GENERATION (ALPHANUMERIC)
# =============================================================================


def _hashdigit_alphanumeric(cnpj, position):  # type: (str, int) -> int
    """
    Calculates the checksum digit at the given `position` for the
    alphanumeric CNPJ format (valid from 2026).

    Conversion uses ASCII values minus 48, as defined by RFB.

    Args:
        cnpj (str): The alphanumeric CNPJ string.
        position (int): The position of the checksum digit.

    Returns:
        int: The calculated checksum digit.
    """
    weightgen = chain(range(position - 8, 1, -1), range(9, 1, -1))
    converted = [ascii_value(ch) for ch in cnpj]
    val = sum(v * w for v, w in zip(converted, weightgen)) % 11
    return 0 if val < 2 else 11 - val


def _checksum_alphanumeric(basenum):  # type: (str) -> str
    """
    Calculates the verifying checksum digits for an alphanumeric
    CNPJ base, following the ASCII - 48 rule and Mod 11.

    Args:
        basenum (str): The 12-character alphanumeric base.

    Returns:
        str: The 2 verifying digits.
    """
    d1 = _hashdigit_alphanumeric(basenum, 13)
    d2 = _hashdigit_alphanumeric(basenum + str(d1), 14)
    return f"{d1}{d2}"


# =============================================================================
# GENERATION
# =============================================================================


def generate(branch=1, new_format=False):  # type: (int, bool) -> str
    """
    Generates a valid CNPJ string.

    If `new_format` is False, a traditional numeric CNPJ will be generated.
    If `new_format` is True, an alphanumeric CNPJ will be generated following
    the 2026 specification (letters allowed in positions 1–12).

    Args:
        branch (int): Optional branch number for numeric CNPJs (default = 1).
        new_format (bool): If True, uses the alphanumeric CNPJ rules.

    Returns:
        str: A valid CNPJ string (numeric or alphanumeric).

    Example:
        >>> generate()
        "30180536000105"
        >>> generate(new_format=True)
        "12AB3C4D0001E5"
    """
    if new_format:
        # Generate alphanumeric root (8 chars) and order (4 chars)
        alphabet = string.ascii_uppercase + string.digits
        base = "".join(choice(alphabet) for _ in range(12))
        return base + _checksum_alphanumeric(base)

    # Legacy numeric format (default)
    branch %= 10000
    branch += int(branch == 0)
    branch = str(branch).zfill(4)
    base = str(randint(0, 99999999)).zfill(8) + branch
    return base + _checksum(base)
