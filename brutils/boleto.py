def validate(boleto):
    boleto_str = str(boleto)

    if not boleto_str.isdigit():
        return False

    if len(boleto_str) != 47 and len(boleto_str) != 48:
        return False

    return True
