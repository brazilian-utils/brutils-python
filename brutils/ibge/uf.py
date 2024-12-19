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


def convert_uf_to_text(uf):  # type: (str) -> str | None
    """
    Converts a given Brazilian state code (UF) to its full state name.

    This function takes a 2-letter UF code and returns the corresponding full state name.
    It handles all Brazilian states and the Federal District.

    Args:
        uf (str): The 2-letter UF code to be converted.

    Returns:
        str or None: The full name of the state corresponding to the UF code,
            or None if the UF code is invalid.

    Example:
        >>> convert_uf_to_text('SP')
        "São Paulo"
        >>> convert_uf_to_text('RJ')
        "Rio de Janeiro"
        >>> convert_uf_to_text('XX')
        None
    """

    try:
        return UF[uf.upper()].value
    except KeyError:
        return None
