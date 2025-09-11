from unittest import TestCase

from brutils.rg import format_rg


class TestRG(TestCase):
    def test_format_rg(self):
        # Testes para RGs válidos
        self.assertEqual(format_rg("12.345.678-9", "SP"), "12.345.678-9")
        self.assertEqual(format_rg("MG-12.345.678", "MG"), "MG-12.345.678")
        self.assertEqual(format_rg("123456789", "RJ"), "12.345.678-9")

        # Testes para RGs parcialmente formatados
        self.assertEqual(format_rg("123.45678-9", "SP"), "12.345.678-9")
        self.assertEqual(format_rg("1.23456789", "SP"), "12.345.678-9")
        self.assertEqual(format_rg("DF12345678", "DF"), "12.345.678-9")

        # Testes para RGs com zeros à esquerda
        self.assertEqual(format_rg("001234567", "SP"), "00.123.456-7")
        self.assertEqual(format_rg("MG-001234567", "MG"), "MG-00.123.456")

        # Testes para RGs inválidos
        self.assertIsNone(format_rg("A12345678", "SP"))  # Letras não permitidas
        self.assertIsNone(format_rg("1234567890", "SP"))  # RG longo demais
        self.assertIsNone(
            format_rg("12.345.678-10", "SP")
        )  # Dígito verificador incorreto

        # Testes para entradas malformadas
        self.assertIsNone(format_rg("", "SP"))  # Entrada vazia
        self.assertIsNone(
            format_rg("12.345.678", "SP")
        )  # Formato incorreto sem dígito verificador
        self.assertIsNone(format_rg("12.345.678-9", "XX"))  # UF inválida
        self.assertIsNone(
            format_rg("12 345 678-9", "SP")
        )  # RG com espaços extras
        self.assertIsNone(
            format_rg("12.34.5678", "SP")
        )  # RG com formato incorreto
