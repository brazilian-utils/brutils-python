import unittest
from brutils.titulo_eleitoral import is_valid_titulo_eleitoral


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


if __name__ == "__main__":
    unittest.main()
