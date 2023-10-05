import re


def is_valid_license_plate_old_format(plate: str) -> bool:
    """
    Checks whether a string matches the old format of Brazilian license plate.
    """
    pattern = re.compile(r"^[aA-zZ]{3}[0-9]{4}$")
    return (
        isinstance(plate, str) and re.match(pattern, plate.strip()) is not None
    )
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
