import gzip
from json import JSONDecodeError, dumps
from unittest import TestCase, main
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

from brutils.ibge.municipality import (
    get_code_by_municipality_name,
    get_municipality_by_code,
)


class TestIBGE(TestCase):
    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code(self, mock):
        def mock_response(url):
            responses = {
                "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3550308": dumps(
                    {
                        "nome": "São Paulo",
                        "microrregiao": {
                            "mesorregiao": {"UF": {"sigla": "SP"}}
                        },
                    }
                ).encode("utf-8"),
                "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3304557": dumps(
                    {
                        "nome": "Rio de Janeiro",
                        "microrregiao": {
                            "mesorregiao": {"UF": {"sigla": "RJ"}}
                        },
                    }
                ).encode("utf-8"),
                "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/5208707": dumps(
                    {
                        "nome": "Goiânia",
                        "microrregiao": {
                            "mesorregiao": {"UF": {"sigla": "GO"}}
                        },
                    }
                ).encode("utf-8"),
                "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/1234567": b"[]",
            }

            mock_file = MagicMock()
            mock_file.__enter__.return_value = (
                mock_file  # mock_file is a context manager
            )
            mock_file.read.return_value = responses.get(url, b"[]")
            mock_file.info.return_value = {"Content-Encoding": None}
            return mock_file

        mock.side_effect = mock_response

        self.assertEqual(
            get_municipality_by_code("3550308"), ("São Paulo", "SP")
        )
        self.assertEqual(
            get_municipality_by_code("3304557"), ("Rio de Janeiro", "RJ")
        )
        self.assertEqual(get_municipality_by_code("5208707"), ("Goiânia", "GO"))
        self.assertIsNone(get_municipality_by_code("1234567"))

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_http_error(self, mock):
        mock.side_effect = HTTPError(
            "http://fakeurl.com", 404, "Not Found", None, None
        )
        result = get_municipality_by_code("342432")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_http_error_1(self, mock):
        mock.side_effect = HTTPError(
            "http://fakeurl.com", 401, "Denied", None, None
        )
        result = get_municipality_by_code("342432")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_excpetion(self, mock):
        mock.side_effect = Exception("Erro desconhecido")
        result = get_municipality_by_code("342432")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_successfull_decompression(self, mock_urlopen):
        valid_json = '{"nome":"São Paulo","microrregiao":{"mesorregiao":{"UF":{"sigla":"SP"}}}}'
        compressed_data = gzip.compress(valid_json.encode("utf-8"))
        mock_response = MagicMock()
        mock_response.read.return_value = compressed_data
        mock_response.info.return_value.get.return_value = "gzip"
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = get_municipality_by_code("3550308")
        self.assertEqual(result, ("São Paulo", "SP"))

    @patch("brutils.ibge.municipality.urlopen")
    def test_successful_json_without_compression(self, mock_urlopen):
        valid_json = '{"nome":"São Paulo","microrregiao":{"mesorregiao":{"UF":{"sigla":"SP"}}}}'
        mock_response = MagicMock()
        mock_response.read.return_value = valid_json
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = get_municipality_by_code("3550308")
        self.assertEqual(result, ("São Paulo", "SP"))

    @patch("gzip.GzipFile.read", side_effect=OSError("Erro na descompressão"))
    def test_error_decompression(self, mock_gzip_read):
        result = get_municipality_by_code("3550308")
        self.assertIsNone(result)

    @patch(
        "gzip.GzipFile.read",
        side_effect=Exception("Erro desconhecido na descompressão"),
    )
    def test_error_decompression_generic_exception(self, mock_gzip_read):
        result = get_municipality_by_code("3550308")
        self.assertIsNone(result)

    @patch("json.loads", side_effect=JSONDecodeError("error", "city.json", 1))
    def test_error_json_load(self, mock_json_loads):
        result = get_municipality_by_code("3550308")
        self.assertIsNone(result)

    @patch("json.loads", side_effect=KeyError)
    def test_error_json_key_error(self, mock_json_loads):
        result = get_municipality_by_code("3550308")
        self.assertIsNone(result)

    def test_get_code_by_municipality_name(self):
        self.assertEqual(
            get_code_by_municipality_name("Florianópolis", "sc"), "4205407"
        )
        self.assertEqual(
            get_code_by_municipality_name("São Paulo", "sp"), "3550308"
        )
        self.assertEqual(
            get_code_by_municipality_name("GOIANIA", "GO"), "5208707"
        )
        self.assertEqual(
            get_code_by_municipality_name("Conceição do Coité", "BA"), "2908408"
        )
        self.assertEqual(
            get_code_by_municipality_name("conceicao do Coite", "Ba"), "2908408"
        )
        self.assertEqual(
            get_code_by_municipality_name("rio de janeiro", "rj"), "3304557"
        )
        self.assertEqual(
            get_code_by_municipality_name("Lauro Müller", "sc"), "4209607"
        )
        self.assertEqual(
            get_code_by_municipality_name("Tôrres", "rs"), "4321501"
        )
        self.assertEqual(
            get_code_by_municipality_name("aurora", "ce"), "2301703"
        )
        self.assertEqual(
            get_code_by_municipality_name("aurora", "sc"), "4201901"
        )
        self.assertIsNone(
            get_code_by_municipality_name("Municipio Inexistente", "RS")
        )
        self.assertIsNone(
            get_code_by_municipality_name("Municipio Inexistente", "")
        )


if __name__ == "__main__":
    main()
