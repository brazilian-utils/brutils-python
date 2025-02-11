from random import randint, choice


def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a tin.

    Args:
        dirty_tin (str): A string containing a tin with possible non-numeric characters.

    Returns:
        str: A cleaned tin containing only alphanumeric characters.

    Example:
        remove_symbols("123-45678-Z") -> "12345678Z"
    """
    return "".join(filter(str.isalnum, dirty_tin))
    

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Spanish tin by checking its structure and control letter.

    Args:
        tin (str): A string containing a tin to validate.

    Returns:
        bool: True if the tin is valid, otherwise False.

    Example:
        is_valid("12345678Z") -> True
    """
    tin = remove_symbols(tin)

    if len(tin) != 9:
        print("The tin must have exactly 9 characters.")
        return False

    first_char = tin[0]
    base, control = tin[:8], tin[8].upper()

    # Validation for DNI (8 digits + letter)
    if first_char.isdigit():
        if base.isdigit() and control.isalpha():
            return control == calculate_letter(base)
        print("Invalid format for DNI (8 digits + 1 letter).")
        return False

    # Validation for NIE (foreigners, starts with X, Y, Z)
    if first_char in "XYZ":
        numeric_base = str("XYZ".index(first_char)) + base[1:]
        if numeric_base.isdigit() and control.isalpha():
            return control == calculate_letter(numeric_base)
        print("Invalid format for NIE (X/Y/Z + 7 digits + 1 letter).")
        return False

    # Validation for NIE without NIE (L, K, M)
    if first_char in "LKM":
        if base[1:].isdigit() and control.isalpha():
            print(f"The tin corresponds to a NIE without NIE ({first_char}).")
            return True
        print("Invalid format for NIE without NIE (L/K/M + 7 digits + 1 letter).")
        return False

    # Validation for tin for legal entities
    if first_char in "ABCDEFGHJNPQSUVW":
        if base[1:].isdigit() and control.isalpha():
            print(f"The tin corresponds to a legal entity ({first_char}).")
            return True
        print("Invalid format for tin for legal entity (Letter + 7 digits + 1 letter).")
        return False

    print("The first character is not valid for a Spanish tin.")
    return False
    

def format_tin(tin):  # type: (str) -> str
    """
    Formats a Spanish tin for display.

    Args:
        tin (str): A cleaned tin string (numbers and letters only).

    Returns:
        str: A formatted tin string for display, or None if invalid length.

    Example:
        format_tin("12345678Z") -> "123-45678-Z"
        format_tin("X1234567L") -> "X-1234567-L"
    """
    tin = remove_symbols(tin)
    
    if len(tin) == 9:
        if tin[0].isalpha():
            return "{}-{}-{}".format(tin[0], tin[1:8], tin[8])
        return "{}-{}-{}".format(tin[:3], tin[3:8], tin[8])
    return None



def generate():  # type: () -> str
    """
    Generates a random valid Spanish tin.

    Returns:
        str: A valid randomly generated tin.

    Example:
        generate() -> "12345678Z"
    """
    type_ = randint(1, 3)
    if type_ == 1:  # DNI
        base = str(randint(10000000, 99999999))
        return base + calculate_letter(base)
    elif type_ == 2:  # NIE (X, Y, or Z)
        prefix = "XYZ"[randint(0, 2)]
        base = str(randint(1000000, 9999999))
        return prefix + base + calculate_letter(str("XYZ".index(prefix)) + base)
    else:  # Legal entity
        prefix = "ABCDEFGHJNPQSUVW"[randint(0, 15)]
        base = str(randint(1000000, 9999999))
        return prefix + base + calculate_letter(base)


def calculate_letter(base):  # type: (str) -> str
    """
    Calculates the control letter for a given tin base.

    Args:
        base (str): The numeric part of a tin.

    Returns:
        str: The control letter for the tin.

    Example:
        calculate_letter("12345678") -> "Z"
    """
    letter_table = "TRWAGMYFPDXBNJZSQVHLCKE"
    number = int(base) % 23
    return letter_table[number]


# USAGE EXAMPLE

tin = generate()
print(f"Generated tin: {tin} - Valid? {is_valid(tin)}")

# Validate a tin (input with symbols, such as dots and dashes)
user_tin = input("Enter your tin: ")
print(is_valid(user_tin))

# Format a tin (input with symbols, such as dots and dashes)
formatted_tin = format_tin(user_tin)
if formatted_tin:
    print(f"Formatted tin: {formatted_tin}")
else:
    print("Invalid tin.")