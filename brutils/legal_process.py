import re

from random import randint
from datetime import datetime

from brutils.assets.legal_process_ids import legal_process_ids


# FORMATTING
############


def format_processo_juridico(legal_process_id):  # type: (str) -> (str)
    """
    Format an adequately formatted numbers-only Legal Process ID number,
    Returns a Legal Process ID number formatted with standard visual aid
    symbols.
    Returns None if Legal Process ID number is invalid.
    """
    if legal_process_id.isdigit() and len(legal_process_id) == 20:
        capture_fields = r"(\d{7})(\d{2})(\d{4})(\d)(\d{2})(\d{4})"
        include_chars = r"\1-\2.\3.\4.\5.\6"
        return re.sub(capture_fields, include_chars, legal_process_id)
    return None


def remove_symbols(processo_juridico: str):  # type: (str) -> str
    """Removes common symbols from a legal process number string.
    The standard symbols removed are "." and "-"

    Args:
                    process_juridico[str]: A legal process number string
    Returns:
                    [str]: A legal process number string without symbols
    """
    return processo_juridico.replace(".", "").replace("-", "")


def generate_processo_juridico(
    ano=datetime.now().year, orgao=randint(1, 9)
):  # type: (int, int) -> (str)
    """
    Generates a random valid number of a Legal Process ID number.
    """
    if ano < datetime.now().year or orgao not in range(1, 9):
        return None

    J = orgao
    _ = legal_process_ids[f"orgao_{J}"]
    TR = str(_["id_tribunal"][randint(0, (len(_["id_tribunal"]) - 1))]).zfill(2)
    OOOO = str(_["id_foro"][randint(0, (len(_["id_foro"])) - 1)]).zfill(4)
    NNNNNNN = randint(0, 9999999)
    DD = _checksum(f"{NNNNNNN}{ano}{J}{TR}{OOOO}")
    return f"{NNNNNNN}{DD}{ano}{J}{TR}{OOOO}"


def _checksum(basenum):  # type: (int) -> str
    """
    Checksum to compute the verification digit for a Legal Process ID number.
    `basenum` needs to be a digit without the verification id.
    """
    return str(97 - ((int(basenum) * 100) % 97)).zfill(2)
