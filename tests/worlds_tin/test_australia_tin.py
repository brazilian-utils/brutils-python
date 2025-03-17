from unittest import TestCase, main
from unittest.mock import patch

from tin_australia import (
    format_tfn,
    generate_abn,
    generate_tfn,
    is_valid_abn,
    is_valid_tfn,
    remove_symbols,
)


class TestTFNABN(TestCase):
    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("123456789"), "123456789")
        self.assertEqual(remove_symbols("12-34.56 789"), "123456789")
        self.assertEqual(remove_symbols("...---..."), "")

    def test_is_valid_tfn(self):
        self.assertEqual(is_valid_tfn("123456782"), "Valid TFN")
        self.assertEqual(
            is_valid_tfn("12345678"), "Invalid TFN: Failed checksum validation."
        )
        self.assertEqual(
            is_valid_tfn("A23456789"),
            "Invalid TFN: Must be 8 or 9 numeric digits.",
        )

    def test_is_valid_abn(self):
        self.assertEqual(is_valid_abn("51824753556"), "Valid ABN")
        self.assertEqual(
            is_valid_abn("12345678901"),
            "Invalid ABN: Failed checksum validation.",
        )
        self.assertEqual(
            is_valid_abn("A2345678901"),
            "Invalid ABN: Must be exactly 11 numeric digits.",
        )

    def test_generate_tfn(self):
        for _ in range(100):
            tfn = generate_tfn()
            self.assertEqual(is_valid_tfn(tfn), "Valid TFN")

    def test_generate_abn(self):
        for _ in range(100):
            abn = generate_abn()
            self.assertEqual(is_valid_abn(abn), "Valid ABN")

    @patch("tin_australia.is_valid_tfn")
    def test_format_tfn(self, mock_is_valid_tfn):
        mock_is_valid_tfn.return_value = "Valid TFN"
        self.assertEqual(format_tfn("123456782"), "12 345 6782")

    def test_format_tin(self, mock_is_valid):
        mock_is_valid.return_value = "Valid Anguilla TIN"
        self.assertEqual(format_tin("AB12345678"), "AB-12345678")
        self.assertEqual(format_tin("ABC1234567"), "ABC-1234567")
        self.assertIsNone(format_tin("A123"))


if __name__ == "__main__":
    main()
