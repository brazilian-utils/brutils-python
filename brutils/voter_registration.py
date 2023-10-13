import re
from typing import Optional

# FORMATTING
############


def format(voter_registration_number: str) -> Optional[str]:
    """
    Formats a voter registration number with spaces
    Returns None with invalid input
    Ex: 017746811074 - > 0177 4681 10 74
        117351120817 - > 1173 5112 08 17
        6455327  - > 'None'
    """

    if not isinstance(voter_registration_number, str) or not _is_valid(
        voter_registration_number
    ):
        return None

    first_four = voter_registration_number[0:4]
    second_four = voter_registration_number[4:8]
    federal_unit_numbers = voter_registration_number[8:10]
    check_digits = voter_registration_number[10:12]

    return f"{first_four} {second_four} {federal_unit_numbers} {check_digits}"


# OPERATIONS
############


def _is_valid(voter_registration_number: str) -> bool:
    """
    Checks if the number check digit calculation is correct
    Also checks if the Federal Unit identifier is valid (1 - 28)
    """
    if not re.match(r"^\d{12}$", voter_registration_number):
        return False

    fu_identifier = int(voter_registration_number[8:10])

    if not (1 <= fu_identifier <= 28):
        return False

    check_digits = voter_registration_number[10:12]
    calculated_check_digits = _calculate_check_digits(voter_registration_number)

    return check_digits == calculated_check_digits


def _calculate_check_digits(
    voter_registration_number: str,
):  # type: (str) -> str
    """
    Calculates voter registration number check digits
    """
    first_digit_sum = sum(
        int(digit) * (index + 2)
        for index, digit in enumerate(voter_registration_number[:8])
    )
    calculated_first_digit = first_digit_sum % 11

    if calculated_first_digit == 10:
        calculated_first_digit = 0

    second_digit_sum = sum(
        int(digit) * (index + 7)
        for index, digit in enumerate(voter_registration_number[8:11])
    )
    calculated_second_digit = second_digit_sum % 11

    if calculated_second_digit == 10:
        calculated_second_digit = 0

    return f"{calculated_first_digit}{calculated_second_digit}"
