from unittest import TestCase, main
from unittest.mock import patch
from urllib.error import HTTPError

from brutils.cnpj import (
    CNPJNotFound,
    InvalidCNPJ,
    _checksum,
    _hashdigit,
    display,
    format_cnpj,
    generate,
    get_cnpj_information,
    is_valid,
    remove_symbols,
    sieve,
    validate,
)


class TestCNPJ(TestCase):
    def test_sieve(self):
        self.assertEqual(sieve("00000000000"), "00000000000")
        self.assertEqual(sieve("12.345.678/0001-90"), "12345678000190")
        self.assertEqual(sieve("134..2435/.-1892.-"), "13424351892")
        self.assertEqual(sieve("abc1230916*!*&#"), "abc1230916*!*&#")
        self.assertEqual(
            sieve("ab.c1.--.2-3/09.-1-./6/-.*.-!*&#"), "abc1230916*!*&#"
        )
        self.assertEqual(sieve("/...---.../"), "")

    def test_display(self):
        self.assertEqual(display("00000000000109"), "00.000.000/0001-09")
        self.assertIsNone(display("00000000000000"))
        self.assertIsNone(display("0000000000000"))
        self.assertIsNone(display("0000000000000a"))

    def test_validate(self):
        self.assertIs(validate("34665388000161"), True)
        self.assertIs(validate("52599927000100"), False)
        self.assertIs(validate("00000000000"), False)

    def test_is_valid(self):
        # When CNPJ is not string, returns False
        self.assertIs(is_valid(1), False)

        # When CNPJ's len is different of 14, returns False
        self.assertIs(is_valid("1"), False)

        # When CNPJ does not contain only digits, returns False
        self.assertIs(is_valid("1112223334445-"), False)

        # When CNPJ has only the same digit, returns false
        self.assertIs(is_valid("11111111111111"), False)

        # When rest_1 is lt 2 and the 13th digit is not 0, returns False
        self.assertIs(is_valid("1111111111315"), False)

        # When rest_1 is gte 2 and the 13th digit is not (11 - rest), returns
        # False
        self.assertIs(is_valid("1111111111115"), False)

        # When rest_2 is lt 2 and the 14th digit is not 0, returns False
        self.assertIs(is_valid("11111111121205"), False)

        # When rest_2 is gte 2 and the 14th digit is not (11 - rest), returns
        # False
        self.assertIs(is_valid("11111111113105"), False)

        # When CNPJ is valid
        self.assertIs(is_valid("34665388000161"), True)
        self.assertIs(is_valid("01838723000127"), True)

    def test_generate(self):
        for _ in range(10_000):
            self.assertIs(validate(generate()), True)
            self.assertIsNotNone(display(generate()))

    def test__hashdigit(self):
        self.assertEqual(_hashdigit("00000000000000", 13), 0)
        self.assertEqual(_hashdigit("00000000000000", 14), 0)
        self.assertEqual(_hashdigit("52513127000292", 13), 9)
        self.assertEqual(_hashdigit("52513127000292", 14), 9)

    def test__checksum(self):
        self.assertEqual(_checksum("00000000000000"), "00")
        self.assertEqual(_checksum("52513127000299"), "99")


@patch("brutils.cnpj.sieve")
class TestRemoveSymbols(TestCase):
    def test_remove_symbols(self, mock_sieve):
        # When call remove_symbols, it calls sieve
        remove_symbols("12.345.678/0001-90")
        mock_sieve.assert_called()


@patch("brutils.cnpj.is_valid")
class TestIsValidToFormat(TestCase):
    def test_when_cnpj_is_valid_returns_true_to_format(self, mock_is_valid):
        mock_is_valid.return_value = True

        # When cnpj is_valid, returns formatted cnpj
        self.assertEqual(format_cnpj("01838723000127"), "01.838.723/0001-27")

        # Checks if function is_valid_cnpj is called
        mock_is_valid.assert_called_once_with("01838723000127")

    def test_when_cnpj_is_not_valid_returns_none(self, mock_is_valid):
        mock_is_valid.return_value = False

        # When cnpj isn't valid, returns None
        self.assertIsNone(format_cnpj("01838723000127"))


@patch("brutils.cnpj.urlopen")
class TestCNPJAPICalls(TestCase):
    @patch("brutils.cnpj.loads")
    def test_get_cnpj_information_success(self, mock_loads, mock_urlopen):
        mock_data = {
            "cnpj_raiz": "42064856",
            "razao_social": "C D TIRABASSI JUNIOR TECNOLOGIA DA INFORMACAO LTDA",
            "estabelecimento": {"nome_fantasia": "BITIZE"},
        }
        mock_loads.return_value = mock_data

        result = get_cnpj_information("42.064.856/0001-70", True)
        self.assertEqual(result["cnpj_raiz"], "42064856")
        self.assertEqual(
            result["razao_social"],
            "C D TIRABASSI JUNIOR TECNOLOGIA DA INFORMACAO LTDA",
        )

    def test_get_cnpj_information_invalid_cnpj_not_raise(self, mock_urlopen):
        self.assertIsNone(get_cnpj_information("invalid_cnpj"))

    def test_get_cnpj_information_invalid_cnpj_raise_exception(
        self, mock_urlopen
    ):
        with self.assertRaises(InvalidCNPJ):
            get_cnpj_information("invalid_cnpj", True)

    def test_get_cnpj_information_http_400_not_raise(self, mock_urlopen):
        http_error = HTTPError(
            url="https://publica.cnpj.ws/cnpj/42064856000170",
            code=400,
            msg="Bad Request",
            hdrs={},
            fp=None,
        )
        mock_urlopen.side_effect = http_error

        self.assertIsNone(get_cnpj_information("42.064.856/0001-70"))

    def test_get_cnpj_information_http_400_raise_exception(self, mock_urlopen):
        http_error = HTTPError(
            url="https://publica.cnpj.ws/cnpj/42064856000170",
            code=400,
            msg="Bad Request",
            hdrs={},
            fp=None,
        )
        mock_urlopen.side_effect = http_error

        with self.assertRaises(InvalidCNPJ):
            get_cnpj_information("42.064.856/0001-70", True)

    def test_get_cnpj_information_http_404_not_raise(self, mock_urlopen):
        http_error = HTTPError(
            url="https://publica.cnpj.ws/cnpj/42064856000170",
            code=404,
            msg="Not Found",
            hdrs={},
            fp=None,
        )
        mock_urlopen.side_effect = http_error

        self.assertIsNone(get_cnpj_information("42.064.856/0001-70"))

    def test_get_cnpj_information_http_404_raise_exception(self, mock_urlopen):
        http_error = HTTPError(
            url="https://publica.cnpj.ws/cnpj/42064856000170",
            code=404,
            msg="Not Found",
            hdrs={},
            fp=None,
        )
        mock_urlopen.side_effect = http_error

        with self.assertRaises(CNPJNotFound):
            get_cnpj_information("42.064.856/0001-70", True)

    def test_get_cnpj_information_other_http_error_not_raise(
        self, mock_urlopen
    ):
        http_error = HTTPError(
            url="https://publica.cnpj.ws/cnpj/42064856000170",
            code=500,
            msg="Internal Server Error",
            hdrs={},
            fp=None,
        )
        mock_urlopen.side_effect = http_error

        self.assertIsNone(get_cnpj_information("42.064.856/0001-70"))

    def test_get_cnpj_information_other_http_error_raise_exception(
        self, mock_urlopen
    ):
        http_error = HTTPError(
            url="https://publica.cnpj.ws/cnpj/42064856000170",
            code=500,
            msg="Internal Server Error",
            hdrs={},
            fp=None,
        )
        mock_urlopen.side_effect = http_error

        with self.assertRaises(HTTPError):
            get_cnpj_information("42.064.856/0001-70", True)

    def test_get_cnpj_information_generic_exception_not_raise(
        self, mock_urlopen
    ):
        mock_urlopen.side_effect = Exception("Generic error")

        self.assertIsNone(get_cnpj_information("42.064.856/0001-70"))

    def test_get_cnpj_information_generic_exception_raise_exception(
        self, mock_urlopen
    ):
        mock_urlopen.side_effect = Exception("Generic error")

        with self.assertRaises(CNPJNotFound):
            get_cnpj_information("42.064.856/0001-70", True)


if __name__ == "__main__":
    main()
