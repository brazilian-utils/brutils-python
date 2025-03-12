from random import randint, choice

# REMOVE FORMATTING
def remove_symbols(dirty_tin):
    """Remove spaces, dots, and hyphens from the input string."""
    return "".join(filter(str.isalnum, dirty_tin))


# VALIDATE ANGUILLAN tin
def is_valid(tin):
    """Validates an Anguilla tin number."""
    tin = remove_symbols(tin)

    if not (10 <= len(tin) <= 12):
        return "Invalid Anguilla tin: Must have between 10 and 12 characters."
    
    if not tin.startswith("AA"):
        return "Invalid Anguilla tin: Must start with 'AA'."

    if not tin[2:].isdigit():
        return "Invalid Anguilla tin: The remaining characters must be numeric."
    
    return "Valid Anguilla tin"

# FORMAT ANGUILLAN tin
def format_anguilla_tin(tin):
    """Formats an Anguilla tin for display."""
    tin = remove_symbols(tin)

    if len(tin) < 10:
        return None
    return f"{tin[:2]}-{tin[2:]}"

# GENERATE ANGUILLAN tin
def generate(is_company=False):
    """Generates a valid Anguilla tin (TIN)."""
    prefix = "AA"  # Prefixo fixo para Anguilla
    if is_company:
        prefix += "B"  # Empresas podem ter um 'B' adicional
    
    num_digits = 8 if not is_company else 7  # Indivíduos têm 8 dígitos, empresas podem ter 7
    numeric_part = "".join(str(randint(0, 9)) for _ in range(num_digits))
    
    return prefix + numeric_part

# EXAMPLES
def example_usage():
    # Generate valid Anguilla tin for individuals and companies
    tin_individual = generate()
    tin_company = generate(is_company=True)

    print(f"Generated Individual tin: {tin_individual} - Valid? {is_valid(tin_individual)}")
    print(f"Generated Company tin: {tin_company} - Valid? {is_valid(tin_company)}")

    # User input validation
    user_input = input("Enter your Anguilla tin: ")
    print(is_valid(user_input))

    formatted_input = format_anguilla_tin(user_input)
    if formatted_input:
        print(f"Formatted Anguilla tin: {formatted_input}")

# Run example
example_usage()
