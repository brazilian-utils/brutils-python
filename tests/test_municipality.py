from unittest import TestCase

from brutils.ibge.municipality import get_code_by_municipality_name


class TestIBGE(TestCase):
    def test_get_code_by_municipality_name(self):
        self.assertEqual(
            get_code_by_municipality_name("Florianópolis", "sc"), "4205407"
        )
        self.assertEqual(
            get_code_by_municipality_name("São Paulo", "sp"), "3550308"
        )
        self.assertEqual(
            get_code_by_municipality_name("GOIANIA", "GO"), "5208707"
        )
        self.assertEqual(
            get_code_by_municipality_name("Conceição do Coité", "BA"), "2908408"
        )
        self.assertEqual(
            get_code_by_municipality_name("conceicao do Coite", "Ba"), "2908408"
        )
        self.assertEqual(
            get_code_by_municipality_name("rio de janeiro", "rj"), "3304557"
        )
        self.assertEqual(
            get_code_by_municipality_name("Lauro Müller", "sc"), "4209607"
        )
        self.assertEqual(
            get_code_by_municipality_name("Tôrres", "rs"), "4321501"
        )
        self.assertEqual(
            get_code_by_municipality_name("aurora", "ce"), "2301703"
        )
        self.assertEqual(
            get_code_by_municipality_name("aurora", "sc"), "4201901"
        )
        self.assertIsNone(
            get_code_by_municipality_name("Municipio Inexistente", "RS")
        )
        self.assertIsNone(
            get_code_by_municipality_name("Municipio Inexistente", "")
        )
