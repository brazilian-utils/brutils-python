import unittest
from brutils import format_titulo_eleitoral


class TestVoterRegistrationFormat(unittest.TestCase):
    def test_valid_number(self):
        # Specific number
        response = format_titulo_eleitoral("370834200183")
        self.assertEqual(
            response, "3708 3420 01 83", "AssertionError for 370834200183"
        )

    def test_valid_numbers_type_and_regexp(self):
        # Valid voter registration numbers
        valid_numbers = [
            "370834200183",
            "107381280116",
            "587816450175",
            "260577100132",
            "248146750108",
        ]
        for n in valid_numbers:
            try:
                formatted = format_titulo_eleitoral(n)
                self.assertIsInstance(formatted, str)
                self.assertRegex(formatted, r"^(\d{4} \d{4} \d{2} \d{2})$")
            except:  # noqa: E722
                print(f"AssertionError for number: {n}")
                raise AssertionError

    def test_invalid_registration_numbers(self):
        # Invalid voter registration numbers should return None
        invalid_numbers = [
            "123",
            "370834200181",
            "107381280111",
            "587816450179",
            "goiaba",
        ]
        for n in invalid_numbers:
            try:
                self.assertEqual(format_titulo_eleitoral(n), None)
            except:  # noqa: E722
                print(f"AssertionError for number: {n}")
                raise AssertionError

    def test_non_string_input(self):
        # Non-string input should also return None
        non_strings = [None, 123, True, ["test@example.com"]]
        for value in non_strings:
            self.assertEqual(format_titulo_eleitoral(value), None)

    def test_empty_string(self):
        # Empty string should return None too
        self.assertEqual(format_titulo_eleitoral(""), None)
