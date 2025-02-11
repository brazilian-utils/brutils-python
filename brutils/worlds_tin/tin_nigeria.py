from random import randint, choice


# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a string.
    """
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATION FUNCTION
def is_valid_tin(tin):  # type: (str) -> str
    """
    Validates a Nigerian TIN (Tax Identification Number).

    Args:
        tin (str): TIN to validate.

    Returns:
        str: 'Valid TIN' if valid, otherwise 'Invalid TIN'.
    """
    tin = remove_symbols(tin)

    if len(tin) == 10 and tin.isdigit():
        return "Valid TIN"
    return "Invalid TIN: Must be exactly 10 numeric digits."

# GENERATE FUNCTION
def generate_tin():  # type: () -> str
    """
    Generates a valid random Nigerian TIN.

    Returns:
        str: A valid randomly generated TIN.
    """
    return f"{randint(1000000000, 9999999999)}"  # 10 digits

# FORMAT FUNCTION
def format_tin(tin):  # type: (str) -> str
    """
    Formats a Nigerian TIN with appropriate spacing for display.

    Args:
        tin (str): TIN to format.

    Returns:
        str: Formatted TIN or None if invalid.
    """
    tin = remove_symbols(tin)

    if is_valid_tin(tin) == "Valid TIN":
        return f"{tin[:3]} {tin[3:6]} {tin[6:]}"  # Split into groups
    return None

# USER INPUT VALIDATION
def is_valid_user_input(user_input):  # type: (str) -> str
    """
    Validates user input as a valid Nigerian TIN.

    Args:
        user_input (str): User input to validate.

    Returns:
        str: The validity of the TIN.
    """
    user_input = remove_symbols(user_input)

    if is_valid_tin(user_input) == "Valid TIN":
        return f"Valid TIN: {user_input}"
    return "Invalid TIN format."

# USAGE EXAMPLES
def example_usage():
    # Generate examples
    generated_tin = generate_tin()
    print(f"Generated TIN: {generated_tin} - Valid? {is_valid_tin(generated_tin)}")
    print(f"Formatted TIN: {format_tin(generated_tin)}")

    # User input
    user_input = input("Enter a Nigerian TIN (with or without symbols): ")
    print(is_valid_user_input(user_input))
    print(f"Formatted TIN: {format_tin(user_input)}")

# Run the example usage
example_usage()
