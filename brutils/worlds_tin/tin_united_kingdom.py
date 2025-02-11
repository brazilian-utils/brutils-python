from random import randint, choice

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, hyphens, and other symbols from a string.

    Args:
        dirty_tin (str): A string containing possible non-alphanumeric characters.

    Returns:
        str: A cleaned string containing only alphanumeric characters.

    Example:
        remove_symbols("AB-12-34-56-C") -> "AB123456C"
    """
    return "".join(filter(str.isalnum, dirty_tin))


def format_nino(nino):  # type: (str) -> str
    """
    Formats a NINO for display.

    Args:
        nino (str): A cleaned NINO in 9-character format.

    Returns:
        str: A formatted NINO for display with spaces, or None if invalid.

    Example:
        format_nino("AB123456C") -> "AB 12 34 56 C"
    """
    nino = remove_symbols(nino)
    if len(nino) == 9 and nino[:2].isalpha() and nino[2:8].isdigit() and nino[8].isalpha():
        return "{} {} {} {} {}".format(nino[:2], nino[2:4], nino[4:6], nino[6:8], nino[8])
    return None


# GENERATE FUNCTIONS
#####################

def generate_nino():  # type: () -> str
    """
    Generates a random valid UK National Insurance Number (NIN).

    Returns:
        str: A valid randomly generated NIN.
    """
    prefix = choice(["AB", "CD", "EF", "GH", "JK", "LM", "OP", "QR", "ST", "XY"])
    digits = f"{randint(100000, 999999)}"
    suffix = choice(["A", "B", "C", "D"])
    return f"{prefix}{digits}{suffix}"


def generate_utr():  # type: () -> str
    """
    Generates a random valid UK Company Unique Taxpayer Reference (UTR).

    Returns:
        str: A valid randomly generated UTR.
    """
    return str(randint(1000000000, 9999999999))


def generate_companies_house_registration_number(company_type='UK') -> str:
    """
    Generates a random valid Companies House Registration Number.

    Args:
        company_type (str): Type of company ('UK', 'SC', 'NI', 'LLP').

    Returns:
        str: A valid randomly generated Companies House Registration Number.
    """
    if company_type == 'UK':  # For English/Welsh companies (8 digits)
        return f"{randint(10000000, 99999999)}"
    elif company_type == 'SC':  # For Scottish companies (SC + 6 digits)
        return f"SC{randint(100000, 999999)}"
    elif company_type == 'NI':  # For Northern Ireland companies (NI + 6 digits)
        return f"NI{randint(100000, 999999)}"
    elif company_type == 'LLP':  # For Limited Liability Partnerships (OC/SL/NL + 6 digits)
        prefix = choice(["OC", "SL", "NL"])
        return f"{prefix}{randint(100000, 999999)}"
    else:
        return "Invalid company type."


# VALIDATE FUNCTIONS
####################

def is_valid_nino(nino):  # type: (str) -> str
    """
    Validates a UK National Insurance Number (NINO).

    Args:
        nino (str): A string containing the NINO to be validated.

    Returns:
        str: Type of NINO if valid, otherwise 'Invalid NINO'.
    """
    nino = remove_symbols(nino)

    # Verificar se o NIN tem exatamente 9 caracteres
    if len(nino) != 9:
        return "Invalid NINO: NINO must have exactly 9 characters."

    # Validar o formato: 2 letras, 6 números, 1 letra
    if not (nino[:2].isalpha() and nino[2:8].isdigit() and nino[8].isalpha()):
        return "Invalid NINO: Format should be 2 letters, 6 digits, and 1 letter."

    # Validar o prefixo, algumas combinações não são válidas (BG, GB, KN, NK, TN, ZZ)
    invalid_prefixes = ["BG", "GB", "KN", "NK", "TN", "ZZ"]
    if nino[:2] in invalid_prefixes:
        return f"Invalid NINO: The prefix {nino[:2]} is not valid."

    # Validar a letra final: A, B, C, ou D
    if nino[8].upper() not in ["A", "B", "C", "D"]:
        return "Invalid NINO: The last letter must be A, B, C, or D."

    return "Valid NINO"


def is_valid_utr(utr):  # type: (str) -> str
    """
    Validates a UK Company Unique Taxpayer Reference (UTR).

    Args:
        utr (str): A string containing the UTR to be validated.

    Returns:
        str: 'UTR' if valid, otherwise 'Invalid UTR'.
    """
    utr = remove_symbols(utr)

    if len(utr) != 10 or not utr.isdigit():
        return "Invalid UTR: UTR must be exactly 10 digits."

    return "Valid UTR"


def is_valid_companies_house_registration_number(reg_number):  # type: (str) -> str
    """
    Validates a Companies House Registration Number.

    Args:
        reg_number (str): A string containing the registration number to be validated.

    Returns:
        str: The type of registration number ('English/Welsh', 'Scottish', 'Northern Irish', 'LLP', or 'Invalid').
    """
    reg_number = remove_symbols(reg_number)

    # Validar o número de registro com base no tipo da empresa (formatos diferentes)
    if len(reg_number) == 8 and reg_number.isdigit():
        return "Valid English/Welsh company registration number."
    elif len(reg_number) == 8 and reg_number[:2] in {"SC", "NI"} and reg_number[2:].isdigit():
        return "Valid Scottish or Northern Irish company registration number."
    elif len(reg_number) == 8 and reg_number[:2] in {"OC", "SL", "NL"} and reg_number[2:].isdigit():
        return "Valid LLP registration number."
    
    return "Invalid Companies House Registration Number."


# USER INTERFACE
################

# Function to validate input and determine its type
def is_valid_user_input(user_input):
    print(f"Validating input: {user_input}")
    
    # Check if it matches any of the possible formats
    nino_result = is_valid_nino(user_input)
    if nino_result.startswith("Valid NINO"):
        return f"Valid NINO: {user_input}"
    
    utr_result = is_valid_utr(user_input)
    if utr_result.startswith("Valid UTR"):
        return f"Valid UTR: {user_input}"
    
    company_result = is_valid_companies_house_registration_number(user_input)
    if company_result.startswith("Valid"):
        return f"{company_result}: {user_input}"
    
    return "Invalid number format."


# EXAMPLE USAGE

# Generate and validate a NIN, UTR, or Companies House Registration Number
def generate_and_display():
    # Generate a random type of number (NIN, UTR, or Company)
    type_choice = choice(["NIN", "UTR", "Company"])
    
    if type_choice == "NIN":
        generated = generate_nino()
        print(f"Generated NIN: {generated} - Valid? {is_valid_nino(generated)}")
        return format_nino(generated) if is_valid_nino(generated) == "Valid NINO" else "Invalid NIN"
    
    elif type_choice == "UTR":
        generated = generate_utr()
        print(f"Generated UTR: {generated} - Valid? {is_valid_utr(generated)}")
        return generated if is_valid_utr(generated) == "Valid UTR" else "Invalid UTR"
    
    else:  # Company
        company_type = choice(["UK", "SC", "NI", "LLP"])
        generated = generate_companies_house_registration_number(company_type)
        print(f"Generated Company Registration Number: {generated} - Valid? {is_valid_companies_house_registration_number(generated)}")
        return generated


# USAGE EXAMPLE

generate_and_display()

# Get user input and validate it
user_input = input("Enter a number (NINO, UTR, or Company Registration Number): ")
validation_result = is_valid_user_input(user_input)
print(f"Validation Result: {validation_result}")