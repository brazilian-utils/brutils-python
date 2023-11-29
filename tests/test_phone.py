from unittest import TestCase, main
from unittest.mock import patch

from brutils.phone import (
    _is_valid_landline,
    _is_valid_mobile,
    format_phone,
    generate,
    is_valid,
    remove_international_code_phone,
    remove_symbols_phone,
)


class TestPhone(TestCase):
    def test_is_valid_when_type_is_mobile(self):
        # Mock _is_valid_mobile return True
        with patch(
            "brutils.phone._is_valid_landline"
        ) as mock__is_valid_landline:
            with patch(
                "brutils.phone._is_valid_mobile", return_value=True
            ) as mock__is_valid_mobile:
                # When mobile phone is_valid, returns True
                self.assertIs(is_valid("11994029275", "mobile"), True)

                # Checks if function _is_valid_mobile is called with the
                # correct argument
                mock__is_valid_mobile.assert_called_once_with("11994029275")

                # Checks if function _is_valid_mobile is not called
                mock__is_valid_landline.assert_not_called()

        # Mock _is_valid_mobile return False
        with patch(
            "brutils.phone._is_valid_landline"
        ) as mock__is_valid_landline:
            with patch(
                "brutils.phone._is_valid_mobile", return_value=False
            ) as mock__is_valid_mobile:
                # When mobile phone is_valid, returns False
                self.assertIs(is_valid("11994029275", "mobile"), False)

                # Checks if function _is_valid_mobile is called with the
                # correct argument
                mock__is_valid_mobile.assert_called_once_with("11994029275")

                # Checks if function _is_valid_mobile is not called
                mock__is_valid_landline.assert_not_called()

    def test_is_valid_when_type_is_landline(self):
        # Mock _is_valid_landline to return True
        with patch(
            "brutils.phone._is_valid_mobile",
        ) as mock__is_valid_mobile:
            with patch(
                "brutils.phone._is_valid_landline", return_value=True
            ) as mock__is_valid_landline:
                # When mobile phone is_valid, returns True
                self.assertIs(is_valid("11994029275", "landline"), True)

                # Checks if function _is_valid_landline is called with the
                # correct argument
                mock__is_valid_landline.assert_called_once_with("11994029275")

                # Checks if function _is_valid_mobile is not called
                mock__is_valid_mobile.assert_not_called()

        # Mock _is_valid_landline to return False
        with patch(
            "brutils.phone._is_valid_mobile",
        ) as mock__is_valid_mobile:
            with patch(
                "brutils.phone._is_valid_landline", return_value=False
            ) as mock__is_valid_landline:
                # When mobile phone is_valid, returns False
                self.assertIs(is_valid("11994029275", "landline"), False)

                # Checks if function _is_valid_landline is called with the
                # correct argument
                mock__is_valid_landline.assert_called_once_with("11994029275")

                # Checks if function _is_valid_mobile is not called
                mock__is_valid_mobile.assert_not_called()

    def test_is_valid_when_type_is_none(self):
        # Mock _is_valid_landline to return True
        with patch(
            "brutils.phone._is_valid_landline", return_value=True
        ) as mock__is_valid_landline:
            with patch(
                "brutils.phone._is_valid_mobile"
            ) as mock__is_valid_mobile:
                # When landline phone is_valid, returns True
                self.assertIs(is_valid("1958814933"), True)

                # Checks if function _is_valid_landline is called with the
                # correct argument
                mock__is_valid_landline.assert_called_once_with("1958814933")
                # Checks if function _is_valid_mobile is not called
                mock__is_valid_mobile.assert_not_called()

        # Mock _is_valid_landline to return False, _is_valid_mobile return True
        with patch(
            "brutils.phone._is_valid_landline", return_value=False
        ) as mock__is_valid_landline:
            with patch(
                "brutils.phone._is_valid_mobile", return_value=True
            ) as mock__is_valid_mobile:
                # When mobile phone is_valid, returns True
                self.assertIs(is_valid("11994029275"), True)

                # Checks if function _is_valid_landline is called with the
                # correct argument
                mock__is_valid_landline.assert_called_once_with("11994029275")
                # Checks if function _is_valid_mobile is called with the
                # correct argument
                mock__is_valid_mobile.assert_called_once_with("11994029275")

        # Mock _is_valid_landline to return False, _is_valid_mobile return False
        with patch(
            "brutils.phone._is_valid_landline", return_value=False
        ) as mock__is_valid_landline:
            with patch(
                "brutils.phone._is_valid_mobile", return_value=False
            ) as mock__is_valid_mobile:
                # When landline phone isn't valid, returns False
                self.assertIs(is_valid("11994029275"), False)

                # Checks if function _is_valid_landline is called with the
                # correct argument
                mock__is_valid_landline.assert_called_once_with("11994029275")
                # Checks if function _is_valid_mobile is called with the
                # correct argument
                mock__is_valid_mobile.assert_called_once_with("11994029275")

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

    def test_remove_symbols_phone(self):
        # When the string empty, it returns an empty string
        self.assertEqual(remove_symbols_phone(""), "")

        # When there are no symbols to remove, it returns the same string
        self.assertEqual(remove_symbols_phone("21994029275"), "21994029275")

        # When there are symbols to remove, it returns the string without
        # symbols
        self.assertEqual(remove_symbols_phone("(21)99402-9275"), "21994029275")
        self.assertEqual(remove_symbols_phone("(21)2569-6969"), "2125696969")

        # When there are extra symbols, it only removes the specified symbols
        self.assertEqual(
            remove_symbols_phone("(21) 99402-9275!"), "21994029275!"
        )

        # When the string contains non-numeric characters, it returns the
        # string without the specified symbols
        self.assertEqual(remove_symbols_phone("(21)ABC-DEF"), "21ABCDEF")

        # When the phone number contains a plus symbol and spaces, they are
        # removed
        self.assertEqual(
            remove_symbols_phone("+55 21 99402-9275"), "5521994029275"
        )

        # When the phone number contains multiple spaces, all are removed
        self.assertEqual(
            remove_symbols_phone("55 21  99402 9275"), "5521994029275"
        )

        # When the phone number contains a mixture of all specified symbols,
        # all are removed
        self.assertEqual(
            remove_symbols_phone("+55 (21) 99402-9275"), "5521994029275"
        )

    def test_format_phone_number(self):
        # When is a invalid number
        self.assertEqual(format_phone("333333"), None)

        # When is a mobile number
        self.assertEqual(format_phone("21994029275"), "(21)99402-9275")
        self.assertEqual(format_phone("21994029275"), "(21)99402-9275")
        self.assertEqual(format_phone("21994029275"), "(21)99402-9275")
        self.assertEqual(format_phone("11994029275"), "(11)99402-9275")

        # When is a landline number
        self.assertEqual(format_phone("1928814933"), "(19)2881-4933")
        self.assertEqual(format_phone("1938814933"), "(19)3881-4933")
        self.assertEqual(format_phone("1948814933"), "(19)4881-4933")
        self.assertEqual(format_phone("1958814933"), "(19)5881-4933")
        self.assertEqual(format_phone("3333333333"), "(33)3333-3333")

    def test_generate(self):
        for _ in range(25):
            with self.subTest():
                no_type_phone_generated = generate()
                self.assertIs(is_valid(no_type_phone_generated), True)
                mobile_phone_generated = generate("mobile")
                self.assertIs(_is_valid_mobile(mobile_phone_generated), True)
                landline_phone_generated = generate("landline")
                self.assertIs(_is_valid_landline(landline_phone_generated), True)

    def test_remove_international_code_phone(self):
        # When the phone number does not have the international code,
        # return the same phone number
        self.assertEqual(
            remove_international_code_phone("21994029275"), "21994029275"
        )
        self.assertEqual(
            remove_international_code_phone("55994024478"), "55994024478"
        )
        self.assertEqual(
            remove_international_code_phone("994024478"), "994024478"
        )

        # When the phone number has the international code,
        # return phone number without international code
        self.assertEqual(
            remove_international_code_phone("5521994029275"), "21994029275"
        )
        self.assertEqual(
            remove_international_code_phone("+5521994029275"), "+21994029275"
        )
        self.assertEqual(
            remove_international_code_phone("+5555994029275"), "+55994029275"
        )
        self.assertEqual(
            remove_international_code_phone("5511994029275"), "11994029275"
        )


if __name__ == "__main__":
    main()
