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
from brutils.cep import (
    is_valid,
    generate,
)
from unittest import TestCase, main


class CEP(TestCase):
    def test_is_valid(self):
        # When CEP is not string, returns False
        assert not is_valid(1)

        # When CEP's len is different of 8, returns False
        assert not is_valid("1")

        # When CEP does not contain only digits, returns False
        assert not is_valid("1234567-")

        # When CEP is valid
        assert is_valid("99999999")
        assert is_valid("88390000")

    def test_generate(self):
        for _ in range(10_000):
            assert is_valid(generate())
        # assert format(generate()) is not None
