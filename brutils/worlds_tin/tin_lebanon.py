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
        remove_symbols("123-456-789") -> "123456789"
    """
    return "".join(filter(str.isdigit, dirty_tin))


def is_valid_tin(tin):  # type: (str) -> str
    """
    Validates a Lebanese tin.

    Args:
        tin (str): A string containing the tin to be validated.

    Returns:
        str: 'Valid tin' if valid, otherwise 'Invalid tin'.
    """
    tin = remove_symbols(tin)

    # Lebanese tin must be exactly 8 digits
    if len(tin) != 8 or not tin.isdigit():
        return "Invalid tin: Must be exactly 8 numeric digits."

    # Validation algorithm: Modulus 11
    weights = [2, 4, 7, 3, 6, 8, 5, 9]  # Weights for the first 7 digits
    checksum = sum(int(tin[i]) * weights[i] for i in range(7)) % 11
    check_digit = int(tin[7])

    if checksum == check_digit:
        return "Valid tin"
    return "Invalid tin: Checksum does not match."


def format_tin(tin):  # type: (str) -> str
    """
    Formats a Lebanese tin for display with visual aid symbols.

    Args:
        tin (str): A string containing the tin.

    Returns:
        str: A formatted tin with visual aids or None if invalid.
    """
    tin = remove_symbols(tin)

    if len(tin) != 8 or not tin.isdigit():
        return None

    return f"{tin[:2]}.{tin[2:5]}.{tin[5:]}"

# GENERATE FUNCTION
###################

def generate_tin():  # type: () -> str
    """
    Generates a random valid Lebanese tin.

    Returns:
        str: A valid randomly generated tin.
    """
    # Generate the first 7 digits randomly
    first_7_digits = [randint(0, 9) for _ in range(7)]

    # Calculate checksum using weights
    weights = [2, 4, 7, 3, 6, 8, 5, 9]
    checksum = sum(first_7_digits[i] * weights[i] for i in range(7)) % 11
    first_7_digits.append(checksum)

    # Combine digits into a string
    return ''.join(map(str, first_7_digits))

# USAGE EXAMPLES
################

def example_usage():
    # Generate a Lebanese tin
    generated_tin = generate_tin()
    formatted_tin = format_tin(generated_tin)
    print(f"Generated tin: {formatted_tin} - Valid? {is_valid_tin(generated_tin)}")

    # Validate user input
    user_input = input("Enter a Lebanese tin: ")
    formatted_user_input = format_tin(user_input)
    if formatted_user_input:
        print(f"Formatted tin: {formatted_user_input}")
    print(is_valid_tin(user_input))

# Run the example usage
example_usage()
