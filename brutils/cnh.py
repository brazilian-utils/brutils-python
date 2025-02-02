import re


def is_valid_cnh(cnh: str) -> bool:
    """
    Validates the Brazilian CNH (Carteira Nacional de Habilitação).

    This function checks if the given CNH is valid based on the format and allowed characters.
    It considers the CNH with or without the verification character.

    Args:
        cnh (str): The CNH number to be validated.

    Returns:
        bool: True if the CNH is valid, False otherwise.

    Example:
        >>> is_valid_cnh('12345678900')
        True
        >>> is_valid_cnh('123456789012345')
        True
        >>> is_valid_cnh('12345')
        False
        >>> is_valid_cnh('A1B2C3D4E5F6')
        True
    """
    if not isinstance(cnh, str):
        return False
    
    if not (11 <= len(cnh) <= 15):
        return False
    
    return bool(re.match(r"^[A-Z0-9]+$", cnh))
