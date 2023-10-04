from unittest import TestCase, main
from brutils.license_plate import is_valid_license_plate_old_format

class TestLicenSePlate(TestCase):
    def test_is_valid_license_old_format(self):
        # When license plate is valid, returns True
        self.assertTrue(is_valid_license_plate_old_format("ABC123"))
        self.assertTrue(is_valid_license_plate_old_format("abc123"))

        # When license plate is valid with whitespaces, returns True
        self.assertTrue(is_valid_license_plate_old_format(" ABC123    "))
        
        # When license plate is not string, returns False
        self.assertFalse(is_valid_license_plate_old_format(123456))

        # When license plate is invalid with special characters, returns False
        self.assertFalse(is_valid_license_plate_old_format("ABC-123"))

        # When license plate is invalid with numbers and letters out of order,
        # returns False
        self.assertFalse(is_valid_license_plate_old_format("A1CA23"))

        # When license plate is invalid with new format, returns False
        self.assertFalse(is_valid_license_plate_old_format("ABC1D23"))
        self.assertFalse(is_valid_license_plate_old_format("abcd123"))


if __name__ == "__main__":
    main()