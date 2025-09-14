import json
import pathlib
import tempfile
from http import HTTPStatus
from json import JSONDecodeError, dumps
from unittest import TestCase, main
from unittest.mock import MagicMock, patch

import requests

from brutils.ibge import municipality
from brutils.ibge.municipality import (
    _get_values,
    get_code_by_municipality_name,
    get_municipality_by_code,
)


class TestIBGE(TestCase):
    @patch("requests.get")
    def test_get_municipality_by_code(self, mock_get):
        def mock_response(url, *args, **kwargs):
            # Verifica se o timeout foi passado corretamente
            self.assertIn("timeout", kwargs)
            self.assertEqual(kwargs["timeout"], 5)
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
    def test_timeout_and_request_exception_handling(self, mock_get):
        # 92-107: Testa timeout e request exception
        # Simula Timeout na primeira chamada, depois sucesso na segunda
        call_count = {"count": 0}

        def side_effect(*args, **kwargs):
            if call_count["count"] == 0:
                call_count["count"] += 1
                raise requests.Timeout("timeout!")
            else:
                mock_resp = MagicMock()
                mock_resp.status_code = 200
                mock_resp.content = b'{"nome": "Test City", "microrregiao": {"mesorregiao": {"UF": {"sigla": "TC"}}}}'
                mock_resp.ok = True
                mock_resp.reason = "OK"
                return mock_resp

        mock_get.side_effect = side_effect

        with self.assertLogs("BrutilsLogger", level="WARNING") as log:
            result, source = municipality._fetch_municipality_data("1234567")
            self.assertEqual(result["nome"], "Test City")
            self.assertEqual(source, "api")
            self.assertTrue(
                any("Timeout ao buscar o código" in msg for msg in log.output)
            )

        # Simula Timeout em todas as tentativas, depois busca localmente
        mock_get.side_effect = requests.Timeout("timeout!")
        with patch(
            "brutils.ibge.municipality._fetch_municipality_data_on_json_file",
            return_value={"city_name": "Local City", "uf": "LC"},
        ):
            with self.assertLogs("BrutilsLogger", level="WARNING") as log:
                result, source = municipality._fetch_municipality_data(
                    "9999999", attempts=2
                )
                self.assertEqual(
                    result, {"city_name": "Local City", "uf": "LC"}
                )
                self.assertEqual(source, "json_file")
                self.assertTrue(
                    any(
                        "Timeout ao buscar o código" in msg
                        for msg in log.output
                    )
                )

        # Simula RequestException
        mock_get.side_effect = requests.RequestException("erro de rede")
        with self.assertLogs("BrutilsLogger", level="ERROR") as log:
            result, source = municipality._fetch_municipality_data("9999999")
            self.assertIsNone(result)
            self.assertEqual(source, "api")
            self.assertTrue(
                any("Erro ao buscar o código" in msg for msg in log.output)
            )

    def test_get_values_json_file(self):
        # 219-220: Test _get_values with source 'json_file'
        data = {"city_name": "sao paulo", "uf": "SP"}
        result = _get_values(data, "json_file")
        self.assertEqual(result, ("sao paulo", "SP"))

    @patch(
        "brutils.ibge.municipality._get_values",
        side_effect=json.JSONDecodeError("msg", "doc", 1),
    )
    def test_get_municipality_by_code_json_decode_error(self, mock_get_values):
        # Test handling of JSONDecodeError in get_municipality_by_code
        with self.assertLogs(
            "BrutilsLogger", level="ERROR"
        ) as logger_called, patch(
            "brutils.ibge.municipality._fetch_municipality_data",
            return_value=({}, "api"),
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
        with self.assertLogs(
            "BrutilsLogger", level="ERROR"
        ) as logger_called, patch(
            "brutils.ibge.municipality._fetch_municipality_data",
            return_value=({}, "api"),
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

    def test_file_not_exists_logs_and_returns_none(self):
        # 42-43: File does not exist
        if self.json_path.exists():
            self.json_path.unlink()
        with self.assertLogs("BrutilsLogger", level="ERROR") as logger_called:
            result = municipality._fetch_municipality_data_on_json_file(
                "9999999"
            )
            self.assertIsNone(result)
            self.assertTrue(
                "Arquivo local não encontrado" in logger_called.output[0]
            )

    def test_file_empty_logs_and_returns_none(self):
        # 49-50: File exists but is empty
        with open(self.json_path, "w", encoding="utf-8") as f:
            f.write("")
        with self.assertLogs("BrutilsLogger", level="ERROR") as logger_called:
            result = municipality._fetch_municipality_data_on_json_file(
                "9999999"
            )
            self.assertIsNone(result)
            self.assertTrue(
                "Erro ao decodificar o arquivo local "
                in logger_called.output[0]
            )

    def test_file_is_blank_logs_and_returns_none(self):
        # 49-50: File exists but is blank
        with open(self.json_path, "w", encoding="utf-8") as f:
            f.write("{}")
        with self.assertLogs("BrutilsLogger", level="ERROR") as logger_called:
            result = municipality._fetch_municipality_data_on_json_file(
                "9999999"
            )
            self.assertIsNone(result)
            self.assertTrue("Arquivo local vazio" in logger_called.output[0])

    def test_code_not_found_logs_and_returns_none(self):
        # 55: Code not found in file
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump({"SP": {"sao paulo": "3550308"}}, f)
        with self.assertLogs("BrutilsLogger", level="ERROR") as logger_called:
            result = municipality._fetch_municipality_data_on_json_file(
                "9999999"
            )
            self.assertIsNone(result)
            self.assertTrue(
                "não encontrado no arquivo local" in logger_called.output[0]
            )


class TestGetValues(TestCase):
    def test_invalid_source_raises_and_logs(self):
        # 202-204: source not in ("api", "json_file")
        with self.assertLogs("BrutilsLogger", level="ERROR") as logger_called:
            with self.assertRaises(ValueError):
                _get_values({}, "invalid_source")
            self.assertIn(
                "Opção invalid_source inválida. As opções disponíveis são 'api' ou 'json_file'",
                logger_called.output[0],
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
        with self.assertLogs("BrutilsLogger", level="ERROR") as logger_called:
            result, source = municipality._fetch_municipality_data("9999999")
            self.assertIsNone(result)
            self.assertEqual(source, "api")
            self.assertIn(
                "Erro desconhecido ao buscar o código", logger_called.output[0]
            )

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
