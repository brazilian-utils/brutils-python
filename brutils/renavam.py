def is_valid_renavam(renavam):  # type: (str) -> bool
    """
    Validates the Brazilian vehicle registration number (RENAVAM).

    This function takes a RENAVAM string and checks if it is valid.
    A valid RENAVAM consists of exactly 11 digits, with the last digit as
    a verification digit calculated from the previous 10 digits.

    Args:
        renavam (str): The RENAVAM string to be validated.

    Returns:
        bool: True if the RENAVAM is valid, False otherwise.

    Example:
        >>> is_valid_renavam('12345678900')
        True
        >>> is_valid_renavam('12345678901')
        False
        >>> is_valid_renavam('1234567890a')
        False
        >>> is_valid_renavam('12345678 901')
        False
        >>> is_valid_renavam('12345678')  # Less than 11 digits
        False
        >>> is_valid_renavam('')  # Empty string
        False
        >>> is_valid_renavam(None)  # None
        False
    """
    if renavam and len(renavam) == 11 and renavam.isnumeric():
        check_digit = int(renavam[-1:])
        renavam_digitis = [int(d) for d in renavam]
        renavam_digitis = renavam_digitis[:-1]
        multipliers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3]
        sum_digits = sum(
            digit * multipliers[i]
            for i, digit in enumerate(renavam_digitis[::-1])
        )
        remainder_division = sum_digits % 11
        if remainder_division <= 1:
            check_digit_calculated = 0
        else:
            check_digit_calculated = 11 - remainder_division
        if check_digit == check_digit_calculated:
            return True
        return False
