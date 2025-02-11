from random import randint, choice


# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, hyphens, and other symbols from a tin.

    Args:
        dirty_tin (str): A string containing a tin with possible non-numeric characters.

    Returns:
        str: A cleaned tin containing only numeric digits.

    Example:
        remove_symbols("80000001-2") -> "800000012"
    """
    return "".join(filter(str.isdigit, dirty_tin))


def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Paraguayan tin based on its sttinture and verifier digit.

    Args:
        tin (str): A string containing the tin to be validated.

    Returns:
        bool: True if the tin is valid, False otherwise.

    Example:
        is_valid("800000012") -> True
    """
    tin = remove_symbols(tin)

    if len(tin) < 7 or len(tin) > 9:
        print("The tin must have between 7 and 9 digits.")
        return False

    base, verifier = tin[:-1], tin[-1]

    if not base.isdigit() or not verifier.isdigit():
        print("The tin must contain only digits.")
        return False

    expected_verifier = calculate_verifier_digit(base)
    if int(verifier) != expected_verifier:
        print(f"Invalid tin: Expected verifier {expected_verifier}, got {verifier}.")
        return False

    print("The tin is valid.")
    return True


def calculate_verifier_digit(base):  # type: (str) -> int
    """
    Calculates the verifier digit for a tin using weights [2, 3, 4, 5, 6, 7].

    Args:
        base (str): The numeric base of the tin (without the verifier digit).

    Returns:
        int: The calculated verifier digit.

    Example:
        calculate_verifier_digit("80000001") -> 2
    """
    weights = [2, 3, 4, 5, 6, 7]
    base_reversed = list(map(int, reversed(base)))

    total = sum(d * weights[i % len(weights)] for i, d in enumerate(base_reversed))
    verifier = 11 - (total % 11)

    return verifier if verifier < 10 else 0  # Return 0 if verifier is 10


def format_tin(tin):  # type: (str) -> str
    """
    Formats a tin for display.

    Args:
        tin (str): A cleaned tin.

    Returns:
        str: A formatted tin for display or None if invalid.

    Example:
        format_tin("800000012") -> "80000001-2"
    """
    tin = remove_symbols(tin)

    if len(tin) >= 7 and len(tin) <= 9:
        return f"{tin[:-1]}-{tin[-1]}"
    return None



# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a valid Paraguayan tin.

    Returns:
        str: A valid tin.

    Example:
        generate() -> "800000012"
    """
    # Generate a random base with 6 to 8 digits
    base = str(randint(100000, 99999999))

    # Calculate the verifier digit
    verifier = calculate_verifier_digit(base)

    # Combine base and verifier to form the full tin
    return base + str(verifier)


# USAGE EXAMPLES
#################

# Generate and validate a tin
generated_tin = generate()
formatted_tin = format_tin(generated_tin)
print(f"Generated tin: {formatted_tin}")
is_valid(generated_tin)

# Validate a tin from user input
user_tin = input("\nEnter a tin: ")
formatted_user_tin = format_tin(user_tin)
if formatted_user_tin:
    print(f"Formatted tin: {formatted_user_tin}")
is_valid(user_tin)
