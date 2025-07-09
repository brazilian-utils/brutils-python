def validate_tin_angola(tin: str) -> bool:
    """
    Valida um TIN (Número de Identificação Fiscal) de Angola.

    Regras:
    - 9 dígitos numéricos.
    - Primeiro dígito em {1,5,6,8}.
    - Dígito verificador (9º) calculado com módulo 11:
      pesos = [9,8,7,6,5,4,3,2].
    """
    # 1) Formato básico
    if not isinstance(tin, str) or not tin.isdigit() or len(tin) != 9:
        return False

    # 2) Primeiro dígito
    if tin[0] not in {"1", "5", "6", "8"}:
        return False

    # 3) Cálculo do dígito verificador
    weights = [9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(d) * w for d, w in zip(tin[:8], weights))
    resto = soma % 11

    dv_calculado = 0 if resto in (0, 1) else 11 - resto
    dv_informado = int(tin[8])

    return dv_calculado == dv_informado
