from datetime import datetime
from unittest import TestCase

from brutils.date_utils import is_holiday


class TestIsHoliday(TestCase):
    def test_feriados_validos(self):
        # Testes com feriados válidos
        self.assertTrue(is_holiday(datetime(2024, 1, 1)))  # Ano Novo
        self.assertTrue(
            is_holiday(datetime(2024, 7, 9), uf="SP")
        )  # Revolução Constitucionalista (SP)
        self.assertTrue(
            is_holiday(datetime(2024, 9, 7))
        )  # Independência do Brasil
        self.assertTrue(is_holiday(datetime(2025, 1, 1)))  # Ano Novo

    def test_dias_normais(self):
        # Testes com dias normais
        self.assertFalse(is_holiday(datetime(2024, 1, 2)))  # Dia normal
        self.assertFalse(
            is_holiday(datetime(2024, 7, 9), uf="RJ")
        )  # Dia normal no RJ

    def test_data_invalida(self):
        # Testes com data inválida
        self.assertIsNone(is_holiday("2024-01-01"))  # Formato incorreto
        self.assertIsNone(is_holiday(None))  # Data None

    def test_uf_invalida(self):
        # Testes com UF inválida
        self.assertIsNone(
            is_holiday(datetime(2024, 1, 1), uf="XX")
        )  # UF inválida
        self.assertIsNone(
            is_holiday(datetime(2024, 1, 1), uf="SS")
        )  # UF inválida

    def test_limite_de_datas(self):
        # Testes com limite de datas
        self.assertTrue(is_holiday(datetime(2024, 12, 25)))  # Natal
        self.assertTrue(
            is_holiday(datetime(2024, 11, 15))
        )  # Proclamação da República

    def test_datas_depois_de_feriados(self):
        # Test data after holidays
        self.assertFalse(is_holiday(datetime(2024, 12, 26)))  # Não é feriado
        self.assertFalse(is_holiday(datetime(2025, 1, 2)))  # Não é feriado

    def test_ano_bissexto(self):
        # Teste ano bissexto
        self.assertFalse(
            is_holiday(datetime(2024, 2, 29))
        )  # Não é feriado, mas data válida
        # Uncomment to test non-leap year invalid date
        # self.assertIsNone(is_holiday(datetime(1900, 2, 29)))  # Ano não bissexto, data inválida

    def test_data_passada_futura(self):
        # Teste de data passada e futura
        self.assertTrue(is_holiday(datetime(2023, 1, 1)))  # Ano anterior
        self.assertTrue(is_holiday(datetime(2150, 12, 25)))  # Ano futuro
        self.assertFalse(
            is_holiday(datetime(2250, 1, 2))
        )  # Dia normal em ano futuro

    def test_data_sem_uf(self):
        # Teste feriado nacional sem UF
        self.assertTrue(
            is_holiday(datetime(2024, 12, 25))
        )  # Natal, feriado nacional
        self.assertFalse(
            is_holiday(datetime(2024, 7, 9))
        )  # Data estadual de SP, sem UF
