from unidecode import unidecode

from brutils.data.enums.uf import CODE_TO_UF, UF


def convert_code_to_uf(code):  # type: (str) -> str | None
    """
    Converts a given IBGE code (2-digit string) to its corresponding UF (state abbreviation).

    This function takes a 2-digit IBGE code and returns the corresponding UF code.
    It handles all Brazilian states and the Federal District.

    Args:
        code (str): The 2-digit IBGE code to be converted.

    Returns:
        str or None: The UF code corresponding to the IBGE code,
            or None if the IBGE code is invalid.

    Example:
        >>> convert_code_to_uf('12')
        'AC'
        >>> convert_code_to_uf('33')
        'RJ'
        >>> convert_code_to_uf('99')
        >>>
    """

    result = None

    if code in CODE_TO_UF.values:
        result = CODE_TO_UF(code).name

    return result


def convert_text_to_uf(state_name):  # type: (str) -> str | None
    """
    Converts a given Brazilian state full name to its corresponding UF code.

    This function takes the full name of a Brazilian state and returns the corresponding
    2-letter UF code. It handles all Brazilian states and the Federal District.

    Args:
        state_name (str): The full name of the state to be converted.

    Returns:
        str or None: The UF code corresponding to the full state name,
            or None if the full state name is invalid.

    Example:
        >>> convert_text_to_uf('São Paulo')
        "SP"
        >>> convert_text_to_uf('Rio de Janeiro')
        "RJ"
        >>> convert_text_to_uf('Minas Gerais')
        "MG"
        >>> convert_text_to_uf('Distrito Federal')
        "DF"
        >>> convert_text_to_uf('Estado Inexistente')
        None
    """

    federal_units = {unidecode(i.value.upper()): i.name for i in UF}

    return federal_units.get(unidecode(state_name.upper()), None)
