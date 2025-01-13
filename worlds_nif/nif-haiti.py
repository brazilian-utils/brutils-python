from random import randint

# FORMATTING
#############


def remove_symbols(dirty_nif):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a NIF.

    Args:
        dirty_nif (str): A string containing a NIF with possible non-numeric characters.

    Returns:
        str: A cleaned NIF containing only numeric digits.

    Example:
        remove_symbols("123-456-7890") -> "1234567890"
    """
    return "".join(filter(str.isdigit, dirty_nif))


def format_nif(nif):  # type: (str) -> str
    """
    Formats a Haitian NIF for display with visual aid symbols.

    This function formats a numbers-only NIF string by adding dashes
    for better readability, commonly used in Haitian documents.

    Args:
        nif (str): A numbers-only NIF string of exactly 10 digits.

    Returns:
        str: A formatted NIF string with dashes, or None if the input is invalid.

    Example:
        format_nif("1234567890") -> "123-456-7890"
    """
    # Clean the NIF first, in case it contains symbols
    nif = remove_symbols(nif)

    # Ensure the NIF is valid for formatting
    if len(nif) != 10:
        return None

    # Add dashes after the third and sixth digits
    return "{}-{}-{}".format(nif[:3], nif[3:6], nif[6:])


# OPERATIONS
#############


def validate(nif):  # type: (str) -> bool
    """
    Validates a Haitian NIF by checking its structure.

    Args:
        nif (str): A string containing a NIF to validate.

    Returns:
        bool: True if the NIF is valid, otherwise False.

    Example:
        validate("1234567890") -> True
    """
    # Clean the NIF first, in case it contains symbols
    nif = remove_symbols(nif)

    # Ensure the NIF has exactly 10 digits
    if len(nif) != 10:
        print("The Haitian NIF must have exactly 10 digits.")
        return False

    # Ensure the NIF contains only numeric characters
    if not nif.isdigit():
        print("The Haitian NIF must contain only numeric characters.")
        return False

    print("The Haitian NIF is valid.")
    return True


def generate():  # type: () -> str
    """
    Generates a random valid Haitian NIF.

    Returns:
        str: A valid randomly generated NIF.

    Example:
        generate() -> "1234567890"
    """
    return str(randint(1000000000, 9999999999))  # Generate a 10-digit NIF


# USAGE EXAMPLE

nif = generate()
print(f"Generated NIF: {nif} - Valid? {validate(nif)}")

# Validate a NIF (input with symbols, such as dots and dashes)
user_nif = input("Enter your NIF: ")
print(validate(user_nif))

# Format a NIF (input with symbols, such as dots, dashes, and spaces)
formatted_nif = format_nif(user_nif)
if formatted_nif:
    print(f"Formatted NIF: {formatted_nif}")
else:
    print("Invalid NIF.")
