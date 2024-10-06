from unittest import TestCase

from brutils.ibge.uf import convert_uf_to_text


class TestUF(TestCase):
    def test_convert_uf_to_text(self):
        # Testes para códigos válidos
        self.assertEqual(convert_uf_to_text("SP"), "São Paulo")
        self.assertEqual(convert_uf_to_text("RJ"), "Rio de Janeiro")
        self.assertEqual(convert_uf_to_text("MG"), "Minas Gerais")
        self.assertEqual(convert_uf_to_text("DF"), "Distrito Federal")
        self.assertEqual(convert_uf_to_text("df"), "Distrito Federal")

        # Testes para códigos inválidos
        self.assertIsNone(convert_uf_to_text("XX"))  # Código não existe
        self.assertIsNone(convert_uf_to_text(""))  # Código vazio

        # Implementar mais casos de teste aqui
        # Testes com espaços em branco
        self.assertIsNone(convert_uf_to_text(" SP "))  # UF com espaços ao redor
        self.assertIsNone(convert_uf_to_text(" "))  # Apenas espaços
        self.assertIsNone(convert_uf_to_text("S"))  # Apenas 1 letra
        self.assertIsNone(convert_uf_to_text("SPX"))  # Mais de 2 letras
