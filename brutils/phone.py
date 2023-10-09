import re


# FORMATTING
############
def format_phone(phone): # type: (str) -> str
    """
    Function responsible for formatting a telephone number

    Args:
        phone_number (str): The phone number to format.

    Returns:
        str: The formatted phone number, or None if the number is not valid.


    >>> format_phone("11994029275")
    '(11)99402-9275'
    >>> format_phone("1635014415")
    '(16)3501-4415'
    >>> format_phone("333333")
    >>>
    """
    if not is_valid(phone):
        return None

    ddd = phone[:2]
    phone_number = phone[2:]

    return f"({ddd}){phone_number[:-4]}-{phone_number[-4:]}"


# OPERATIONS
############


def is_valid_landline(phone_number):  # type: (str) -> bool
    """
    Returns whether or not the verifying first 3 digits are a
    match.This function validates only Brazilian landline numbers
    and does not verify if the number actually exists.
    Input should be a digit string of proper length.

    """
    pattern = re.compile(r"^[1-9][1-9][2-5]\d{7}$")
    return (
        isinstance(phone_number, str)
        and re.match(pattern, phone_number) is not None
    )


def is_valid_mobile(phone_number):  # type: (str) -> bool
    """
    Returns whether or not the verifying first 3 digits are a
    match.This function validates only Brazilian mobile numbers
    and does not verify if the number actually exists.
    Input should be a digit string of proper length.

    """
    pattern = re.compile(r"^[1-9][1-9][9]\d{8}$")
    return (
        isinstance(phone_number, str)
        and re.match(pattern, phone_number) is not None
    )


def is_valid(phone_number):  # type: (str) -> bool
    """
    Returns whether or not the verifying first 3 digits are a
    match.This function validates only Brazilian phone numbers
    and does not verify if the number actually exists.
    Input should be a digit string of proper length.

    """
    return is_valid_landline(phone_number) or is_valid_mobile(phone_number)


def remove_symbols_phone(phone_number):  # type: (str) -> str
    """
    Removes common symbols from a Brazilian phone number string.

    """
    cleaned_phone = (
        phone_number.replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace("+", "")
        .replace(" ", "")
    )
    return cleaned_phone
