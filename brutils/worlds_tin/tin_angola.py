from random import randint, choice

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes any non-digit characters from an Angolan tin.
    """
    return "".join(filter(str.isdigit, dirty_tin))


# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates an Angolan tin (Número de Identificação Fiscal).
    """
    tin = remove_symbols(tin)
    if len(tin) != 9 or not tin.isdigit():
        return False
    if tin[0] not in "1568":
        return False
    base, check_digit = tin[:-1], int(tin[-1])
    return _calculate_digit(base) == check_digit


# CHECK DIGIT CALCULATION
###########################

def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the check digit for an Angolan tin.
    """
    weights = [9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(int(d) * w for d, w in zip(base, weights))
    remainder = total % 11
    return 0 if remainder in (0, 1) else 11 - remainder


def format_tin(tin):  # type: (str) -> str
    """
    Formats an Angolan tin for readability.
    """
    tin = remove_symbols(tin)
    if len(tin) != 9:
        return None
    return f"{tin[:3]}.{tin[3:6]}.{tin[6:]}"


# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a valid Angolan tin.
    """
    prefix = choice(['1', '5', '6', '8'])  # Based on entity type
    base = prefix + str(randint(1000000, 9999999))
    dv = _calculate_digit(base)
    return base + str(dv)


# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your Angolan tin: ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")