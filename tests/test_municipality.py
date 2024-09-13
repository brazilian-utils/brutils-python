from unittest import TestCase
from brutils.ibge.municipality import get_code_by_municipality_name

class TestIBGE(TestCase):
    def test_get_code_by_municipality_name(self):
        self.assertEqual(get_code_by_municipality_name("São Paulo", "sp" ), "3550308")
        self.assertEqual(get_code_by_municipality_name("GOIANIA", "GO"), "5208707")
        self.assertEqual(get_code_by_municipality_name("Conceição do Coité", "BA"), "2908408")
        self.assertEqual(get_code_by_municipality_name("conceicao do Coite", "Ba"), "2908408") 
        self.assertIsNone(get_code_by_municipality_name("Municipio Inexistente",""))
        self.assertEqual(get_code_by_municipality_name("rio de janeiro", "rj"), "3304557")
