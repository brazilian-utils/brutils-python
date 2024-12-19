import gzip
import io
import json
import pathlib
import unicodedata
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


def get_code_by_municipality_name(municipality_name: str, uf: str):  # type: (str, str) -> str | None
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

    abs_path = pathlib.Path(__file__).resolve()
    script_dir = abs_path.parent.parent

    json_cities_code_path = script_dir / "data" / "cities_code.json"
    uf = uf.upper()

    with open(json_cities_code_path, "r", encoding="utf-8") as file:
        cities_uf_code = json.load(file)

    if uf not in cities_uf_code.keys():
        return None

    cities_code = cities_uf_code.get(uf)
    name_city = _transform_text(municipality_name)

    if name_city not in cities_code.keys():
        return None

    code = cities_code.get(name_city)

    return code


def _get_values(data):
    municipio = data["nome"]
    estado = data["microrregiao"]["mesorregiao"]["UF"]["sigla"]
    return (municipio, estado)


def _is_empty(zip):
    return zip == b"[]" or len(zip) == 0


def _transform_text(municipality_name: str):  # type: (str) -> str
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
    case_fold_string = normalized_string.casefold()

    return case_fold_string
