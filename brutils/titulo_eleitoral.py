from random import randint


WEIGHTS = [2, 3, 4, 5, 6, 7, 8, 9]
UFs = {
    "SP": "01",
    "MG": "02",
    "RJ": "03",
    "RS": "04",
    "BA": "05",
    "PR": "06",
    "CE": "07",
    "PE": "08",
    "SC": "09",
    "GO": "10",
    "MA": "11",
    "PB": "12",
    "PA": "13",
    "ES": "14",
    "PI": "15",
    "RN": "16",
    "AL": "17",
    "MT": "18",
    "MS": "19",
    "DF": "20",
    "SE": "21",
    "AM": "22",
    "RO": "23",
    "AC": "24",
    "AP": "25",
    "RR": "26",
    "TO": "27",
}


def generate_titulo_eleitoral(state="") -> str:
    """
    Generates a random valid Brazilian voter registration.

    Args:
        Federative unit[str]

    Returns:
        value[str]: Brazilian voter registration.
    """

    state = state.upper()
    if state in (UFs):
        base = str(randint(0, 99999999)).zfill(8)
        base_digits = list(map(int, base))
        base_sum_d1 = sum(
            digit * weight for digit, weight in zip(base_digits, WEIGHTS)
        )
        d1 = base_sum_d1 % 11 


        ufs = list(map(int, UFs[state] + str(d1)))
        base_sum_d2 = sum(uf * weight for uf, weight in zip(ufs, WEIGHTS[5:]))
        d2 = base_sum_d2 % 11
        
        if _verify_dv1(d1, UFs[state], list(str(d1) + str(d2)))[0] == True:
            d1
        else:
            d1 = _verify_dv1(d1, UFs[state], list(str(d1) + str(d2)))[1]
            d1
      
        if _verify_dv2(UFs[state], d1, list(str(d1) + str(d2)))[0] == True:
            d2
        else: 
            d2 = _verify_dv2(UFs[state], d1, list(str(d1) + str(d2)))[1]
            d2
            
        return f"{base}{UFs[state]}{d1}{d2}"
    
    elif state == "":
        base = str(randint(0, 99999999)).zfill(8)
        base_digits = list(map(int, base))
        base_sum_d1 = sum(
            digit * weight for digit, weight in zip(base_digits, WEIGHTS)
        )
        d1 = base_sum_d1 % 11
        
        foreigners = list(map(int, (str(28) + str(d1))))
        base_sum_d2 = sum(
            foreigner * weight
            for foreigner, weight in zip(foreigners, WEIGHTS[5:])
        )
        d2 = base_sum_d2 % 11
        
        if _verify_dv1(d1, "28", list(str(d1) + str(d2)))[0] == True:
            d1
        else:
            d1 = _verify_dv1(d1, "28", list(str(d1) + str(d2)))[1]
            d1
      
        if _verify_dv2("28", d1, list(str(d1) + str(d2)))[0] == True:
            d2
        else: 
            d2 = _verify_dv2("28", d1, list(str(d1) + str(d2)))[1]
            d2
            
        return f"{base}{28}{d1}{d2}"
     


def is_valid_titulo_eleitoral(numero_titulo: str):
    """
    Return True when 'numero_titulo' is a valid titulo eleitoral
    brasileiro, False otherwise.
    Input should be a string of proper length. Some specific positional
    characters need to adeher to certain conditions in order to be validated.
    References: https://pt.wikipedia.org/wiki/T%C3%ADtulo_de_eleitor,
    http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-titulo-de-eleitor/

    Args:
        numero_titulo[str]: string representing the titulo
        eleitoral to be verified

    Returns:
        bool[bool]: boolean indicating whether the given numero_titulo
        is a valid string conforming with the titulo eleitoral build rules
    """

    # ensure 'numero_titulo' only contains numerical characters
    if not isinstance(numero_titulo, str) or not numero_titulo.isdigit():
        return False

    # split string into 'numero sequencial', 'unidade federativa' &
    # 'digitos verificadores'
    # edge case: 13-digit length mitigates here. The 9th sequential
    # digit is not used for calculations.
    sequential_number, uf, dig_verifiers = _get_titulo_eleitoral_parts(
        numero_titulo
    )

    # verify length
    if not _verify_length(numero_titulo, uf):
        return False

    # calculate dv1
    dv1 = _calculate_dv1(sequential_number)

    verified_dv1 = _verify_dv1(dv1, uf, dig_verifiers)

    # calculate dv2
    verified_dv2 = _verify_dv2(uf, dv1, dig_verifiers)

    # verify UF
    verified_uf = _verify_uf(uf)

    # return True if all conditions are met, else False
    return all([verified_dv1, verified_dv2, verified_uf])


def _get_titulo_eleitoral_parts(input_string: str):
    """split string into 'numero sequencial', 'unidade federativa' &
    'digitos verificadores'
    here I indexed uf and dig_verifiers from the back due to the
    below reference:
    '- Alguns títulos eleitorais de São Paulo e Minas Gerais podem ter nove
    dígitos em seu número sequencial, em vez de oito. Tal fato não compromete
    o cálculo dos DVs, pois este é feito com base nos oito primeiros números
    sequenciais.'
    http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-titulo-de-eleitor/

    Args:
        input_string[str]: an example of titulo eleitoral brasileiro

    Returns:
        sequential_number[list]: sequential number sliced from input_string
        uf[list]: Unidade Federal sliced from input_string
        dig_verifiers[list]: DV sliced from input_string
    """
    sequential_number = input_string[:8]
    uf = input_string[-4:-2]
    dig_verifiers = input_string[-2:]

    return sequential_number, uf, dig_verifiers


def _verify_length(numero_titulo, uf):
    """
    verify length of numero_titulo
    considers edge case with 13 digits for SP & MG
    Args:
        numero_titulo[str]: an example of titulo eleitoral brasileiro
        uf[list]: Unidade Federal sliced from input_string

    Returns:
        length_verified[bool]: boolean indicating whether the length of
        numero_titulo is verified, or not.

    """
    if len(numero_titulo) == 12:
        return True

    # edge case: for SP & MG with 9 digit long 'numero sequencial'
    return len(numero_titulo) == 13 and uf in ["01", "02"]


def _calculate_dv1(sequential_number):
    """calculate dv1
    Args:
        sequential_number[list]: sequential number sliced from input_string
    Returns:
        v1[list]: list containing the resulting operation to calculate v1
    """
    x1, x2, x3, x4, x5, x6, x7, x8 = range(2, 10)

    v1 = (
        (int(sequential_number[0]) * x1)
        + (int(sequential_number[1]) * x2)
        + (int(sequential_number[2]) * x3)
        + (int(sequential_number[3]) * x4)
        + (int(sequential_number[4]) * x5)
        + (int(sequential_number[5]) * x6)
        + (int(sequential_number[6]) * x7)
        + (int(sequential_number[7]) * x8)
    )

    dv1 = v1 % 11

    return dv1


def _verify_dv1(dv1, uf, dig_verifiers):
    """verify dv1

    Args:
        dv1[int]: calculated digito verificador 1
        uf[list]: UF slice of the given titulo eleitoral
        dig_verifiers[list]: DV sliced from the given
        titulo eleitoral string
    Returns:
        bool[bool]: boolean indicating whether dv1 has been
        verified or not.
    """
    # edge case: dv1 mod 11 == 0 and UF is SP or MG
    if dv1 == 0 and uf in ["01", "02"]:
        dv1 = 1

    # edge case: dv1 == 10, declare as zero instead
    if dv1 == 10:
        dv1 = 0

    # verify dv1
    return int(dig_verifiers[0]) == dv1, dv1


def _verify_dv2(uf, dv1, dig_verifiers):
    """calculate dv2

    Args:
        uf[list]: Unidade Federal sliced from input_string
        dv1[int]: result from v1 mod 11 operation
        dig_verifiers[str]: Digits verifiers from titulo eleitoral

    Returns:
        dv2[int]: result from v2 mod 11 operation

    """
    x9, x10, x11 = 7, 8, 9
    v2 = (int(uf[0]) * x9) + (int(uf[1]) * x10) + (dv1 * x11)

    dv2 = v2 % 11
    # edge case: if UF is "01" or "02" (for SP & MG) AND dv2 == 0
    # declare dv2 as 1 instead
    if uf in ["01", "02"] and dv2 == 0:
        dv2 = 1

    # edge case: dv2 == 10, declare as zero instead  
    if dv2 == 10:
        dv2 = 0

    return int(dig_verifiers[1]) == dv2, dv2


def _verify_uf(uf):
    """verify UF

    Args:
        uf[list]: Unidade Federal sliced from input_string
    Returns:
        verified_uf[bool]: boolean indicating whether UF has been verified,
        or not.
    """

    return uf in ["{:02d}".format(i) for i in range(1, 29)]
