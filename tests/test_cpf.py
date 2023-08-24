from os import pardir
from os.path import abspath, join, dirname
from sys import path, version_info, dont_write_bytecode
from inspect import getsourcefile
from unittest.mock import patch

dont_write_bytecode = True
range = range if version_info.major >= 3 else xrange
path.insert(
    1, abspath(join(dirname(abspath(getsourcefile(lambda: 0))), pardir))
)
from brutils.cpf import (
    sieve,
    display,
    validate,
    generate,
    is_valid,
    format_cpf,
    remove_symbols,
    _hashdigit,
    _checksum,
)
from unittest import TestCase, main


class CPF(TestCase):
    def test_sieve(self):
        self.assertEqual(sieve("00000000000"), "00000000000")
        self.assertEqual(sieve("123.456.789-10"), "12345678910")
        self.assertEqual(sieve("134..2435.-1892.-"), "13424351892")
        self.assertEqual(sieve("abc1230916*!*&#"), "abc1230916*!*&#")
        self.assertEqual(
            sieve("ab.c1.--.2-309.-1-.6-.*.-!*&#"), "abc1230916*!*&#"
        )
        self.assertEqual(sieve("...---..."), "")

    def test_remove_symbols(self):
        with patch("brutils.cpf.sieve") as mock_sieve:
            # When call remove_symbols, it calls sieve
            remove_symbols("123.456.789-10")
            mock_sieve.assert_called()

    def test_display(self):
        self.assertEqual(display("00000000011"), "000.000.000-11")
        self.assertIsNone(display("00000000000"))
        self.assertIsNone(display("0000000000a"))
        self.assertIsNone(display("000000000000"))

    def test_format_cpf(self):
        with patch("brutils.cpf.is_valid", return_value=True) as mock_is_valid:
            # When cpf is_valid, returns formatted cpf
            self.assertEqual(format_cpf("11144477735"), "111.444.777-35")

        # Checks if function is_valid_cpf is called
        mock_is_valid.assert_called_once_with("11144477735")

        with patch("brutils.cpf.is_valid", return_value=False) as mock_is_valid:
            # When cpf isn't valid, returns None
            self.assertIsNone(format_cpf("11144477735"))

    def test_validate(self):
        self.assertTrue(validate("52513127765"))
        self.assertTrue(validate("52599927765"))
        self.assertFalse(validate("00000000000"))

    def test_is_valid(self):
        # When cpf is not string, returns False
        self.assertFalse(is_valid(1))

        # When cpf's len is different of 11, returns False
        self.assertFalse(is_valid("1"))

        # When cpf does not contain only digits, returns False
        self.assertFalse(is_valid("1112223334-"))

        # When CPF has only the same digit, returns false
        self.assertFalse(is_valid("11111111111"))

        # When rest_1 is lt 2 and the 10th digit is not 0, returns False
        self.assertFalse(is_valid("11111111215"))

        # When rest_1 is gte 2 and the 10th digit is not (11 - rest), returns False
        self.assertFalse(is_valid("11144477705"))

        # When rest_2 is lt 2 and the 11th digit is not 0, returns False
        self.assertFalse(is_valid("11111111204"))

        # When rest_2 is gte 2 and the 11th digit is not (11 - rest), returns False
        self.assertFalse(is_valid("11144477732"))

        # When cpf is valid
        self.assertTrue(is_valid("11144477735"))
        self.assertTrue(is_valid("11111111200"))

    def test_generate(self):
        for _ in range(10_000):
            self.assertTrue(validate(generate()))
            self.assertIsNotNone(display(generate()))

    def test__hashdigit(self):
        self.assertEqual(_hashdigit("000000000", 10), 0)
        self.assertEqual(_hashdigit("0000000000", 11), 0)
        self.assertEqual(_hashdigit("52513127765", 10), 6)
        self.assertEqual(_hashdigit("52513127765", 11), 5)

    def test_checksum(self):
        self.assertEqual(_checksum("000000000"), "00")
        self.assertEqual(_checksum("525131277"), "65")


if __name__ == "__main__":
    main()
