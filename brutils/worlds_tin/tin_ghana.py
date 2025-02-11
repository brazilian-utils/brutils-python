from random import randint, choice

# REMOVE SYMBOLS
def remove_symbols(dirty_tin):
    """Remove spaces, dots, and hyphens from the input string."""
    return "".join(filter(str.isalnum, dirty_tin))

# VALIDATE GRA TIN
def is_valid_ghana_tin(tin):
    """Validate a Ghana GRA TIN."""
    tin = remove_symbols(tin)
    
    if not any(tin.startswith(prefix) for prefix in ["P00", "C00", "G00", "Q00", "V00"]):
        return "Invalid GRA TIN: Must start with a valid prefix (P00, C00, G00, Q00, V00)."
    
    if len(tin) != 11:  # Prefixo (3) + 8 dígitos
        return "Invalid GRA TIN: Must have 11 characters."
    
    return "Valid GRA TIN"

# VALIDATE GHANACARD PIN
def is_valid_ghanacard_pin(tin):
    """Validate a Ghana Ghanacard PIN."""
    tin = remove_symbols(tin)
    
    if not tin.startswith("GHA"):
        return "Invalid GhanaCard PIN: Must start with 'GHA'."
    
    base_number = tin[3:-1]  # Remove 'GHA' e último dígito
    provided_digit = tin[-1]
    
    expected_digit = calculate_check_digit(base_number)
    
    if expected_digit == provided_digit:
        return "Valid GhanaCard PIN"
    return "Invalid GhanaCard PIN: Checksum mismatch."

# CALCULATE CHECK DIGIT (SIMPLIFIED MOD 11 APPROACH)
def calculate_check_digit(base_number):
    """Calculates the check digit for the Ghanacard PIN using Mod 11 algorithm."""
    weights = [3, 7, 1] * 3  # Exemplo de pesos alternados
    total_sum = sum(int(d) * w for d, w in zip(base_number, weights[:len(base_number)]))
    
    check_digit = total_sum % 11
    return str(check_digit) if check_digit != 10 else choice("ABCDEFGHJKLMNPQRSTUVWXYZ")

# GENERATE GRA TIN
def generate_ghana_tin():
    """Generate a valid Ghana GRA TIN."""
    prefix = choice(["P00", "C00", "G00", "Q00", "V00"])
    number = str(randint(10000000, 99999999))
    
    return f"{prefix}-{number}"

# GENERATE GHANACARD PIN
def generate_ghanacard_pin():
    """Generate a valid Ghana Ghanacard PIN."""
    country_code = "GHA"
    number = str(randint(10000000, 999999999))  # 8 ou 9 dígitos
    check_digit = calculate_check_digit(number)
    
    return f"{country_code}-{number}-{check_digit}"


# FORMAT GHANACARD PIN
def format_ghanacard_pin(tin):
    """Format the GhanaCard PIN for display."""
    tin = remove_symbols(tin)
    
    if len(tin) not in [12, 13]:  # GHA + (8 ou 9 dígitos) + checksum
        return None
    return f"{tin[:3]}-{tin[3:-1]}-{tin[-1]}"

# EXAMPLES
def example_usage():
    # Generate valid Ghanaian IDs
    tin = generate_ghana_tin()
    ghanacard = generate_ghanacard_pin()

    print(f"Generated Ghana TIN: {tin} - Valid? {is_valid_ghana_tin(tin)}")
    print(f"Generated GhanaCard PIN: {ghanacard} - Valid? {is_valid_ghanacard_pin(ghanacard)}")

    # User input validation
    user_input = input("Enter your tin (GRA TIN or GhanaCard PIN): ")
    
    # Check if it is a GRA TIN or a GhanaCard PIN
    if any(user_input.startswith(prefix) for prefix in ["P00", "C00", "G00", "Q00", "V00"]):
        print(is_valid_ghana_tin(user_input))
    elif user_input.startswith("GHA"):
        print(is_valid_ghanacard_pin(user_input))
    else:
        print("Invalid tin format: Must be either a valid GRA TIN or GhanaCard PIN.")

    formatted_input = format_ghanacard_pin(user_input)
    if formatted_input:
        print(f"Formatted GhanaCard PIN: {formatted_input}")

# Run example
example_usage()
