import unittest
from your_module import remove_symbols, is_valid, format_tin, generate, _calculate_digit

class TestAngolanTIN(unittest.TestCase):

    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("123.456.789"), "123456789")
        self.assertEqual(remove_symbols(" 1-2/3*4#5&6 7!8@9 "), "123456789")
        self.assertEqual(remove_symbols("ABC"), "")
        self.assertEqual(remove_symbols(""), "")

    def test_valid_tin(self):
        valid_tin = generate()
        self.assertTrue(is_valid(valid_tin))

    def test_invalid_structure(self):
        self.assertFalse(is_valid("012345678"))  # Prefix not allowed
        self.assertFalse(is_valid("12345678"))   # Too short
        self.assertFalse(is_valid("1234567890")) # Too long
        self.assertFalse(is_valid("12345678A"))  # Non-digit at the end

    def test_invalid_check_digit(self):
        base = "15678901"  # valid prefix + 7 digits
        incorrect_dv = (_calculate_digit(base) + 1) % 10
        invalid_tin = base + str(incorrect_dv)
        self.assertFalse(is_valid(invalid_tin))

    def test_calculate_digit(self):
        base = "15678901"
        digit = _calculate_digit(base)
        self.assertIsInstance(digit, int)
        self.assertGreaterEqual(digit, 0)
        self.assertLessEqual(digit, 9)

    def test_format_tin(self):
        self.assertEqual(format_tin("123456789"), "123.456.789")
        self.assertEqual(format_tin(" 1.2-3/4#5&6 7@8!9 "), "123.456.789")
        self.assertIsNone(format_tin("12345678"))  # Too short

    def test_generate_produces_valid_tin(self):
        for _ in range(10):
            tin = generate()
            self.assertTrue(is_valid(tin))

if __name__ == "__main__":
    unittest.main()
