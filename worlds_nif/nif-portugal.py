from random import randint

# FORMATTING
#############


def remove_symbols(dirty_nif):  # type: (str) -> str
    """
    Removes spaces, dots, and other symbols from a NIF.

    Args:
        dirty_nif (str): A string containing a NIF with possible non-numeric characters.

    Returns:
        str: A cleaned NIF containing only numeric digits.

    Example:
        remove_symbols("123.456.789") -> "123456789"
    """
    return "".join(filter(str.isdigit, dirty_nif))


def format_nif(nif):  # type: (str) -> str
    """
    Formats a Portuguese NIF for display with visual aid symbols.

    This function formats a numbers-only NIF string by adding periods and
    a dash for better readability, commonly used in Portuguese documents.

    Args:
        nif (str): A numbers-only NIF string of exactly 9 digits.

    Returns:
        str: A formatted NIF string with periods and a dash, or None
        if the input is invalid.

    Example:
        format_nif("123456789") -> "123.456.789-0"
    """
    # Clean the NIF first, in case it's with any symbols
    nif = remove_symbols(nif)

    # Ensure the NIF is valid for formatting
    if len(nif) != 9:
        return None

    # Add periods after the third and sixth digits, and a dash before the last digit
    return "{}.{}.{}-{}".format(nif[:3], nif[3:6], nif[6:8], nif[8])


# OPERATIONS
#############


def validate(nif):  # type: (str) -> bool
    """
    Validates a NIF by checking its structure, type, and control digit.

    Args:
        nif (str): A string containing a NIF to validate.

    Returns:
        bool: True if the NIF is valid, otherwise False.

    Example:
        validate("123456789") -> False (control digit mismatch)
    """
    # Clean the NIF first, in case it's with any symbols
    nif = remove_symbols(nif)

    # 1. Ensure the NIF has exactly 9 characters and is numeric
    if len(nif) != 9:
        print("The NIF must have exactly 9 digits.")
        return False

    if not nif.isdigit():
        print("The NIF must contain only numbers.")
        return False

    # 2. Determine the taxpayer type by the first digit
    first_digit = int(nif[0])

    # List of valid first digits for Portuguese NIFs
    valid_types = [1, 2, 4, 5, 6, 7, 9]

    if first_digit not in valid_types:
        print(
            f"The first digit {first_digit} is not valid for a Portuguese NIF."
        )
        return False

    base, check_digit = nif[:8], int(nif[8])
    return _calculate_digit(base) == check_digit


def generate():  # type: () -> str
    """
    Generates a random valid NIF.

    Returns:
        str: A valid randomly generated NIF.

    Example:
        generate() -> "123456780"
    """
    base = str(randint(10000000, 99999999))  # Generate the first 8 digits
    return base + str(_calculate_digit(base))


def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the control digit for a given NIF base.

    Args:
        base (str): The first 8 digits of a NIF.

    Returns:
        int: The control digit calculated using the Portuguese NIF rules.

    Example:
        _calculate_digit("12345678") -> 0
    """
    weights = range(9, 1, -1)  # Descending weights from 9 to 2
    total = sum(int(digit) * weight for digit, weight in zip(base, weights))
    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder


# USAGE EXAMPLE

nif = generate()
print(f"Generated NIF: {nif} - Valid? {validate(nif)}")

# Validate a NIF (input with symbols, such as dots and dashes)
user_nif = input("Enter your NIF: ")
print(validate(user_nif))

# Format a NIF (input with symbols, such as dots and dashes)
formatted_nif = format_nif(user_nif)
if formatted_nif:
    print(f"Formatted NIF: {formatted_nif}")
else:
    print("Invalid NIF.")
