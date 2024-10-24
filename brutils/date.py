import re
from typing import Union

from num2words import num2words

from brutils.data.enums.months import MonthsEnum


def convert_date_to_text(date: str) -> Union[str, None]:
    """
    Converts a given date in Brazilian format (dd/mm/yyyy) to its textual representation.

    This function takes a date as a string in the format dd/mm/yyyy and converts it
    to a string with the date written out in Brazilian Portuguese, including the full
    month name and the year.

    Args:
        date (str): The date to be converted into text. Expected format: dd/mm/yyyy.

    Returns:
        str or None: A string with the date written out in Brazilian Portuguese,
        or None if the date is invalid.

    """
    pattern = re.compile(r"\d{2}/\d{2}/\d{4}")
    if not re.match(pattern, date):
        raise ValueError(
            "Date is not a valid date. Please pass a date in the format dd/mm/yyyy."
        )

    day_str, month_str, year_str = date.split("/")
    day = int(day_str)
    month = int(month_str)
    year = int(year_str)

    if 0 <= day > 31:
        return None

    if not MonthsEnum.is_valid_month(month):
        return None

    # Leap year.
    if MonthsEnum(int(month)) is MonthsEnum.FEVEREIRO:
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or (
            int(year) % 400 == 0
        ):
            if day > 29:
                return None
        else:
            if day > 28:
                return None

    day_string = "Primeiro" if day == 1 else num2words(day, lang="pt")
    month = MonthsEnum(month)
    year_string = num2words(year, lang="pt")

    date_string = (
        day_string.capitalize()
        + " de "
        + month.month_name
        + " de "
        + year_string
    )
    return date_string
