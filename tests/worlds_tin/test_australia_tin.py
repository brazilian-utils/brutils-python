from unittest import TestCase, main
from unittest.mock import patch

from tin_australia import (
    remove_symbols,
    is_valid_tfn,
    is_valid_abn,
    format_tfn,
    format_abn,
    generate_tfn,
    generate_abn,
)


class TestTFNABN(TestCase):
    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("123456789"), "123456789")
        self.assertEqual(remove_symbols("12-34.56 789"), "123456789")
        self.assertEqual(remove_symbols("...---..."), "")

    def test_is_valid_tfn(self):
        self.assertEqual(is_valid_tfn("123456782"), "Valid TFN")
        self.assertEqual(is_valid_tfn("12345678"), "Invalid TFN: Failed checksum validation.")
        self.assertEqual(is_valid_tfn("A23456789"), "Invalid TFN: Must be 8 or 9 numeric digits.")

    def test_is_valid_abn(self):
        self.assertEqual(is_valid_abn("51824753556"), "Valid ABN")
        self.assertEqual(is_valid_abn("12345678901"), "Invalid ABN: Failed checksum validation.")
        self.assertEqual(is_valid_abn("A2345678901"), "Invalid ABN: Must be exactly 11 numeric digits.")

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
        self.assertIsNone(format_tfn("123"))

    @patch("tin_australia.is_valid_abn")
    def test_format_abn(self, mock_is_valid_abn):
        mock_is_valid_abn.return_value = "Valid ABN"
        self.assertEqual(format_abn("51824753556"), "51 824 753 556")
        self.assertIsNone(format_abn("123"))


if __name__ == "__main__":
    main()