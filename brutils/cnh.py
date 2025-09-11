from __future__ import annotations

import re
from typing import Final

__all__ = ["is_valid_cnh", "remove_symbols_cnh"]

_DIGITS_RE: Final = re.compile(r"\D+")


def remove_symbols_cnh(cnh: str | None) -> str | None:
    """
    Removes any character that is not a digit from a CNH.

    Args:
        cnh (str | None): String containing the CNH with or without symbols.

    Returns:
        str | None: The CNH containing only digits, or None if the input is invalid.
    """
    if not isinstance(cnh, str):
        return None
    return _DIGITS_RE.sub("", cnh)


def is_valid_cnh(cnh: str | None) -> bool:
    """
    Check if a CNH number is valid by format rules:
    - Must be a non-empty string with exactly 11 digits.
    - Cannot be a sequence of the same digit (e.g., '00000000', '11111111').

    Note:
        This does NOT query bases oficiais (Detran/Senatran) nem valida dígitos verificadores,
        serve apenas como pré-validação de formato e repetição.

    Args:
        cnh (str | None): CNH string (symbols will be ignored).

    Returns:
        bool: True if CNH has 11 numeric digits and is not all the same digit.
    """
    if not cnh:
        return False

    digits_only = "".join(ch for ch in cnh if ch.isdigit())

    if len(digits_only) != 11:
        return False

    # Reject sequences as "00000000000", "11111111111", etc.
    if digits_only == digits_only[0] * 11:
        return False

    return True
