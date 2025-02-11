from random import randint, choice

# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, and hyphens from the input string.
    """
    return "".join(filter(str.isalnum, dirty_tin))
    

# VALIDATE tin
def is_valid(tin):  # type: (str) -> str
    """
    Validate a Taiwan tin.
    """
    tin = remove_symbols(tin)
    if len(tin) != 10 or not tin[0].isalpha() or not tin[1:].isdigit():
        return "Invalid Taiwan tin: Must be 10 characters with a letter followed by digits."
    expected_digit = calculate_control_digit(tin)
    actual_digit = int(tin[-1])
    if expected_digit == actual_digit:
        return "Valid Taiwan tin"
    return "Invalid Taiwan tin: Checksum mismatch."


# CONVERT LETTER TO NUMERIC VALUE
def letter_to_numeric(letter):  # type: (str) -> tuple[int, int]
    """
    Convert the first letter of a Taiwan tin to its numeric equivalent.
    """
    value = ord(letter.upper()) - 55  # A=10, B=11, ..., Z=35
    return divmod(value, 10)

# CALCULATE CONTROL DIGIT
def calculate_control_digit(tin):  # type: (str) -> int
    """
    Calculate the control digit for a Taiwan tin.
    """
    letter_part = letter_to_numeric(tin[0])
    numeric_part = [int(d) for d in tin[1:9]]
    weights = [1, 9, 8, 7, 6, 5, 4, 3, 2]
    full_sequence = list(letter_part) + numeric_part
    weighted_sum = sum(w * d for w, d in zip(weights, full_sequence))
    control_digit = (10 - (weighted_sum % 10)) % 10
    return control_digit


# FORMAT tin
def format_tin(tin):  # type: (str) -> str
    """
    Format a Taiwan tin for display.
    """
    tin = remove_symbols(tin)
    if len(tin) != 10:
        return None
    return f"{tin[:1]}-{tin[1:9]}-{tin[9]}"
    

# GENERATE tin
def generate():  # type: () -> str
    """
    Generate a valid Taiwan tin.
    """
    first_letter = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # Location code
    gender_digit = choice("12")  # 1 for male, 2 for female
    sequence = f"{randint(1000000, 9999999)}"
    partial_tin = f"{first_letter}{gender_digit}{sequence}"
    control_digit = calculate_control_digit(partial_tin)
    return partial_tin + str(control_digit)


# EXAMPLES
def example_usage():
    # Generate a valid Taiwan tin
    tin = generate()
    print(f"Generated Taiwan tin: {format_tin(tin)} - Valid? {is_valid(tin)}")
    
    # User input
    user_input = input("Enter your Taiwan tin (with or without formatting): ")
    print(is_valid(user_input))
    formatted_input = format_tin(user_input)
    if formatted_input:
        print(f"Formatted Taiwan tin: {formatted_input}")
    else:
        print("Invalid Taiwan tin format.")

# Run example
example_usage()
