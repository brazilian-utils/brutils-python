from unittest import TestCase

from brutils.boleto import format_boleto
from brutils.types.boleto import Boleto


class TestBoleto(TestCase):
    def test_format_boleto(self):
        boleto = Boleto(
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
            document_value="0000000100",
        )

        formatted_boleto = format_boleto(boleto)

        expected_boleto = (
            "00190.50095 40144.816069 06809.350314 3 37370000000100"
        )

        self.assertEqual(
            formatted_boleto,
            expected_boleto,
            f"Teste falhou! Esperado: {expected_boleto}, Obtido: {formatted_boleto}",
        )
