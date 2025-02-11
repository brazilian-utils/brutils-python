from random import randint, choice


# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, and hyphens from the input string.
    """
    return "".join(filter(str.isdigit, dirty_tin))
    

# VALIDATE EMIRATES ID
def is_valid(tin):  # type: (str) -> str
    """
    Validate an Emirates ID.
    """
    tin = remove_symbols(tin)
    if len(tin) != 15 or not tin.isdigit():
        return "Invalid Emirates ID: Must be exactly 15 numeric digits."
    calculated_digit = calculate_control_digit(tin)
    actual_digit = int(tin[-1])
    if calculated_digit == actual_digit:
        return "Valid Emirates ID"
    return "Invalid Emirates ID: Checksum mismatch."


# CALCULATE CONTROL DIGIT
def calculate_control_digit(tin):  # type: (str) -> int
    """
    Calculate the control digit for the Emirates ID using the modulo 11 algorithm.
    """
    weights = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    base_digits = [int(d) for d in tin[:14]]
    weighted_sum = sum(d * w for d, w in zip(base_digits, weights))
    remainder = weighted_sum % 11
    control_digit = (11 - remainder) if remainder != 10 else 0
    return control_digit
    

# FORMAT FOR DISPLAY
def format_tin(tin):  # type: (str) -> str
    """
    Format the Emirates ID for display as XXX-YYYY-XXXXXXX-C.
    """
    tin = remove_symbols(tin)
    if len(tin) != 15:
        return None
    return f"{tin[:3]}-{tin[3:7]}-{tin[7:14]}-{tin[14]}"

# GENERATE EMIRATES ID
def generate():  # type: () -> str
    """
    Generate a valid Emirates ID.
    """
    country_code = "784"
    year = str(randint(1800, 2029))
    serial_number = f"{randint(1000000, 9999999)}"
    base_number = f"{country_code}{year}{serial_number}"
    control_digit = calculate_control_digit(base_number)
    return base_number + str(control_digit)


# EXAMPLES
def example_usage():
    # Generate a valid Emirates ID
    tin = generate()
    print(f"Generated Emirates ID: {format_tin(tin)} - Valid? {is_valid(tin)}")
    
    # User input
    user_input = input("Enter your Emirates ID (with or without formatting): ")
    print(is_valid(user_input))
    formatted_input = format_tin(user_input)
    if formatted_input:
        print(f"Formatted Emirates ID: {formatted_input}")
    else:
        print("Invalid Emirates ID format.")

# Run example
example_usage()
