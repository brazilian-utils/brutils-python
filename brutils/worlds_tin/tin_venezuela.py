from random import randint, choice
import re

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dashes, and other symbols from a tin and standardizes the letter case.
    """
    cleaned = "".join(filter(str.isalnum, dirty_tin))
    return cleaned.capitalize() if cleaned else cleaned


# VALIDATION
#############

def is_valid_tin(tin):  # type: (str) -> bool
    """
    Validates a Venezuelan tin based on its structure and check digit.
    """
    tin = remove_symbols(tin)
    if not re.fullmatch(r"[VEJG][0-9]{8,9}", tin):
        return False
    base, check_digit = tin[:-1], int(tin[-1])
    return _calculate_digit(base) == check_digit


# CHECK DIGIT CALCULATION
###########################

def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the check digit for a given tin base.
    """
    weights = {
        'V': 4, 'E': 8, 'J': 3, 'G': 5, 'P': 9
    }generate
    total = weights.get(base[0], 0) * 10  # First character weight
    multipliers = [2, 3, 4, 5, 6, 7, 2, 3, 4]
    total += sum(int(d) * m for d, m in zip(base[1:], multipliers))
    remainder = total % 11
    return (11 - remainder) % 11


# FORMATTING
#############

def format_tin(tin):  # type: (str) -> str
    """
    Formats a Venezuelan tin for readability.
    """
    tin = remove_symbols(tin)
    if len(tin) < 9 or len(tin) > 10:
        return None
    return "{}-{}-{}".format(tin[0], tin[1:-1], tin[-1])


# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a random valid Venezuelan tin.
    """
    prefix = choice(['V', 'E', 'J', 'G', 'P'])
    base_number = str(randint(10000000, 999999999))[:8]  # Ensure 8-digit base
    base = prefix + base_number
    check_digit = _calculate_digit(base)
    return base + str(check_digit)


# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid_tin(tin)}")

user_tin = input("Enter your tin: ")
print(is_valid_tin(user_tin))
print(f"Formatted tin: {format_tin(user_tin)}")