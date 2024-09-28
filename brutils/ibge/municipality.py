import json
import pathlib
import unicodedata


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
