import re

# FORMATTING
############


def display(legal_process_id):
    """
    Format an adequately formatted numbers-only Legal Process ID number string,
    adding in standard formatting visual aid symbols for display.
    """

    if (
        not legal_process_id.isdigit()
        or len(legal_process_id) != 20
        or len(set(legal_process_id)) == 1
    ):
        return None
    return format_processo_juridico(legal_process_id)


def format_processo_juridico(legal_process_id):  # type: (str) -> (str)
    """
    Format an adequately formatted numbers-only Legal Process ID number,
    Returns a Legal Process ID number formatted with standard visual aid symbols.
    Returns None if Legal Process ID number is invalid.
    """
    if legal_process_id.isdigit() and len(legal_process_id) == 20:
        capture_fields = r"(\d{7})(\d{2})(\d{4})(\d)(\d{2})(\d{4})"
        include_chars = r"\1-\2.\3.\4.\5.\6"
        return re.sub(capture_fields, include_chars, legal_process_id)
    return None
