from random import randint, choice

# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a string.
    """
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATION FUNCTIONS
def is_valid_tfn(tfn):  # type: (str) -> str
    """
    Validates an Australian Tax File Number (TFN).

    A TFN must be 8 or 9 digits and pass a weighted checksum validation.

    Args:
        tfn (str): TFN to validate.

    Returns:
        str: 'Valid TFN' if valid, otherwise 'Invalid TFN'.
    """
    tfn = remove_symbols(tfn)

    # TFN must be 8 or 9 digits
    if len(tfn) not in [8, 9] or not tfn.isdigit():
        return "Invalid TFN: Must be 8 or 9 numeric digits."

    # Weighted checksum validation
    weights = [1, 4, 3, 7, 5, 8, 6, 9, 10][:len(tfn)]
    checksum = sum(int(digit) * weight for digit, weight in zip(tfn, weights))
    if checksum % 11 == 0:
        return "Valid TFN"
    return "Invalid TFN: Failed checksum validation."

def is_valid_abn(abn):  # type: (str) -> str
    """
    Validates an Australian Business Number (ABN).

    An ABN must be 11 digits and pass a modulo 89 checksum validation.

    Args:
        abn (str): ABN to validate.

    Returns:
        str: 'Valid ABN' if valid, otherwise 'Invalid ABN'.
    """
    abn = remove_symbols(abn)

    # ABN must be 11 digits
    if len(abn) != 11 or not abn.isdigit():
        return "Invalid ABN: Must be exactly 11 numeric digits."

    # Adjust the first digit and calculate checksum
    adjusted_digits = [int(abn[0]) - 1] + [int(d) for d in abn[1:]]
    weights = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    checksum = sum(d * w for d, w in zip(adjusted_digits, weights))
    if checksum % 89 == 0:
        return "Valid ABN"
    return "Invalid ABN: Failed checksum validation."

# GENERATE FUNCTIONS
def generate_tfn():  # type: () -> str
    """
    Generates a valid Australian Tax File Number (TFN).

    Returns:
        str: A valid TFN.
    """
    while True:
        tfn = f"{randint(10**7, 10**9 - 1)}"
        if is_valid_tfn(tfn) == "Valid TFN":
            return tfn

def generate_abn():  # type: () -> str
    """
    Generates a valid Australian Business Number (ABN).

    Returns:
        str: A valid ABN.
    """
    while True:
        identifier = f"{randint(10**7, 10**9 - 1)}"
        for prefix in range(10, 100):
            abn = f"{prefix}{identifier}"
            if is_valid_abn(abn) == "Valid ABN":
                return abn

# FORMAT FUNCTIONS
def format_tfn(tfn):  # type: (str) -> str
    """
    Formats a TFN as XXX XXX XXX or XX XXX XXX.

    Args:
        tfn (str): TFN to format.

    Returns:
        str: Formatted TFN or None if invalid.
    """
    tfn = remove_symbols(tfn)
    if is_valid_tfn(tfn) == "Valid TFN":
        if len(tfn) == 9:
            return f"{tfn[:3]} {tfn[3:6]} {tfn[6:]}"
        if len(tfn) == 8:
            return f"{tfn[:2]} {tfn[2:5]} {tfn[5:]}"
    return None

def format_abn(abn):  # type: (str) -> str
    """
    Formats an ABN as XX XXX XXX XXX.

    Args:
        abn (str): ABN to format.

    Returns:
        str: Formatted ABN or None if invalid.
    """
    abn = remove_symbols(abn)
    if is_valid_abn(abn) == "Valid ABN":
        return f"{abn[:2]} {abn[2:5]} {abn[5:8]} {abn[8:]}"
    return None

# USAGE EXAMPLES
def example_usage():
    # Generate examples
    generated_tfn = generate_tfn()
    print(f"Generated TFN: {generated_tfn} - Valid? {is_valid_tfn(generated_tfn)}")
    print(f"Formatted TFN: {format_tfn(generated_tfn)}")

    generated_abn = generate_abn()
    print(f"Generated ABN: {generated_abn} - Valid? {is_valid_abn(generated_abn)}")
    print(f"Formatted ABN: {format_abn(generated_abn)}")

    # User input
    user_input = input("Enter a TFN or ABN (with or without symbols): ")
    if len(remove_symbols(user_input)) in [8, 9]:
        print(is_valid_tfn(user_input))
        print(f"Formatted TFN: {format_tfn(user_input)}")
    elif len(remove_symbols(user_input)) == 11:
        print(is_valid_abn(user_input))
        print(f"Formatted ABN: {format_abn(user_input)}")
    else:
        print("Invalid input. Please enter a valid TFN or ABN.")

# Run example
example_usage()
