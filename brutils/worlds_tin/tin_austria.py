from random import randint, choice


# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a string.
    """
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATION FUNCTION
def is_valid(tin):  # type: (str) -> str
    """
    Validates an Austrian tin (Tax Identification Number).

    Args:
        tin (str): tin to validate.

    Returns:
        str: 'Valid tin' if valid, otherwise 'Invalid tin'.
    """
    tin = remove_symbols(tin)

    if len(tin) == 9 or len(tin) == 13:
        if tin.isdigit():
            return "Valid tin"
    return "Invalid tin: Must be 9 or 13 numeric digits."

# GENERATE FUNCTION
def generate(tin_type="individual"):  # type: (str) -> str
    """
    Generates a valid random Austrian tin.

    Args:
        tin_type (str): Type of tin to generate ('individual' or 'business').

    Returns:
        str: A valid randomly generated tin.
    """
    if tin_type == "individual":
        return f"{randint(100000000, 999999999)}"  # 9 digits
    elif tin_type == "business":
        return f"{randint(1000000000000, 9999999999999)}"  # 13 digits
    else:
        raise ValueError("Invalid tin type. Use 'individual' or 'business'.")

# FORMAT FUNCTION
def format_tin(tin):  # type: (str) -> str
    """
    Formats an Austrian tin with appropriate spacing for display.

    Args:
        tin (str): tin to format.

    Returns:
        str: Formatted tin or None if invalid.
    """
    tin = remove_symbols(tin)

    if is_valid(tin) == "Valid tin":
        if len(tin) == 9:
            return f"{tin[:3]} {tin[3:6]} {tin[6:]}"  # Split into groups of 3 digits
        elif len(tin) == 13:
            return f"{tin[:4]} {tin[4:8]} {tin[8:]}"  # Split into groups for 13-digit numbers
    return None

# USER INPUT VALIDATION
def is_valid_user_input(user_input):  # type: (str) -> str
    """
    Validates user input as a valid Austrian tin.

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

    generated_business_tin = generate("business")
    print(f"Generated Business tin: {generated_business_tin} - Valid? {is_valid(generated_business_tin)}")
    print(f"Formatted Business tin: {format_tin(generated_business_tin)}")

    # User input
    user_input = input("Enter an Austrian tin (with or without symbols): ")
    print(is_valid_user_input(user_input))
    print(f"Formatted tin: {format_tin(user_input)}")

# Run the example usage
example_usage()
