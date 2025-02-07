from unittest import TestCase, main

from brutils.boleto import format_boleto


class TestFormatBoleto(TestCase):
    def test_boleto_curto(self):
        self.assertIsNone(format_boleto("12345678"))

    def test_boleto_com_letras(self):
        self.assertIsNone(
            format_boleto("1234A678901234567890123456789012345678901234")
        )


if __name__ == "__main__":
    main()
