from typing import TypedDict


class Boleto(TypedDict):
    num_bank: str
    code_coin: str
    first_free_field: str
    second_free_field: str
    verify_digit_first_field: str
    thirty_free_field: str
    verify_digit_second_field: str
    forty_free_field: str
    verify_digit_thirty_field: str
    verify_digit_barcode: str
    maturity_factor: str
    document_value: str
