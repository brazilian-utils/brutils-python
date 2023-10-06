from brutils.license_plate import (
    is_valid_license_plate_old_format,
    is_valid_mercosul,
    convert_to_mercosul,
    format,
)

from unittest import TestCase, main


class TestLicensePlate(TestCase):
    def test_is_valid_license_old_format(self):
        # When license plate is valid, returns True
        self.assertTrue(is_valid_license_plate_old_format("ABC1234"))
        self.assertTrue(is_valid_license_plate_old_format("abc1234"))

        # When license plate is valid with whitespaces, returns True
        self.assertTrue(is_valid_license_plate_old_format(" ABC1234    "))

        # When license plate is not string, returns False
        self.assertFalse(is_valid_license_plate_old_format(123456))

        # When license plate is invalid with special characters, returns False
        self.assertFalse(is_valid_license_plate_old_format("ABC-1234"))

        # When license plate is invalid with numbers and letters out of order, returns False
        self.assertFalse(is_valid_license_plate_old_format("A1CA23W"))

        # When license plate is invalid with new format, returns False
        self.assertFalse(is_valid_license_plate_old_format("ABC1D23"))
        self.assertFalse(is_valid_license_plate_old_format("abcd123"))

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

    def test_convert_license_plate_to_mercosul(self):
        # when license plate is not an instance of string, returns None
        self.assertIsNone(convert_to_mercosul(1234567))

        # when license plate has a length different from 7, returns None
        self.assertIsNone(convert_to_mercosul("ABC123"))
        self.assertIsNone(convert_to_mercosul("ABC12356"))

        # when then license plate's 5th character is not a number, return None
        self.assertIsNone(convert_to_mercosul("ABC1A34"))
        self.assertIsNone(convert_to_mercosul("ABC1-34"))
        self.assertIsNone(convert_to_mercosul("ABC1*34"))
        self.assertIsNone(convert_to_mercosul("ABC1_34"))
        self.assertIsNone(convert_to_mercosul("ABC1%34"))
        self.assertIsNone(convert_to_mercosul("ABC1 34"))

        # when then license plate's 5th character is 0, return with a letter A
        self.assertEqual(convert_to_mercosul("AAA1011"), "AAA1A11")
        # when then license plate's 5th character is 1, return with a letter B
        self.assertEqual(convert_to_mercosul("AAA1111"), "AAA1B11")
        # when then license plate's 5th character is 2, return with a letter C
        self.assertEqual(convert_to_mercosul("AAA1211"), "AAA1C11")
        # when then license plate's 5th character is 3, return with a letter D
        self.assertEqual(convert_to_mercosul("AAA1311"), "AAA1D11")
        # when then license plate's 5th character is 4, return with a letter E
        self.assertEqual(convert_to_mercosul("AAA1411"), "AAA1E11")
        # when then license plate's 5th character is 5, return with a letter F
        self.assertEqual(convert_to_mercosul("AAA1511"), "AAA1F11")
        # when then license plate's 5th character is 6, return with a letter G
        self.assertEqual(convert_to_mercosul("AAA1611"), "AAA1G11")
        # when then license plate's 5th character is 7, return with a letter H
        self.assertEqual(convert_to_mercosul("AAA1711"), "AAA1H11")
        # when then license plate's 5th character is 8, return with a letter I
        self.assertEqual(convert_to_mercosul("AAA1811"), "AAA1I11")
        # when then license plate's 5th character is 9, return with a letter J
        self.assertEqual(convert_to_mercosul("AAA1911"), "AAA1J11")

        # when then license is provided in lowercase, it's correctly converted
        # and then returned value is in uppercase
        self.assertEqual(convert_to_mercosul("abc1234"), "ABC1C34")

    def test_format_license_plate(self):
        self.assertEqual(format("ABC1234"), "ABC-1234")
        self.assertEqual(format("abc1234"), "ABC-1234")
        self.assertEqual(format("ABC1D23"), "ABC1D23")
        self.assertEqual(format("abc1d23"), "ABC1D23")
        self.assertIsNone(format("ABCD123"))


if __name__ == "__main__":
    main()
