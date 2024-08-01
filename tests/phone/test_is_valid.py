from unittest import TestCase, main
from unittest.mock import patch

from brutils.phone import (
    _is_valid_landline,
    _is_valid_mobile,
    is_valid,
)


@patch("brutils.phone._is_valid_landline")
@patch("brutils.phone._is_valid_mobile")
class TestIsValidWithTypeMobile(TestCase):
    def test_when_mobile_is_valid_returns_true(
        self, mock__is_valid_mobile, mock__is_valid_landline
    ):
        mock__is_valid_mobile.return_value = True

        self.assertIs(is_valid("11994029275", "mobile"), True)
        mock__is_valid_mobile.assert_called_once_with("11994029275")
        mock__is_valid_landline.assert_not_called()

    def test_when_mobile_is_not_valid_returns_false(
        self, mock__is_valid_mobile, mock__is_valid_landline
    ):
        mock__is_valid_mobile.return_value = False

        self.assertIs(is_valid("119940", "mobile"), False)
        mock__is_valid_mobile.assert_called_once_with("119940")
        mock__is_valid_landline.assert_not_called()


@patch("brutils.phone._is_valid_mobile")
@patch("brutils.phone._is_valid_landline")
class TestIsValidWithTypeLandline(TestCase):
    def test_when_landline_is_valid_returns_true(
        self, mock__is_valid_landline, mock__is_valid_mobile
    ):
        mock__is_valid_landline.return_value = True

        self.assertIs(is_valid("11994029275", "landline"), True)
        mock__is_valid_landline.assert_called_once_with("11994029275")
        mock__is_valid_mobile.assert_not_called()

    def test_when_landline_is_not_valid_returns_false(
        self, mock__is_valid_landline, mock__is_valid_mobile
    ):
        mock__is_valid_landline.return_value = False

        self.assertIs(is_valid("11994029275", "landline"), False)
        mock__is_valid_landline.assert_called_once_with("11994029275")
        mock__is_valid_mobile.assert_not_called()


@patch("brutils.phone._is_valid_landline")
@patch("brutils.phone._is_valid_mobile")
class TestIsValidWithTypeNone(TestCase):
    def test_when_landline_is_valid(
        self, mock__is_valid_mobile, mock__is_valid_landline
    ):
        mock__is_valid_landline.return_value = True

        self.assertIs(is_valid("1958814933"), True)
        mock__is_valid_landline.assert_called_once_with("1958814933")
        mock__is_valid_mobile.assert_not_called()

    def test_when_landline_invalid_mobile_valid(
        self, mock__is_valid_mobile, mock__is_valid_landline
    ):
        mock__is_valid_landline.return_value = False
        mock__is_valid_mobile.return_value = True

        self.assertIs(is_valid("11994029275"), True)
        mock__is_valid_landline.assert_called_once_with("11994029275")
        mock__is_valid_mobile.assert_called_once_with("11994029275")

    def test_when_landline_and_mobile_are_invalid(
        self, mock__is_valid_mobile, mock__is_valid_landline
    ):
        mock__is_valid_landline.return_value = False
        mock__is_valid_mobile.return_value = False

        self.assertIs(is_valid("11994029275"), False)
        mock__is_valid_landline.assert_called_once_with("11994029275")
        mock__is_valid_mobile.assert_called_once_with("11994029275")


class TestIsValidLandline(TestCase):
    def test__is_valid_landline(self):
        # When landline phone is not string, returns False
        self.assertIs(_is_valid_landline(1938814933), False)

        # When landline phone doesn't contain only digits, returns False
        self.assertIs(_is_valid_landline("(19)388149"), False)

        # When landline phone is an empty string, returns False
        self.assertIs(_is_valid_landline(""), False)

        # When landline phone's len is different of 10, returns False
        self.assertIs(_is_valid_landline("193881"), False)

        # When landline phone's first digit is 0, returns False
        self.assertIs(_is_valid_landline("0938814933"), False)

        # When landline phone's second digit is 0, returns False
        self.assertIs(_is_valid_landline("1038814933"), False)

        # When landline phone's third digit is different of 2,3,4 or 5,
        # returns False
        self.assertIs(_is_valid_landline("1998814933"), False)

        # When landline phone is valid
        self.assertIs(_is_valid_landline("1928814933"), True)
        self.assertIs(_is_valid_landline("1938814933"), True)
        self.assertIs(_is_valid_landline("1948814933"), True)
        self.assertIs(_is_valid_landline("1958814933"), True)
        self.assertIs(_is_valid_landline("3333333333"), True)


class TestIsValidMobile(TestCase):
    def test__is_valid_mobile(self):
        # When mobile is not string, returns False
        self.assertIs(_is_valid_mobile(1), False)

        # When mobile doesn't contain only digits, returns False
        self.assertIs(_is_valid_mobile(119940 - 2927), False)

        # When mobile is an empty string, returns False
        self.assertIs(_is_valid_mobile(""), False)

        # When mobile's len is different of 11, returns False
        self.assertIs(_is_valid_mobile("119940"), False)

        # When mobile's first digit is 0, returns False
        self.assertIs(_is_valid_mobile("01994029275"), False)

        # When mobile's second digit is 0, returns False
        self.assertIs(_is_valid_mobile("90994029275"), False)

        # When mobile's third digit is different of 9, returns False
        self.assertIs(_is_valid_mobile("11594029275"), False)

        # When mobile is valid
        self.assertIs(_is_valid_mobile("99999999999"), True)
        self.assertIs(_is_valid_mobile("11994029275"), True)


if __name__ == "__main__":
    main()
