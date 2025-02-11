from random import randint, choice


# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, and hyphens from the input string.
    """
    return "".join(filter(str.isalnum, dirty_tin))


# VALIDATE tin
def is_valid_tin(tin):  # type: (str) -> str
    """
    Validate a Cabo Verde tin.
    """
    tin = remove_symbols(tin)
    
    if len(tin) != 9 or not tin.isdigit():
        return "Invalid Cabo Verde tin: Must be exactly 9 digits."
    
    # Calculate the control digit
    expected_digit = calculate_control_digit(tin)
    actual_digit = int(tin[-1])
    
    if expected_digit == actual_digit:
        return "Valid Cabo Verde tin"
    return "Invalid Cabo Verde tin: Checksum mismatch."


# CALCULATE CONTROL DIGIT USING MODULE 11
def calculate_control_digit(tin):  # type: (str) -> int
    """
    Calculate the control digit for the Cabo Verde tin using modulo 11 algorithm.
    """
    # Weights for the calculation
    weights = [2, 3, 4, 5, 6, 7, 8, 9]
    
    # Multiply each digit of the tin by the respective weight
    total_sum = sum(int(digit) * weight for digit, weight in zip(tin[:8], weights))
    
    # Calculate the remainder when divided by 11
    remainder = total_sum % 11
    
    # Calculate the control digit
    control_digit = 11 - remainder
    if control_digit == 10:
        control_digit = 0
    elif control_digit == 11:
        control_digit = 1
    
    return control_digit


# GENERATE tin
def generate_tin():  # type: () -> str
    """
    Generate a valid Cabo Verde tin (9 digits).
    """
    # Generate the first 8 digits (random)
    first_8_digits = "".join(str(randint(0, 9)) for _ in range(8))
    
    # Calculate the control digit
    control_digit = calculate_control_digit(first_8_digits)
    
    # Return the full tin with the control digit
    return first_8_digits + str(control_digit)

# FORMAT tin
def format_tin(tin):  # type: (str) -> str
    """
    Format the Cabo Verde tin for display.
    """
    tin = remove_symbols(tin)
    if len(tin) != 9:
        return None
    return f"{tin[:8]}-{tin[8]}"


# EXAMPLES
def example_usage():
    # Generate a valid Cabo Verde tin
    tin = generate_tin()
    print(f"Generated Cabo Verde tin: {format_tin(tin)} - Valid? {is_valid_tin(tin)}")
    
    # User input
    user_input = input("Enter your Cabo Verde tin (with or without formatting): ")
    print(is_valid_tin(user_input))
    formatted_input = format_tin(user_input)
    if formatted_input:
        print(f"Formatted Cabo Verde tin: {formatted_input}")
    else:
        print("Invalid Cabo Verde tin format.")

# Run example
example_usage()
