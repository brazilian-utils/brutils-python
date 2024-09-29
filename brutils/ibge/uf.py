from brutils.data.enums.uf import CODE_TO_UF


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
