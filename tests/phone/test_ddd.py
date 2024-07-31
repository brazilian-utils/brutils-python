from unittest import TestCase, main
#import brutils
from brutils.phone import return_region_from_ddd

class TestDDD(TestCase):
    def test_invalid_Number(self):
        # Caso onde o ddd não existe
        invalid_phone= [
            "123",            # Número muito curto
            "12345678901234", # Número Muito longo
            "abcdefghijk",     # Número contém caracteres não numéricos
        ]
        for phone in invalid_phone:
            with self.subTest(phone=phone):
                self.assertIs(return_region_from_ddd(phone), None)  # Assume None para formatos inválidos

    def test_invalid_number_with_invalid_ddd(self):
        # Casos onde o numero é inválido
        phone = '123'
        self.assertIs(return_region_from_ddd(phone), False)

        phone = 'abcdefghijk'
        self.assertIs(return_region_from_ddd(phone), False)

    def test_valid_number_with_invalid_ddd(self):
        # Casos onde o numero é válido e o ddd não
        phone = '23999731703'
        self.assertIs(return_region_from_ddd(phone), "DDD não existe")

        phone = '5238761234'
        self.assertIs(return_region_from_ddd(phone), "DDD não existe")

    def test_valid_ddd_and_find_region(self):
        # Casos onde o numero é válido e o ddd também, deve-se retornar a região
        phone = '19999731703'
        self.assertIs(return_region_from_ddd(phone), "Campinas e região")

        phone = '1138761234'
        self.assertIs(return_region_from_ddd(phone), "São Paulo")

if __name__ == '__main__':
    main()
