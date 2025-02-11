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
        remove_symbols("123-456-7890") -> "1234567890"
    """
    return "".join(filter(str.isdigit, dirty_tin))


def format_tin(tin):  # type: (str) -> str
    """
    Formats a Haitian tin for display with visual aid symbols.

    This function formats a numbers-only tin string by adding dashes 
    for better readability, commonly used in Haitian documents.

    Args:
        tin (str): A numbers-only tin string of exactly 10 digits.

    Returns:
        str: A formatted tin string with dashes, or None if the input is invalid.

    Example:
        format_tin("1234567890") -> "123-456-7890"
    """
    # Clean the tin first, in case it contains symbols
    tin = remove_symbols(tin)

    # Ensure the tin is valid for formatting
    if len(tin) != 10:
        return None

    # Add dashes after the third and sixth digits
    return "{}-{}-{}".format(tin[:3], tin[3:6], tin[6:])


# OPERATIONS
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Haitian tin by checking its structure.

    Args:
        tin (str): A string containing a tin to validate.

    Returns:
        bool: True if the tin is valid, otherwise False.

    Example:
        validate("1234567890") -> True
    """
    # Clean the tin first, in case it contains symbols
    tin = remove_symbols(tin)

    # Ensure the tin has exactly 10 digits
    if len(tin) != 10:
        print("The Haitian tin must have exactly 10 digits.")
        return False

    # Ensure the tin contains only numeric characters
    if not tin.isdigit():
        print("The Haitian tin must contain only numeric characters.")
        return False

    print("The Haitian tin is valid.")
    return True


def generate():  # type: () -> str
    """
    Generates a random valid Haitian tin.

    Returns:
        str: A valid randomly generated tin.

    Example:
        generate() -> "1234567890"
    """
    return str(randint(1000000000, 9999999999))  # Generate a 10-digit tin


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