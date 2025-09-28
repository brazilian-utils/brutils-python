import json
import pathlib
import tempfile
from http import HTTPStatus
from json import dumps
from unittest import TestCase, main
from unittest.mock import MagicMock, patch

import requests

from brutils.ibge import municipality
from brutils.ibge.municipality import (
    get_code_by_municipality_name,
    get_municipality_by_code,
)


class TestIBGE(TestCase):
    @patch("requests.get")
    def test_get_municipality_by_code(self, mock_get):
        def mock_response(url, *args, **kwargs):
            # Verifica se o timeout foi passado corretamente
            self.assertIn("timeout", kwargs)
            self.assertEqual(kwargs["timeout"], 30)
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
    def test_timeout_handling(self, mock_get):
        # Simula Timeout em todas as tentativas
        mock_get.side_effect = requests.Timeout("timeout!")
        with self.assertLogs("BR_Utils_Logger", level="WARNING") as log:
            result = municipality._fetch_municipality_data(code="1234567")
            self.assertIsNone(result)
            self.assertTrue(
                any("Timeout ao buscar o código" in msg for msg in log.output)
            )

    @patch(
        "brutils.ibge.municipality._get_values",
        side_effect=json.JSONDecodeError("msg", "doc", 1),
    )
    def test_get_municipality_by_code_json_decode_error(self, mock_get_values):
        # Test handling of JSONDecodeError in get_municipality_by_code
        with (
            self.assertLogs("BR_Utils_Logger", level="ERROR") as logger_called,
            patch(
                "brutils.ibge.municipality._fetch_municipality_data",
                return_value={},
            ),
        ):
            result = get_municipality_by_code("3550308")
            self.assertIsNone(result)
            self.assertTrue(
                any(
                    "Erro ao decodificar os dados JSON" in msg
                    for msg in logger_called.output
                )
            )

    @patch(
        "brutils.ibge.municipality._get_values", side_effect=KeyError("nome")
    )
    def test_get_municipality_by_code_key_error(self, mock_get_values):
        # Test handling of KeyError in get_municipality_by_code
        with (
            self.assertLogs("BR_Utils_Logger", level="ERROR") as logger_called,
            patch(
                "brutils.ibge.municipality._fetch_municipality_data",
                return_value={},
            ),
        ):
            result = get_municipality_by_code("3550308")
            self.assertIsNone(result)
            self.assertTrue(
                any(
                    "Erro ao acessar os dados do município" in msg
                    for msg in logger_called.output
                )
            )

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

        with self.assertLogs("BR_Utils_Logger", level="ERROR") as logger_called:
            result = get_municipality_by_code("342432")
            self.assertIsNone(result)
            self.assertTrue(
                any(
                    "Código inválido: 342432. Deve conter exatamente 7 dígitos."
                    in message
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
        with self.assertLogs("BR_Utils_Logger", level="ERROR") as logger_called:
            result = get_municipality_by_code("342432")
            self.assertIsNone(result)
            self.assertTrue(
                any(
                    "Código inválido: 342432. Deve conter exatamente 7 dígitos"
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
        with self.assertLogs(
            "BR_Utils_Logger", level="WARNING"
        ) as logger_called:
            result = get_municipality_by_code("3424322")
            self.assertIsNone(result)
            self.assertTrue(
                any(
                    "Erro HTTP ao buscar o código 3424322: (500) Internal Server Error."
                    in message
                    for message in logger_called.output
                )
            )

    @patch("requests.get")
    def test_get_code_by_municipality_name(self, mock_get):
        # Florianópolis, SC
        mock_resp_1 = MagicMock()
        mock_resp_1.status_code = 200
        mock_resp_1.content = json.dumps(
            [{"id": "4205407", "nome": "Florianópolis"}]
        ).encode("utf-8")
        mock_resp_1.ok = True
        mock_get.return_value = mock_resp_1
        self.assertEqual(
            get_code_by_municipality_name("Florianópolis", "sc"), "4205407"
        )

        # São Paulo, SP
        mock_resp_2 = MagicMock()
        mock_resp_2.status_code = 200
        mock_resp_2.content = json.dumps(
            [{"id": "3550308", "nome": "São Paulo"}]
        ).encode("utf-8")
        mock_resp_2.ok = True
        mock_get.return_value = mock_resp_2
        self.assertEqual(
            get_code_by_municipality_name("São Paulo", "sp"), "3550308"
        )

        # GOIANIA, GO
        mock_resp_3 = MagicMock()
        mock_resp_3.status_code = 200
        mock_resp_3.content = json.dumps(
            [{"id": "5208707", "nome": "GOIANIA"}]
        ).encode("utf-8")
        mock_resp_3.ok = True
        mock_get.return_value = mock_resp_3
        self.assertEqual(
            get_code_by_municipality_name("GOIANIA", "GO"), "5208707"
        )

        # Conceição do Coité, BA
        mock_resp_4 = MagicMock()
        mock_resp_4.status_code = 200
        mock_resp_4.content = json.dumps(
            [{"id": "2908408", "nome": "Conceição do Coité"}]
        ).encode("utf-8")
        mock_resp_4.ok = True
        mock_get.return_value = mock_resp_4
        self.assertEqual(
            get_code_by_municipality_name("Conceição do Coité", "BA"), "2908408"
        )

        # conceicao do Coite, Ba (variação sem acento)
        mock_resp_5 = MagicMock()
        mock_resp_5.status_code = 200
        mock_resp_5.content = json.dumps(
            [{"id": "2908408", "nome": "Conceição do Coité"}]
        ).encode("utf-8")
        mock_resp_5.ok = True
        mock_get.return_value = mock_resp_5
        self.assertEqual(
            get_code_by_municipality_name("conceicao do Coite", "Ba"), "2908408"
        )

        # rio de janeiro, rj
        mock_resp_6 = MagicMock()
        mock_resp_6.status_code = 200
        mock_resp_6.content = json.dumps(
            [{"id": "3304557", "nome": "Rio de Janeiro"}]
        ).encode("utf-8")
        mock_resp_6.ok = True
        mock_get.return_value = mock_resp_6
        self.assertEqual(
            get_code_by_municipality_name("rio de janeiro", "rj"), "3304557"
        )

        # Lauro Müller, sc
        mock_resp_7 = MagicMock()
        mock_resp_7.status_code = 200
        mock_resp_7.content = json.dumps(
            [{"id": "4209607", "nome": "Lauro Müller"}]
        ).encode("utf-8")
        mock_resp_7.ok = True
        mock_get.return_value = mock_resp_7
        self.assertEqual(
            get_code_by_municipality_name("Lauro Müller", "sc"), "4209607"
        )

        # Tôrres, rs
        mock_resp_8 = MagicMock()
        mock_resp_8.status_code = 200
        mock_resp_8.content = json.dumps(
            [{"id": "4321501", "nome": "Tôrres"}]
        ).encode("utf-8")
        mock_resp_8.ok = True
        mock_get.return_value = mock_resp_8
        self.assertEqual(
            get_code_by_municipality_name("Tôrres", "rs"), "4321501"
        )

        # aurora, ce
        mock_resp_9 = MagicMock()
        mock_resp_9.status_code = 200
        mock_resp_9.content = json.dumps(
            [{"id": "2301703", "nome": "Aurora"}]
        ).encode("utf-8")
        mock_resp_9.ok = True
        mock_get.return_value = mock_resp_9
        self.assertEqual(
            get_code_by_municipality_name("aurora", "ce"), "2301703"
        )

        # aurora, sc
        mock_resp_10 = MagicMock()
        mock_resp_10.status_code = 200
        mock_resp_10.content = json.dumps(
            [{"id": "4201901", "nome": "Aurora"}]
        ).encode("utf-8")
        mock_resp_10.ok = True
        mock_get.return_value = mock_resp_10
        self.assertEqual(
            get_code_by_municipality_name("aurora", "sc"), "4201901"
        )

        # Municipio Inexistente, RS
        mock_resp_11 = MagicMock()
        mock_resp_11.status_code = 200
        mock_resp_11.content = json.dumps(
            [{"id": "4205407", "nome": "Florianópolis"}]
        ).encode("utf-8")
        mock_resp_11.ok = True
        mock_get.return_value = mock_resp_11
        self.assertIsNone(
            get_code_by_municipality_name("Municipio Inexistente", "RS")
        )

        # Municipio Inexistente, ""
        mock_resp_12 = MagicMock()
        mock_resp_12.status_code = 200
        mock_resp_12.content = json.dumps(
            [{"id": "4205407", "nome": "Florianópolis"}]
        ).encode("utf-8")
        mock_resp_12.ok = True
        mock_get.return_value = mock_resp_12
        self.assertIsNone(
            get_code_by_municipality_name("Municipio Inexistente", "")
        )


if __name__ == "__main__":
    main()


class TestMunicipalityFileScenarios(TestCase):
    def setUp(self):
        # Patch the __get_cities_code_file_path to use a temp file
        self.temp_dir = tempfile.TemporaryDirectory()
        self.json_path = pathlib.Path(self.temp_dir.name) / "cities_code.json"
        self.patcher = patch(
            "brutils.ibge.municipality.__get_cities_code_file_path",
            return_value=self.json_path,
        )
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.temp_dir.cleanup()

    def test_code_found_returns_city_and_uf(self):
        # Test happy path where municipality code is found
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(
                {"SP": {"sao paulo": "3550308", "campinas": "3509502"}}, f
            )
        result = municipality._fetch_municipality_data_on_json_file("3550308")
        self.assertEqual(result, {"city_name": "Sao Paulo", "uf": "SP"})
        result2 = municipality._fetch_municipality_data_on_json_file("3509502")
        self.assertEqual(result2, {"city_name": "Campinas", "uf": "SP"})

    def test_json_decode_error_logs_and_returns_none(self):
        # 129: Simula erro de decodificação JSON ao abrir o arquivo
        with open(self.json_path, "w", encoding="utf-8") as f:
            f.write("{invalid json")
        with self.assertLogs("BR_Utils_Logger", level="ERROR") as logger_called:
            result = municipality._fetch_municipality_data_on_json_file(
                "9999999"
            )
            self.assertIsNone(result)
            self.assertTrue(
                "Erro ao decodificar o arquivo local" in logger_called.output[0]
            )

    def test_file_empty_logs_and_returns_none(self):
        # 49-50: File exists but is empty
        with open(self.json_path, "w", encoding="utf-8") as f:
            f.write("")
        with self.assertLogs("BR_Utils_Logger", level="ERROR") as logger_called:
            result = municipality._fetch_municipality_data_on_json_file(
                "9999999"
            )
            self.assertIsNone(result)
            self.assertTrue(
                "Erro ao decodificar o arquivo local" in logger_called.output[0]
            )

    def test_file_is_blank_logs_and_returns_none(self):
        # 49-50: File exists but is blank
        with open(self.json_path, "w", encoding="utf-8") as f:
            f.write("{}")
        with self.assertLogs("BR_Utils_Logger", level="ERROR") as logger_called:
            result = municipality._fetch_municipality_data_on_json_file(
                "9999999"
            )
            self.assertIsNone(result)
            self.assertTrue("Arquivo local vazio" in logger_called.output[0])

    def test_code_not_found_logs_and_returns_none(self):
        # 55: Code not found in file
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump({"SP": {"sao paulo": "3550308"}}, f)
        with self.assertLogs("BR_Utils_Logger", level="ERROR") as logger_called:
            result = municipality._fetch_municipality_data_on_json_file(
                "9999999"
            )
            self.assertIsNone(result)
            self.assertTrue(
                "não encontrado no arquivo local" in logger_called.output[0]
            )


class TestFetchMunicipalityData(TestCase):
    @patch("requests.get")
    def test_unexpected_error_logs_and_returns_none(self, mock_get):
        # 213-214: unexpected error (e.g., status_code=400)
        mock_resp = MagicMock()
        mock_resp.status_code = 400
        mock_resp.content = b"[]"
        mock_resp.ok = False
        mock_resp.reason = "Bad Request"
        mock_get.return_value = mock_resp
        with self.assertLogs("BR_Utils_Logger", level="ERROR") as logger_called:
            result = municipality._fetch_municipality_data(code="9999999")
            self.assertIsNone(result)
            self.assertIn(
                "Erro desconhecido ao buscar o código", logger_called.output[0]
            )

    @patch("requests.get")
    def test_get_code_by_municipality_name_found(self, mock_get):
        # Arrange
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.content = json.dumps(
            [{"id": "4205407", "nome": "Florianópolis"}]
        ).encode("utf-8")
        mock_resp.ok = True
        mock_get.return_value = mock_resp

        # Act
        result = get_code_by_municipality_name("Florianópolis", "sc")

        # Assert
        self.assertEqual(result, "4205407")

    @patch("requests.get")
    def test_get_code_by_municipality_name_not_found(self, mock_get):
        # Arrange
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.content = json.dumps(
            [{"id": "4205407", "nome": "Florianópolis"}]
        ).encode("utf-8")
        mock_resp.ok = True
        mock_get.return_value = mock_resp

        # Act
        result = get_code_by_municipality_name("Cidade Inexistente", "sc")

        # Assert
        self.assertIsNone(result)

    @patch("requests.get")
    def test_get_code_by_municipality_name_empty_response(self, mock_get):
        # Arrange
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.content = b"[]"
        mock_resp.ok = True
        mock_get.return_value = mock_resp

        # Act
        result = get_code_by_municipality_name("Florianópolis", "sc")

        # Assert
        self.assertIsNone(result)

    @patch("requests.get")
    def test_get_code_by_municipality_name_api_error(self, mock_get):
        # Arrange
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.content = b"[]"
        mock_resp.ok = False
        mock_resp.reason = "Internal Server Error"
        mock_get.return_value = mock_resp

        # Act
        result = get_code_by_municipality_name("Florianópolis", "sc")

        # Assert
        self.assertIsNone(result)

    @patch("requests.get")
    def test_get_code_by_municipality_name_request_exception(self, mock_get):
        # Arrange
        mock_get.side_effect = requests.RequestException("Erro de rede")

        # Act
        result = get_code_by_municipality_name("Florianópolis", "sc")

        # Assert
        self.assertIsNone(result)


if __name__ == "__main__":
    main()
