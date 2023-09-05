# FORMATTING
############


# OPERATIONS
############


def is_valid_landline(phone_number):  # type: (str) -> bool
    return (
        isinstance(phone_number, str)
        and phone_number.isdigit()
        and len(phone_number) == 10
        and phone_number[0] != "0"
        and phone_number[1] != "0"
        and phone_number[2] in ["2", "3", "4", "5"]
    )


def is_valid_mobile(phone_number):  # type: (str) -> bool
    return (
        isinstance(phone_number, str)
        and phone_number.isdigit()
        and len(phone_number) == 11
        and phone_number[0] != "0"
        and phone_number[1] != "0"
        and phone_number[2] == "9"
    )


def is_valid(phone_number):  # type: (str) -> bool
    return is_valid_landline(phone_number) or is_valid_mobile(phone_number)
