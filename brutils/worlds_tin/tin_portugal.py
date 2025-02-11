from random import randint, choice


# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, and other symbols from a tin.

    Args:
        dirty_tin (str): A string containing a tin with possible non-numeric characters.

    Returns:
        str: A cleaned tin containing only numeric digits.

    Example:
        remove_symbols("123.456.789") -> "123456789"
    """
    return "".join(filter(str.isdigit, dirty_tin))


def format_tin(tin):  # type: (str) -> str
    """
    Formats a Portuguese tin for display with visual aid symbols.

    This function formats a numbers-only tin string by adding periods and 
    a dash for better readability, commonly used in Portuguese documents.

    Args:
        tin (str): A numbers-only tin string of exactly 9 digits.

    Returns:
        str: A formatted tin string with periods and a dash, or None 
        if the input is invalid.

    Example:
        format_tin("123456789") -> "123.456.789-0"
    """
    # Clean the tin first, in case it's with any symbols
    tin = remove_symbols(tin)

    # Ensure the tin is valid for formatting
    if len(tin) != 9:
        return None

    # Add periods after the third and sixth digits, and a dash before the last digit
    return "{}.{}.{}-{}".format(tin[:3], tin[3:6], tin[6:8], tin[8])


# OPERATIONS
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a tin by checking its structure, type, and control digit.

    Args:
        tin (str): A string containing a tin to validate.

    Returns:
        bool: True if the tin is valid, otherwise False.

    Example:
        validate("123456789") -> False (control digit mismatch)
    """
    # Clean the tin first, in case it's with any symbols
    tin = remove_symbols(tin)

    # 1. Ensure the tin has exactly 9 characters and is numeric
    if len(tin) != 9:
        print("The tin must have exactly 9 digits.")
        return False

    if not tin.isdigit():
        print("The tin must contain only numbers.")
        return False

    # 2. Determine the taxpayer type by the first digit
    first_digit = int(tin[0])
    
    # List of valid first digits for Portuguese tins
    valid_types = [1, 2, 4, 5, 6, 7, 9]
    
    if first_digit not in valid_types:
        print(f"The first digit {first_digit} is not valid for a Portuguese tin.")
        return False

    base, check_digit = tin[:8], int(tin[8])
    return _calculate_digit(base) == check_digit


def generate():  # type: () -> str
    """
    Generates a random valid tin.

    Returns:
        str: A valid randomly generated tin.

    Example:
        generate() -> "123456780"
    """
    base = str(randint(10000000, 99999999))  # Generate the first 8 digits
    return base + str(_calculate_digit(base))


def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the control digit for a given tin base.

    Args:
        base (str): The first 8 digits of a tin.

    Returns:
        int: The control digit calculated using the Portuguese tin rules.

    Example:
        _calculate_digit("12345678") -> 0
    """
    weights = range(9, 1, -1)  # Descending weights from 9 to 2
    total = sum(int(digit) * weight for digit, weight in zip(base, weights))
    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder


# USAGE EXAMPLE

tin = generate()
print(f"Generated tin: {tin} - Valid? {is_valid(tin)}")

# Validate a tin (input with symbols, such as dots and dashes)
user_tin = input("Enter your tin: ")
print(is_valid(user_tin))

# Format a tin (input with symbols, such as dots and dashes)
formatted_tin = format_tin(user_tin)
if formatted_tin:
    print(f"Formatted tin: {formatted_tin}")
else:
    print("Invalid tin.")