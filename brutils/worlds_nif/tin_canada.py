from random import randint, choice

# FORMAT AND VALIDATION FUNCTIONS
#################################

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, hyphens, and other symbols from a string.

    Args:
        dirty_tin (str): A string containing possible non-alphanumeric characters.

    Returns:
        str: A cleaned string containing only alphanumeric characters.

    Example:
        remove_symbols("123-456-789") -> "123456789"
    """
    return "".join(filter(str.isalnum, dirty_tin))


def is_valid_sin(sin):  # type: (str) -> str
    """
    Validates a Canadian Social Insurance Number (SIN).

    Args:
        sin (str): A string containing the SIN to be validated.

    Returns:
        str: 'Valid SIN' if valid, otherwise 'Invalid SIN'.
    """
    sin = remove_symbols(sin)

    if len(sin) == 9 and sin.isdigit():
        return "Valid SIN"
    return "Invalid SIN: SIN must be exactly 9 numeric digits."


def is_valid_bn(bn):  # type: (str) -> str
    """
    Validates a Canadian Business Number (BN).

    Args:
        bn (str): A string containing the BN to be validated.

    Returns:
        str: 'Valid BN' if valid, otherwise 'Invalid BN'.
    """
    bn = remove_symbols(bn)

    if len(bn) == 9 and bn.isdigit():
        return "Valid BN"
    return "Invalid BN: BN must be exactly 9 numeric digits."


def is_valid_trust_account_number(tan):  # type: (str) -> str
    """
    Validates a Canadian Trust Account Number (TAN).

    Args:
        tan (str): A string containing the TAN to be validated.

    Returns:
        str: 'Valid Trust Account Number' if valid, otherwise 'Invalid Trust Account Number'.
    """
    tan = remove_symbols(tan)

    if len(tan) == 9 and tan[0].upper() == "T" and tan[1:].isdigit():
        return "Valid Trust Account Number"
    return "Invalid Trust Account Number: Format must be 'T' followed by 8 digits."


def format_tin(tin):  # type: (str) -> str
    """
    Format a Canadian tin (SIN, BN, TAN) for display with visual aid symbols.

    Args:
        tin (str): A cleaned tin string (numbers-only or numbers and 'T').

    Returns:
        str: A formatted tin string with visual aid symbols, or None if invalid.

    Example:
        format_tin("123456789") -> "123-456-789"  # SIN
        format_tin("T12345678") -> "T-123-456-78"  # TAN
        format_tin("123456789") -> "123-45-6789"  # BN
    """
    tin = remove_symbols(tin)

    # Detect and format SIN
    if is_valid_sin(tin) == "Valid SIN":
        return f"{tin[:3]}-{tin[3:6]}-{tin[6:]}"  # Format: XXX-XXX-XXX

    # Detect and format BN
    if is_valid_bn(tin) == "Valid BN":
        return f"{tin[:3]}-{tin[3:5]}-{tin[5:]}"  # Format: XXX-XX-XXXX

    # Detect and format TAN
    if is_valid_trust_account_number(tin) == "Valid Trust Account Number":
        return f"{tin[0]}-{tin[1:4]}-{tin[4:7]}-{tin[7:]}"  # Format: T-XXX-XXX-XX

    # Invalid tin
    return None


# GENERATE FUNCTIONS
####################

def generate_sin():  # type: () -> str
    """
    Generates a random valid Social Insurance Number (SIN).

    Returns:
        str: A valid randomly generated SIN.
    """
    return f"{randint(100000000, 999999999)}"


def generate_bn():  # type: () -> str
    """
    Generates a random valid Business Number (BN).

    Returns:
        str: A valid randomly generated BN.
    """
    return f"{randint(100000000, 999999999)}"


def generate_trust_account_number():  # type: () -> str
    """
    Generates a random valid Trust Account Number (TAN).

    Returns:
        str: A valid randomly generated Trust Account Number.
    """
    return f"T{randint(10000000, 99999999)}"


# USER INPUT AND VALIDATION
###########################

def is_valid_user_input(user_input):  # type: (str) -> str
    """
    Validates a user input against SIN, BN, and Trust Account Number formats.

    Args:
        user_input (str): A string input to be validated.

    Returns:
        str: The type and validity of the input.
    """
    user_input = remove_symbols(user_input)

    # Check for SIN
    if is_valid_sin(user_input) == "Valid SIN":
        return f"Valid SIN: {user_input}"

    # Check for BN
    if is_valid_bn(user_input) == "Valid BN":
        return f"Valid BN: {user_input}"

    # Check for Trust Account Number
    if is_valid_trust_account_number(user_input) == "Valid Trust Account Number":
        return f"Valid Trust Account Number: {user_input}"

    return "Invalid input format."


# USAGE EXAMPLES
################

def example_usage():
    # Generate examples
    generated_sin = generate_sin()
    print(f"Generated SIN: {format_tin(generated_sin)} - Valid? {is_valid_sin(generated_sin)}")

    generated_bn = generate_bn()
    print(f"Generated BN: {format_tin(generated_bn)} - Valid? {is_valid_bn(generated_bn)}")

    generated_tan = generate_trust_account_number()
    print(f"Generated Trust Account Number: {format_tin(generated_tan)} - Valid? {is_valid_trust_account_number(generated_tan)}")

    # Validate user input
    user_input = input("Enter a number (SIN, BN, or Trust Account Number): ")
    validation_result = is_valid_user_input(user_input)
    formatted_input = format_tin(user_input)

    if formatted_input:
        print(f"Validation Result: {validation_result}. Formatted Input: {formatted_input}")
    else:
        print(f"Validation Result: {validation_result}. Unable to format input.")


# Run the example usage
example_usage()
