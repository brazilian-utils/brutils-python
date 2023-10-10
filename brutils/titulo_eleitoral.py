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
    tit_sequence, tit_uf, tit_dig_verifiers = _split_string(numero_titulo)

    # verify length
    if not _verify_length(numero_titulo, tit_uf):
        return False
    else:
        lentgh_verified = True

    # list valid UFs
    unidades_federativas = ["{:02d}".format(i) for i in range(1, 29)]

    # calculate dv1
    dv1, verified_dv1 = _calculate_dv1(tit_sequence, tit_uf, tit_dig_verifiers)

    # calculate dv2
    verified_dv2 = _calculate_dv2(tit_uf, dv1, tit_dig_verifiers)

    # verify UF
    verified_uf = _verify_uf(tit_uf, unidades_federativas)

    # return True if all conditions are met, else False
    return all([verified_dv1, verified_dv2, lentgh_verified, verified_uf])


def _split_string(input_string: str):
    """split string into 'numero sequencial', 'unidade federativa' &
    'digitos verificadores'
    here I indexed tit_uf and tit_dig_verifiers from the back due to the
    below reference:
    '- Alguns títulos eleitorais de São Paulo e Minas Gerais podem ter nove
    dígitos em seu número sequencial, em vez de oito. Tal fato não compromete
    o cálculo dos DVs, pois este é feito com base nos oito primeiros números
    sequenciais.'
    http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-titulo-de-eleitor/

    Args:
            input_string[str]: an example of titulo eleitoral brasileiro

    Returns:
        tit_sequence[list]: sequential number sliced from input_string
        tit_uf[list]: Unidade Federal sliced from input_string
        tit_dig_verifiers[list]: DV sliced from input_string
    """
    tit_sequence = input_string[:8]
    tit_uf = input_string[-4:-2]
    tit_dig_verifiers = input_string[-2:]

    return tit_sequence, tit_uf, tit_dig_verifiers


def _verify_length(numero_titulo, tit_uf):
    """
    verify length of numero_titulo
    considers edge case with 13 digits for SP & MG
    Args:
        numero_titulo[str]: an example of titulo eleitoral brasileiro
        tit_uf[list]: Unidade Federal sliced from input_string

    Returns:
        lentgh_verified[bool]: boolean indicating whether length of
        numero_titulo is verified, or not.

    """
    if len(numero_titulo) == 12:
        lentgh_verified = True

    # edge case: for SP & MG with 9 digit long 'numero sequencial'
    elif len(numero_titulo) == 13 and tit_uf in ["01", "02"]:
        lentgh_verified = True
    else:
        lentgh_verified = False

    return lentgh_verified


def _calculate_dv1(tit_sequence, tit_uf, tit_dig_verifiers):
    """calculate dv1
    Args:
        tit_sequence[list]: sequential number sliced from input_string
    Returns:
        v1[list]: list containing the resulting operation to calculate v1
    """
    x1, x2, x3, x4, x5, x6, x7, x8 = range(2, 10)

    v1 = (
        (int(tit_sequence[0]) * x1)
        + (int(tit_sequence[1]) * x2)
        + (int(tit_sequence[2]) * x3)
        + (int(tit_sequence[3]) * x4)
        + (int(tit_sequence[4]) * x5)
        + (int(tit_sequence[5]) * x6)
        + (int(tit_sequence[6]) * x7)
        + (int(tit_sequence[7]) * x8)
    )

    dv1 = v1 % 11
    # edge case: dv1 mod 11 == 0 and UF is SP or MG
    if dv1 == 0 and tit_uf not in ["01", "02"]:
        dv1 = 1

    # edge case: dv1 == 10, declare as zero instead
    if dv1 == 10:
        dv1 = 0

    # verify dv1
    return dv1, int(tit_dig_verifiers[0]) == dv1


def _calculate_dv2(tit_uf, dv1, tit_dig_verifiers):
    """calculate dv2

    Args:
        tit_uf[list]: Unidade Federal sliced from input_string
        dv1[int]: result from v1 mod 11 operation

    Returns:
        dv2[int]: result from v2 mod 11 operation

    """
    x9, x10, x11 = 7, 8, 9
    v2 = (int(tit_uf[0]) * x9) + (int(tit_uf[1]) * x10) + (dv1 * x11)

    dv2 = v2 % 11
    # edge case: if UF is "01" or "02" (for SP & MG) AND dv2 == 0; dv2 = 1
    if tit_uf in ["01", "02"] and dv2 == 0:
        dv2 = 1

    return dv2, int(tit_dig_verifiers[1]) == dv2


def _verify_uf(tit_uf, unidades_federativas):
    """verify UF

    Args:
        tit_uf[list]: Unidade Federal sliced from input_string
        unidades_federativas[list]: list containing all possible UFs
    Returns:
        verified_uf[bool]: boolean indicating whether UF has been verified,
        or not.
    """
    return tit_uf in unidades_federativas
