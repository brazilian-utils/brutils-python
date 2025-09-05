from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

from brutils.date_utils import is_holiday


class TestIsHoliday(TestCase):
    @patch("brutils.date_utils.is_holiday")
    def test_feriados_validos(self, mock_is_holiday):
        # Testes com feriados válidos
        mock_is_holiday.return_value = True
        self.assertTrue(is_holiday(datetime(2024, 1, 1)))  # Ano Novo
        self.assertTrue(is_holiday(datetime(2024, 7, 9), uf="SP"))  # Revolução Constitucionalista (SP)
        self.assertTrue(is_holiday(datetime(2024, 9, 7)))  # Independência do Brasil
        self.assertTrue(is_holiday(datetime(2025, 1, 1)))  # Ano Novo

    @patch("brutils.date_utils.is_holiday")
    def test_dias_normais(self, mock_is_holiday):
        # Testes com dias normais
        mock_is_holiday.return_value = False
        self.assertFalse(is_holiday(datetime(2024, 1, 2)))  # Dia normal
        self.assertFalse(is_holiday(datetime(2024, 7, 9), uf="RJ"))  # Dia normal no RJ

    @patch("brutils.date_utils.is_holiday")
    def test_data_invalida(self, mock_is_holiday):
        # Testes com data inválida
        mock_is_holiday.return_value = None
        self.assertIsNone(is_holiday("2024-01-01"))  # Formato incorreto
        self.assertIsNone(is_holiday(None))  # Data None

    @patch("brutils.date_utils.is_holiday")
    def test_uf_invalida(self, mock_is_holiday):
        # Testes com UF inválida
        mock_is_holiday.return_value = None
        self.assertIsNone(is_holiday(datetime(2024, 1, 1), uf="XX"))  # UF inválida
        self.assertIsNone(is_holiday(datetime(2024, 1, 1), uf="SS"))  # UF inválida

    @patch("brutils.date_utils.is_holiday")
    def test_limite_de_datas(self, mock_is_holiday):
        # Testes com limite de datas
        mock_is_holiday.return_value = True
        self.assertTrue(is_holiday(datetime(2024, 12, 25)))  # Natal
        self.assertTrue(is_holiday(datetime(2024, 11, 15)))  # Proclamação da República

    @patch("brutils.date_utils.is_holiday")
    def test_datas_depois_de_feriados(self, mock_is_holiday):
        # Test data after holidays
        mock_is_holiday.return_value = False
        self.assertFalse(is_holiday(datetime(2024, 12, 26)))  # Não é feriado
        self.assertFalse(is_holiday(datetime(2025, 1, 2)))  # Não é feriado

    @patch("brutils.date_utils.is_holiday")
    def test_ano_bissexto(self, mock_is_holiday):
        # Teste ano bissexto
        mock_is_holiday.return_value = False
        self.assertFalse(is_holiday(datetime(2024, 2, 29)))  # Não é feriado, mas data válida
        # Uncomment to test non-leap year invalid date
        # self.assertIsNone(is_holiday(datetime(1900, 2, 29)))  # Ano não bissexto, data inválida

    @patch("brutils.date_utils.is_holiday")
    def test_data_passada_futura(self, mock_is_holiday):
        # Teste de data passada e futura
        mock_is_holiday.return_value = True
        self.assertTrue(is_holiday(datetime(2023, 1, 1)))  # Ano anterior
        self.assertTrue(is_holiday(datetime(2100, 12, 25)))  # Ano futuro
        self.assertFalse(is_holiday(datetime(2100, 1, 2)))  # Dia normal em ano futuro

    @patch("brutils.date_utils.is_holiday")
    def test_data_sem_uf(self, mock_is_holiday):
        # Teste feriado nacional sem UF
        mock_is_holiday.return_value = True
        self.assertTrue(is_holiday(datetime(2024, 12, 25)))  # Natal, feriado nacional
        self.assertFalse(is_holiday(datetime(2024, 7, 9)))  # Data estadual de SP, sem UF
