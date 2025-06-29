from unittest import TestCase, main
from unittest.mock import patch

from brutils.pis import (
    _checksum,
    format_pis,
    generate,
    is_valid_pis_pasep,
    remove_symbols,
)


class TestPIS(TestCase):
    def test_is_valid_pis_pasep(self):
        # When PIS is not string, returns False
        self.assertIs(is_valid_pis_pasep(1), False)
        self.assertIs(is_valid_pis_pasep([]), False)
        self.assertIs(is_valid_pis_pasep({}), False)
        self.assertIs(is_valid_pis_pasep(None), False)

        # When PIS's len is different of 11, returns False
        self.assertIs(is_valid_pis_pasep("123456789"), False)

        # When PIS does not contain only digits, returns False
        self.assertIs(is_valid_pis_pasep("123pis"), False)
        self.assertIs(is_valid_pis_pasep("123456789ab"), False)
        self.assertIs(is_valid_pis_pasep("123.456.789-X"), False)
        self.assertIs(is_valid_pis_pasep("123.456.789-0-1"), False)

        # When checksum digit doesn't match last digit, returns False
        self.assertIs(is_valid_pis_pasep("11111111111"), False)
        self.assertIs(is_valid_pis_pasep("11111111215"), False)
        self.assertIs(is_valid_pis_pasep("12038619493"), False)
        self.assertIs(is_valid_pis_pasep("123.45678.90-0"), False)

        # When PIS is valid
        self.assertIs(is_valid_pis_pasep("12038619494"), True)
        self.assertIs(is_valid_pis_pasep("12016784018"), True)
        self.assertIs(is_valid_pis_pasep("12083210826"), True)
        self.assertIs(is_valid_pis_pasep("123.45678.90-1"), True)
        self.assertIs(is_valid_pis_pasep("120.89315.65-8"), True)

    def test_checksum(self):
        # Checksum digit is 0 when the subtracted number is 10 or 11
        self.assertEqual(_checksum("1204152015"), 0)
        self.assertEqual(_checksum("1204433157"), 0)

        # Checksum digit is equal the subtracted number
        self.assertEqual(_checksum("1204917738"), 2)
        self.assertEqual(_checksum("1203861949"), 4)
        self.assertEqual(_checksum("1208321082"), 6)

    def test_generate(self):
        for _ in range(10_000):
            self.assertIs(is_valid_pis_pasep(generate()), True)

    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("00000000000"), "00000000000")
        self.assertEqual(remove_symbols("170.33259.50-4"), "17033259504")
        self.assertEqual(remove_symbols("134..2435/.-1892.-"), "1342435/1892")
        self.assertEqual(remove_symbols("abc1230916*!*&#"), "abc1230916*!*&#")
        self.assertEqual(remove_symbols("...---..."), "")

    @patch("brutils.pis.is_valid")
    def test_format_valid_pis(self, mock_is_valid_pis_pasep):
        mock_is_valid_pis_pasep.return_value = True

        # When PIS is_valid, returns formatted PIS
        self.assertEqual(format_pis("14372195539"), "143.72195.53-9")

        # Checks if function is_valid_pis is called
        mock_is_valid_pis_pasep.assert_called_once_with("14372195539")

    @patch("brutils.pis.is_valid")
    def test_format_invalid_pis(self, mock_is_valid_pis_pasep):
        mock_is_valid_pis_pasep.return_value = False

        # When PIS isn't valid, returns None
        self.assertIsNone(format_pis("14372195539"))


if __name__ == "__main__":
    main()
