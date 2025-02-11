from random import randint, choice


# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, hyphens, and other symbols from a tin.

    Args:
        dirty_tin (str): A string containing a tin with possible non-numeric characters.

    Returns:
        str: A cleaned tin containing only numeric digits.

    Example:
        remove_symbols("12.345.678-9") -> "123456789"
    """
    return "".join(filter(str.isdigit, dirty_tin))


def is_valid_rut(tin):  # type: (str) -> bool
    """
    Validates a RUT (Registro Único Tributario) based on its structure.

    Args:
        tin (str): A string containing the RUT to be validated.

    Returns:
        bool: True if the RUT is valid, False otherwise.

    Example:
        is_valid_rut("123456789012") -> True
    """
    tin = remove_symbols(tin)
    if len(tin) != 12 or not tin.isdigit():
        print("The RUT must have exactly 12 numeric digits.")
        return False

    print("The RUT is valid.")
    return True


def is_valid_foreign_id(tin):  # type: (str) -> bool
    """
    Validates a Foreign Identification Number based on its structure.

    Args:
        tin (str): A string containing the foreign ID to be validated.

    Returns:
        bool: True if the foreign ID is valid, False otherwise.

    Example:
        is_valid_foreign_id("912345678") -> True
    """
    tin = remove_symbols(tin)
    if len(tin) != 9 or not tin.isdigit() or tin[0] != "9":
        print("The Foreign ID must have 9 digits, starting with '9'.")
        return False

    print("The Foreign ID is valid.")
    return True


def is_valid_identity_card(tin):  # type: (str) -> bool
    """
    Validates an Identity Card Number based on its structure.

    Args:
        tin (str): A string containing the Identity Card Number to be validated.

    Returns:
        bool: True if the Identity Card Number is valid, False otherwise.

    Example:
        is_valid_identity_card("12345678") -> True
    """
    tin = remove_symbols(tin)
    if len(tin) != 8 or not tin.isdigit():
        print("The Identity Card Number must have 8 numeric digits.")
        return False

    print("The Identity Card Number is valid.")
    return True


def is_valid_tin(tin):  # type: (str) -> None
    """
    Validates any Uruguayan tin based on its type.

    Args:
        tin (str): A string containing the tin to be validated.

    Returns:
        None: Prints the validation result.

    Example:
        is_valid_tin("12.345678-9012") -> "The RUT is valid."
        is_valid_tin("9.123456-7") -> "The Foreign ID is valid."
        is_valid_tin("1.234567-8") -> "The Identity Card Number is valid."
    """
    tin = remove_symbols(tin)

    if len(tin) == 12:
        is_valid_rut(tin)
    elif len(tin) == 9 and tin[0] == "9":
        is_valid_foreign_id(tin)
    elif len(tin) == 8:
        is_valid_identity_card(tin)
    else:
        print("The tin is not valid for any Uruguayan format.")


def format_tin(tin):  # type: (str) -> str
    """
    Formats a tin for display based on its length.

    Args:
        tin (str): A cleaned tin.

    Returns:
        str: A formatted tin for display or None if invalid.

    Example:
        format_tin("123456789012") -> "12.345678-9012" (RUT)
        format_tin("91234567") -> "9.123456-7" (Foreign ID)
        format_tin("12345678") -> "1.234567-8" (Identity Card Number)
    """
    tin = remove_symbols(tin)

    if len(tin) == 12:  # RUT
        return "{}.{}-{}".format(tin[:2], tin[2:8], tin[8:])
    elif len(tin) == 9 and tin[0] == "9":  # Foreign ID
        return "{}.{}-{}".format(tin[:1], tin[1:8], tin[8:])
    elif len(tin) == 8:  # Identity Card Number
        return "{}.{}-{}".format(tin[:1], tin[1:7], tin[7:])
    return None



def generate_rut():  # type: () -> str
    """Generates a mock RUT (12 digits)."""
    return "123456789012"


def generate_foreign_id():  # type: () -> str
    """Generates a mock Foreign ID (9 digits starting with 9)."""
    return "912345678"


def generate_identity_card():  # type: () -> str
    """Generates a mock Identity Card Number (8 digits)."""
    return "12345678"


# USAGE EXAMPLES
#################

# Generate and validate tins
print("Generated RUT:", format_tin(generate_rut()))
is_valid_tin(generate_rut())

print("\nGenerated Foreign ID:", format_tin(generate_foreign_id()))
is_valid_tin(generate_foreign_id())

print("\nGenerated Identity Card:", format_tin(generate_identity_card()))
is_valid_tin(generate_identity_card())

# Input a tin and validate/format it
user_tin = input("\nEnter a tin: ")
formatted_tin = format_tin(user_tin)
if formatted_tin:
    print(f"Formatted tin: {formatted_tin}")
is_valid_tin(user_tin)
