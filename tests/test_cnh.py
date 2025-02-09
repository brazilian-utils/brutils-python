from unittest import TestCase, main

from brutils.cnh import is_valid_cnh


class TestCNH(TestCase):
    def test_is_valid_cnh(self):
        # Testes para CNHs válidas
        self.assertTrue(is_valid_cnh("12345678900"))
        self.assertTrue(is_valid_cnh("123456789012345"))
        self.assertTrue(is_valid_cnh("ABCDE123456789"))
        self.assertTrue(is_valid_cnh("1234567890ABCDE"))
        self.assertTrue(is_valid_cnh("A123B456C789D"))

        # Testes para CNHs inválidas
        self.assertFalse(is_valid_cnh("12345"))
        self.assertFalse(is_valid_cnh("1234567890123456"))
        self.assertFalse(is_valid_cnh("1234-5678"))
        self.assertFalse(is_valid_cnh(""))
        self.assertFalse(is_valid_cnh("1234567890!@#"))
        self.assertFalse(is_valid_cnh("12345678 901"))
        self.assertFalse(is_valid_cnh("ABCD-1234567"))
        self.assertFalse(is_valid_cnh("1234567890_"))


if __name__ == "__main__":
    main()
