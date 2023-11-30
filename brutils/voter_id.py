def is_valid(voter_id):  # type: (str) -> bool
    """
    Check if a Brazilian voter id number is valid.
    It does not verify if the voter id actually exists.

    References:
    - https://pt.wikipedia.org/wiki/T%C3%ADtulo_de_eleitor,
    - http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-titulo-de-eleitor/

    Args:
        voter_id(str): string representing the voter id to be verified.

    Returns:
        bool: True if the voter id is valid. False otherwise.
    """

    # ensure voter_id only contains numerical characters and has a valid length
    if (
        not isinstance(voter_id, str)
        or not voter_id.isdigit()
        or not _is_length_valid(voter_id)
    ):
        return False

    # the voter id is composed of 3 parts, in this order:
    #   - sequential_number (8 or 9 digits)
    #   - federative_union (2 digits)
    #   - verifying digits (2 digits)
    sequential_number = _get_sequential_number(voter_id)
    federative_union = _get_federative_union(voter_id)
    verifying_digits = _get_verifying_digits(voter_id)

    # ensure federative union is valid
    if not _is_federative_union_valid(federative_union):
        return False

    # ensure the first verifying digit is valid
    vd1 = _calculate_vd1(sequential_number, federative_union)
    if vd1 != int(verifying_digits[0]):
        return False

    # ensure the second verifying digit is valid
    vd2 = _calculate_vd2(federative_union, vd1)
    if vd2 != int(verifying_digits[1]):
        return False

    return True


def _is_length_valid(voter_id):  # type: (str) -> bool
    """
    Check if the length of the provided voter id is valid.
    Typically, the length should be 12, but there are cases for SP and MG where
    the length might be 13. This occurs as an edge case when the sequential
    number has 9 digits instead of 8.

    Args:
        voter_id (str): string representing the voter id to be verified

    Returns:
        bool: True if the length is valid. False otherwise.
    """

    federative_union = _get_federative_union(voter_id)

    if len(voter_id) == 12:
        return True

    # edge case: for SP and MG with 9 digit long 'sequential number'
    return len(voter_id) == 13 and federative_union in ["01", "02"]


def _get_sequential_number(voter_id):  # type: (str) -> str
    """
    Some voter ids in São Paulo and Minas Gerais may have nine digits in their
    sequential number instead of eight. This fact does not compromise the
    calculation of the check digits, as it is done based on the first eight
    sequential numbers.

    Args:
        voter_id (str): string representing the voter id to be verified.

    Returns:
        str: eight-digit string representing the sequential number for the
             given voter id
    """

    return voter_id[:8]


def _get_federative_union(voter_id):  # type: (str) -> str
    """
    Returns the two digits that represent the federative union for the given
    voter id. Indexing it backwards, as the sequential_number can have eight
    or nine digits.

    Args:
        voter_id (str): string representing the voter id to be verified

    Returns:
        str: two-digits string representing the federative union for the given voter id
    """

    return voter_id[-4:-2]


def _get_verifying_digits(voter_id):  # type: (str) -> str
    """
    Returns the two verifying digits for the given voter id. Indexing it
    backwards, as the sequential_number can have eight or nine digits.

    Args:
        voter_id (str): string representing the voter id to be verified

    Returns:
        str: the two verifying digits for the given voter id
    """

    return voter_id[-2:]


def _is_federative_union_valid(federative_union):  # type: (str) -> bool
    """
    Check if the federative union is valid.

    Args:
        federative_union(str): federative union for the given voter id

    Returns:
        bool: True if the federative union is valid. False otherwise.
    """

    # valid federative unions: from '01' to '28'
    return federative_union in ["{:02d}".format(i) for i in range(1, 29)]


def _calculate_vd1(sequential_number, federative_union):  # type: (str, str) -> bool
    """
    Calculate the first verifying digit.

    Args:
        sequential_number(str): sequential number sliced from the voter_id
        federative_union(str): federative union for the given voter id

    Returns:
        int: the expected value for the first verifying digit for the given
             voter id
    """

    # 2, 3, 4, 5, 6, 7, 8, 9
    x1, x2, x3, x4, x5, x6, x7, x8 = range(2, 10)

    sum = (
        (int(sequential_number[0]) * x1)
        + (int(sequential_number[1]) * x2)
        + (int(sequential_number[2]) * x3)
        + (int(sequential_number[3]) * x4)
        + (int(sequential_number[4]) * x5)
        + (int(sequential_number[5]) * x6)
        + (int(sequential_number[6]) * x7)
        + (int(sequential_number[7]) * x8)
    )

    rest = sum % 11
    vd1 = rest

    # edge case: rest == 0 and federative_union is SP or MG
    if rest == 0 and federative_union in ["01", "02"]:
        vd1 = 1

    # edge case: rest == 10, declare vd1 as zero
    if rest == 10:
        vd1 = 0

    return vd1


def _calculate_vd2(federative_union, vd1):  # type: (str, int) -> str
    """
    Calculate the second verifying digit.

    Args:
        federative_union(str): federative union for the given voter id
        vd1(int): first verifying digit calculated for the given voter id

    Returns:
        int: the expected value for the second verifying digit for the given
             voter id
    """

    x9, x10, x11 = 7, 8, 9

    sum = (
        (int(federative_union[0]) * x9)
        + (int(federative_union[1]) * x10)
        + (vd1 * x11)
    )

    rest = sum % 11
    vd2 = rest

    # edge case: if federative_union is "01" or "02" (for SP and MG) AND
    # rest == 0, declare vd2 as 1
    if federative_union in ["01", "02"] and rest == 0:
        vd2 = 1

    return vd2
