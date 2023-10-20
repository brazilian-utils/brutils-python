import re
from typing import Optional
from random import choice, randint
from string import ascii_uppercase

# FORMATTING
############


def convert_to_mercosul(license_plate: str) -> Optional[str]:
    """
    Converts an old pattern license plate (LLLNNNN) to a Mercosul format
    (LLLNLNN).

    Args:
        license_plate (str): A string of proper length representing the
                             old pattern license plate.

    Returns:
        Optional[str]: The converted Mercosul license plate (LLLNLNN) or
                       'None' if the input is invalid.

    Example:
        >>> convert_to_mercosul("ABC4567")
        'ABC4F67'
        >>> convert_to_mercosul("ABC4*67")
        None
    """

    if not is_valid_old_format(license_plate):
        return None

    digits = [letter for letter in license_plate.upper()]
    digits[4] = chr(ord("A") + int(digits[4]))
    return "".join(digits)


def format(license_plate: str) -> Optional[str]:
    """
    Formats a license plate into the correct pattern.
    This function receives a license plate in any pattern (LLLNNNN or LLLNLNN)
    and returns a formatted version.

    Args:
        license_plate (str): A license plate string.

    Returns:
        Optional[str]: The formatted license plate string or 'None' if the
                       input is invalid.

    Example:
        >>> format("ABC1234") # old format (contains a dash)
        'ABC-1234'
        >>> format("abc1e34") # mercosul format
        'ABC1E34'
        >>> format("ABC123")
        None
    """

    license_plate = license_plate.upper()

    if is_valid_old_format(license_plate):
        return license_plate[0:3] + "-" + license_plate[3:]

    if is_valid_mercosul(license_plate):
        return license_plate.upper()

    return None


# OPERATIONS
############


def is_valid(license_plate: str) -> bool:
    """
    Check if a license plate is valid.
    This function does not verify if the license plate is a real license plate;
    it only validates the format of the string.

    Args:
        license_plate (str): A license plate string.

    Returns:
        bool: True if the license plate is valid, False otherwise.

    Example:
        >>> is_valid('def5678')
        True
        >>> is_valid('abc1e67')
        True
        >>> is_valid('abe67')
        False
    """

    return is_valid_old_format(license_plate) or is_valid_mercosul(
        license_plate
    )


def is_valid_old_format(license_plate: str) -> bool:
    """
    Checks whether a string matches the old format of Brazilian license plate
    (LLLNNNN).
    This function does not verify if the license plate is a real license plate;
    it only validates the format of the string.

    Args:
        license_plate (str): A license plate string.

    Returns:
        bool: True if the string corresponds to a license plate in the old
              pattern format, False otherwise.

    Example:
        >>> is_valid_old_format('def5678')
        True
        >>> is_valid_old_format('GHI-4567')
        False
    """

    pattern = re.compile(r"^[A-Za-z]{3}[0-9]{4}$")
    return (
        isinstance(license_plate, str)
        and re.match(pattern, license_plate.strip()) is not None
    )


def is_valid_mercosul(license_plate: str) -> bool:
    """
    Checks whether a string matches the Mercosul license plate format (LLLNNNN).
    This function does not verify if the license plate is a real license plate;
    it only validates the format of the string.

    Args:
        license_plate (str): A license plate string.

    Returns:
        bool: True if the string corresponds to a license plate in the Mercosul
              pattern format, False otherwise.

    Example:
        >>> is_valid_mercosul('abc4e67')
        True
        >>> is_valid_mercosul('abc167')
        False
    """

    if not isinstance(license_plate, str):
        return False

    license_plate = license_plate.upper().strip()
    pattern = re.compile(r"^[A-Z]{3}\d[A-Z]\d{2}$")

    return re.match(pattern, license_plate) is not None


def remove_symbols(license_plate_number: str) -> str:
    """
    Removes the dash (-) symbol from a license plate string.

    Args:
        license_plate_number (str): A license plate number containing symbols to
                                    be removed.

    Returns:
        str: The license plate number with the specified symbols removed.

    Example:
        >>> remove_symbols("ABC-123")
        "ABC123"
        >>> remove_symbols("abc123")
        "abc123"
        >>> remove_symbols("ABCD123")
        "ABCD123"
    """

    return license_plate_number.replace("-", "")


def get_format(license_plate: str) -> Optional[str]:
    """
    Return the format of a license plate. 'LLLNNNN' for the old pattern and
    'LLLNLNN' for the Mercosul one.

    Args:
        license_plate (str): A license plate string without symbols.

    Returns:
        str: The format of the license plate (LLLNNNN, LLLNLNN) or
             'None' if the format is invalid.

    Example:
        >>> get_format("abc123")
        "LLLNNNN"
        >>> get_format("abc1d23")
        "LLLNLNN"
        >>> get_format("ABCD123")
        None
    """

    if is_valid_old_format(license_plate):
        return "LLLNNNN"

    if is_valid_mercosul(license_plate):
        return "LLLNLNN"

    return None


def generate(format="LLLNLNN"):  # type: (str) -> str | None
    """
    Generate a valid license plate in the given format. In case no format is
    provided, it will return a license plate in the Mercosul format.

    Args:
        format (str): The desired format for the license plate.
                      'LLLNNNN' for the old pattern or 'LLLNLNN' for the
                      Mercosul one. Default is 'LLLNLNN'

    Returns:
        str: A randomly generated license plate number or
             'None' if the format is invalid.

    Example:
        >>> generate()
        "ABC1D23"
        >>> generate(format="LLLNLNN")
        "ABC4D56"
        >>> generate(format="LLLNNNN")
        "ABC123"
        >>> generate(format="invalid")
        None
    """

    generated = ""

    format = format.upper()

    if format not in ("LLLNLNN", "LLLNNNN"):
        return None

    for char in format:
        if char == "L":
            generated += choice(ascii_uppercase)
        else:
            generated += str(randint(0, 9))

    return generated
