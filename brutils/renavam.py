RENAVAM_DV_WEIGHTS = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3]


def _validate_renavam_format(renavam: str):
    if not isinstance(renavam, str):
        raise ValueError("Invalid RENAVAM: must be a string.")
    if len(renavam) != 11 or not renavam.isdigit():
        raise ValueError(
            "Invalid RENAVAM: must contain exactly 11 numeric digits."
        )


def _sum_weighted_digits(renavam: str) -> int:
    base_digits = [int(d) for d in renavam[:-1][::-1]]
    return sum(x * y for x, y in zip(base_digits, RENAVAM_DV_WEIGHTS))


def _calculate_renavam_dv(renavam: str):
    weighted_sum = _sum_weighted_digits(renavam)
    dv = 11 - (weighted_sum % 11)
    return 0 if dv >= 10 else dv


def is_valid_renavam(renavam: str) -> bool:
    """
    Validates the Brazilian vehicle registration number (RENAVAM).

    This function takes a RENAVAM string and checks if it is valid.
    A valid RENAVAM consists of exactly 11 digits, with the last digit as
    a verification digit calculated from the previous 10 digits.

    Args:
        renavam (str): The RENAVAM string to be validated.

    Returns:
        bool: True if the RENAVAM is valid, False otherwise.

    Raises:
        ValueError: If the input is not a string, contains non-numeric
                    characters, or does not have exactly 11 digits.
    """
    _validate_renavam_format(renavam)

    return _calculate_renavam_dv(renavam) == int(renavam[-1])
