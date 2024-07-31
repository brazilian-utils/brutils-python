from unittest import TestCase, main
from unittest.mock import patch

from brutils.cep import (
    format_cep,
    generate,
    is_valid,
    remove_symbols,
)


class TestCEP(TestCase):
    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("00000000"), "00000000")
        self.assertEqual(remove_symbols("01310-200"), "01310200")
        self.assertEqual(remove_symbols("01..310.-200.-"), "01310200")
        self.assertEqual(remove_symbols("abc01310200*!*&#"), "abc01310200*!*&#")
        self.assertEqual(
            remove_symbols("ab.c1.--.3-102.-0-.0-.*.-!*&#"), "abc1310200*!*&#"
        )
        self.assertEqual(remove_symbols("...---..."), "")

    def test_is_valid(self):
        # When CEP is not string, returns False
        self.assertIs(is_valid(1), False)

        # When CEP's len is different of 8, returns False
        self.assertIs(is_valid("1"), False)

        # When CEP does not contain only digits, returns False
        self.assertIs(is_valid("1234567-"), False)

        # When CEP is valid
        self.assertIs(is_valid("99999999"), True)
        self.assertIs(is_valid("88390000"), True)

    def test_generate(self):
        for _ in range(10_000):
            self.assertIs(is_valid(generate()), True)
        # assert format(generate()) is not None


@patch("brutils.cep.is_valid")
class TestIsValidToFormat(TestCase):
    def test_when_cep_is_valid_returns_true_to_format(self, mock_is_valid):
        mock_is_valid.return_value = True

        self.assertEqual(format_cep("01310200"), "01310-200")

        # Checks if function is_valid_cnpj is called
        mock_is_valid.assert_called_once_with("01310200")

    def test_when_cep_is_not_valid_returns_none(self, mock_is_valid):
        mock_is_valid.return_value = False

        # When cep isn't valid, returns None
        self.assertIsNone(format_cep("013102009"))


if __name__ == "__main__":
    main()
