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
from brutils.cnpj import (
    sieve,
    display,
    validate,
    generate,
    is_valid,
    format_cnpj,
    remove_symbols,
    _hashdigit,
    _checksum,
)
from unittest import TestCase, main


class CNPJ(TestCase):
    def test_sieve(self):
        assert sieve("00000000000") == "00000000000"
        assert sieve("12.345.678/0001-90") == "12345678000190"
        assert sieve("134..2435/.-1892.-") == "13424351892"
        assert sieve("abc1230916*!*&#") == "abc1230916*!*&#"
        assert sieve("ab.c1.--.2-3/09.-1-./6/-.*.-!*&#") == "abc1230916*!*&#"
        assert sieve("/...---.../") == ""

    def test_remove_symbols(self):
        with patch("brutils.cnpj.sieve") as mock_sieve:
            # When call remove_symbols, it calls sieve
            remove_symbols("12.345.678/0001-90")
            mock_sieve.assert_called()

    def test_display(self):
        assert display("00000000000109") == "00.000.000/0001-09"
        assert display("00000000000000") is None
        assert display("0000000000000a") is None
        assert display("0000000000000") is None

    def test_format_cnpj(self):
        with patch("brutils.cnpj.is_valid", return_value=True) as mock_is_valid:
            # When cnpj is_valid, returns formatted cnpj
            assert format_cnpj("01838723000127") == "01.838.723/0001-27"

        # Checks if function is_valid_cnpj is called
        mock_is_valid.assert_called_once_with("01838723000127")

        with patch(
            "brutils.cnpj.is_valid", return_value=False
        ) as mock_is_valid:
            # When cnpj isn't valid, returns None
            assert format_cnpj("01838723000127") is None

    def test_validate(self):
        assert validate("34665388000161")
        assert not validate("52599927000100")
        assert not validate("00000000000")

    def test_is_valid(self):
        # When CNPJ is not string, returns False
        assert not is_valid(1)

        # When CNPJ's len is different of 14, returns False
        assert not is_valid("1")

        # When CNPJ does not contain only digits, returns False
        assert not is_valid("1112223334445-")

        # When CNPJ has only the same digit, returns false
        assert not is_valid("11111111111111")

        # When rest_1 is lt 2 and the 13th digit is not 0, returns False
        assert not is_valid("1111111111315")

        # When rest_1 is gte 2 and the 13th digit is not (11 - rest), returns False
        assert not is_valid("1111111111115")

        # When rest_2 is lt 2 and the 14th digit is not 0, returns False
        assert not is_valid("11111111121205")

        # When rest_2 is gte 2 and the 14th digit is not (11 - rest), returns False
        assert not is_valid("11111111113105")

        # When CNPJ is valid
        assert is_valid("34665388000161")
        assert is_valid("01838723000127")

    def test_generate(self):
        for _ in range(10_000):
            assert validate(generate())
            assert display(generate()) is not None

    def test__hashdigit(self):
        assert _hashdigit("00000000000000", 13) == 0
        assert _hashdigit("00000000000000", 14) == 0
        assert _hashdigit("52513127000292", 13) == 9
        assert _hashdigit("52513127000292", 14) == 9

    def test__checksum(self):
        assert _checksum("00000000000000") == "00"
        assert _checksum("52513127000299") == "99"


if __name__ == "__main__":
    main()
