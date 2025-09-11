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
    Returns whether the check digits of the provided CNH match its base number.

    Notes:
    - This function does not query official databases (BINCO/SENATRAN). It only performs
    the arithmetic validation of the check digits (pre-validation).
    - Rejects sequences where all digits are the same.

    Rules (modulo 11 – common practice in Brazilian documents):
    1) Consider the first 9 digits as the base.
    2) First check digit (10th digit):
        sum1 = Σ base[i] * decreasing weight (9..1)
        dv1 = sum1 % 11; if dv1 >= 10 → dv1 = 0
    3) Second check digit (11th digit):
        sum2 = Σ base[i] * increasing weight (1..9) + dv1 * 2
        dv2 = sum2 % 11; if dv2 >= 10 → dv2 = 0

    Args:
        cnh (str | None): CNH string with 11 digits (symbols will be ignored).

    Returns:
        bool: True if the check digits are consistent, False otherwise.
    """
    digits_only = remove_symbols_cnh(cnh)
    if not digits_only or len(digits_only) != 11 or not digits_only.isdigit():
        return False

    # reject sequences like 000..., 111..., etc.
    if digits_only == digits_only[0] * 11:
        return False

    nums = [int(ch) for ch in digits_only]

    # base: first 9 digits
    base = nums[:9]
    dv_expected_1 = nums[9]
    dv_expected_2 = nums[10]

    # first check digit: weights 9..1
    soma1 = sum(d * w for d, w in zip(base, range(9, 0, -1)))
    dv1 = soma1 % 11
    if dv1 >= 10:
        dv1 = 0

    # second check digit: weights 1..9 + dv1*2
    soma2 = sum(d * w for d, w in zip(base, range(1, 10))) + dv1 * 2
    dv2 = soma2 % 11
    if dv2 >= 10:
        dv2 = 0

    return dv1 == dv_expected_1 and dv2 == dv_expected_2
