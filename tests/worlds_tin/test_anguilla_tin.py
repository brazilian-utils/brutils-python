from unittest import TestCase, main
from unittest.mock import patch

from tin_anguilla import (
    remove_symbols,
    is_valid_individual,
    is_valid_company,
    is_valid,
    format_tin,
    generate,
)


class TestTIN(TestCase):
    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("AB12345678"), "AB12345678")
        self.assertEqual(remove_symbols("AB-12.34 5678"), "AB12345678")
        self.assertEqual(remove_symbols("...---..."), "")

    def test_is_valid_individual(self):
        self.assertEqual(is_valid_individual("AB12345678"), "Valid Anguilla TIN")
        self.assertEqual(is_valid_individual("A12345678"), "Invalid Anguilla TIN: Must have 10 characters.")
        self.assertEqual(is_valid_individual("1234567890"), "Invalid Anguilla TIN: Must start with two letters.")
        self.assertEqual(is_valid_individual("AB12345ABC"), "Invalid Anguilla TIN: The remaining characters must be numeric.")

    def test_is_valid_company(self):
        self.assertEqual(is_valid_company("ABC1234567"), "Valid Anguilla TIN")
        self.assertEqual(is_valid_company("AB1234567"), "Invalid Anguilla TIN: Must start with three letters.")
        self.assertEqual(is_valid_company("ABC12345ABC"), "Invalid Anguilla TIN: The remaining characters must be numeric.")

    def test_is_valid(self):
        self.assertEqual(is_valid("AB12345678"), "Valid Anguilla TIN")
        self.assertEqual(is_valid("ABC1234567"), "Valid Anguilla TIN")
        self.assertEqual(is_valid("1234567890"), "Invalid Anguilla TIN: Must start with two letters.")

    def test_generate(self):
        for _ in range(100):
            tin = generate()
            self.assertEqual(is_valid_individual(tin), "Valid Anguilla TIN")

            tin_company = generate(is_company=True)
            self.assertEqual(is_valid_company(tin_company), "Valid Anguilla TIN")

    @patch("tin_anguilla.is_valid")
    def test_format_tin(self, mock_is_valid):
        mock_is_valid.return_value = "Valid Anguilla TIN"
        self.assertEqual(format_tin("AB12345678"), "AB-12345678")
        self.assertEqual(format_tin("ABC1234567"), "ABC-1234567")
        self.assertIsNone(format_tin("A123"))


if __name__ == "__main__":
    main()