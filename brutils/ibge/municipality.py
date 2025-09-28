import json
import unicodedata
from contextlib import suppress
from http import HTTPStatus
from pathlib import Path

import requests

from brutils.logger import logger


def __get_cities_code_file_path() -> Path:  # pragma: no cover
    """
    Returns the path to the local cities code JSON file.

    This function resolves and returns the path to the 'cities_code.json' file
    located in the data directory of the project.

    Returns:
        Path: The path to the 'cities_code.json' file.
    """
    current_file_path = Path(__file__).resolve()
    return current_file_path.parent.parent / "data" / "cities_code.json"


def _fetch_municipality_data_on_json_file(
    code: str,
) -> dict | None:  # pragma: no cover
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


def _fetch_municipality_data(**kwargs: dict) -> dict | None:
    """
    Fetches municipality data from the IBGE API using either a code or a municipality name and UF.

    This function retrieves municipality data from the IBGE API. It accepts either a code or a combination
    of municipality name and UF as input. The function validates the input, builds the appropriate API URL,
    and handles request errors, timeouts, and response status codes. It returns the municipality data as a
    dictionary if found, or None otherwise.

    Args:
        **kwargs (dict): Keyword arguments that may include:
            - code (str): The IBGE code of the municipality.
            - municipality_name (str): The name of the municipality.
            - uf (str): The UF (state) code.

    Returns:
        dict | None: The municipality data as a dictionary, or None if not found or on error.
    """
    code = kwargs.get("code", "").strip()
    municipality_name = kwargs.get("municipality_name", "").strip()
    uf = kwargs.get("uf", "").strip()

    if code and (not code.isdigit() or len(code) != 7):
        logger.error(
            f"Código inválido: {code}. Deve conter exatamente 7 dígitos."
        )
        return None

    if any([municipality_name and not uf, uf and not municipality_name]):
        logger.error("Necessário informar nome da cidade e UF")
        return None

    logger_message = (
        f"Buscando dados do município para o código {code}"
        if code and not (municipality_name and uf)
        else (
            f"Buscando dados do município para o nome '{municipality_name}' e UF '{uf}'"
        )
    )
    logger.debug(logger_message)

    base_url = (
        f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{code}"
    )
    if municipality_name and uf:
        base_url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"

    try:
        response = requests.get(base_url, timeout=30)

    except requests.Timeout as e:
        logger.warning(f"Timeout ao buscar o código {code}: {e}.")
        return None

    except requests.RequestException as e:
        logger.error(f"Erro ao buscar o código {code}: {e}")
        return None

    content = _get_content_from_response(code, municipality_name, uf, response)

    # Not Found or OK with empty content
    if any(
        [
            response.status_code == HTTPStatus.NOT_FOUND,
            response.status_code == HTTPStatus.OK and _is_empty(content),
        ]
    ):
        logger.error(f"{code} é um código inválido")
        return None

    if response.status_code >= HTTPStatus.INTERNAL_SERVER_ERROR:
        logger.error(
            f"Erro HTTP ao buscar o código {code}: ({response.status_code}) {response.reason}."
        )
        return None

    # Happy path
    if response.ok and content:
        return content

    # Some other errors
    logger.error(
        f"Erro desconhecido ao buscar o código {code}: {response.reason}"
    )
    return None


def _get_content_from_response(
    code: str,
    municipality_name: str,
    uf: str,
    response: requests.Response,
) -> dict | None:
    """
    Extracts and returns the relevant municipality content from the API response.

    This function parses the API response content and returns either the municipality data
    for a given code or the matching municipality from a list when searching by name and UF.

    Args:
        code (str): The IBGE code of the municipality.
        municipality_name (str): The name of the municipality.
        uf (str): The UF (state) code.
        response: The HTTP response object from the API.

    Returns:
        dict or None: The municipality data as a dictionary, or None if not found or on error.
    """
    content = None

    with suppress(Exception):
        if code:
            content = json.loads(response.content)
        elif municipality_name and uf and response.ok:
            municipalities = json.loads(response.content)
            content = next(
                (
                    municipality
                    for municipality in municipalities
                    if (
                        _transform_text(municipality["nome"])
                        == _transform_text(municipality_name)
                    )
                ),
                None,
            )

    return content


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

    municipality_data = _fetch_municipality_data(code=code)

    if municipality_data is None:
        return None

    try:
        return _get_values(municipality_data)
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
    municipality_data = _fetch_municipality_data(
        municipality_name=municipality_name, uf=uf
    )

    return str(municipality_data["id"]) if municipality_data else None


def _get_values(data: dict) -> tuple[str, str]:
    return (
        data["nome"],
        data["microrregiao"]["mesorregiao"]["UF"]["sigla"],
    )


def _is_empty(zip):
    return zip is None or zip == b"[]" or len(zip) == 0


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
