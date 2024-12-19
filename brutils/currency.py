from decimal import Decimal, InvalidOperation


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
