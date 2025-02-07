def format_boleto(boleto: str) -> str:
    """
    Formatar um número de boleto bancário em sua versão legível.
    Retorna None para entradas inválidas
    """
    if not isinstance(boleto, str) or not boleto.isdigit() or len(boleto) != 44:
        return None

    return (
        f"{boleto[:5]}.{boleto[5:10]} "
        f"{boleto[10:15]}.{boleto[15:21]} "
        f"{boleto[21:26]}.{boleto[26:32]} "
        f"{boleto[32]} {boleto[33:]}"
    )
