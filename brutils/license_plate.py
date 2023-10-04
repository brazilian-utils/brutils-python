import re


def is_valid_mercosul(license_plate):  # type: (str) -> bool
    """
    Returns whether or not the provided license_plate is valid according to the
    Mercosul pattern (LLLNLNN). Input should be a digit string of proper
    length. Ex: ABC4E67
    """
    if not isinstance(license_plate, str):
        return False

    license_plate = license_plate.upper().strip()
    pattern = re.compile(r"^[A-Z]{3}\d[A-Z]\d{2}$")
    return re.match(pattern, license_plate) is not None


def is_valid_old_format(license_plate):
    """
    Returns whether or not the provided license_plate is valid according to the
    old Brazilian pattern (LLLNNNN). Input should be a digit string of proper
    length. Ex: ABC5678
    """
    if not isinstance(license_plate, str):
        return False

    license_plate = license_plate.upper().strip()
    pattern = re.compile(r"^[A-Z]{3}\d{4}$")
    return re.match(pattern, license_plate) is not None
