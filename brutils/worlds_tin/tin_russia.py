from random import randint, choice


# Format and Validation Functions
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
    return "".join(filter(str.isdigit, dirty_tin))


def is_valid(tin):  # type: (str) -> str
    """
    Validates a Russian tin (Taxpayer Identification Number).

    Args:
        tin (str): A string containing the tin to be validated.

    Returns:
        str: 'Valid tin' if valid, otherwise 'Invalid tin'.
    """
    tin = remove_symbols(tin)

    if len(tin) not in [10, 12]:
        return "Invalid tin: Must be 10 or 12 digits."

    if len(tin) == 10:
        return "Valid tin" if is_valid_10_digit_tin(tin) else "Invalid tin: Checksum does not match."

    if len(tin) == 12:
        return "Valid tin" if is_valid_12_digit_tin(tin) else "Invalid tin: Checksum does not match."


def is_valid_10_digit_tin(tin):  # type: (str) -> bool
    """
    Validates a 10-digit tin using a checksum algorithm.

    Args:
        tin (str): A 10-digit tin.

    Returns:
        bool: True if valid, False otherwise.
    """
    weights = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    checksum = sum(int(digit) * weight for digit, weight in zip(tin[:-1], weights)) % 11 % 10
    return checksum == int(tin[-1])


def is_valid_12_digit_tin(tin):  # type: (str) -> bool
    """
    Validates a 12-digit tin using a checksum algorithm.

    Args:
        tin (str): A 12-digit tin.

    Returns:
        bool: True if valid, False otherwise.
    """
    weights_1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
    weights_2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]

    checksum_1 = sum(int(digit) * weight for digit, weight in zip(tin[:-2], weights_1)) % 11 % 10
    checksum_2 = sum(int(digit) * weight for digit, weight in zip(tin[:-1], weights_2)) % 11 % 10

    return checksum_1 == int(tin[-2]) and checksum_2 == int(tin[-1])


def format_tin(tin):  # type: (str) -> str
    """
    Format an tin for display with visual aid symbols.

    Args:
        tin (str): A string containing a valid tin.

    Returns:
        str: A formatted tin string with visual aid symbols or None if invalid.
    """
    if is_valid(tin) == "Valid tin":
        if len(tin) == 10:
            return "{} {} {}".format(tin[:3], tin[3:6], tin[6:])
        elif len(tin) == 12:
            return "{} {} {} {}".format(tin[:3], tin[3:6], tin[6:9], tin[9:])
    return None

# Generate Functions
####################

def generate_10_digit_tin():  # type: () -> str
    """
    Generates a random valid 10-digit tin.

    Returns:
        str: A valid randomly generated 10-digit tin.
    """
    base = [randint(0, 9) for _ in range(9)]
    weights = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    checksum = sum(digit * weight for digit, weight in zip(base, weights)) % 11 % 10
    return "".join(map(str, base)) + str(checksum)


def generate_12_digit_tin():  # type: () -> str
    """
    Generates a random valid 12-digit tin.

    Returns:
        str: A valid randomly generated 12-digit tin.
    """
    base = [randint(0, 9) for _ in range(10)]
    weights_1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
    weights_2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]

    checksum_1 = sum(digit * weight for digit, weight in zip(base[:10], weights_1)) % 11 % 10
    checksum_2 = sum(digit * weight for digit, weight in zip(base[:10] + [checksum_1], weights_2)) % 11 % 10

    return "".join(map(str, base)) + str(checksum_1) + str(checksum_2)

# User Input and Validation
###########################

def is_valid_user_input(user_input):  # type: (str) -> str
    """
    Validates a user input against 10-digit and 12-digit tin formats.

    Args:
        user_input (str): A string input to be validated.

    Returns:
        str: The type and validity of the input.
    """
    user_input = remove_symbols(user_input)
    return is_valid(user_input)

# Usage Examples
################

def example_usage():
    # Generate examples
    generated_10_tin = generate_10_digit_tin()
    print(f"Generated 10-digit tin: {generated_10_tin} - Valid? {is_valid(generated_10_tin)}")
    print(f"Formatted: {format_tin(generated_10_tin)}")

    generated_12_tin = generate_12_digit_tin()
    print(f"Generated 12-digit tin: {generated_12_tin} - Valid? {is_valid(generated_12_tin)}")
    print(f"Formatted: {format_tin(generated_12_tin)}")

    # Validate user input
    user_input = input("Enter an tin (10 or 12 digits, with or without symbols): ")
    print(f"Validation result: {is_valid_user_input(user_input)}")


# Run the example usage
example_usage()
