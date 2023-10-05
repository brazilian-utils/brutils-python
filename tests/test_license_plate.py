from brutils.license_plate import (
    remove_symbols,
)
from unittest import TestCase, main


class TestLicensePlate(TestCase):
    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("ABC-123"), "ABC123")
        self.assertEqual(remove_symbols("abc123"), "abc123")
        self.assertEqual(remove_symbols("ABCD123"), "ABCD123")
        self.assertEqual(remove_symbols("A-B-C-1-2-3"), "ABC123")
        self.assertEqual(remove_symbols("@abc#-#123@"), "@abc##123@")
        self.assertEqual(remove_symbols("@---#"), "@#")
        self.assertEqual(remove_symbols("---"), "")
