import json
import pathlib
import unicodedata
from contextlib import suppress
from http import HTTPStatus

import requests

from brutils.logger import logger


def __get_cities_code_file_path() -> pathlib.Path:
    """
    Returns the path to the local cities code JSON file.

    This function resolves and returns the path to the 'cities_code.json' file
    located in the data directory of the project.

    Returns:
        pathlib.Path: The path to the 'cities_code.json' file.
    """
    current_file_path = pathlib.Path(__file__).resolve()
    return current_file_path.parent.parent / "data" / "cities_code.json"


def _fetch_municipality_data_on_json_file(code: str) -> dict | None:
    """
    Retrieves municipality data from a local JSON file by code.

    This function searches for the municipality data in a local JSON file using the provided code.
    If the file does not exist, is empty, or the code is not found, it returns None and logs an error.

    Args:
        code (str): The IBGE code of the municipality.

    Returns:
        dict | None: A dictionary with the municipality name and UF, or None if not found.
    """
    json_cities_code_path = __get_cities_code_file_path()

    if not json_cities_code_path.exists():
        logger.error(f"Arquivo local não encontrado: {json_cities_code_path}")
        return None

    try:
        with open(json_cities_code_path, "r", encoding="utf-8") as file:
            content = json.load(file)
    except json.JSONDecodeError as e:
        logger.error(
            f"Erro ao decodificar o arquivo local {json_cities_code_path}: {e}"
        )
        return None

    if not content:
        logger.error(f"Arquivo local vazio: {json_cities_code_path}")
        return None

    for uf, cities in content.items():
        for city, city_code in cities.items():
            if code == city_code:
                return {"city_name": city.title(), "uf": uf}

    logger.error(
        f"Código {code} não encontrado no arquivo local: {json_cities_code_path}"
    )
    return None


def _fetch_municipality_data(
    code: str, attempts: int = 0
) -> tuple[dict, str] | tuple[None, str]:
    """
    Retrieves municipality data from the IBGE API or a local JSON file.

    This function attempts to fetch municipality data from the IBGE API using the provided code.
    If the API returns an error or empty result, it will attempt to fetch the data from a local JSON file.

    Args:
        code (str): The IBGE code of the municipality.

    Returns:
        tuple[dict, str] | None: A tuple containing the municipality data and the data source ('api' or 'json_file'),
            or None if the data could not be retrieved.
    """
    logger.debug(f"Buscando dados do município para o código {code}")

    base_url = (
        f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{code}"
    )
    data_source = "api"

    try:
        response = requests.get(base_url, timeout=5)
    except requests.Timeout as e:
        logger.warning(
            f"Timeout ao buscar o código {code}: {e}. Tentando buscar localmente."
        )
        # Try again once before fetching locally
        if attempts < 2:
            attempts += 1
            return _fetch_municipality_data(code, attempts)

        data_source = "json_file"
        return _fetch_municipality_data_on_json_file(code), data_source
    except requests.RequestException as e:
        logger.error(f"Erro ao buscar o código {code}: {e}")
        return None, data_source

    content = {}

    with suppress(Exception):
        content = json.loads(response.content)

    # Not Found or OK with empty content
    if response.status_code == HTTPStatus.NOT_FOUND or (
        response.status_code == HTTPStatus.OK and _is_empty(content)
    ):
        logger.error(f"{code} é um código inválido")
        return None, data_source

    # Server Error: try to fetch locally
    if response.status_code >= HTTPStatus.INTERNAL_SERVER_ERROR:
        logger.warning(
            f"Erro HTTP ao buscar o código {code}: ({response.status_code}) {response.reason}."
            " Tentando buscar localmente."
        )
        data_source = "json_file"
        return _fetch_municipality_data_on_json_file(code), data_source

    # Happy path
    if response.ok and content:
        return content, data_source

    # Some other errors
    logger.error(
        f"Erro desconhecido ao buscar o código {code}: {response.reason}"
    )
    return None, data_source


def get_municipality_by_code(code: str) -> tuple[str, str] | None:
    """
    Returns the municipality name and UF for a given IBGE code.

    This function takes a string representing an IBGE municipality code
    and returns a tuple with the municipality's name and its corresponding UF.

    Args:
        code (str): The IBGE code of the municipality.

    Returns:
        tuple: A tuple formatted as ("Município", "UF").
            - Returns None if the code is not valid.

    Example:
        >>> get_municipality_by_code("3550308")
        ("São Paulo", "SP")
    """

    municipality_data, data_source = _fetch_municipality_data(code)

    if municipality_data is None:
        return None

    try:
        return _get_values(municipality_data, data_source)
    except json.JSONDecodeError as e:
        logger.error(f"Erro ao decodificar os dados JSON: {e}")
        return None
    except KeyError as e:
        logger.error(f"Erro ao acessar os dados do município: {e}")
        return None


def get_code_by_municipality_name(
    municipality_name: str, uf: str
) -> str | None:
    """
    Returns the IBGE code for a given municipality name and uf code.

    This function takes a string representing a municipality's name
    and uf's code and returns the corresponding IBGE code (string). The function
    will handle names by ignoring differences in case, accents, and
    treating the character ç as c and ignoring case differences for the uf code.

    Args:
        municipality_name (str): The name of the municipality.
        uf (str): The uf code of the state.

    Returns:
        str: The IBGE code of the municipality.
            - Returns None if the name is not valid or does not exist.

    Example:
        >>> get_code_by_municipality_name("São Paulo", "SP")
        "3550308"
        >>> get_code_by_municipality_name("goiania", "go")
        "5208707"
        >>> get_code_by_municipality_name("Conceição do Coité", "BA")
        "2908408"
        >>> get_code_by_municipality_name("conceicao do Coite", "Ba")
        "2908408"
        >>> get_code_by_municipality_name("Municipio Inexistente", "")
        None
        >>> get_code_by_municipality_name("Municipio Inexistente", "RS")
        None
    """

    json_cities_code_path = __get_cities_code_file_path()
    uf = uf.upper()

    with open(json_cities_code_path, "r", encoding="utf-8") as file:
        cities_uf_code = json.load(file)

    if uf not in cities_uf_code.keys():
        return None

    cities_code = cities_uf_code.get(uf)
    name_city = _transform_text(municipality_name)

    return (
        cities_code.get(name_city) if name_city in cities_code.keys() else None
    )


def _get_values(data: dict, source: str = "api") -> tuple[str, str]:
    if source not in ("api", "json_file"):
        message = f"Opção {source} inválida. As opções disponíveis são 'api' ou 'json_file'"
        logger.error(message)
        raise ValueError(message)

    values = ("", "")

    if source == "api":
        values = (
            data["nome"],
            data["microrregiao"]["mesorregiao"]["UF"]["sigla"],
        )
    elif source == "json_file":
        values = (data["city_name"], data["uf"])

    return values


def _is_empty(zip):
    return zip == b"[]" or len(zip) == 0


def _transform_text(municipality_name: str) -> str:
    """
    Normalize municipality name and returns the normalized string.

    Args:
        municipality_name (str): The name of the municipality.

    Returns:
        str: The normalized string

    Example:
        >>> _transform_text("São Paulo")
        "sao paulo"
        >>> _transform_text("Goiânia")
        "goiania"
        >>> _transform_text("Conceição do Coité")
        "'conceicao do coite'
    """

    normalized_string = (
        unicodedata.normalize("NFKD", municipality_name)
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    return normalized_string.casefold()
