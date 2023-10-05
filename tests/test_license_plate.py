# from unittest.mock import patch

# from brutils.phone import is_valid_landline, is_valid_mobile, is_valid
from brutils.license_plate import is_valid_mercosul

from unittest import TestCase, main


class TestLicensePlate(TestCase):
    def test_is_valid_license_plate_mercosul(self):
        # When license plate is not string, returns False
        self.assertIs(is_valid_mercosul(1234567), False)

        # When license plate doesn't match the pattern LLLNLNN, returns False
        self.assertIs(is_valid_mercosul("ABCDEFG"), False)
        self.assertIs(is_valid_mercosul("1234567"), False)
        self.assertIs(is_valid_mercosul("ABC4567"), False)
        self.assertIs(is_valid_mercosul("ABCD567"), False)
        self.assertIs(is_valid_mercosul("ABC45F7"), False)
        self.assertIs(is_valid_mercosul("ABC456G"), False)
        self.assertIs(is_valid_mercosul("ABC123"), False)

        # When license plate is an empty string, returns False
        self.assertIs(is_valid_mercosul(""), False)

        # When license plate's length is different of 7, returns False
        self.assertIs(is_valid_mercosul("ABC4E678"), False)

        # When license plate has separator, returns false
        self.assertIs(is_valid_mercosul("ABC-1D23"), False)

        # When license plate is valid
        self.assertIs(is_valid_mercosul("ABC4E67"), True)
        self.assertIs(is_valid_mercosul("AAA1A11"), True)
        self.assertIs(is_valid_mercosul("XXX9X99"), True)

        # Check if function is case insensitive
        self.assertIs(is_valid_mercosul("abc4e67"), True)


if __name__ == "__main__":
    main()
