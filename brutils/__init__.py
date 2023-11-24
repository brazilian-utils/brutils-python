# flake8: noqa: F401

from brutils.cpf import (
    format_cpf,
    generate as generate_cpf,
    is_valid as is_valid_cpf,
    remove_symbols as remove_symbols_cpf,
)

from brutils.cnpj import (
    format_cnpj,
    generate as generate_cnpj,
    is_valid as is_valid_cnpj,
    remove_symbols as remove_symbols_cnpj,
)

from brutils.cep import (
    format_cep,
    generate as generate_cep,
    is_valid as is_valid_cep,
    remove_symbols as remove_symbols_cep,
)

from brutils.phone import (
    format_phone,
    generate_landline_phone,
    generate_mobile_phone,
    is_valid as is_valid_phone,
)

from brutils.license_plate import (
    convert_to_mercosul as convert_license_plate_to_mercosul,
    format as format_license_plate,
    get_format as get_license_plate_format,
    is_valid as is_valid_license_plate,
    remove_symbols as remove_symbols_license_plate,
)

from brutils.email import is_valid as is_valid_email

from brutils.pis import (
    format_pis,
    generate as generate_pis,
    is_valid as is_valid_pis,
    remove_symbols as remove_symbols_pis,
)

from brutils.legal_process import (
    format_legal_process,
    generate as generate_legal_process,
    is_valid as is_valid_legal_process,
    remove_symbols as remove_symbols_legal_process,
)
