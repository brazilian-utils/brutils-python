from json import loads
from unicodedata import normalize
from urllib.request import urlopen

from brutils.data.enums import UF
from brutils.types import Address


# Reference: https://viacep.com.br/
def get_address_from_cep(cep: str) -> Address | None:
    """
    Fetches address information from a given CEP (Postal Code) using the ViaCEP API.

    Args:
        cep (str): The CEP (Postal Code) to be used in the search.
        raise_exceptions (bool, optional): Whether to raise exceptions when the CEP is invalid or not found. Defaults to False.

    Raises:
        ValueError: raised by urlopen.

    Returns:
        Address | None: An Address object (TypedDict) containing the address information if the CEP is found, None otherwise.

    Example:
        >>> get_address_from_cep("12345678")
        {
            "cep": "12345-678",
            "logradouro": "Rua Example",
            "complemento": "",
            "bairro": "Example",
            "localidade": "Example",
            "uf": "EX",
            "ibge": "1234567",
            "gia": "1234",
            "ddd": "12",
            "siafi": "1234"
        }

        >>> get_address_from_cep("abcdefg")
        None

        >>> get_address_from_cep("abcdefg")
        None

        >>> get_address_from_cep("00000000")
        None
    """
    base_api_url = "https://viacep.com.br/ws/{}/json/"

    # Removing some symbols from cep.
    clean_cep = "".join(filter(lambda char: char not in ".-", cep))
    # Cheking if a cep is value.
    cep_is_valid = isinstance(cep, str) and len(cep) == 8 and cep.isdigit()

    if not cep_is_valid:
        return None

    try:
        with urlopen(base_api_url.format(clean_cep)) as f:
            response = f.read()
            data = loads(response)
            return None if data.get("erro") else Address(**loads(response))

    except ValueError:
        return None


def get_cep_information_from_address(
    federal_unit: str, city: str, street: str
) -> list[Address] | None:
    """
    Fetches CEP (Postal Code) options from a given address using the ViaCEP API.

    Args:
        federal_unit (str): The two-letter abbreviation of the Brazilian state.
        city (str): The name of the city.
        street (str): The name (or substring) of the street.
        raise_exceptions (bool, optional): Whether to raise exceptions when the address is invalid or not found. Defaults to False.

    Raises:
        ValueError: raised by urlopen.

    Returns:
        list[Address] | None: A list of Address objects (TypedDict) containing the address information if the address is found, None otherwise.

    Example:
        >>> get_cep_information_from_address("EX", "Example", "Rua Example")
        [
            {
                "cep": "12345-678",
                "logradouro": "Rua Example",
                "complemento": "",
                "bairro": "Example",
                "localidade": "Example",
                "uf": "EX",
                "ibge": "1234567",
                "gia": "1234",
                "ddd": "12",
                "siafi": "1234"
            }
        ]

        >>> get_cep_information_from_address("A", "Example", "Rua Example")
        None

        >>> get_cep_information_from_address("XX", "Example", "Example", True)
        None

        >>> get_cep_information_from_address("SP", "Example", "Example", True)
        None
    """
    if federal_unit in UF.values:
        federal_unit = UF(federal_unit).name

    if federal_unit not in UF.names:
        return None

    base_api_url = "https://viacep.com.br/ws/{}/{}/{}/json/"

    parsed_city = (
        normalize("NFD", city)
        .encode("ascii", "ignore")
        .decode("utf-8")
        .replace(" ", "%20")
    )
    parsed_street = (
        normalize("NFD", street)
        .encode("ascii", "ignore")
        .decode("utf-8")
        .replace(" ", "%20")
    )

    try:
        with urlopen(
            base_api_url.format(federal_unit, parsed_city, parsed_street)
        ) as f:
            response = f.read()
            response = loads(response)
            return (
                None
                if len(response) == 0
                else [Address(**address) for address in response]
            )

    except ValueError:
        return None
