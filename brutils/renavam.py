def is_valid_renavam(renavam):  # type: (str) -> bool
    """
    Validates the Brazilian vehicle registration number (RENAVAM).

    This function takes a RENAVAM string and checks if it is valid.
    A valid RENAVAM consists of exactly 11 digits. Theast digit a check digit
    calculated from the the first 10 digits using a specific weighting system.

    Args:
        renavam (str): The RENAVAM string to be validated.

    Returns:
        bool: True if the RENAVAM is valid, False otherwise.

    Example:
        >>> is_valid_renavam('35298206229')
        True
        >>> is_valid_renavam('12345678900')
        False
        >>> is_valid_renavam('1234567890a')
        False
        >>> is_valid_renavam('12345678 901')
        False
        >>> is_valid_renavam('12345678')  # Less than 11 digits
        False
        >>> is_valid_renavam('')  # Empty string
        False
    """

    if len(renavam) != 11 or not renavam.isdigit():
        return False

    ## Calculating the check digit
    digits = [int(digit) for digit in renavam[:10]]  # 10 digits
    weights = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    checksum = sum(
        digit * weight for digit, weight in zip(digits, weights)
    )  # Sum of the products of the digits and weights

    remainder = checksum % 11
    check_digit = 0 if remainder == 0 else 11 - remainder

    # If the calculated check digit is 0, return False
    if check_digit == 0:
        return False

    # Checking if the calculated check digit is equal to the last digit of the RENAVAM
    return int(renavam[-1]) == check_digit
