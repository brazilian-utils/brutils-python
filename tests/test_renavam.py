from unittest import TestCase

from brutils.renavam import is_valid_renavam


class TestRENAVAM(TestCase):
    def test_valid_renavam(self):
        # First
        self.assertTrue(is_valid_renavam("79831854647"))
        self.assertFalse(is_valid_renavam("1234567890"))  # Less than 11 digits
        self.assertFalse(
            is_valid_renavam("123456789012")
        )  # More than 11 digits
        # Second
        self.assertFalse(is_valid_renavam("1234567890a"))  # With letter
        self.assertFalse(is_valid_renavam("12345678 901"))  # With space
        self.assertFalse(
            is_valid_renavam("12345678901!")
        )  # With special character
        self.assertFalse(is_valid_renavam(""))  # Empty string

    # Third
    def test_renavam_check_digit(self):
        self.assertTrue(is_valid_renavam("01044683357"))
        self.assertFalse(is_valid_renavam("12345678901"))  # Invalid check digit

    # Fourth - Issue
    def test_is_valid_renavam(self):
        # Tests for valid RENAVAM
        self.assertTrue(
            is_valid_renavam("35298206229")
        )  # Change this one because in the issue example it is invalid
        self.assertFalse(is_valid_renavam("12345678900"))

        # Tests for invalid RENAVAM
        self.assertFalse(is_valid_renavam("1234567890a"))
        self.assertFalse(is_valid_renavam("12345678 901"))
        self.assertFalse(is_valid_renavam("12345678"))
        self.assertFalse(is_valid_renavam(""))
        self.assertFalse(is_valid_renavam("123456789012"))
        self.assertFalse(is_valid_renavam("abcdefghijk"))
        self.assertFalse(is_valid_renavam("12345678901!"))
