from unittest import TestCase

from brutils.ibge.uf import convert_code_to_uf


class TestUF(TestCase):
    def test_convert_code_to_uf(self):
        # Testes para códigos válidos
        self.assertEqual(convert_code_to_uf("12"), "AC")  # Acre
        self.assertEqual(convert_code_to_uf("33"), "RJ")  # Rio de Janeiro
        self.assertEqual(convert_code_to_uf("31"), "MG")  # Minas Gerais
        self.assertEqual(convert_code_to_uf("52"), "GO")  # Goiás

        # Testes para códigos inválidos
        self.assertIsNone(convert_code_to_uf("99"))  # Código não existe
        self.assertIsNone(convert_code_to_uf("00"))  # Código não existe
        self.assertIsNone(convert_code_to_uf(""))  # Código vazio
        self.assertIsNone(convert_code_to_uf("AB"))  # Código não numérico

        # implementar mais casos de teste aqui se necessário
