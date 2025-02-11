from random import randint, choice


# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  
    
    """Remove spaces, dots, and hyphens from the input string."""
    
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATE tin
def is_valid(tin):  
    """Validate a Pakistan tin."""
    tin = remove_symbols(tin)
    
    if len(tin) != 13:
        return "Invalid Pakistan tin: Must be exactly 13 numeric digits."
    
    base_number = tin[:-1]
    provided_digit = int(tin[-1])
    
    expected_digit = calculate_check_digit(base_number)
    
    if expected_digit == provided_digit:
        return "Valid Pakistan tin"
    return "Invalid Pakistan tin: Checksum mismatch."

# FORMAT tin
def format_tin(tin):  
    """Format the Pakistan tin for display."""
    tin = remove_symbols(tin)
    
    if len(tin) != 13:
        return None
    return f"{tin[:5]}-{tin[5:12]}-{tin[12]}"


# CALCULATE CHECK DIGIT USING MOD 10 (LUHN-LIKE ALGORITHM)
def calculate_check_digit(tin_base):  
    """Calculates the check digit for the Pakistan tin using a Mod 10 algorithm."""
    tin_digits = [int(d) for d in tin_base]
    
    # Passo 1: Multiplicar os dígitos ímpares por 2 e somar os dígitos individuais
    total_sum = 0
    reverse_digits = tin_digits[::-1]
    
    for i, digit in enumerate(reverse_digits, start=1):
        if i % 2 == 0:
            total_sum += digit  # Dígitos pares somam normalmente
        else:
            double = digit * 2
            total_sum += double if double < 10 else double - 9  # Soma dos dígitos individuais

    # Passo 2: Encontrar o dígito que faz o total ser múltiplo de 10
    check_digit = (10 - (total_sum % 10)) % 10
    return check_digit

# GENERATE tin
def generate():  
    """Generate a valid Pakistan tin (without dashes)."""
    province_code = str(randint(1, 99999)).zfill(5)  # Código de região
    unique_number = str(randint(1, 9999999)).zfill(7)  # Número único da pessoa
    
    base_tin = province_code + unique_number
    check_digit = calculate_check_digit(base_tin)
    
    return f"{province_code}-{unique_number}-{check_digit}"


# EXAMPLES
def example_usage():
    # Generate a valid tin
    tin = generate()
    print(f"Generated Pakistan tin: {tin} - Valid? {is_valid(tin)}")
    
    # User input validation
    user_input = input("Enter your Pakistan tin (with or without formatting): ")
    print(is_valid(user_input))
    
    formatted_input = format_tin(user_input)
    if formatted_input:
        print(f"Formatted Pakistan tin: {formatted_input}")
    else:
        print("Invalid Pakistan tin format.")

# Run example
example_usage()