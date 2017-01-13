from os import pardir
from os.path import abspath, join, dirname
from sys import path, version_info, dont_write_bytecode
from inspect import getsourcefile

dont_write_bytecode = True
range = range if version_info.major >= 3 else xrange
path.insert(1, abspath(join(dirname(abspath(getsourcefile(lambda:0))), pardir)))
from brutils.cpf import sieve, display, hashdigit, checksum, validate, generate
from unittest import TestCase, main


class CPF(TestCase):
    def test_sieve(self):
        self.assertEqual(sieve('00000000000'), '00000000000')
        self.assertEqual(sieve('123.456.789-10'), '12345678910')
        self.assertEqual(sieve('134..2435.-1892.-'), '13424351892')
        self.assertEqual(sieve('abc1230916*!*&#'), 'abc1230916*!*&#')
        self.assertEqual(sieve('ab.c1.--.2-309.-1-.6-.*.-!*&#'), 'abc1230916*!*&#')
        self.assertEqual(sieve('...---...'), '')

    def test_display(self):
        self.assertEqual(display('00000000011'), '000.000.000-11')
        self.assertIsNone(display('00000000000'))
        self.assertIsNone(display('0000000000a'))
        self.assertIsNone(display('000000000000'))

    def test_hashdigit(self):
        self.assertEqual(hashdigit('000000000', 10), 0)
        self.assertEqual(hashdigit('0000000000', 11), 0)
        self.assertEqual(hashdigit('52513127765', 10), 6)
        self.assertEqual(hashdigit('52513127765', 11), 5)

    def test_checksum(self):
        self.assertEqual(checksum('000000000'), '00')
        self.assertEqual(checksum('525131277'), '65')

    def test_validate(self):
        self.assertTrue(validate('52513127765'))
        self.assertTrue(validate('52599927765'))
        self.assertFalse(validate('00000000000'))

    def test_generate(self):
        for i in range(1000):
            self.assertTrue(validate(generate()))
            self.assertIsNotNone(display(generate()))


if __name__ == '__main__':
    main()

