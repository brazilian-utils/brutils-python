from random import randint

# FORMATTING
############


def sieve(dirty):  # type: (str) -> str
    """
    Removes specific symbols from a Passport string.

    This function takes a Passport string as input and removes all occurrences of
    the '.', '-' and space characters from it.

    Args:
        passport (str): The Passport string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.

    Example:
        >>> sieve("CS-265.436")
        'CS265436'
        >>> sieve("cs 265 436")
        'cs265436'

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """

    return "".join(filter(lambda char: char not in ".- ", dirty))


def remove_symbols(dirty):  # type: (str) -> str
    """
    Alias for the `sieve` function. Better naming.

    Args:
        passport (str): The Passport string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.
    """

    return sieve(dirty)


def display(passport):  # type: (str) -> str
    """
    Normalize a Passport string for display.

    This function takes a Passport string (possibly with visual-aid symbols) and
    returns an uppercase, symbols-free representation if valid.

    Args:
        passport (str): A Passport string with or without symbols.

    Returns:
        str: An uppercase Passport string without symbols or None if the input
            is invalid.

    Example:
        >>> display("cs 265.436")
        'CS265436'
        >>> display("AB123456")
        'AB123456'

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """

    if not isinstance(passport, str):
        return None

    cleaned = sieve(passport).upper()
    if len(cleaned) != 8:
        return None

    # Pattern: 2 letters + 6 digits
    if not (cleaned[:2].isalpha() and cleaned[2:].isdigit()):
        return None

    return cleaned


def format_passport(passport):  # type: (str) -> str
    """
    Normalize a Passport string for display.

    This function takes a Passport string (possibly with visual-aid symbols) and
    returns an uppercase, symbols-free representation if valid.

    Args:
        passport (str): A Passport string with or without symbols.

    Returns:
        str: An uppercase Passport string without symbols or None if the input
        is invalid.

    Example:
        >>> format_passport("cs 265436")
        'CS265436'
        >>> format_passport("C-5265436")
        None
    """
    if is_valid(passport):
        return sieve(passport).upper()

    # Clean common separators and validate again
    cleaned = remove_symbols(passport)
    if cleaned != passport and is_valid(cleaned):
        return cleaned.upper()

    return None


# OPERATIONS
############


def validate(passport):  # type: (str) -> bool
    """
    Validate the format of a Brazilian Passport number.

    This function checks whether the given Passport matches the expected format:
    exactly two letters (series) followed by six digits. It does not verify the
    existence of a real document.

    Args:
        passport (str): A Passport string.

    Returns:
        bool: True if the format is valid, False otherwise.

    Example:
        >>> validate("CS265436")
        True
        >>> validate("AA000001")
        True
    """
    if len(passport) != 8:
        return False
    return passport[:2].isalpha() and passport[2:].isdigit()


def is_valid(passport):  # type: (str) -> bool
    """
    Returns whether or not the given Passport matches the expected format.

    This function does not verify the existence of the Passport; it only
    validates the format of the string (two letters followed by six digits).

    Args:
        passport (str): The Passport to be validated.

    Returns:
        bool: True if the string matches the required pattern, False otherwise.

    Example:
        >>> is_valid("CS265436")
        True
        >>> is_valid("A123456")
        False
    """
    return isinstance(passport, str) and validate(passport)


def generate():  # type: () -> str
    """
    Generate a random syntactically valid Passport string.

    This function generates a random Passport string composed of two uppercase
    letters followed by six digits. It does not correspond to a real document.

    Returns:
        str: A random syntactically valid Passport string.

    Example:
        >>> p = generate()
        >>> len(p), p[:2].isalpha(), p[2:].isdigit()
        (8, True, True)
    """

    # two uppercase letters (A–Z)
    letters = "".join(chr(randint(ord("A"), ord("Z"))) for _ in range(2))
    # six digits (0–9)
    digits = "".join(str(randint(0, 9)) for _ in range(6))
    return letters + digits
