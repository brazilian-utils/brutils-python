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
        if d1 == 0 and state in ["SP", "MG"]:
            d1 = 1
        if d1 == 10:
            d1 = 0
        else:
            d1

        ufs = list(map(int, UFs[state] + str(d1)))
        base_sum_d2 = sum(uf * weight for uf, weight in zip(ufs, WEIGHTS[5:]))
        d2 = base_sum_d2 % 11
        if d2 == 0 and state in ["SP", "MG"]:
            d2 = 1
            titulo = f"{base}{UFs[state]}{d1}{d2}"
            return titulo
        if d2 == 10:
            d2 = 0
            return f"{base}{UFs[state]}{d1}{d2}"
        else:
            d2
            titulo = f"{base}{UFs[state]}{d1}{d2}"
            return titulo
    else:
        base = str(randint(0, 99999999)).zfill(8)
        base_digits = list(map(int, base))
        base_sum_d1 = sum(
            digit * weight for digit, weight in zip(base_digits, WEIGHTS)
        )
        d1 = base_sum_d1 % 11
        if d1 == 10:
            d1 = 0
        else:
            d1
        foreigners = list(map(int, (str(28) + str(d1))))
        base_sum_d2 = sum(
            foreigner * weight
            for foreigner, weight in zip(foreigners, WEIGHTS[5:])
        )
        d2 = base_sum_d2 % 11
        if d2 == 10:
            d2 = 0
            titulo = f"{base}{28}{d1}{d2}"
            return titulo
        else:
            d2
            titulo = f"{base}{28}{d1}{d2}"
            return titulo
