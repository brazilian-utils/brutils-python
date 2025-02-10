import re

def is_valid_rg(rg: str, uf: str) -> bool:
    """
    Validates a Brazilian RG (Registro Geral) based on the state (UF).

    This function checks whether a given RG is valid for a specific state in Brazil.
    Each state may have its own RG format, and this function handles these differences.
    
    Args:
        rg (str): The RG number to be validated.
        uf (str): The state (UF) where the RG was issued.

    Returns:
        bool: Returns True if the RG is valid, False otherwise.

    Example:
        >>> is_valid_rg("12.345.678-9", "SP")
        True
        >>> is_valid_rg("MG-12.345.678", "MG")
        True
        >>> is_valid_rg("12345678-9", "RJ")
        False
        >>> is_valid_rg("A12345678", "SP")
        False
        >>> is_valid_rg("12.345.678", "SP")
        False
    """
    if not isinstance(rg, str) or not isinstance(uf, str):
        return False
    
    uf = uf.upper()
    rg = re.sub(r'[^0-9A-Za-z]', '', rg)  # Remove special characters
    
    uf_rg_formats = {
        "AC": r"^\d{2}\.?\d{3}\.?\d{3}-?[0-9Xx]$",
        "AL": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "AP": r"^\d{9}$",
        "AM": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "BA": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "CE": r"^\d{2}\.?\d{3}\.?\d{3}-?[0-9Xx]$",
        "DF": r"^\d{7}$",
        "ES": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "GO": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "MA": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "MT": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "MS": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "MG": r"^MG-\d{2}\.?\d{3}\.?\d{3}$",
        "PA": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "PB": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "PR": r"^\d{2}\.?\d{3}\.?\d{3}-?[0-9Xx]$",
        "PE": r"^\d{9}$",
        "PI": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "RJ": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "RN": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "RS": r"^\d{1,2}\.\d{3}\.\d{3}$",
        "RO": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "RR": r"^\d{9}$",
        "SC": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "SP": r"^\d{2}\.?\d{3}\.?\d{3}-?[0-9Xx]$",
        "SE": r"^\d{2}\.?\d{3}\.?\d{3}$",
        "TO": r"^\d{2}\.?\d{3}\.?\d{3}$",
    }
    
    if uf not in uf_rg_formats:
        return False  # Invalid or unsupported UF
    
    if not re.match(uf_rg_formats[uf], rg):
        return False  # Invalid format for the UF
    
    if len(set(rg)) == 1:
        return False  # Avoid repetitive sequences (e.g., 111111111)
    
    return True
