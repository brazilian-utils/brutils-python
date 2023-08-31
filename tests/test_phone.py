import unittest
from unittest.mock import patch

from brutils.phone import is_valid_landline, is_valid_mobile, is_valid

from unittest import TestCase, main


class TestPhone(TestCase):
    def test_is_valid_landline(self):
        # When phone is not string, returns False
        self.assertFalse(is_valid_landline(1938814933))

        # When phone doesn't contain only digits, returns False
        self.assertFalse(is_valid_landline("(19)388149"))

        # When phone is an empty string, returns False
        self.assertFalse(is_valid_landline(""))

        # When phone's len is different of 10, returns False
        self.assertFalse(is_valid_landline("193881"))

        # When phone's first digit is 0, returns False
        self.assertFalse(is_valid_landline("0938814933"))

        # When phone's second digit is 0, returns False
        self.assertFalse(is_valid_landline("1038814933"))

        # When phone's third digit is different of 2,3,4 or 5, returns False
        self.assertFalse(is_valid_landline("1998814933"))

        # When phone is valid
        self.assertTrue(is_valid_landline("1928814933"))
        self.assertTrue(is_valid_landline("1938814933"))
        self.assertTrue(is_valid_landline("1948814933"))
        self.assertTrue(is_valid_landline("1958814933"))
        self.assertTrue(is_valid_landline("3333333333"))

    def test_is_valid_mobile(self):
        # When cellphone is not string, returns False
        self.assertFalse(is_valid_mobile(1))

        # When cellphone doesn't contain only digits, returns False
        self.assertFalse(is_valid_mobile(119940 - 2927))

        # When cellphone is an empty string, returns False
        self.assertFalse(is_valid_mobile(""))

        # When cellphone's len is different of 11, returns False
        self.assertFalse(is_valid_mobile("119940"))

        # When cellphone's first digit is 0, returns False
        self.assertFalse(is_valid_mobile("01994029275"))

        # When cellphone's second digit is 0, returns False
        self.assertFalse(is_valid_mobile("90994029275"))

        # When cellphone's third digit is different of 9, returns False
        self.assertFalse(is_valid_mobile("11594029275"))

        # When cellphone is valid
        self.assertTrue(is_valid_mobile("99999999999"))
        self.assertTrue(is_valid_mobile("11994029275"))

    def test_is_valid(self):
        # Mock is_valid_landline to return True
        with patch(
            "brutils.phone.is_valid_landline", return_value=True
        ) as mock_is_valid_landline:
            # When landline phone is_valid, returns True
            self.assertTrue(is_valid_landline("1958814933"))

            # Checks if function is_valid_landline is called with the correct argument
            mock_is_valid_landline.assert_called_once_with("1958814933")

        # Mock is_valid_landline to return False
        with patch(
            "brutils.phone.is_valid_landline", return_value=False
        ) as mock_is_valid_landline:
            # When landline phone isn't valid, returns False
            self.assertFalse(is_valid_landline("1998814933"))

            # Checks if function is_valid_landline is called with the correct argument
            mock_is_valid_landline.assert_called_once_with("1998814933")

        # Mock is_valid_mobile to return True
        with patch(
            "brutils.phone.is_valid_mobile", return_value=True
        ) as mock_is_valid_mobile:
            # When mobile phone is_valid, returns True
            self.assertTrue(is_valid_mobile("11994029275"))

            # Checks if function is_valid_mobile is called with the correct argument
            mock_is_valid_mobile.assert_called_once_with("11994029275")

        # Mock is_valid_mobile to return False
        with patch(
            "brutils.phone.is_valid_mobile", return_value=False
        ) as mock_is_valid_mobile:
            # When mobile phone isn't valid, returns False
            self.assertFalse(is_valid_mobile("11594029275"))

            # Checks if function is_valid_mobile is called with the correct argument
            mock_is_valid_mobile.assert_called_once_with("11594029275")


if __name__ == "__main__":
    main()
