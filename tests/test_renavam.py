from unittest import TestCase

from brutils.renavam import is_valid_renavam


class TestRENAVAM(TestCase):
    def test_is_valid_renavam(self):
        self.assertTrue(is_valid_renavam("86769597308"))
        self.assertFalse(is_valid_renavam("12345678901"))

        self.assertRaises(ValueError,is_valid_renavam,"1234567890a")
        self.assertRaises(ValueError,is_valid_renavam,"12345678 901")
        self.assertRaises(ValueError,is_valid_renavam,"12345678")
        self.assertRaises(ValueError,is_valid_renavam,"")
        self.assertRaises(ValueError,is_valid_renavam,"123456789012")
        self.assertRaises(ValueError,is_valid_renavam,"abcdefghijk")
        self.assertRaises(ValueError,is_valid_renavam,"12345678901!")
