from random import randint, choice


# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a string.
    """
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATION FUNCTIONS
def is_valid_tin_individual(tin):  # type: (str) -> str
    """
    Validates an Australian Individual TIN.

    An individual TIN must be exactly 11 digits.

    Args:
        tin (str): TIN to validate.

    Returns:
        str: 'Valid Individual TIN' if valid, otherwise 'Invalid Individual TIN'.
    """
    tin = remove_symbols(tin)

    if len(tin) == 11 and tin.isdigit():
        return "Valid Individual TIN"
    return "Invalid Individual TIN: Must be exactly 11 numeric digits."

def is_valid_tin_business(tin):  # type: (str) -> str
    """
    Validates an Australian Business TIN.

    A business TIN must be exactly 10 digits.

    Args:
        tin (str): TIN to validate.

    Returns:
        str: 'Valid Business TIN' if valid, otherwise 'Invalid Business TIN'.
    """
    tin = remove_symbols(tin)

    if len(tin) == 10 and tin.isdigit():
        return "Valid Business TIN"
    return "Invalid Business TIN: Must be exactly 10 numeric digits."

# GENERATE FUNCTIONS
def generate_tin_individual():  # type: () -> str
    """
    Generates a valid Australian Individual TIN.

    Returns:
        str: A valid Individual TIN.
    """
    return f"{randint(10**10, 10**11 - 1)}"

def generate_tin_business():  # type: () -> str
    """
    Generates a valid Australian Business TIN.

    Returns:
        str: A valid Business TIN.
    """
    return f"{randint(10**9, 10**10 - 1)}"

# FORMAT FUNCTIONS
def format_tin(tin):  # type: (str) -> str
    """
    Formats a TIN with spaces for display.

    Args:
        tin (str): TIN to format.

    Returns:
        str: Formatted TIN or None if invalid.
    """
    tin = remove_symbols(tin)

    # Format for Individual TIN (11 digits)
    if is_valid_tin_individual(tin) == "Valid Individual TIN":
        return f"{tin[:3]} {tin[3:6]} {tin[6:9]} {tin[9:]}"

    # Format for Business TIN (10 digits)
    if is_valid_tin_business(tin) == "Valid Business TIN":
        return f"{tin[:3]} {tin[3:6]} {tin[6:]}"

    return None

# USER INPUT VALIDATION
def is_valid_user_input(user_input):  # type: (str) -> str
    """
    Validates a user input as either an Individual or Business TIN.

    Args:
        user_input (str): User input to validate.

    Returns:
        str: The type and validity of the TIN.
    """
    user_input = remove_symbols(user_input)

    if is_valid_tin_individual(user_input) == "Valid Individual TIN":
        return f"Valid Individual TIN: {user_input}"

    if is_valid_tin_business(user_input) == "Valid Business TIN":
        return f"Valid Business TIN: {user_input}"

    return "Invalid TIN format."

# USAGE EXAMPLES
def example_usage():
    # Generate examples
    generated_individual_tin = generate_tin_individual()
    print(f"Generated Individual TIN: {generated_individual_tin} - Valid? {is_valid_tin_individual(generated_individual_tin)}")
    print(f"Formatted Individual TIN: {format_tin(generated_individual_tin)}")

    generated_business_tin = generate_tin_business()
    print(f"Generated Business TIN: {generated_business_tin} - Valid? {is_valid_tin_business(generated_business_tin)}")
    print(f"Formatted Business TIN: {format_tin(generated_business_tin)}")

    # User input
    user_input = input("Enter an Individual or Business TIN (with or without symbols): ")
    print(is_valid_user_input(user_input))
    print(f"Formatted TIN: {format_tin(user_input)}")

# Run example
example_usage()
