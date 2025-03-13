from random import choice, randint


# REMOVE FORMATTING
def remove_symbols(dirty_tin):
    """Remove spaces, dots, and hyphens from the input string."""
    return "".join(filter(str.isalnum, dirty_tin))


# VALIDATE ANGUILLAN TIN
def is_valid_individual(tin):
    """Example:
    >>> is_valid_individual("AB12345678") => 'Valid Anguilla TIN'
    >>> is_valid_individual("XYZ1234567") => 'Invalid Anguilla TIN: Must start with two letters.'"""
    tin = remove_symbols(tin)

    if len(tin) != 10:
        return "Invalid Anguilla TIN: Must have 10 characters."

    if not tin[:2].isalpha():
        return "Invalid Anguilla TIN: Must start with two letters."

    if not tin[2:].isdigit():
        return "Invalid Anguilla TIN: The remaining characters must be numeric."

    return "Valid Anguilla TIN"


def is_valid_company(tin):
    """Example:
    >>> from tin_anguilla import is_valid_company
    >>> is_valid_company("ABC12345678") => 'Valid Anguilla TIN'
    >>> is_valid_company("XY1234567") => 'Invalid Anguilla TIN: Must start with three letters.'"""
    tin = remove_symbols(tin)

    if not (10 <= len(tin) <= 12):
        return "Invalid Anguilla TIN: Must have between 10 and 12 characters."

    if not tin[:3].isalpha():
        return "Invalid Anguilla TIN: Must start with three letters."

    if not tin[3:].isdigit():
        return "Invalid Anguilla TIN: The remaining characters must be numeric."

    return "Valid Anguilla TIN"


def is_valid(tin):
    """Determines whether the TIN is valid for either individuals or companies."""
    if len(remove_symbols(tin)) == 10:
        return is_valid_individual(tin)
    return is_valid_company(tin)


# FORMAT ANGUILLAN TIN
def format_tin(tin):
    """Formats an Anguilla TIN for display."""
    tin = remove_symbols(tin)

    if len(tin) < 10:
        return None

    return f"{tin[:2]}-{tin[2:]}" if len(tin) == 10 else f"{tin[:3]}-{tin[3:]}"


# GENERATE ANGUILLAN TIN
def generate(is_company=False):
    """Generates a valid Anguilla TIN (TIN)."""
    prefix = "".join(
        choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for _ in range(2 if not is_company else 3)
    )
    num_digits = (
        8 if not is_company else 7
    )  # Individuals: 8 digits, Companies: 7 digits
    numeric_part = "".join(str(randint(0, 9)) for _ in range(num_digits))
    return prefix + numeric_part


# EXAMPLES
def example_usage():
    # Generate valid Anguilla TIN for individuals and companies
    tin_individual = generate()
    tin_company = generate(is_company=True)

    print(
        f"Generated Individual TIN: {tin_individual} - Valid? {is_valid(tin_individual)}"
    )
    print(
        f"Generated Company TIN: {tin_company} - Valid? {is_valid(tin_company)}"
    )

    # User input validation
    user_input = input("Enter your Anguilla TIN: ")
    print(is_valid(user_input))

    formatted_input = format_tin(user_input)
    if formatted_input:
        print(f"Formatted Anguilla TIN: {formatted_input}")


# Run example
example_usage()
