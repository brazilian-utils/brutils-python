from unittest import TestCase, main
from unittest.mock import patch

from brutils.cnpj import (
    _checksum,
    _hashdigit,
    display,
    format_cnpj,
    generate,
    is_valid,
    remove_symbols,
    sieve,
    validate,
    is_valid_new_cnpj
)


class TestCNPJ(TestCase):
    def test_sieve(self):
        self.assertEqual(sieve("00000000000"), "00000000000")
        self.assertEqual(sieve("12.345.678/0001-90"), "12345678000190")
        self.assertEqual(sieve("134..2435/.-1892.-"), "13424351892")
        self.assertEqual(sieve("abc1230916*!*&#"), "abc1230916*!*&#")
        self.assertEqual(
            sieve("ab.c1.--.2-3/09.-1-./6/-.*.-!*&#"), "abc1230916*!*&#"
        )
        self.assertEqual(sieve("/...---.../"), "")

    def test_display(self):
        self.assertEqual(display("00000000000109"), "00.000.000/0001-09")
        self.assertIsNone(display("00000000000000"))
        self.assertIsNone(display("0000000000000"))
        self.assertIsNone(display("0000000000000a"))

    def test_validate(self):
        self.assertIs(validate("34665388000161"), True)
        self.assertIs(validate("52599927000100"), False)
        self.assertIs(validate("00000000000"), False)

    def test_is_valid(self):
        # When CNPJ is not string, returns False
        self.assertIs(is_valid(1), False)

        # When CNPJ's len is different of 14, returns False
        self.assertIs(is_valid("1"), False)

        # When CNPJ does not contain only digits, returns False
        self.assertIs(is_valid("1112223334445-"), False)

        # When CNPJ has only the same digit, returns false
        self.assertIs(is_valid("11111111111111"), False)

        # When rest_1 is lt 2 and the 13th digit is not 0, returns False
        self.assertIs(is_valid("1111111111315"), False)

        # When rest_1 is gte 2 and the 13th digit is not (11 - rest), returns
        # False
        self.assertIs(is_valid("1111111111115"), False)

        # When rest_2 is lt 2 and the 14th digit is not 0, returns False
        self.assertIs(is_valid("11111111121205"), False)

        # When rest_2 is gte 2 and the 14th digit is not (11 - rest), returns
        # False
        self.assertIs(is_valid("11111111113105"), False)

        # When CNPJ is valid
        self.assertIs(is_valid("34665388000161"), True)
        self.assertIs(is_valid("01838723000127"), True)

    def test_generate(self):
        for _ in range(10_000):
            self.assertIs(validate(generate()), True)
            self.assertIsNotNone(display(generate()))

    def test__hashdigit(self):
        self.assertEqual(_hashdigit("00000000000000", 13), 0)
        self.assertEqual(_hashdigit("00000000000000", 14), 0)
        self.assertEqual(_hashdigit("52513127000292", 13), 9)
        self.assertEqual(_hashdigit("52513127000292", 14), 9)

    def test__checksum(self):
        self.assertEqual(_checksum("00000000000000"), "00")
        self.assertEqual(_checksum("52513127000299"), "99")

    def test_empty_string(self):
        self.assertFalse(is_valid_new_cnpj(""))
    
    def test_length_not_14(self):
        self.assertFalse(is_valid_new_cnpj("123456789012")) #menos de 14 dígitos 
        self.assertFalse(is_valid_new_cnpj("123456789012345"))  # mais de 14 dígitos
    
    def test_alphanumeric(self):
        self.assertTrue(is_valid_new_cnpj("ABC123DEF45678"))  
        self.assertFalse(is_valid_new_cnpj("ABC123DEF45@78"))  

    def test_last_2_digits_numeric(self):
        self.assertTrue(is_valid_new_cnpj("ABC123DEF45678")) 
        self.assertFalse(is_valid_new_cnpj("ABC123DEF4567A"))  


@patch("brutils.cnpj.sieve")
class TestRemoveSymbols(TestCase):
    def test_remove_symbols(self, mock_sieve):
        # When call remove_symbols, it calls sieve
        remove_symbols("12.345.678/0001-90")
        mock_sieve.assert_called()


@patch("brutils.cnpj.is_valid")
class TestIsValidToFormat(TestCase):
    def test_when_cnpj_is_valid_returns_true_to_format(self, mock_is_valid):
        mock_is_valid.return_value = True

        # When cnpj is_valid, returns formatted cnpj
        self.assertEqual(format_cnpj("01838723000127"), "01.838.723/0001-27")

        # Checks if function is_valid_cnpj is called
        mock_is_valid.assert_called_once_with("01838723000127")

    def test_when_cnpj_is_not_valid_returns_none(self, mock_is_valid):
        mock_is_valid.return_value = False

        # When cnpj isn't valid, returns None
        self.assertIsNone(format_cnpj("01838723000127"))


if __name__ == "__main__":
    main()
