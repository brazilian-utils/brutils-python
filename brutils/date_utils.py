from datetime import datetime
from typing import Union

import holidays


def is_holiday(target_date: datetime, uf: str = None) -> Union[bool, None]:
    """
    Checks if the given date is a national or state holiday in Brazil.

    This function takes a date as a `datetime` object and an optional UF (Unidade Federativa),
    returning a boolean value indicating whether the date is a holiday or `None` if the date or
    UF are invalid.

    The method does not handle municipal holidays.

    Args:
        target_date (datetime): The date to be checked.
        uf (str, optional): The state abbreviation (UF) to check for state holidays.
                            If not provided, only national holidays will be considered.

    Returns:
        bool | None: Returns `True` if the date is a holiday, `False` if it is not,
                     or `None` if the date or UF are invalid.

    Note:
        The function logic should be implemented using the `holidays` library.
        For more information, refer to the documentation at: https://pypi.org/project/holidays/

    Usage Examples:
        >>> from datetime import datetime
        >>> is_holiday(datetime(2024, 1, 1))
        True

        >>> is_holiday(datetime(2024, 1, 2))
        False

        >>> is_holiday(datetime(2024, 3, 2), uf="SP")
        False

        >>> is_holiday(datetime(2024, 12, 25), uf="RJ")
        True
    """

    if not isinstance(target_date, datetime):
        return None

    valid_ufs = holidays.Brazil().subdivisions
    if uf is not None and uf not in valid_ufs:
        return None

    national_holidays = holidays.Brazil(years=target_date.year)

    if uf is None:
        return target_date in national_holidays

    state_holidays = holidays.Brazil(prov=uf, years=target_date.year)
    return target_date in state_holidays
