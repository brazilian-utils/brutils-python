from unittest import TestCase

from brutils.ibge.uf import convert_code_to_uf, convert_uf_to_name


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

    def test_convert_uf_to_name(self):
        # Testes para códigos válidos
        self.assertEqual(convert_uf_to_name("SP"), "São Paulo")
        self.assertEqual(convert_uf_to_name("RJ"), "Rio de Janeiro")
        self.assertEqual(convert_uf_to_name("MG"), "Minas Gerais")
        self.assertEqual(convert_uf_to_name("DF"), "Distrito Federal")
        self.assertEqual(convert_uf_to_name("df"), "Distrito Federal")

        # Testes para códigos inválidos
        self.assertIsNone(convert_code_to_uf("XX"))
        self.assertIsNone(convert_code_to_uf(""))
