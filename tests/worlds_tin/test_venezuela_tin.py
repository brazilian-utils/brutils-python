import unittest
from tin_venezuela import (
    remove_symbols,
    is_valid_tin,
    format_tin,
    generate,
    _calculate_digit,
)


class TestVenezuelanTIN(unittest.TestCase):
    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("v-12345678-9"), "V123456789")
        self.assertEqual(remove_symbols("J.123.456.789"), "J123456789")
        self.assertEqual(remove_symbols(" e12345678 "), "E12345678")
        self.assertEqual(remove_symbols(""), "")

    def test_valid_tin(self):
        valid_tin = generate()
        self.assertTrue(is_valid_tin(valid_tin))

    def test_invalid_tin_structure(self):
        self.assertFalse(is_valid_tin("X12345678"))  # Invalid prefix
        self.assertFalse(is_valid_tin("V1234A6789"))  # Non-digit character
        self.assertFalse(is_valid_tin("V123"))  # Too short
        self.assertFalse(is_valid_tin("V1234567890"))  # Too long

    def test_invalid_check_digit(self):
        valid_base = "V12345678"
        wrong_digit = (_calculate_digit(valid_base) + 1) % 10
        invalid_tin = valid_base + str(wrong_digit)
        self.assertFalse(is_valid_tin(invalid_tin))

    def test_format_tin(self):
        self.assertEqual(format_tin("V123456789"), "V-12345678-9")
        self.assertEqual(format_tin("e-12345678-1"), "E-12345678-1")
        self.assertIsNone(format_tin("X1234"))

    def test_calculate_digit(self):
        # Known correct calculation: you can add real known TINs for accurate testing
        base = "V12345678"
        digit = _calculate_digit(base)
        self.assertIsInstance(digit, int)
        self.assertGreaterEqual(digit, 0)
        self.assertLessEqual(digit, 10)

    def test_generate_produces_valid_tin(self):
        for _ in range(10):
            tin = generate()
            self.assertTrue(is_valid_tin(tin))


if __name__ == "__main__":
    unittest.main()
