import gzip
import io
import json
from urllib.error import HTTPError
from urllib.request import urlopen


def get_municipality_by_code(code):  # type: (str) -> Tuple[str, str] | None
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
    baseUrl = (
        f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{code}"
    )
    try:
        with urlopen(baseUrl) as f:
            compressed_data = f.read()
            if _is_empty(compressed_data):
                print(f"{code} é um código inválido")
                return None

    except HTTPError as e:
        if e == 404:
            print(f"{code} é um código inválido")
            return None

    with gzip.GzipFile(fileobj=io.BytesIO(compressed_data)) as gzip_file:
        descompressed_data = gzip_file.read()

    json_data = json.loads(descompressed_data)
    return _get_values(json_data)


def _get_values(data):
    municipio = data["nome"]
    estado = data["microrregiao"]["mesorregiao"]["UF"]["sigla"]
    return (municipio, estado)


def _is_empty(zip):
    # compressed value for []
    return (
        zip
        == b"\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03\x8b\x8e\x05\x00)\xbbL\r\x02\x00\x00\x00"
    )
