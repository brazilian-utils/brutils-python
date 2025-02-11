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
    Validates a Polish tin (National Identification Number).

    Args:
        tin (str): tin to validate.

    Returns:
        str: 'Valid tin' if valid, otherwise 'Invalid tin'.
    """
    tin = remove_symbols(tin)

    if len(tin) != 11 or not tin.isdigit():
        return "Invalid tin: Must be exactly 11 numeric digits."

    # Weight factors for tin checksum calculation
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    # Calculate checksum
    total = sum(int(tin[i]) * weights[i] for i in range(10))
    check_digit = (10 - (total % 10)) % 10

    if check_digit == int(tin[-1]):
        return "Valid tin"
    return "Invalid tin: Checksum failed."

# GENERATE FUNCTION
def generate():  # type: () -> str
    """
    Generates a valid random Polish tin (National Identification Number).

    Returns:
        str: A valid randomly generated tin.
    """
    # Generate a random date (YYMMDD)
    year = randint(1900, 2099)
    month = randint(1, 12)
    day = randint(1, 28)  # Simplified day range for all months

    # Adjust month for tin year encoding
    if 2000 <= year <= 2099:
        month += 20
    elif 1800 <= year <= 1899:
        month += 80

    # Random sequence number
    seq = randint(1000, 9999)

    # Base tin without checksum
    tin_base = f"{str(year)[-2:]:0>2}{month:0>2}{day:0>2}{seq:0>4}"

    # Calculate checksum
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    total = sum(int(tin_base[i]) * weights[i] for i in range(10))
    check_digit = (10 - (total % 10)) % 10

    return tin_base + str(check_digit)

# FORMAT FUNCTION
def format_tin(tin):  # type: (str) -> str
    """
    Formats a Polish tin with appropriate spacing for display.

    Args:
        tin (str): tin to format.

    Returns:
        str: Formatted tin or None if invalid.
    """
    tin = remove_symbols(tin)

    if is_valid(tin) == "Valid tin":
        return f"{tin[:2]}-{tin[2:4]}-{tin[4:6]}-{tin[6:11]}"
    return None

# USER INPUT VALIDATION
def validate_user_input(user_input):  # type: (str) -> str
    """
    Validates user input as a valid Polish tin.

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
    generated_tin = generate()
    print(f"Generated tin: {generated_tin} - Valid? {is_valid(generated_tin)}")
    print(f"Formatted tin: {format_tin(generated_tin)}")

    # User input
    user_input = input("Enter a Polish tin (with or without symbols): ")
    print(validate_user_input(user_input))
    print(f"Formatted tin: {format_tin(user_input)}")

# Run the example usage
example_usage()
