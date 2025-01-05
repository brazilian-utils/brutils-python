from brutils.types.boleto import Boleto


def format_boleto(boleto: Boleto) -> str:
    """
     This function takes information from a boleto
     and turns it into a string.

     **Args:**
     boleto (Boleto): A dictionary with boleto information

     **Return:**
     str: A string with the formatted boleto reading code

    **Example:**
     >>> boleto = Boleto(
             num_bank="001",
             code_coin="9",
             first_free_field="0500",
             second_free_field="9",
             verify_digit_first_field="5",
             thirty_free_field="4014481606",
             verify_digit_second_field="9",
             forty_free_field="0680935031",
             verify_digit_thirty_field="4",
             verify_digit_barcode="3",
             maturity_factor="3737",
             document_value="0000000100"
         )
     >>> format_boleto(boleto)
     >>> "00190.50095 40144.816069 06809.350314 3 37370000000100"
    """

    boleto = (
        boleto["num_bank"]
        + boleto["code_coin"]
        + boleto["first_free_field"]
        + boleto["second_free_field"]
        + boleto["verify_digit_first_field"]
        + boleto["thirty_free_field"]
        + boleto["verify_digit_second_field"]
        + boleto["forty_free_field"]
        + boleto["verify_digit_thirty_field"]
        + boleto["verify_digit_barcode"]
        + boleto["maturity_factor"]
        + boleto["document_value"]
    )

    boleto_array = list(boleto)

    first_piece = "".join(boleto_array[:5])
    second_piece = "".join(boleto_array[5:10])
    third_piece = "".join(boleto_array[10:15])
    fourth_piece = "".join(boleto_array[15:21])
    fifth_piece = "".join(boleto_array[21:26])
    sixth_piece = "".join(boleto_array[26:32])
    seventh_piece = "".join(boleto_array[32:33])
    eighth_piece = "".join(boleto_array[33:])

    formatted_boleto = (
        f"{first_piece}.{second_piece} "
        + f"{third_piece}.{fourth_piece} "
        + f"{fifth_piece}.{sixth_piece} "
        + f"{seventh_piece} "
        + f"{eighth_piece}"
    )

    return formatted_boleto
