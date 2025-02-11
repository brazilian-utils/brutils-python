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


def is_valid_tin(tin):  # type: (str) -> str
    """
    Validates a Salvadoran NIT (Número de Identificación Tributaria).

    Args:
        tin (str): A string containing the tin to be validated.

    Returns:
        str: 'Valid tin' if valid, otherwise 'Invalid tin'.
    """
    tin = remove_symbols(tin)

    if len(tin) != 14:
        return "Invalid tin: Must be exactly 14 digits."

    # Extract the main number and the checksum digit
    main_digits = tin[:-1]
    checksum_digit = int(tin[-1])

    # Calculate the checksum
    weights = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2]
    checksum = sum(int(digit) * weight for digit, weight in zip(main_digits, weights)) % 11

    # Check the result
    if checksum == 10:
        checksum = 0

    return "Valid tin" if checksum == checksum_digit else "Invalid tin: Checksum does not match."


def format_tin(tin):  # type: (str) -> str
    """
    Format a tin for display with visual aid symbols.

    Args:
        tin (str): A string containing a valid tin.

    Returns:
        str: A formatted tin string with visual aid symbols or None if invalid.
    """
    if is_valid_tin(tin) == "Valid tin":
        return f"{tin[:4]}-{tin[4:10]}-{tin[10:13]}-{tin[13]}"
    return None


# Generate Functions
####################

def generate_tin():  # type: () -> str
    """
    Generates a random valid Salvadoran tin.

    Returns:
        str: A valid randomly generated tin.
    """
    main_digits = [randint(0, 9) for _ in range(13)]
    weights = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2]
    checksum = sum(digit * weight for digit, weight in zip(main_digits, weights)) % 11

    if checksum == 10:
        checksum = 0

    return "".join(map(str, main_digits)) + str(checksum)


# User Input and Validation
###########################

def is_valid_user_input(user_input):  # type: (str) -> str
    """
    Validates a user input against tin format.

    Args:
        user_input (str): A string input to be validated.

    Returns:
        str: The type and validity of the input.
    """
    user_input = remove_symbols(user_input)
    return is_valid_tin(user_input)


# Usage Examples
################

def example_usage():
    # Generate examples
    generated_tin = generate_tin()
    print(f"Generated tin: {generated_tin} - Valid? {is_valid_tin(generated_tin)}")
    print(f"Formatted: {format_tin(generated_tin)}")

    # Validate user input
    user_input = input("Enter a tin (with or without symbols): ")
    print(f"Validation result: {is_valid_user_input(user_input)}")

# Run the example usage
example_usage()
