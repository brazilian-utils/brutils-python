# flake8: noqa: F401

from brutils.cpf import (
    is_valid as is_valid_cpf,
    format_cpf,
    remove_symbols as remove_symbols_cpf,
    generate as generate_cpf,
)

from brutils.cnpj import (
    is_valid as is_valid_cnpj,
    format_cnpj,
    remove_symbols as remove_symbols_cnpj,
    generate as generate_cnpj,
)

from brutils.cep import (
    is_valid as is_valid_cep,
    format_cep,
    generate as generate_cep,
    remove_symbols as remove_symbols_cep,
)

from brutils.phone import (
    is_valid_landline as is_valid_landline_phone,
    is_valid_mobile as is_valid_mobile_phone,
    is_valid as is_valid_phone,
    format_phone,
    generate_mobile_phone,
)

from brutils.license_plate import (
    is_valid_mercosul as is_valid_license_plate_mercosul,
    is_valid_license_plate_old_format,
    is_valid as is_valid_license_plate,
    convert_to_mercosul as convert_license_plate_to_mercosul,
    format as format_license_plate,
    remove_symbols as remove_symbols_license_plate,
    get_format as get_license_plate_format,
)

from brutils.email import is_valid as is_valid_email

from brutils.pis import (
    is_valid as is_valid_pis,
    generate as generate_pis,
    remove_symbols as remove_symbols_pis,
    format_pis,
)

from brutils.legal_process import (
    format_processo_juridico,
    generate_processo_juridico,
    remove_symbols as remove_symbols_processo_juridico,
)
