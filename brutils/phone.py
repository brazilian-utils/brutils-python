# FORMATTING
############


# OPERATIONS
############


def is_valid_landline(phone_number):
    return (
        isinstance(phone_number, str)
        and phone_number.isdigit()
        and len(phone_number) == 10
        and phone_number[0] != "0"
        and phone_number[1] != "0"
        and (
            phone_number[2] == "2"
            or phone_number[2] == "3"
            or phone_number[2] == "4"
            or phone_number[2] == "5"
        )
    )


def is_valid_mobile(phone_number):
    return (
        isinstance(phone_number, str)
        and phone_number.isdigit()
        and len(phone_number) == 11
        and phone_number[0] != "0"
        and phone_number[1] != "0"
        and phone_number[2] == "9"
    )


def is_valid(phone_number):
    return is_valid_landline(phone_number) or is_valid_mobile(phone_number)
