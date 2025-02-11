from random import randint, choice


# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a Steuer-ID.

    Args:
        dirty_tin (str): A string containing a Steuer-ID with possible non-numeric characters.

    Returns:
        str: A cleaned Steuer-ID containing only numeric digits.

    Example:
        remove_symbols("12.345.678-901") -> "12345678901"
    """
    return "".join(filter(str.isdigit, dirty_tin))


def format_tin(tin):  # type: (str) -> str
    """
    Formats a Steuer-ID for display.

    Args:
        tin (str): A cleaned Steuer-ID of 11 digits.

    Returns:
        str: A formatted Steuer-ID for display with spaces, or None if invalid.

    Example:
        format_tin("12345678901") -> "123 456 789 01"
    """
    tin = remove_symbols(tin)
    if len(tin) == 11:
        return "{} {} {} {}".format(tin[:3], tin[3:6], tin[6:9], tin[9:])
    return None


# OPERATIONS
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a German Steuer-ID by checking its structure and control digit.

    Args:
        tin (str): A string containing the Steuer-ID to validate.

    Returns:
        bool: True if the Steuer-ID is valid, False otherwise.

    Example:
        is_valid("12345678901") -> True
    """
    tin = remove_symbols(tin)

    if len(tin) != 11:
        print("The Steuer-ID must have exactly 11 digits.")
        return False

    if not tin.isdigit():
        print("The Steuer-ID must contain only numbers.")
        return False

    base, control = tin[:10], int(tin[10])
    if control == _calculate_digit(base):
        print("The TIN is valid.")
        return True
    print("The TIN is invalid.")
    return False


def generate():  # type: () -> str
    """
    Generates a valid German Steuer-ID.

    Returns:
        str: A randomly generated Steuer-ID.

    Example:
        generate() -> "12345678901"
    """
    base = "".join(str(randint(0, 9)) for _ in range(10))
    return base + str(_calculate_digit(base))


def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the control digit for a German Steuer-ID.

    Args:
        base (str): The first 10 digits of the Steuer-ID.

    Returns:
        int: The calculated control digit.

    Example:
        _calculate_digit("1234567890") -> 3
    """
    sum_ = 0
    weight = 2

    # Calculate weighted sum
    for digit in reversed(base):
        sum_ += int(digit) * weight
        weight += 1
        if weight > 10:  # Reset weight to 2 after 10
            weight = 2

    # Calculate the control digit
    remainder = sum_ % 11
    return (10 - remainder) % 10


# USAGE EXAMPLE

tin = generate()
print(f"Generated tin: {tin} - Valid? {is_valid(tin)}")

# Validate a tin (input with symbols, such as dots and dashes)
user_tin = input("Enter your tin: ")
print(is_valid(user_tin))

# Format a tin (input with symbols, such as dots, dashes, and spaces)
formatted_tin = format_tin(user_tin)
if formatted_tin:
    print(f"Formatted tin: {formatted_tin}")
else:
    print("Invalid tin.")
