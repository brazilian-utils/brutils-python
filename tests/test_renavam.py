from unittest import TestCase

from brutils.renavam import is_valid_renavam


class TestRENAVAM(TestCase):
    def test_is_valid_renavam(self):
        # Testes para RENAVAM válidos
        self.assertFalse(is_valid_renavam("12345678901"))
        self.assertFalse(is_valid_renavam("09945438645"))
        self.assertFalse(is_valid_renavam("94521237655"))
        self.assertFalse(is_valid_renavam("45403264305"))
        self.assertFalse(is_valid_renavam("45403471665"))
        self.assertFalse(is_valid_renavam("34743721835"))
        self.assertFalse(is_valid_renavam("69277208515"))

        self.assertTrue(is_valid_renavam("12345678900"))
        self.assertTrue(is_valid_renavam("92876838150"))
        self.assertTrue(is_valid_renavam("65720648534"))
        self.assertTrue(is_valid_renavam("63601073019"))
        self.assertTrue(is_valid_renavam("09945438641"))
        self.assertTrue(is_valid_renavam("94521237651"))
        self.assertTrue(is_valid_renavam("45403264308"))
        self.assertTrue(is_valid_renavam("45403471664"))
        self.assertTrue(is_valid_renavam("34743721831"))
        self.assertTrue(is_valid_renavam("69277208510"))

        # Testes para entradas inválidas
        self.assertFalse(is_valid_renavam("1234567890a"))  # Contém letra
        self.assertFalse(is_valid_renavam("12345678 901"))  # Contém espaço
        self.assertFalse(is_valid_renavam("12345678"))  # Menos de 11 dígitos
        self.assertFalse(is_valid_renavam(""))  # String vazia
        self.assertFalse(is_valid_renavam("123456789012"))  # Mais de 11 dígitos
        self.assertFalse(is_valid_renavam("abcdefghijk"))  # Apenas letras
        self.assertFalse(
            is_valid_renavam("12345678901!")
        )  # Contém caractere especial
        self.assertFalse(is_valid_renavam(None))  # Contém caractere especial
