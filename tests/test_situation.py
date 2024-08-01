from unittest import TestCase, main
import brutils
from brutils.voter_id import verify_situation

class TestSituation(TestCase):
    def test_invalid_format(self):
        # Caso onde o formato do título de eleitor não é válido
        invalid_voter_ids = [
            "123",            # Muito curto
            "12345678901234", # Muito longo
            "abcdefghijk"     # Contém caracteres não numéricos
        ]
        for voter_id in invalid_voter_ids:
            with self.subTest(voter_id=voter_id):
                self.assertIs(verify_situation(voter_id), None)  # Assume None para formatos inválidos

    def test_invalid_and_irregular(self):
        # Casos onde o título de eleitor é inválido pelo formato e é irregular
        voter_id = "12345678"
        self.assertIs(verify_situation(voter_id), False)

        voter_id = "123456789017"
        self.assertIs(verify_situation(voter_id), False)

    def test_valid_and_irregular(self):
        # Casos onde o título de eleitor é válido pelo formato e não é regular
        voter_id = '217633460930'
        self.assertIs(verify_situation(voter_id), False)

        voter_id = '183475722801'
        self.assertIs(verify_situation(voter_id), False)

    def test_valid_and_regular(self):
        # Caso onde o título de eleitor é válido pelo formato e é regular
        voter_id = '460230490124'
        self.assertIs(verify_situation(voter_id), True)

if __name__ == '__main__':
    main()
