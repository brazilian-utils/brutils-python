from http import HTTPStatus
from json import JSONDecodeError, dumps
from unittest import TestCase, main
from unittest.mock import MagicMock, patch

from brutils.ibge.municipality import (
    get_code_by_municipality_name,
    get_municipality_by_code,
)


class TestIBGE(TestCase):
    @patch("requests.get")
    def test_get_municipality_by_code(self, mock_get):
        def mock_response(url, *args, **kwargs):
            responses = {
                "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3550308": {
                    "content": dumps(
                        {
                            "nome": "São Paulo",
                            "microrregiao": {
                                "mesorregiao": {"UF": {"sigla": "SP"}}
                            },
                        }
                    ).encode("utf-8"),
                    "status_code": 200,
                    "ok": True,
                    "reason": "OK",
                },
                "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3304557": {
                    "content": dumps(
                        {
                            "nome": "Rio de Janeiro",
                            "microrregiao": {
                                "mesorregiao": {"UF": {"sigla": "RJ"}}
                            },
                        }
                    ).encode("utf-8"),
                    "status_code": 200,
                    "ok": True,
                    "reason": "OK",
                },
                "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/5208707": {
                    "content": dumps(
                        {
                            "nome": "Goiânia",
                            "microrregiao": {
                                "mesorregiao": {"UF": {"sigla": "GO"}}
                            },
                        }
                    ).encode("utf-8"),
                    "status_code": 200,
                    "ok": True,
                    "reason": "OK",
                },
                "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/1234567": {
                    "content": b"[]",
                    "status_code": 404,
                    "ok": False,
                    "reason": "Not Found",
                },
            }
            resp_data = responses.get(
                url,
                {
                    "content": b"[]",
                    "status_code": 404,
                    "ok": False,
                    "reason": "Not Found",
                },
            )
            mock_resp = MagicMock()
            mock_resp.content = resp_data["content"]
            mock_resp.status_code = resp_data["status_code"]
            mock_resp.ok = resp_data["ok"]
            mock_resp.reason = resp_data["reason"]
            return mock_resp

        mock_get.side_effect = mock_response

        self.assertEqual(
            get_municipality_by_code("3550308"), ("São Paulo", "SP")
        )
        self.assertEqual(
            get_municipality_by_code("3304557"), ("Rio de Janeiro", "RJ")
        )
        self.assertEqual(get_municipality_by_code("5208707"), ("Goiânia", "GO"))
        self.assertIsNone(get_municipality_by_code("1234567"))

    @patch("requests.get")
    def test_get_municipality_http_error(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = (
            HTTPStatus.OK
        )  # A API retorna 200 com conteúdo vazio para código inválido
        mock_resp.content = b"[]"
        mock_resp.ok = False
        mock_resp.reason = "Not Found"

        mock_get.return_value = mock_resp

        with self.assertLogs("BrutilsLogger", level="ERROR") as logger_called:
            result = get_municipality_by_code("342432")
            self.assertIsNone(result)
            self.assertTrue(
                any(
                    "342432 é um código inválido" in message
                    for message in logger_called.output
                )
            )

    @patch("requests.get")
    def test_get_municipality_http_error_1(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 401
        mock_resp.content = b"[]"
        mock_resp.ok = False
        mock_resp.reason = "Denied"
        mock_get.return_value = mock_resp
        with self.assertLogs("BrutilsLogger", level="ERROR") as logger_called:
            result = get_municipality_by_code("342432")
            self.assertIsNone(result)
            self.assertTrue(
                any(
                    "Erro desconhecido ao buscar o código 342432: Denied"
                    in message
                    for message in logger_called.output
                )
            )

    @patch("requests.get")
    def test_get_municipality_server_error(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        mock_resp.content = b"[]"
        mock_resp.ok = False
        mock_resp.reason = "Internal Server Error"
        mock_get.return_value = mock_resp
        with self.assertLogs("BrutilsLogger", level="WARNING") as logger_called:
            result = get_municipality_by_code("342432")
            self.assertIsNone(result)
            self.assertTrue(
                any(
                    "Erro HTTP ao buscar o código 342432: (500) Internal Server Error. Tentando buscar localmente."
                    in message
                    for message in logger_called.output
                )
            )

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
