from unittest import TestCase
from brutils.phone import is_valid

class TestIsValidDefaultMCDC(TestCase):
    def test_CT_A_landline_true(self):
        # CT-A: L=True (fixo válido), M=False → resultado True
        self.assertTrue(is_valid("1928814933"))

    def test_CT_B_both_false(self):
        # CT-B: L=False, M=False (ambos inválidos) → resultado False
        self.assertFalse(is_valid("0000000000"))

    def test_CT_C_mobile_true(self):
        # CT-C: L=False, M=True (móvel válido) → resultado True
        self.assertTrue(is_valid("11994029275"))
