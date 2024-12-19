from unittest import TestCase

from num2words import num2words

from brutils import convert_date_to_text
from brutils.data.enums.months import MonthsEnum


class TestNum2Words(TestCase):
    def test_num_conversion(self) -> None:
        """
        Smoke test of the num2words library.
        This test is used to guarantee that our dependency still works.
        """
        self.assertEqual(num2words(30, lang="pt-br"), "trinta")
        self.assertEqual(num2words(42, lang="pt-br"), "quarenta e dois")
        self.assertEqual(
            num2words(2024, lang="pt-br"), "dois mil e vinte e quatro"
        )
        self.assertEqual(num2words(0, lang="pt-br"), "zero")
        self.assertEqual(num2words(-1, lang="pt-br"), "menos um")


class TestDate(TestCase):
    def test_convert_date_to_text(self):
        self.assertEqual(
            convert_date_to_text("15/08/2024"),
            "Quinze de agosto de dois mil e vinte e quatro",
        )
        self.assertEqual(
            convert_date_to_text("01/01/2000"),
            "Primeiro de janeiro de dois mil",
        )
        self.assertEqual(
            convert_date_to_text("31/12/1999"),
            "Trinta e um de dezembro de mil novecentos e noventa e nove",
        )

        #
        self.assertIsNone(convert_date_to_text("30/02/2020"), None)
        self.assertIsNone(convert_date_to_text("30/00/2020"), None)
        self.assertIsNone(convert_date_to_text("30/02/2000"), None)
        self.assertIsNone(convert_date_to_text("50/09/2000"), None)
        self.assertIsNone(convert_date_to_text("25/15/2000"), None)
        self.assertIsNone(convert_date_to_text("29/02/2019"), None)

        # Invalid date pattern.
        self.assertRaises(ValueError, convert_date_to_text, "Invalid")
        self.assertRaises(ValueError, convert_date_to_text, "25/1/2020")
        self.assertRaises(ValueError, convert_date_to_text, "1924/08/20")
        self.assertRaises(ValueError, convert_date_to_text, "5/09/2020")

        self.assertEqual(
            convert_date_to_text("29/02/2020"),
            "Vinte e nove de fevereiro de dois mil e vinte",
        )
        self.assertEqual(
            convert_date_to_text("01/01/1900"),
            "Primeiro de janeiro de mil e novecentos",
        )

    months_year = [
        (1, "janeiro"),
        (2, "fevereiro"),
        (3, "marco"),
        (4, "abril"),
        (5, "maio"),
        (6, "junho"),
        (7, "julho"),
        (8, "agosto"),
        (9, "setembro"),
        (10, "outubro"),
        (11, "novembro"),
        (12, "dezembro"),
    ]

    def testMonthEnum(self):
        for number_month, name_month in self.months_year:
            month = MonthsEnum(number_month)
            self.assertEqual(month.month_name, name_month)
