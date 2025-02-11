from random import randint, choice


# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a string.
    """
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATION FUNCTIONS
def is_valid(tin):  # type: (str) -> str
    """
    Validates a Senegalese tin.

    A valid tin must:
    - Be 9 digits long.
    - Start with '1' (individual) or '2' (corporate entity).

    Args:
        tin (str): tin to validate.

    Returns:
        str: 'Valid tin' if valid, otherwise 'Invalid tin'.
    """
    tin = remove_symbols(tin)

    if len(tin) == 9 and tin[0] in {"1", "2"} and tin.isdigit():
        return "Valid tin"
    return "Invalid tin: Must be 9 digits and start with '1' or '2'."

# GENERATE FUNCTIONS
def generate(taxpayer_type="individual"):  # type: (str) -> str
    """
    Generates a valid Senegalese tin.

    Args:
        taxpayer_type (str): 'individual' or 'corporate'.

    Returns:
        str: A valid tin.
    """
    if taxpayer_type.lower() == "individual":
        prefix = "1"
    elif taxpayer_type.lower() == "corporate":
        prefix = "2"
    else:
        raise ValueError("Invalid taxpayer type. Must be 'individual' or 'corporate'.")

    return f"{prefix}{randint(10000000, 99999999):08}"

# FORMAT FUNCTIONS
def format_tin(tin):  # type: (str) -> str
    """
    Formats a tin with spaces for display.

    Args:
        tin (str): tin to format.

    Returns:
        str: Formatted tin or None if invalid.
    """
    tin = remove_symbols(tin)

    if is_valid(tin) == "Valid tin":
        return f"{tin[:3]} {tin[3:6]} {tin[6:]}"
    return None

# USER INPUT VALIDATION
def is_valid_user_input(user_input):  # type: (str) -> str
    """
    Validates a user input as a Senegalese tin.

    Args:
        user_input (str): User input to validate.

    Returns:
        str: The validity of the tin.
    """
    user_input = remove_symbols(user_input)

    if is_valid(user_input) == "Valid tin":
        return f"Valid tin: {user_input}"
    return "Invalid tin format."

# USAGE EXAMPLES
def example_usage():
    # Generate examples
    generated_individual_tin = generate("individual")
    print(f"Generated Individual tin: {generated_individual_tin} - Valid? {is_valid(generated_individual_tin)}")
    print(f"Formatted Individual tin: {format_tin(generated_individual_tin)}")

    generated_corporate_tin = generate("corporate")
    print(f"Generated Corporate tin: {generated_corporate_tin} - Valid? {is_valid(generated_corporate_tin)}")
    print(f"Formatted Corporate tin: {format_tin(generated_corporate_tin)}")

    # User input
    user_input = input("Enter a tin (with or without symbols): ")
    print(is_valid_user_input(user_input))
    print(f"Formatted tin: {format_tin(user_input)}")

# Run example
example_usage()
