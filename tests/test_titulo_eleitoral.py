import unittest
from brutils.titulo_eleitoral import (
    is_valid_titulo_eleitoral,
    split_string,
    verify_length,
)


class TestIsValidTituloEleitoral(unittest.TestCase):
    def test_valid_titulo_eleitoral(self):
        # test a valid titulo eleitoral number
        valid_titulo = "217633460930"
        self.assertTrue(is_valid_titulo_eleitoral(valid_titulo))

    def test_invalid_titulo_eleitoral(self):
        # test an invalid titulo eleitoral number (dv1 & UF fail)
        invalid_titulo = "123456789011"
        self.assertFalse(is_valid_titulo_eleitoral(invalid_titulo))

    def test_invalid_length(self):
        # Test an invalid length for titulo eleitoral
        invalid_length_short = "12345678901"
        invalid_length_long = "1234567890123"
        self.assertFalse(is_valid_titulo_eleitoral(invalid_length_short))
        self.assertFalse(is_valid_titulo_eleitoral(invalid_length_long))

    def test_invalid_characters(self):
        # Test titulo eleitoral with non-numeric characters
        invalid_characters = "ABCD56789012"
        invalid_characters_space = "217633 460 930"
        self.assertFalse(is_valid_titulo_eleitoral(invalid_characters))
        self.assertFalse(is_valid_titulo_eleitoral(invalid_characters_space))

    def test_valid_special_case(self):
        # Test a valid edge case (SP & MG with 13 digits)
        valid_special = "1234567890191"
        self.assertTrue(is_valid_titulo_eleitoral(valid_special))


class TestSplitString(unittest.TestCase):
    def test_split_string(self):
        input_string = "12345678AB12"
        tit_sequence, tit_unid_fed, tit_dig_verifiers = split_string(
            input_string
        )
        self.assertEqual(tit_sequence, "12345678")
        self.assertEqual(tit_unid_fed, "AB")
        self.assertEqual(tit_dig_verifiers, "12")


class TestVerifyLength(unittest.TestCase):
    def test_valid_length(self):
        numero_titulo = "123456789012"
        tit_unid_fed = "AB"
        self.assertTrue(verify_length(numero_titulo, tit_unid_fed))

    def test_invalid_length(self):
        numero_titulo = "12345678AB123"  # Invalid length
        tit_unid_fed = "AB"
        self.assertFalse(verify_length(numero_titulo, tit_unid_fed))


if __name__ == "__main__":
    unittest.main()
