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
)

from brutils.license_plate import (
    is_valid_mercosul as is_valid_license_plate_mercosul,
)

from brutils.email import is_valid as is_valid_email
from brutils.legal_process import (
    format_processo_juridico,
    remove_symbols as remove_symbols_legal_process,
)
from brutils.license_plate import is_valid_license_plate_old_format

from brutils.pis import (
    is_valid as is_valid_pis,
    generate as generate_pis,
)
