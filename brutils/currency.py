from decimal import ROUND_DOWN, Decimal, InvalidOperation
from typing import Union

from num2words import num2words


def format_currency(value):  # type: (float) -> str | None
    """
    Formats a given float as Brazilian currency (R$).

    This function takes a float value and returns a formatted string representing
    the value as Brazilian currency, using the correct thousand and decimal separators.

    Args:
        value (float or Decimal): The numeric value to be formatted.

    Returns:
        str or None: A string formatted as Brazilian currency, or None if the input is invalid.

    Example:
        >>> format_currency(1234.56)
        "R$ 1.234,56"
        >>> format_currency(0)
        "R$ 0,00"
        >>> format_currency(-9876.54)
        "R$ -9.876,54"
        >>> format_currency(None)
        None
        >>> format_currency("not a number")
        None
    """

    try:
        decimal_value = Decimal(value)
        formatted_value = (
            f"R$ {decimal_value:,.2f}".replace(",", "_")
            .replace(".", ",")
            .replace("_", ".")
        )

        return formatted_value
    except InvalidOperation:
        return None


def convert_real_to_text(amount: Decimal) -> Union[str, None]:
    """
    Converts a given monetary value in Brazilian Reais to its textual representation.

    This function takes a decimal number representing a monetary value in Reais
    and converts it to a string with the amount written out in Brazilian Portuguese. It
    handles both the integer part (Reais) and the fractional part (centavos), respecting
    the correct grammar for singular and plural cases, as well as special cases like zero
    and negative values.

    Args:
        amount (decimal): The monetary value to be converted into text.
            - The integer part represents Reais.
            - The decimal part represents centavos.
            - 2 decimal places

    Returns:
        str: A string with the monetary value written out in Brazilian Portuguese.
            - Returns "Zero reais" for a value of 0.00.
            - Returns None if the amount is invalid or absolutely greater than 1 trillion.
            - Handles negative values, adding "Menos" at the beginning of the string.

    Example:
        >>> convert_real_to_text(1523.45)
        "Mil, quinhentos e vinte e três reais e quarenta e cinco centavos"
        >>> convert_real_to_text(1.00)
        "Um real"
        >>> convert_real_to_text(0.50)
        "Cinquenta centavos"
        >>> convert_real_to_text(0.00)
        "Zero reais"
        >>> convert_real_to_text(-50.25)
        "Menos cinquenta reais e vinte e cinco centavos"
    """

    try:
        amount = Decimal(str(amount)).quantize(
            Decimal("0.01"), rounding=ROUND_DOWN
        )
    except InvalidOperation:
        return None

    if amount.is_nan() or amount.is_infinite():
        return None

    if abs(amount) >= Decimal("1000000000000000.00"):  # 1 quadrillion
        return None

    negative = amount < 0
    amount = abs(amount)

    reais = int(amount)
    centavos = int((amount - reais) * 100)

    parts = []

    if reais > 0:
        """"
        Note:
        Although the `num2words` library provides a "to='currency'" feature, it has known
        issues with the representation of "zero reais" and "zero centavos". Therefore, this
        implementation uses only the traditional number-to-text conversion for better accuracy.
        """
        reais_text = num2words(reais, lang="pt_BR")
        currency_text = "real" if reais == 1 else "reais"
        conector = "de " if reais_text.endswith(("lhão", "lhões")) else ""
        parts.append(f"{reais_text} {conector}{currency_text}")

    if centavos > 0:
        centavos_text = f"{num2words(centavos, lang='pt_BR')} {'centavo' if centavos == 1 else 'centavos'}"
        if reais > 0:
            parts.append(f"e {centavos_text}")
        else:
            parts.append(centavos_text)

    if reais == 0 and centavos == 0:
        parts.append("Zero reais")

    result = " ".join(parts)
    if negative:
        result = f"Menos {result}"

    return result.capitalize()
