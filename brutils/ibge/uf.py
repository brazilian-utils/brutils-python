from brutils.data.enums.uf import UF, UF_CODE


def convert_code_to_uf(code: str) -> str | None:
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
    if code not in UF_CODE.values:
        return None

    return UF_CODE(code).name


def convert_uf_to_name(uf: str) -> str | None:
    """
    Convert a Brazilian UF code (e.g., 'SP') to its full state name ('São Paulo').

    - The lookup is case-insensitive and ignores surrounding whitespace.
    - Returns ``None`` if the input is invalid or the UF code is not recognized.

    Args:
        uf (str): A two-letter UF code (e.g., 'RJ', 'sp').

    Returns:
        str | None: The full state name if found, or ``None`` if the code is invalid.

    Examples:
        >>> convert_uf_to_name('SP')
        'São Paulo'
        >>> convert_uf_to_name('rj')
        'Rio de Janeiro'
    """
    if not uf or not isinstance(uf, str) or len(uf.strip()) != 2:
        return None

    federal_unit = uf.strip().upper()

    if federal_unit not in UF.names:
        return None

    result = UF[federal_unit].value

    return result
