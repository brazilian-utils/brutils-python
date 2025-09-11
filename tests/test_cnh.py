from unittest import TestCase, main

from brutils.cnh import is_valid_cnh, remove_symbols_cnh


class TestCNH(TestCase):
    def test_remove_symbols_cnh_ok(self):
        cases = [
            ("123.456.789-00", "12345678900"),
            ("  053.180.594-10  ", "05318059410"),
            ("41010881538", "41010881538"),
            ("", ""),  # empty string remains empty
            ("abc", ""),  # no digits → empty string
            ("--93-825.480-731--", "93825480731"),
        ]
        for raw, expected in cases:
            with self.subTest(raw=raw):
                self.assertEqual(remove_symbols_cnh(raw), expected)

    def test_remove_symbols_cnh_invalid_types(self):
        invalid_inputs = [None, 123, 12.3, object()]
        for invalid in invalid_inputs:
            with self.subTest(invalid=invalid):
                self.assertIsNone(remove_symbols_cnh(invalid))

    def test_is_valid_cnh_true_digits_only(self):
        valid_cases = [
            "05318059410",
            "41010881538",
            "55541187371",
            "89134024277",
            "93825480731",
        ]
        for cnh in valid_cases:
            with self.subTest(cnh=cnh):
                self.assertTrue(is_valid_cnh(cnh))

    def test_is_valid_cnh_true_with_symbols(self):
        formatted_cases = [
            "053.180.594-10",
            "410.108.815-38",
            "555.411.873-71",
            "891.340.242-77",
            "938.254.807-31",
        ]
        for cnh in formatted_cases:
            with self.subTest(cnh=cnh):
                self.assertTrue(is_valid_cnh(cnh))

    def test_is_valid_cnh_false(self):
        invalid_cases = [
            # repeated digit sequences
            "00000000000",
            "11111111111",
            "22222222222",
            # invalid length
            "1234567890",  # 10 digits
            "123456789012",  # 12 digits
            # non-numeric after cleaning
            "abc",
            "",
            # wrong check digit
            "05318059411",  # last digit changed
            "41010881530",  # last digit changed
        ]
        for cnh in invalid_cases:
            with self.subTest(cnh=cnh):
                self.assertFalse(is_valid_cnh(cnh))

    def test_is_valid_cnh_none_input(self):
        self.assertFalse(is_valid_cnh(None))

    def test_pipeline_remove_then_validate(self):
        """Full pipeline: remove symbols then validate."""
        raw = " 053.180.594-10 "
        cleaned = remove_symbols_cnh(raw)
        self.assertEqual(cleaned, "05318059410")
        self.assertTrue(is_valid_cnh(cleaned))


if __name__ == "__main__":
    main()
