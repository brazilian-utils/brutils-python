# CEP Imports
from brutils.cep import (
    format_cep,
    get_address_from_cep,
    get_cep_information_from_address,
)
from brutils.cep import (
    generate as generate_cep,
)
from brutils.cep import (
    is_valid as is_valid_cep,
)
from brutils.cep import (
    remove_symbols as remove_symbols_cep,
)

# CNPJ Imports
from brutils.cnpj import (
    format_cnpj,
)
from brutils.cnpj import (
    generate as generate_cnpj,
)
from brutils.cnpj import (
    is_valid as is_valid_cnpj,
)
from brutils.cnpj import (
    remove_symbols as remove_symbols_cnpj,
)

# CPF Imports
from brutils.cpf import (
    format_cpf,
)
from brutils.cpf import (
    generate as generate_cpf,
)
from brutils.cpf import (
    is_valid as is_valid_cpf,
)
from brutils.cpf import (
    remove_symbols as remove_symbols_cpf,
)

# Email Import
from brutils.email import is_valid as is_valid_email

# IBGE Imports
from brutils.ibge.uf import (
    convert_code_to_uf,
)

# Legal Process Imports
from brutils.legal_process import (
    format_legal_process,
)
from brutils.legal_process import (
    generate as generate_legal_process,
)
from brutils.legal_process import (
    is_valid as is_valid_legal_process,
)
from brutils.legal_process import (
    remove_symbols as remove_symbols_legal_process,
)

# License Plate Imports
from brutils.license_plate import (
    convert_to_mercosul as convert_license_plate_to_mercosul,
)
from brutils.license_plate import (
    format_license_plate,
)
from brutils.license_plate import (
    generate as generate_license_plate,
)
from brutils.license_plate import (
    get_format as get_format_license_plate,
)
from brutils.license_plate import (
    is_valid as is_valid_license_plate,
)
from brutils.license_plate import (
    remove_symbols as remove_symbols_license_plate,
)

# Phone Imports
from brutils.phone import (
    format_phone,
    remove_international_dialing_code,
    remove_symbols_phone,
)
from brutils.phone import (
    generate as generate_phone,
)
from brutils.phone import (
    is_valid as is_valid_phone,
)

# PIS Imports
from brutils.pis import (
    format_pis,
)
from brutils.pis import (
    generate as generate_pis,
)
from brutils.pis import (
    is_valid as is_valid_pis,
)
from brutils.pis import (
    remove_symbols as remove_symbols_pis,
)

# RENAVAM Imports
from brutils.renavam import (
    is_valid_renavam,
)

# Voter ID Imports
from brutils.voter_id import (
    format_voter_id,
)
from brutils.voter_id import (
    generate as generate_voter_id,
)
from brutils.voter_id import (
    is_valid as is_valid_voter_id,
)

# Defining __all__ to expose the public methods
__all__ = [
    # CEP
    "format_cep",
    "get_address_from_cep",
    "get_cep_information_from_address",
    "generate_cep",
    "is_valid_cep",
    "remove_symbols_cep",
    # CNPJ
    "format_cnpj",
    "generate_cnpj",
    "is_valid_cnpj",
    "remove_symbols_cnpj",
    # CPF
    "format_cpf",
    "generate_cpf",
    "is_valid_cpf",
    "remove_symbols_cpf",
    # Email
    "is_valid_email",
    # Legal Process
    "format_legal_process",
    "generate_legal_process",
    "is_valid_legal_process",
    "remove_symbols_legal_process",
    # License Plate
    "convert_license_plate_to_mercosul",
    "format_license_plate",
    "generate_license_plate",
    "get_format_license_plate",
    "is_valid_license_plate",
    "remove_symbols_license_plate",
    # Phone
    "format_phone",
    "remove_international_dialing_code",
    "remove_symbols_phone",
    "generate_phone",
    "is_valid_phone",
    # PIS
    "format_pis",
    "generate_pis",
    "is_valid_pis",
    "remove_symbols_pis",
    # Voter ID
    "format_voter_id",
    "generate_voter_id",
    "is_valid_voter_id",
    # IBGE
    "convert_code_to_uf",
    # RENAVAM
    "is_valid_renavam",
]
