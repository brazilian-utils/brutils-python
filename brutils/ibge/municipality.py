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
            if f.info().get("Content-Encoding") == "gzip":
                try:
                    with gzip.GzipFile(
                        fileobj=io.BytesIO(compressed_data)
                    ) as gzip_file:
                        decompressed_data = gzip_file.read()
                except OSError as e:
                    print(f"Erro ao descomprimir os dados: {e}")
                    return None
                except Exception as e:
                    print(f"Erro desconhecido ao descomprimir os dados: {e}")
                    return None
            else:
                decompressed_data = compressed_data

            if _is_empty(decompressed_data):
                print(f"{code} é um código inválido")
                return None

    except HTTPError as e:
        if e.code == 404:
            print(f"{code} é um código inválido")
            return None
        else:
            print(f"Erro HTTP ao buscar o código {code}: {e}")
            return None

    except Exception as e:
        print(f"Erro desconhecido ao buscar o código {code}: {e}")
        return None

    try:
        json_data = json.loads(decompressed_data)
        return _get_values(json_data)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar os dados JSON: {e}")
        return None
    except KeyError as e:
        print(f"Erro ao acessar os dados do município: {e}")
        return None


def _get_values(data):
    municipio = data["nome"]
    estado = data["microrregiao"]["mesorregiao"]["UF"]["sigla"]
    return (municipio, estado)


def _is_empty(zip):
    return zip == b"[]" or len(zip) == 0
