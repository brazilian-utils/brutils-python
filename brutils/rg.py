import re


def is_valid_rg(rg: str, uf: str) -> bool:
    """
    Validates a Brazilian RG (Registro Geral) based on the state (UF).

    This function checks whether a given RG is valid for a specific state in Brazil.
    Each state may have its own RG format, and the function should handle these differences.

    Additionally, for RGs issued by various states, the function verifies the mathematical rule
    for the check digit where applicable.

    Args:
        rg (str): The RG to be validated.
        uf (str): The state (UF) for which the RG should be validated.

    Returns:
        bool: Returns True if the RG is valid, or False if it is invalid.

    Example:
        >>> is_valid_rg('12.345.678-9', 'SP')
        True
        >>> is_valid_rg('MG-12.345.678', 'MG')
        True
        >>> is_valid_rg('123456789', 'RJ')
        False
        >>> is_valid_rg('A12345678', 'SP')
        False
        >>> is_valid_rg('12.345.678', 'SP')
        False
    """
    # Se rg ou uf forem None, retorna False
    if rg is None or uf is None:
        return False

    # Remove caracteres indesejados (mantém dígitos, letras, pontos e hífens)
    rg_cleaned = re.sub(r"[^0-9A-Za-z.-]", "", rg)

    # Definição de padrões comuns para RG
    common_patterns = {
        "9_digits": r"^\d{9}$",  # Ex.: '123456789'
        "8_digits_dash": r"^\d{8}-\d$",  # Ex.: '12345678-9'
        "7_10_digits": r"^\d{1,2}\.\d{3}\.\d{3}$",  # Ex.: '1.234.567' ou '12.345.678'
        "3_groups": r"^\d{3}\.\d{3}\.\d{3}$",  # Ex.: '123.456.789'
        "3_groups_dash": r"^\d{2}\.\d{3}\.\d{3}-[0-9X]$",  # Ex.: '12.345.678-9' ou com 'X' no dígito verificador
        "2_groups_dash": r"^\d{2}\.\d{3}\.\d{3}$",  # Ex.: '12.345.678'
        "2_3_groups_dash": r"^\d{2}\.\d{3}\.\d{3}-\d$",  # Ex.: '12.345.678-9'
        "mg_format": r"^MG-\d{2}\.\d{3}\.\d{3}$",  # Ex.: 'MG-12.345.678'
    }

    # Mapeamento dos padrões de RG para cada UF
    rg_patterns = {
        # Norte
        "AC": common_patterns["2_3_groups_dash"],
        "AP": common_patterns["2_3_groups_dash"],
        "AM": common_patterns["2_3_groups_dash"],
        "PA": common_patterns["2_3_groups_dash"],
        "RO": common_patterns["2_3_groups_dash"],
        "RR": common_patterns["2_3_groups_dash"],
        "TO": common_patterns["2_3_groups_dash"],
        # Nordeste
        "AL": common_patterns["2_3_groups_dash"],
        "BA": common_patterns["8_digits_dash"],
        "CE": common_patterns["2_3_groups_dash"],
        "MA": common_patterns["2_3_groups_dash"],
        "PB": common_patterns["9_digits"],
        "PE": common_patterns["2_3_groups_dash"],
        "PI": common_patterns["2_3_groups_dash"],
        "RN": common_patterns["2_3_groups_dash"],
        "SE": common_patterns["9_digits"],
        # Centro-Oeste
        "DF": common_patterns["2_3_groups_dash"],
        "GO": common_patterns["2_3_groups_dash"],
        "MT": common_patterns["2_3_groups_dash"],
        "MS": common_patterns["2_3_groups_dash"],
        # Sudeste
        "ES": common_patterns["2_3_groups_dash"],
        "MG": common_patterns["mg_format"],
        # Para RJ, aceita RG composto por 9 dígitos sem formatação
        "RJ": common_patterns["9_digits"],
        "SP": common_patterns["3_groups_dash"],
        # Sul
        "PR": common_patterns["3_groups_dash"],
        "RS": common_patterns["7_10_digits"],
        "SC": common_patterns["3_groups"],
    }

    # Se a UF não estiver mapeada, retorna False
    if uf not in rg_patterns:
        return False

    # Verifica se o RG corresponde ao padrão esperado para a UF
    if not re.match(rg_patterns[uf], rg_cleaned):
        return False

    # Validação do dígito verificador apenas para São Paulo (SP)
    if uf == "SP":
        # Formato esperado: "12.345.678-9"
        parts = rg_cleaned.split("-")
        if len(parts) != 2:
            return False
        # Remove quaisquer caracteres não numéricos da parte principal
        main = re.sub(r"\D", "", parts[0])
        check_digit = parts[1]
        # O número principal deve ter exatamente 8 dígitos
        if len(main) != 8:
            return False
        # Cálculo: multiplica cada dígito pelos pesos [2, 3, 4, 5, 6, 7, 8, 9]
        total = sum(int(d) * w for d, w in zip(main, [2, 3, 4, 5, 6, 7, 8, 9]))
        remainder = total % 11
        expected = "X" if remainder == 10 else str(remainder)
        if check_digit != expected:
            return False

    return True
