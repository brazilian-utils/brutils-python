from os import pardir
from os.path import abspath, join, dirname
from sys import path, version_info, dont_write_bytecode
from inspect import getsourcefile

dont_write_bytecode = True
range = range if version_info.major >= 3 else xrange
path.insert(1, abspath(join(dirname(abspath(getsourcefile(lambda:0))), pardir)))
from brutils.cnpj import sieve, display, hashdigit, checksum, validate, generate
from unittest import TestCase, main


class CNPJ(TestCase):
    def test_sieve(self):
        self.assertEqual(sieve('00000000000'), '00000000000')
        self.assertEqual(sieve('12.345.678/0001-90'), '12345678000190')
        self.assertEqual(sieve('134..2435/.-1892.-'), '13424351892')
        self.assertEqual(sieve('abc1230916*!*&#'), 'abc1230916*!*&#')
        self.assertEqual(sieve('ab.c1.--.2-3/09.-1-./6/-.*.-!*&#'), 'abc1230916*!*&#')
        self.assertEqual(sieve('/...---.../'), '')

    def test_display(self):
        self.assertEqual(display('00000000000109'), '00.000.000/0001-09')
        self.assertIsNone(display('00000000000000'))
        self.assertIsNone(display('0000000000000a'))
        self.assertIsNone(display('0000000000000'))

    def test_hashdigit(self):
        self.assertEqual(hashdigit('00000000000000', 13), 0)
        self.assertEqual(hashdigit('00000000000000', 14), 0)
        self.assertEqual(hashdigit('52513127000292', 13), 9)
        self.assertEqual(hashdigit('52513127000292', 14), 9)

    def test_checksum(self):
        self.assertEqual(checksum('00000000000000'), '00')
        self.assertEqual(checksum('52513127000299'), '99')

    def test_validate(self):
        self.assertTrue(validate('34665388000161'))
        self.assertFalse(validate('52599927000100'))
        self.assertFalse(validate('00000000000'))

    def test_generate(self):
        for i in range(1000):
            self.assertTrue(validate(generate()))
            self.assertIsNotNone(display(generate()))


if __name__ == '__main__':
    main()

