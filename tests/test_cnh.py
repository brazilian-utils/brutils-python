# tests/test_cnh.py
import unittest

from brutils.cnh import is_valid_cnh, remove_symbols_cnh


class TestIsValidCnhRobust(unittest.TestCase):
    # Valid inputs (11 digits, not all equal)
    def test_valid_plain_digits(self):
        for cnh in ["02926434554", "12345678901", "98765432109", "00000000001"]:
            with self.subTest(cnh=cnh):
                self.assertTrue(is_valid_cnh(cnh))

    def test_valid_with_common_formatting(self):
        cases = [
            "029.264.345-54",
            "  123.456.789-01  ",
            "\n987.654.321-09\t",
            "000.000.000-01",
            "123-456-789-01",
            "123 456 789 01",
        ]
        for cnh in cases:
            with self.subTest(cnh=cnh):
                self.assertTrue(is_valid_cnh(cnh))

    def test_valid_with_letters_and_symbols_ignored(self):
        # Non-digits are ignored: letters/symbols are stripped; still 11 digits total
        cases = [
            "A12B345C678D90E1",
            "XX029YY264ZZ345--54",
            "id(987)key[654]{321}<09>",
        ]
        for cnh in cases:
            with self.subTest(cnh=cnh):
                self.assertTrue(is_valid_cnh(cnh))

    def test_valid_with_unicode_spaces(self):
        # Non-breaking space (U+00A0), zero-width space (U+200B) etc. are ignored
        cnh = "123" + "\u00a0" + "456" + "\u200b" + "789" + "\u00a0" + "01"
        self.assertTrue(is_valid_cnh(cnh))

    # Invalid: not exactly 11 digits after cleaning
    def test_invalid_length(self):
        cases = [
            "",  # empty
            "12345678",  # 8 digits
            "1234567890",  # 10 digits
            "123456789012",  # 12 digits
            ".....-----",  # only symbols -> 0 digits
            "abc",  # only letters -> 0 digits
        ]
        for cnh in cases:
            with self.subTest(cnh=cnh):
                self.assertFalse(is_valid_cnh(cnh))

    def test_invalid_many_digits_mixed_noise(self):
        # After stripping, > 11 digits → invalid
        cases = [
            "12345678901" + "23",  # 13 digits
            "id: 02926434554 and 999",  # 14 digits total
            "111222333444555",  # 15 digits
        ]
        for cnh in cases:
            with self.subTest(cnh=cnh):
                self.assertFalse(is_valid_cnh(cnh))

    # Invalid: all digits equal
    def test_invalid_all_digits_equal(self):
        cases = [
            "00000000000",
            "11111111111",
            "99999999999",
            "000.000.000-00",  # formatted, but all equal after cleaning
        ]
        for cnh in cases:
            with self.subTest(cnh=cnh):
                self.assertFalse(is_valid_cnh(cnh))

    # Whitespace / control chars / line breaks
    def test_whitespace_and_control_chars(self):
        cases = [
            " \t\n12345678901\r\n",
            "\f123.456.789-01\v",
        ]
        for cnh in cases:
            with self.subTest(cnh=cnh):
                self.assertTrue(is_valid_cnh(cnh))

    # None and non-string behavior
    def test_none_input(self):
        self.assertFalse(is_valid_cnh(None))

    # Pipeline with remove_symbols_cnh
    def test_pipeline_remove_symbols_then_validate(self):
        raw = " 029.264.345-54 "
        cleaned = remove_symbols_cnh(raw)  # should be "02926434554"
        self.assertEqual(cleaned, "02926434554")
        self.assertTrue(is_valid_cnh(cleaned))

    # Edge cases around leading zeros and near-repetition
    def test_leading_zeros_not_all_equal(self):
        self.assertTrue(is_valid_cnh("00000000009"))  # 10 zeros + 9 (valid)

    def test_repetition_with_one_change_is_valid(self):
        self.assertTrue(
            is_valid_cnh("11111111112")
        )  # mostly equal, but not all


if __name__ == "__main__":
    unittest.main()
