import re


def format_rg(rg, uf):  # type: (str, str) -> str | None
    """
    Formats a Brazilian RG (Registro Geral) based on the state (UF).

    This function takes a Brazilian RG and formats it according to the specific
    requirements of the given UF. It should handle various input formats and
    ensure the output is standardized.

    Args:
        rg (str): The RG to be formatted.
        uf (str): The state (UF) for which the RG should be formatted.

    Returns:
        str or None: The formatted RG if valid, or None if the input is invalid.

    Example:
        >>> format_rg('12.345.678-9', 'SP')
        "12.345.678-9"
        >>> format_rg('MG-12.345.678', 'MG')
        "MG-12.345.678"
        >>> format_rg('123456789', 'RJ')
        "12.345.678-9"
        >>> format_rg('A12345678', 'SP')
        None
        >>> format_rg('12.345.678', 'SP')
        None
    """
    if not isinstance(rg, str) or not isinstance(uf, str):
        return None

    clean_rg = rg.strip().upper()
    clean_uf = uf.strip().upper()

    # Verified RG formats for each Brazilian state.
    rg_formats = {
        "AC": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "AL": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "AP": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "AM": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "BA": {
            "length": 10,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8:]}",
        },
        "CE": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "DF": {
            "length": [7, 8],
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:]}-9"
            if len(x) == 8
            else f"{x[0]}.{x[1:4]}.{x[4:]}",
        },
        "ES": {"length": 7, "format": lambda x: f"{x[0]}.{x[1:4]}.{x[4:]}"},
        "GO": {
            "length": 8,
            "format": lambda x: f"{x[:1]}.{x[1:4]}.{x[4:7]}-{x[7]}",
        },
        "MA": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "MT": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "MS": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "MG": {
            "length": [8, 9],
            "format": lambda x: f"MG-{x[:2]}.{x[2:5]}.{x[5:8]}",
        },
        "PA": {"length": 7, "format": lambda x: f"{x[0]}.{x[1:4]}.{x[4:]}"},
        "PB": {
            "length": 8,
            "format": lambda x: f"{x[:1]}.{x[1:4]}.{x[4:7]}-{x[7]}",
        },
        "PR": {
            "length": 8,
            "format": lambda x: f"{x[:1]}.{x[1:4]}.{x[4:7]}-{x[7]}",
        },
        "PE": {
            "length": 8,
            "format": lambda x: f"{x[:1]}.{x[1:4]}.{x[4:7]}-{x[7]}",
        },
        "PI": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "RJ": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "RN": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "RS": {
            "length": 10,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8:]}",
        },
        "RO": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "RR": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "SC": {"length": 7, "format": lambda x: f"{x[0]}.{x[1:4]}.{x[4:]}"},
        "SP": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "SE": {
            "length": 9,
            "format": lambda x: f"{x[:2]}.{x[2:5]}.{x[5:8]}-{x[8]}",
        },
        "TO": {
            "length": 8,
            "format": lambda x: f"{x[:1]}.{x[1:4]}.{x[4:7]}-{x[7]}",
        },
    }

    if clean_uf not in rg_formats:
        return None

    if clean_rg.startswith(clean_uf):
        clean_rg = clean_rg[len(clean_uf) :]
    if clean_rg.startswith("-"):
        clean_rg = clean_rg[1:]

    # Validate that the RG contains only numbers, 'X', '.', and '-'.
    temp_rg_for_validation = clean_rg.replace(".", "").replace("-", "")
    if not re.match(r"^[0-9X]+$", temp_rg_for_validation):
        return None

    rg_only_digits = re.sub(r"[^0-9X]", "", clean_rg)

    # Check if the length of the numeric RG matches the state's requirements.
    expected_length = rg_formats[clean_uf]["length"]
    if isinstance(expected_length, list):
        if len(rg_only_digits) not in expected_length:
            return None
    elif len(rg_only_digits) != expected_length:
        return None

    try:
        return rg_formats[clean_uf]["format"](rg_only_digits)
    except Exception:
        return None
