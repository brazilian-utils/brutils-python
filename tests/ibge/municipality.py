import gzip
from unittest import TestCase, main
from unittest.mock import MagicMock, patch

from requests import HTTPError

from brutils.ibge.municipality import get_municipality_by_code


class TestIBGE(TestCase):
    def test_get_municipality_by_code(self):
        self.assertEqual(
            get_municipality_by_code("3550308"), ("São Paulo", "SP")
        )
        self.assertEqual(
            get_municipality_by_code("3304557"), ("Rio de Janeiro", "RJ")
        )
        self.assertEqual(get_municipality_by_code("5208707"), ("Goiânia", "GO"))
        self.assertIsNone(get_municipality_by_code("1234567"))

    from unittest import TestCase, main

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code_success(self, mock_urlopen):
        # Mock data for a valid municipality code
        valid_json = '{"nome":"São Paulo","microrregiao":{"mesorregiao":{"UF":{"sigla":"SP"}}}'
        compressed_data = gzip.compress(valid_json.encode("utf-8"))

        mock_response = MagicMock()
        mock_response.read.return_value = compressed_data
        mock_urlopen.return_value = mock_response

        self.assertEqual(
            get_municipality_by_code("3550308"), ("São Paulo", "SP")
        )
        self.assertEqual(
            get_municipality_by_code("3304557"), ("Rio de Janeiro", "RJ")
        )
        self.assertEqual(get_municipality_by_code("5208707"), ("Goiânia", "GO"))

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code_empty_data(self, mock_urlopen):
        # Mock data for an empty response
        empty_json = "[]"
        compressed_data = gzip.compress(empty_json.encode("utf-8"))

        mock_response = MagicMock()
        mock_response.read.return_value = compressed_data
        mock_urlopen.return_value = mock_response

        self.assertIsNone(get_municipality_by_code("1234567"))

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code_http_error(self, mock_urlopen):
        # Mock HTTPError
        mock_urlopen.side_effect = HTTPError(
            url="https://servicodados.ibge.gov.br/api/v1/localidades/municipios/1234567",
            code=404,
            msg="Not Found",
            hdrs=None,
            fp=None,
        )

        self.assertIsNone(get_municipality_by_code("1234567"))

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code_unexpected_error(self, mock_urlopen):
        # Mock an unexpected error during URL open
        mock_urlopen.side_effect = Exception("Some unexpected error")

        with self.assertRaises(Exception):
            get_municipality_by_code("1234567")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
