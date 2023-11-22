from unittest import TestCase, main
from unittest.mock import patch

from brutils.license_plate import (
    _is_valid_mercosul,
    _is_valid_old_format,
    convert_to_mercosul,
    format,
    generate,
    get_format,
    is_valid,
    remove_symbols,
)


class TestLicensePlate(TestCase):
    def test_is_valid_when_type_is_old_format(self):
        # Mock _is_valid_old_format return True
        with patch(
            "brutils.license_plate._is_valid_mercosul"
        ) as mock__is_valid_mercosul:
            with patch(
                "brutils.license_plate._is_valid_old_format", return_value=True
            ) as mock__is_valid_old_format:
                # When license plate old format is_valid, returns True
                self.assertIs(is_valid("ABC1234", "old_format"), True)

                # Checks if function _is_valid_old_format is called with the
                # correct argument
                mock__is_valid_old_format.assert_called_once_with("ABC1234")

                # Checks if function _is_valid_mercosul is not called
                mock__is_valid_mercosul.assert_not_called()

        # Mock _is_valid_old_format return False
        with patch(
            "brutils.license_plate._is_valid_mercosul"
        ) as mock__is_valid_mercosul:
            with patch(
                "brutils.license_plate._is_valid_old_format", return_value=False
            ) as mock__is_valid_old_format:
                # When licence plate old format isn't valid, returns False
                self.assertIs(is_valid("123456", "old_format"), False)

                # Checks if function _is_valid_old_format is called with the
                # correct argument
                mock__is_valid_old_format.assert_called_once_with("123456")

                # Checks if function _is_valid_mercosul is not called
                mock__is_valid_mercosul.assert_not_called()

    def test_is_valid_when_type_is_mercosul(self):
        # Mock _is_valid_mercosul to return True
        with patch(
            "brutils.license_plate._is_valid_old_format",
        ) as mock__is_valid_old_format:
            with patch(
                "brutils.license_plate._is_valid_mercosul", return_value=True
            ) as mock__is_valid_mercosul:
                # When license plate as mercosul is_valid, returns True
                self.assertIs(is_valid("ABC4E67", "mercosul"), True)

                # Checks if function _is_valid_mercosu is called with the
                # correct argument
                mock__is_valid_mercosul.assert_called_once_with("ABC4E67")

                # Checks if function _is_valid_old_format is not called
                mock__is_valid_old_format.assert_not_called()

        # Mock _is_valid_mercosul to return False
        with patch(
            "brutils.license_plate._is_valid_old_format",
        ) as mock__is_valid_old_format:
            with patch(
                "brutils.license_plate._is_valid_mercosul", return_value=False
            ) as mock__is_valid_mercosul:
                # When mercosul plate is not valid, returns False
                self.assertIs(is_valid("11994029275", "mercosul"), False)

                # Checks if function _is_valid_mercosul is called with the
                # correct argument
                mock__is_valid_mercosul.assert_called_once_with("11994029275")

                # Checks if function _is_valid_old_format is not called
                mock__is_valid_old_format.assert_not_called()

    def test_is_valid_when_type_is_none(self):
        # Mock _is_valid_mercosul to return True
        with patch(
            "brutils.license_plate._is_valid_mercosul", return_value=True
        ) as mock__is_valid_mercosul:
            with patch(
                "brutils.license_plate._is_valid_old_format"
            ) as mock__is_valid_old_format:
                # When license plate as mercosul is_valid, returns True
                self.assertIs(is_valid("ABC4E67"), True)

                # Checks if function _is_valid_mercosul is called with the
                # correct argument
                mock__is_valid_mercosul.assert_called_once_with("ABC4E67")

                # Checks if function _is_valid_old_format is not called
                mock__is_valid_old_format.assert_not_called()

        # Mock _is_valid_mercosul to return False,
        # _is_valid_old_format return True
        with patch(
            "brutils.license_plate._is_valid_mercosul", return_value=False
        ) as mock__is_valid_mercosul:
            with patch(
                "brutils.license_plate._is_valid_old_format", return_value=True
            ) as mock__is_valid_old_format:
                # When license plate old format is_valid, returns True
                self.assertIs(is_valid("ABC1234"), True)

                # Checks if function _is_valid_mercosul is called with the
                # correct argument
                mock__is_valid_mercosul.assert_called_once_with("ABC4E67")
                # Checks if function _is_valid_old_format is called with the
                # correct argument
                mock__is_valid_old_format.assert_called_once_with("ABC1234")

        # Mock _is_valid_mercosul to return False,
        # _is_valid_old_format return False
        with patch(
            "brutils.license_plate._is_valid_mercosul", return_value=False
        ) as mock__is_valid_mercosul:
            with patch(
                "brutils.license_plate._is_valid_old_format", return_value=False
            ) as mock__is_valid_old_format:
                # When license isn't valid, returns False
                self.assertIs(is_valid("ABC-123"), False)

                # Checks if function _is_valid_mercosul is called with the
                # correct argument
                mock__is_valid_mercosul.assert_called_once_with("ABC-123")
                # Checks if function _is_valid_old_format is called with the
                # correct argument
                mock__is_valid_old_format.assert_called_once_with("123-456")

    def test_is_valid(self):
        # Invalid old license plate
        self.assertFalse(is_valid(123456))
        self.assertFalse(is_valid("123-456"))

        # Invalid mercosul license plate
        self.assertFalse(is_valid("ABCDEFG"))
        self.assertFalse(is_valid("ABC-123"))

        # Valid old license plate
        self.assertTrue(is_valid("ABC1234"))
        self.assertTrue(is_valid("abc1234"))

        # Valid mercosul license plate
        self.assertTrue(is_valid("ABC4E67"))
        self.assertTrue(is_valid("XXX9X99"))

    def test__is_valid_old_format(self):
        # When license plate is valid, returns True
        self.assertTrue(_is_valid_old_format("ABC1234"))
        self.assertTrue(_is_valid_old_format("abc1234"))

        # When license plate is valid with whitespaces, returns True
        self.assertTrue(_is_valid_old_format(" ABC1234    "))

        # When license plate is not string, returns False
        self.assertFalse(_is_valid_old_format(123456))

        # When license plate is invalid with special characters, returns False
        self.assertFalse(_is_valid_old_format("ABC-1234"))

        # When license plate is invalid with numbers and letters out of order,
        # returns False
        self.assertFalse(_is_valid_old_format("A1CA23W"))

        # When license plate is invalid with new format, returns False
        self.assertFalse(_is_valid_old_format("ABC1D23"))
        self.assertFalse(_is_valid_old_format("abcd123"))

    def test__is_valid_mercosul(self):
        # When license plate is not string, returns False
        self.assertIs(_is_valid_mercosul(1234567), False)

        # When license plate doesn't match the pattern LLLNLNN, returns False
        self.assertIs(_is_valid_mercosul("ABCDEFG"), False)
        self.assertIs(_is_valid_mercosul("1234567"), False)
        self.assertIs(_is_valid_mercosul("ABC4567"), False)
        self.assertIs(_is_valid_mercosul("ABCD567"), False)
        self.assertIs(_is_valid_mercosul("ABC45F7"), False)
        self.assertIs(_is_valid_mercosul("ABC456G"), False)
        self.assertIs(_is_valid_mercosul("ABC123"), False)

        # When license plate is an empty string, returns False
        self.assertIs(_is_valid_mercosul(""), False)

        # When license plate's length is different of 7, returns False
        self.assertIs(_is_valid_mercosul("ABC4E678"), False)

        # When license plate has separator, returns false
        self.assertIs(_is_valid_mercosul("ABC-1D23"), False)

        # When license plate is valid
        self.assertIs(_is_valid_mercosul("ABC4E67"), True)
        self.assertIs(_is_valid_mercosul("AAA1A11"), True)
        self.assertIs(_is_valid_mercosul("XXX9X99"), True)

        # Check if function is case insensitive
        self.assertIs(_is_valid_mercosul("abc4e67"), True)

    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("ABC-123"), "ABC123")
        self.assertEqual(remove_symbols("abc123"), "abc123")
        self.assertEqual(remove_symbols("ABCD123"), "ABCD123")
        self.assertEqual(remove_symbols("A-B-C-1-2-3"), "ABC123")
        self.assertEqual(remove_symbols("@abc#-#123@"), "@abc##123@")
        self.assertEqual(remove_symbols("@---#"), "@#")
        self.assertEqual(remove_symbols("---"), "")

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

    def test_get_format(self):
        # Old format
        self.assertEqual(get_format("ABC1234"), "LLLNNNN")
        self.assertEqual(get_format("abc1234"), "LLLNNNN")

        # Mercosul
        self.assertEqual(get_format("ABC4E67"), "LLLNLNN")
        self.assertEqual(get_format("XXX9X99"), "LLLNLNN")

        # Invalid
        self.assertIsNone(get_format(None))
        self.assertIsNone(get_format(""))
        self.assertIsNone(get_format("ABC-1D23"))
        self.assertIsNone(get_format("invalid plate"))

    def test_generate_license_plate(self):
        with patch("brutils.license_plate.choice", return_value="X"):
            with patch("brutils.license_plate.randint", return_value=9):
                self.assertEqual(generate(format="LLLNNNN"), "XXX9999")
                self.assertEqual(generate(format="LLLNLNN"), "XXX9X99")

        for _ in range(10_000):
            self.assertTrue(_is_valid_mercosul(generate(format="LLLNLNN")))

        for _ in range(10_000):
            self.assertTrue(_is_valid_old_format(generate(format="LLLNNNN")))

        # When no format is provided, returns a valid Mercosul license plate
        self.assertTrue(_is_valid_mercosul(generate()))

        # When invalid format is provided, returns None
        self.assertIsNone(generate("LNLNLNL"))


if __name__ == "__main__":
    main()
