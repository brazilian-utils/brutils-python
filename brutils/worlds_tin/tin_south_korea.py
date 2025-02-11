from random import randint, choice

# FORMAT AND VALIDATION FUNCTIONS
#################################

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, hyphens, and other symbols from a string.

    Args:
        dirty_tin (str): A string containing possible non-alphanumeric characters.

    Returns:
        str: A cleaned string containing only numeric characters.

    Example:
        remove_symbols("900101-1234568") -> "9001011234568"
    """
    return "".join(filter(str.isdigit, dirty_tin))


def is_valid(tin):  # type: (str) -> str
    """
    Validates a South Korean Resident Registration Number (tin).

    Args:
        tin (str): A string containing the tin to be validated.

    Returns:
        str: 'Valid tin' if valid, otherwise 'Invalid tin'.
    """
    tin = remove_symbols(tin)

    if len(tin) != 13:
        return "Invalid tin: tin must be exactly 13 digits."

    # Extract gender digit
    gender_digit = int(tin[6])

    # Check valid gender digit
    if gender_digit not in range(1, 9):
        return "Invalid tin: Gender digit must be 1–8."

    # Validate checksum
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    checksum = sum(int(tin[i]) * weights[i] for i in range(12)) % 11
    calculated_digit = (11 - checksum) % 10

    if calculated_digit != int(tin[12]):
        return "Invalid tin: Checksum does not match."

    return "Valid tin"


# GENERATE FUNCTIONS
####################

def generate(is_foreigner=False):  # type: (bool) -> str
    """
    Generates a random valid South Korean Resident Registration Number (tin).

    Args:
        is_foreigner (bool): If True, generates an tin for a foreigner. Defaults to False.

    Returns:
        str: A valid randomly generated tin.
    """
    # Generate birth date (YYMMDD)
    year = randint(1900, 2023)
    month = randint(1, 12)
    day = randint(1, 28)  # Simplified to avoid leap year complexity
    birth_date = f"{year % 100:02d}{month:02d}{day:02d}"

    # Determine gender digit
    if year < 2000:
        gender_digit = choice([1, 2]) if not is_foreigner else choice([5, 6])
    else:
        gender_digit = choice([3, 4]) if not is_foreigner else choice([7, 8])

    # Generate unique 5-digit identifier
    unique_identifier = f"{randint(0, 99999):05d}"

    # Combine for first 12 digits
    tin_without_checksum = f"{birth_date}{gender_digit}{unique_identifier}"

    # Calculate checksum
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    checksum = sum(int(tin_without_checksum[i]) * weights[i] for i in range(12)) % 11
    check_digit = (11 - checksum) % 10

    # Complete tin
    return f"{tin_without_checksum}{check_digit}"


# FORMAT FUNCTION
#################

def format_tin(tin):  # type: (str) -> str
    """
    Formats an tin for display with hyphens.

    Args:
        tin (str): A string containing the tin.

    Returns:
        str: A formatted tin with a hyphen or None if invalid.
    """
    tin = remove_symbols(tin)

    if len(tin) != 13 or not tin.isdigit():
        return None

    return f"{tin[:6]}-{tin[6:]}"


# USAGE EXAMPLES
################

def example_usage():
    # Generate examples
    generated_tin = generate()
    print(f"Generated tin (Resident): {format_tin(generated_tin)} - Valid? {is_valid(generated_tin)}")

    generated_tin_foreigner = generate(is_foreigner=True)
    print(f"Generated tin (Foreigner): {format_tin(generated_tin_foreigner)} - Valid? {is_valid(generated_tin_foreigner)}")

    # Validate user input
    user_input = input("Enter a Resident Registration Number (tin): ")
    formatted_tin = format_tin(user_input)
    if formatted_tin:
        print(f"Formatted tin: {formatted_tin}")
    print(is_valid(user_input))


# Run the example usage
example_usage()
