import unittest
from unittest.mock import patch
from random import randint

from tin_united_states_of_america import (
    remove_symbols,
    is_valid_ssn,
    is_valid_ein,
    format_ssn,
    format_ein,
    generate_ssn,
    generate_ein,
)


class TestTINFunctions(unittest.TestCase):
    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("123-45-6789"), "123456789")
        self.assertEqual(remove_symbols("12 34 5678"), "12345678")
        self.assertEqual(remove_symbols("12.34.5678"), "12345678")
        self.assertEqual(remove_symbols("abc123def"), "123")
        self.assertEqual(remove_symbols("!@#123$%^&*()"), "123")

    def test_is_valid_ssn(self):
        self.assertTrue(is_valid_ssn("123-45-6789"))
        self.assertFalse(is_valid_ssn("000-12-3456"))
        self.assertFalse(is_valid_ssn("666-12-3456"))
        self.assertFalse(is_valid_ssn("987-65-4321"))
        self.assertFalse(is_valid_ssn("123-00-4567"))
        self.assertFalse(is_valid_ssn("123-45-0000"))
        self.assertFalse(is_valid_ssn("12345678"))
        self.assertFalse(is_valid_ssn("1234567890"))

    def test_is_valid_ein(self):
        self.assertTrue(is_valid_ein("12-3456789"))
        self.assertFalse(is_valid_ein("1-3456789"))
        self.assertFalse(is_valid_ein("1234567890"))
        self.assertFalse(is_valid_ein("abcdefghj"))

    def test_format_ssn(self):
        self.assertEqual(format_ssn("123456789"), "123-45-6789")
        self.assertIsNone(format_ssn("12345"))
        self.assertIsNone(format_ssn("abcdefgh"))

    def test_format_ein(self):
        self.assertEqual(format_ein("123456789"), "12-3456789")
        self.assertIsNone(format_ein("12345"))
        self.assertIsNone(format_ein("abcdefgh"))

    def test_generate_ssn(self):
        for _ in range(100):
            ssn = generate_ssn()
            self.assertTrue(is_valid_ssn(ssn))

    def test_generate_ein(self):
        for _ in range(100):
            ein = generate_ein()
            self.assertTrue(is_valid_ein(ein))


if __name__ == "__main__":
    unittest.main()
