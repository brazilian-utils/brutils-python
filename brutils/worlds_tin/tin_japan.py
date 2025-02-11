from random import randint, choice


# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a tin.

    Args:
        dirty_tin (str): A string containing a tin with possible non-numeric characters.

    Returns:
        str: A cleaned tin containing only numeric digits.

    Example:
        remove_symbols("123-4567-8901") -> "12345678901"
    """
    return "".join(filter(str.isdigit, dirty_tin))


def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Japanese tin by checking its structure.

    Args:
        tin (str): A string containing a tin to validate.

    Returns:
        bool: True if the tin is valid (12 digits for My Number or 13 digits for Corporate Number), otherwise False.

    Example:
        is_valid("123456789012") -> True
    """
    # Clean the tin first, in case it contains symbols
    tin = remove_symbols(tin)

    # Check if the tin is a valid My Number or Corporate Number
    if len(tin) == 12 and tin.isdigit():
        print("The tin is a valid My Number (12 digits for individuals).")
        return True
    elif len(tin) == 13 and tin.isdigit():
        print("The tin is a valid Corporate Number (13 digits for businesses).")
        return True
    else:
        print("The Japanese tin must have 12 digits for My Number (individuals) or 13 digits for Corporate Number (businesses).")
        return False


def format_tin(tin):  # type: (str) -> str
    """
    Formats a Japanese tin (My Number or Corporate Number) for display.

    This function adds dashes for better readability, commonly used in 
    Japanese documents.

    Args:
        tin (str): A numbers-only tin string of exactly 12 or 13 digits.

    Returns:
        str: A formatted tin string with dashes, or None if the input is invalid.

    Example:
        format_tin("123456789012") -> "1234-5678-9012"
        format_tin("1234567890123") -> "123-4567-8901-23"
    """
    # Clean the tin first, in case it contains symbols
    tin = remove_symbols(tin)

    if len(tin) == 12:  # My Number (individual)
        return "{}-{}-{}".format(tin[:4], tin[4:8], tin[8:])
    elif len(tin) == 13:  # Corporate Number
        return "{}-{}-{}-{}".format(tin[:3], tin[3:7], tin[7:11], tin[11:])
    else:
        return None


def generate():  # type: () -> str
    """
    Generates a random valid Japanese tin.

    Returns:
        str: A valid randomly generated tin.

    Example:
        generate() -> "123456789012"
    """
    # Randomly decide between a 12-digit My Number or a 13-digit Corporate Number
    if randint(0, 1) == 0:
        return str(randint(100000000000, 999999999999))  # My Number (12 digits)
    else:
        return str(randint(1000000000000, 9999999999999))  # Corporate Number (13 digits)


# USAGE EXAMPLE

tin = generate()
print(f"Generated tin: {tin} - Valid? {is_valid(tin)}")

# Validate a tin (input with symbols, such as dots and dashes)
user_tin = input("Enter your tin: ")
print(is_valid(user_tin))

# Format a tin (input with symbols, such as dots, dashes, and spaces)
formatted_tin = format_tin(user_tin)
if formatted_tin:
    print(f"Formatted tin: {formatted_tin}")
else:
    print("Invalid tin.")
