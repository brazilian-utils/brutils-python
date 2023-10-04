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
from brutils.pis import validate, is_valid, _checksum
from unittest import TestCase, main


class TestPIS(TestCase):
    def test_validate(self):
        self.assertIs(validate("123456789ab"), False)
        self.assertIs(validate("901.85930.32-3"), False)
        self.assertIs(validate("90185930323"), True)
        self.assertIs(validate("93616217820"), True)

    def test_is_valid(self):
        # When PIS is not string, returns False
        self.assertIs(is_valid(1), False)
        self.assertIs(is_valid([]), False)
        self.assertIs(is_valid({}), False)
        self.assertIs(is_valid(None), False)

        # When PIS's len is different of 11, returns False
        self.assertIs(is_valid("123456789"), False)

        # When PIS does not contain only digits, returns False
        self.assertIs(is_valid("123pis"), False)

        # When checksum digit doesn't match last digit, returns False
        self.assertIs(is_valid("11111111111"), False)
        self.assertIs(is_valid("11111111215"), False)
        self.assertIs(is_valid("12038619493"), False)

        # When PIS is valid
        self.assertIs(is_valid("12038619494"), True)
        self.assertIs(is_valid("12016784018"), True)
        self.assertIs(is_valid("12083210826"), True)

    def test_checksum(self):
        # Checksum digit is 0 when the subtracted number is 10 or 11
        self.assertEqual(_checksum("1204152015"), 0)
        self.assertEqual(_checksum("1204433157"), 0)

        # Checksum digit is equal the subtracted number
        self.assertEqual(_checksum("1204917738"), 2)
        self.assertEqual(_checksum("1203861949"), 4)
        self.assertEqual(_checksum("1208321082"), 6)


if __name__ == "__main__":
    main()
