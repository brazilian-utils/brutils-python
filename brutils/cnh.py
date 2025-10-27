



def is_valid_cnh(cnh: str | None) -> bool:
    """
    Validates the registration number for the Brazilian CNH (Carteira Nacional de Habilitação) that was created in 2022.
    This function checks if the given CNH is valid based on the format and allowed characters,
    verifying the registration and verification digits.

    Args:
        cnh (str | None): CNH string (symbols will be ignored).

    Returns:
        bool: True if CNH has a valid format.
    """

    cnh_digits, verification_cnh_digits = _get_cnh_number_and_last_two_digits(cnh)

    if not cnh:
        return False

    if len(cnh_digits ) != 11:
        return False

     # Reject sequences as "00000000000", "11111111111", etc.
    if cnh_digits == cnh_digits[0] * 11:
        return False

    digits = _get_cnh_digits(cnh_digits)

    first_validation_digit = _get_tenth_digit(digits, cnh_digits)

    if cnh_digits[9] != str(first_validation_digit): # checking the 10th digit
        return False

    second_validation_digit = _get_eleventh_digit(digits, cnh_digits, first_validation_digit)

    return _validate_cnh(verification_cnh_digits, first_validation_digit, second_validation_digit)

def _get_cnh_number_and_last_two_digits(cnh):
    # removing symbols
    cnh_digits  = ''.join(filter(str.isdigit, cnh))
    verification_cnh_digits = cnh_digits[9:11]

    return cnh_digits, verification_cnh_digits

def _get_cnh_digits(cnh_digits):
    # get digits as list of integers 
    return [int(ch) for ch in cnh_digits ]

def _get_tenth_digit(digits, cnh_digits):
    ''' generating the first verification digit, which is the 10th digit of the CNH '''

    sum_first = 0
    for i in range(9):
        sum_first += digits[i] * (9 - i)
        
    sum_first = sum_first % 11
    first_validation_digit = 0 if sum_first > 9 else sum_first
    
    return first_validation_digit

def _get_eleventh_digit(digits, cnh_digits, first_validation_digit):
    ''' generating the second verification digit, which is the 11th digit of the CNH '''
    sum_second = 0
    for i in range(9):
        sum_second += digits[i] * (i + 1)
    
    second_validation_digit = sum_second % 11

    if first_validation_digit > 9:
        second_validation_digit = second_validation_digit + 9 if (second_validation_digit - 2) < 0 else second_validation_digit - 2

    if second_validation_digit > 9:
        second_validation_digit = 0 
    
    return second_validation_digit

def _validate_cnh(verification_cnh_digits, first_validation_digit, second_validation_digit):
    ''' comparing the CNH verification digits with the generated verification digits  '''
    calculated_cnh_digits = [str(first_validation_digit), str(second_validation_digit)]
    return verification_cnh_digits == calculated_cnh_digits