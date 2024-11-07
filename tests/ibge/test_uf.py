from unittest import TestCase

from brutils.ibge.uf import convert_code_to_uf, convert_text_to_uf


class TestUF(TestCase):
    def test_convert_code_to_uf(self):
        # Testes para códigos válidos
        self.assertEqual(convert_code_to_uf("12"), "AC")
        self.assertEqual(convert_code_to_uf("33"), "RJ")
        self.assertEqual(convert_code_to_uf("31"), "MG")
        self.assertEqual(convert_code_to_uf("52"), "GO")

        # Testes para códigos inválidos
        self.assertIsNone(convert_code_to_uf("99"))
        self.assertIsNone(convert_code_to_uf("00"))
        self.assertIsNone(convert_code_to_uf(""))
        self.assertIsNone(convert_code_to_uf("AB"))

    def test_convert_text_to_uf(self):
        # Testes para nomes válidos
        self.assertEqual(convert_text_to_uf("São Paulo"), "SP")
        self.assertEqual(convert_text_to_uf("Rio de Janeiro"), "RJ")
        self.assertEqual(convert_text_to_uf("Minas Gerais"), "MG")
        self.assertEqual(convert_text_to_uf("Distrito Federal"), "DF")
        self.assertEqual(
            convert_text_to_uf("são paulo"), "SP"
        )  # Teste com minúsculas
        self.assertEqual(
            convert_text_to_uf("riO de janeiRo"), "RJ"
        )  # Teste com misturas de maiúsculas e minúsculas
        self.assertEqual(
            convert_text_to_uf("minas gerais"), "MG"
        )  # Teste com minúsculas
        self.assertEqual(
            convert_text_to_uf("sao paulo"), "SP"
        )  # Teste sem acento

        # Testes para nomes inválidos
        self.assertIsNone(
            convert_text_to_uf("Estado Inexistente")
        )  # Nome não existe
        self.assertIsNone(convert_text_to_uf(""))  # Nome vazio
        self.assertIsNone(convert_text_to_uf("123"))  # Nome com números
        self.assertIsNone(
            convert_text_to_uf("São Paulo SP")
        )  # Nome com sigla incluída
        self.assertIsNone(convert_text_to_uf("A"))  # Nome com letra não mapeada
        self.assertIsNone(
            convert_text_to_uf("ZZZ")
        )  # Nome com mais de 2 letras
