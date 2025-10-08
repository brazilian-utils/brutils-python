from unittest import TestCase, main
from unittest.mock import patch

from brutils.passport import (
    display,
    format_passport,
    generate,
    is_valid,
    remove_symbols,
    sieve,
    validate,
)


class TestPassport(TestCase):
    def test_sieve(self):
        self.assertEqual(sieve("CS265436"), "CS265436")
        self.assertEqual(sieve("CS-265.436"), "CS265436")
        self.assertEqual(sieve("cs 265 436"), "cs265436")
        self.assertEqual(sieve("..--  "), "")
        self.assertEqual(sieve("ab.CS 265-436*!"), "abCS265436*!")

    def test_display(self):
        self.assertEqual(display("cs 265.436"), "CS265436")
        self.assertEqual(display("AB123456"), "AB123456")

        # invalid: not str
        self.assertIsNone(display(123))  # type: ignore[arg-type]
        # invalid: wrong length
        self.assertIsNone(display("A123456"))  # 7 chars
        self.assertIsNone(display("ABC12345"))  # 8 chars but 3 letters
        self.assertIsNone(display("AB1234567"))  # 9 chars
        # invalid: wrong pattern
        self.assertIsNone(display("A_123456"))  # underscore
        self.assertIsNone(display("12A34567"))  # digit in letter slot

    def test_validate(self):
        self.assertIs(validate("CS265436"), True)
        self.assertIs(validate("aa000001"), True)
        self.assertIs(validate("A123456"), False)
        self.assertIs(validate("ABC12345"), False)
        self.assertIs(validate("A_123456"), False)

    def test_is_valid(self):
        # When passport is not string, returns False
        self.assertIs(is_valid(1), False)  # type: ignore[arg-type]

        # When length is wrong, returns False
        self.assertIs(is_valid("A123456"), False)

        # When characters are invalid, returns False
        self.assertIs(is_valid("CS-265.436"), False)
        self.assertIs(is_valid("C_265436"), False)
        self.assertIs(is_valid("12A34567"), False)

        # When valid
        self.assertIs(is_valid("CS265436"), True)
        self.assertIs(is_valid("aa000001"), True)

    def test_generate(self):
        # multiple generations must be valid & displayable
        for _ in range(10_000):
            p = generate()
            self.assertIs(validate(p), True)
            self.assertIsNotNone(display(p))


@patch("brutils.passport.sieve")
class TestRemoveSymbols(TestCase):
    def test_remove_symbols_calls_sieve(self, mock_sieve):
        # When call remove_symbols, it calls sieve (same pattern as CPF)
        remove_symbols("CS-265.436")
        mock_sieve.assert_called()


@patch("brutils.passport.is_valid")
class TestIsValidToFormat(TestCase):
    def test_when_passport_is_valid_returns_formatted(self, mock_is_valid):
        mock_is_valid.return_value = True

        # When passport is valid, returns normalized uppercase without symbols
        self.assertEqual(format_passport("cs 265436"), "CS265436")

        # Checks if function is_valid is called
        mock_is_valid.assert_called_once_with("cs 265436")

    def test_when_passport_is_not_valid_returns_none(self, mock_is_valid):
        mock_is_valid.return_value = False

        # When passport isn't valid, returns None
        self.assertIsNone(format_passport("cs-26543"))


if __name__ == "__main__":
    main()
