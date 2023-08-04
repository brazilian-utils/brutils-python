from unittest import TestCase
from brutils.boleto import validate


class Boleto(TestCase):
    def test_validate(self):
        ## When boleto's len is different than 47 and 48, returns false
        self.assertFalse(validate("1"))
        self.assertTrue(validate(47 * "1"))
        self.assertTrue(validate(48 * "1"))
        ## When boleto is not string, returns False
        self.assertFalse(validate(1))
        ##verificação  -> fazer
