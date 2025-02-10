import unittest
from brutils.rg import is_valid_rg

class TestIsValidRG(unittest.TestCase):
    """
    Unit tests for the is_valid_rg function.

    This test suite checks the validity of different RG formats 
    for all Brazilian states.
    """
    
    def test_is_valid_rg(self):
        valid_rgs = {
            "AC": "12.345.678-9", "AL": "12.345.678", "AP": "123456789", "AM": "12.345.678",
            "BA": "12.345.678", "CE": "12.345.678-9", "DF": "1234567", "ES": "12.345.678",
            "GO": "12.345.678", "MA": "12.345.678", "MT": "12.345.678", "MS": "12.345.678",
            "MG": "MG-12.345.678", "PA": "12.345.678", "PB": "12.345.678", "PR": "12.345.678-9",
            "PE": "123456789", "PI": "12.345.678", "RJ": "12.345.678", "RN": "12.345.678",
            "RS": "1.234.567", "RO": "12.345.678", "RR": "123456789", "SC": "12.345.678",
            "SP": "12.345.678-9", "SE": "12.345.678", "TO": "12.345.678"
        }
        for uf, rg in valid_rgs.items():
            with self.subTest(uf=uf):
                self.assertTrue(is_valid_rg(rg, uf))
    
    def test_invalid_rg_format(self):
        self.assertFalse(is_valid_rg("A12345678", "SP"))
        self.assertFalse(is_valid_rg("1234567890", "SP"))
        self.assertFalse(is_valid_rg("12.345.678-10", "SP"))
        self.assertFalse(is_valid_rg("", "SP"))
        self.assertFalse(is_valid_rg("12.345.678", "SP"))
        self.assertFalse(is_valid_rg("12 345 678", "SP"))
        self.assertFalse(is_valid_rg("12.345.678 9", "SP"))

    def test_invalid_rg_state(self):
        self.assertFalse(is_valid_rg("12.345.678-9", "XX"))
    
    def test_repeated_digits(self):
        for uf in ["SP", "RJ", "MG", "BA", "PR"]:
            with self.subTest(uf=uf):
                self.assertFalse(is_valid_rg("111111111", uf))
                self.assertFalse(is_valid_rg("222222222", uf))
    
    def test_edge_cases(self):
        self.assertFalse(is_valid_rg(None, "SP"))
        self.assertFalse(is_valid_rg(123456789, "SP"))
        self.assertFalse(is_valid_rg("12.345.678-9", None))
        self.assertFalse(is_valid_rg("12.345.678-9", 123))

    def test_invalid_digit_verifier(self):
        self.assertFalse(is_valid_rg("12.345.678-0", "SP"))
        self.assertFalse(is_valid_rg("MG-12.345.679", "MG"))

    def test_rg_with_special_characters(self):
        self.assertTrue(is_valid_rg("12.345.678-9", "SP"))
        self.assertTrue(is_valid_rg("12/345.678-9", "SP"))
