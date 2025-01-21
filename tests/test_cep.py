from unittest import TestCase, main
from unittest.mock import MagicMock, patch

from brutils.cep import (
    get_address_from_cep,
    get_cep_information_from_address,
)


@patch("brutils.cep.urlopen")
class TestCEPAPICalls(TestCase):
    @patch("brutils.cep.loads")
    def test_get_address_from_cep_success(self, mock_loads, mock_urlopen):
        mock_loads.return_value = {"cep": "01310-200"}

        self.assertEqual(get_address_from_cep("01310200"), {"cep": "01310-200"})

    def test_get_address_from_cep_with_erro_in_response(
        self, mock_urlopen
    ) -> None:
        mock_data = MagicMock()
        mock_data.read.return_value = {"erro": True}
        mock_urlopen.return_value = mock_data

        self.assertIsNone(get_address_from_cep("013102009"))

    def test_get_address_from_cep_raise_error(self, mock_url_open) -> None:
        mock_url_open.side_effect = ValueError
        self.assertIsNone(get_address_from_cep("01310200"))

    @patch("brutils.cep.loads")
    def test_get_cep_information_from_address_success(
        self, mock_loads, mock_urlopen
    ):
        mock_loads.return_value = [{"cep": "01310-200"}]

        self.assertDictEqual(
            get_cep_information_from_address("SP", "Example", "Rua Example")[0],
            {"cep": "01310-200"},
        )

    @patch("brutils.cep.loads")
    def test_get_cep_information_from_address_success_with_uf_conversion(
        self, mock_loads, mock_urlopen
    ):
        mock_loads.return_value = [{"cep": "01310-200"}]

        self.assertDictEqual(
            get_cep_information_from_address(
                "São Paulo", "Example", "Rua Example"
            )[0],
            {"cep": "01310-200"},
        )

    @patch("brutils.cep.loads")
    def test_get_cep_information_from_address_empty_response(
        self, mock_loads, mock_urlopen
    ):
        mock_loads.return_value = []

        self.assertIsNone(
            get_cep_information_from_address("SP", "Example", "Rua Example")
        )

    @patch("brutils.cep.loads")
    def test_get_cep_information_from_address_raise_exception_invalid_cep(
        self, mock_loads, mock_urlopen
    ):
        mock_loads.return_value = []

        self.assertIsNone(
            get_cep_information_from_address("SP", "Example", "Rua Example")
        )

    def test_get_cep_information_from_address_invalid_cep_dont_raise_exception_invalid_uf(
        self, mock_urlopen
    ):
        self.assertIsNone(
            get_cep_information_from_address("ABC", "Example", "Rua Example")
        )

    def test_get_cep_information_from_address_invalid_cep_raise_value_error(
        self, mock_urlopen
    ):
        mock_urlopen.side_effect = ValueError
        self.assertIsNone(
            get_cep_information_from_address("RS", "Example", "Rua Example")
        )


if __name__ == "__main__":
    main()
