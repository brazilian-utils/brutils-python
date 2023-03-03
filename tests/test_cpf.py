from os import pardir
from os.path import abspath, join, dirname
from sys import path, version_info, dont_write_bytecode
from inspect import getsourcefile

dont_write_bytecode = True
range = range if version_info.major >= 3 else xrange
path.insert(
    1, abspath(join(dirname(abspath(getsourcefile(lambda: 0))), pardir))
)
from brutils.cpf import sieve, display, hashdigit, checksum, validate, generate
from unittest import TestCase, main


class CPF(TestCase):
    def test_sieve(self):
        assert sieve("00000000000") == "00000000000"
        assert sieve("123.456.789-10") == "12345678910"
        assert sieve("134..2435.-1892.-") == "13424351892"
        assert sieve("abc1230916*!*&#") == "abc1230916*!*&#"
        assert sieve("ab.c1.--.2-309.-1-.6-.*.-!*&#") == "abc1230916*!*&#"
        assert sieve("...---...") == ""

    def test_display(self):
        assert display("00000000011") == "000.000.000-11"
        assert display("00000000000") is None
        assert display("0000000000a") is None
        assert display("000000000000") is None

    def test_hashdigit(self):
        assert hashdigit("000000000", 10) == 0
        assert hashdigit("0000000000", 11) == 0
        assert hashdigit("52513127765", 10) == 6
        assert hashdigit("52513127765", 11) == 5

    def test_checksum(self):
        assert checksum("000000000") == "00"
        assert checksum("525131277") == "65"

    def test_validate(self):
        assert validate("52513127765")
        assert validate("52599927765")
        assert not validate("00000000000")

    def test_generate(self):
        for i in range(1000):
            assert validate(generate())
            assert display(generate()) is not None


if __name__ == "__main__":
    main()
