from unittest import TestCase

import brutils


class TestImport(TestCase):
    def test_import(self):
        defined_names = dir(brutils)

        utilities = (
            "cpf",
            "is_valid_cpf",
            "format_cpf",
            "remove_symbols_cpf",
            "generate_cpf",
            "cnpj",
            "is_valid_cnpj",
            "format_cnpj",
            "remove_symbols_cnpj",
            "generate_cnpj",
            "cep",
            "is_valid_cep",
            "format_cep",
            "remove_symbols_cep",
            "generate_cep",
            "phone",
            "is_valid_phone",
            "format_phone",
            "remove_symbols_phone",
            "remove_international_dialing_code",
            "generate_phone",
            "email",
            "is_valid_email",
            "license_plate",
            "is_valid_license_plate",
            "format_license_plate",
            "remove_symbols_license_plate",
            "generate_license_plate",
            "convert_license_plate_to_mercosul",
            "get_format_license_plate",
            "pis",
            "is_valid_pis",
            "format_pis",
            "remove_symbols_pis",
            "generate_pis",
            "legal_process",
            "is_valid_legal_process",
            "format_legal_process",
            "remove_symbols_legal_process",
            "generate_legal_process",
            "voter_id",
            "is_valid_voter_id",
        )

        self.assertEqual(set(utilities) - set(defined_names), set({}))
