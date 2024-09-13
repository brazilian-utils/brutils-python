import unicodedata
import json
from ..data.enums.uf import UF_CODE
import pathlib

def get_code_by_municipality_name(municipality_name: str, uf: str) -> str | None: 
    """
    Returns the IBGE code for a given municipality name.

    This function takes a string representing a municipality's name 
    and returns the corresponding IBGE code (string). The function 
    will handle names by ignoring differences in case, accents, and 
    treating the character ç as c.

    Args:
        municipality_name (str): The name of the municipality.

    Returns:
        str: The IBGE code of the municipality.
            - Returns None if the name is not valid or does not exist.

    Example:
        >>> get_code_by_municipality_name("São Paulo", "SP")
        "3550308"
        >>> get_code_by_municipality_name("goiania", "go")
        "5208707"
        >>> get_code_by_municipality_name("Conceição do Coité", "BA")
        "2909401"
        >>> get_code_by_municipality_name("conceicao do Coite", "Ba")
        "2909401"
        >>> get_code_by_municipality_name("Municipio Inexistente", "")
        None
    """
    abs_path = pathlib.Path(__file__).resolve()
    script_dir = abs_path.parent.parent

    json_file_path = script_dir / 'data' / 'cities_code.json'
    uf = uf.upper()
    uf_codes = UF_CODE.names
    
    if uf not in uf_codes:
        return None 
    
    name_city = transform_text(municipality_name)
    with open(json_file_path, 'r', encoding='utf-8') as file:
        file_cities = json.load(file)
   
    value = file_cities.get(name_city)

    if value == None:
        return None
    
    return str(UF_CODE[uf].value) + value

def transform_text(municipality_name: str): 
   
   normalized_string = unicodedata.normalize('NFKD', municipality_name).encode('ascii','ignore').decode('ascii')
   without_accent = ''.join(c for c in normalized_string if not unicodedata.combining(c)).casefold()

   return without_accent