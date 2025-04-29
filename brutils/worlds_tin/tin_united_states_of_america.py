from random import randint
import re

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dashes, and other symbols from a TIN.
    """
    return "".join(filter(str.isdigit, dirty_tin))


# VALIDATION
#############

def is_valid_ssn(ssn):  # type: (str) -> bool
    """
    Validates an SSN based on its structure.
    """
    ssn = remove_symbols(ssn)
    if len(ssn) != 9:
        return False
    if ssn.startswith("000") or ssn.startswith("666") or ssn.startswith("9"):
        return False
    if ssn[3:5] == "00" or ssn[5:] == "0000":
        return False
    return True

def is_valid_ein(ein):  # type: (str) -> bool
    """
    Validates an EIN based on its structure.
    """
    ein = remove_symbols(ein)
    if len(ein) != 9:
        return False
    if not ein[:2].isdigit() or not ein[2:].isdigit():
        return False
    return True


# FORMATTING
#############

def format_ssn(ssn):  # type: (str) -> str
    """
    Formats a Social Security Number (SSN) for readability.
    """
    ssn = remove_symbols(ssn)
    if len(ssn) != 9:
        return None
    return "{}-{}-{}".format(ssn[:3], ssn[3:5], ssn[5:])

def format_ein(ein):  # type: (str) -> str
    """
    Formats an Employer Identification Number (EIN) for readability.
    """
    ein = remove_symbols(ein)
    if len(ein) != 9:
        return None
    return "{}-{}".format(ein[:2], ein[2:])


# GENERATION
#############

def generate_ssn():  # type: () -> str
    """
    Generates a random valid SSN.
    """
    area = randint(100, 899)  # Avoid invalid ranges
    group = randint(10, 99)
    serial = randint(1000, 9999)
    return "{}{}{}".format(area, group, serial)

def generate_ein():  # type: () -> str
    """
    Generates a random valid EIN.
    """
    prefix = randint(10, 99)  # EIN prefixes are assigned in ranges
    serial = randint(1000000, 9999999)
    return "{}{}".format(prefix, serial)


# USAGE EXAMPLES
ssn = generate_ssn()
print(f"Generated SSN: {format_ssn(ssn)} - Valid? {is_valid_ssn(ssn)}")

ein = generate_ein()
print(f"Generated EIN: {format_ein(ein)} - Valid? {is_valid_ein(ein)}")

user_ssn = input("Enter your SSN: ")
print(is_valid_ssn(user_ssn))
print(f"Formatted SSN: {format_ssn(user_ssn)}")

user_ein = input("Enter your EIN: ")
print(is_valid_ein(user_ein))
print(f"Formatted EIN: {format_ein(user_ein)}")