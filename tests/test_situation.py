#existem 3 casos a serem tratados antes, um se o formato não é válido e é outro processo que analisa isso, um onde ele é valido e a situação é irregular,
#outro onde ele é válido e a situação é regular

from unittest import TestCase, main
import brutils
from brutils.voter_id import (
    _calculate_vd1,
    _calculate_vd2,
    _get_federative_union,
    _get_sequential_number,
    _get_verifying_digits,
    _is_length_valid,
    format_voter_id,
    generate,
    is_valid,
    verify_situation
)

class TestSituation(TestCase):
    def test_is_valid(self):
        voter_id = "12345678" #caso onde o Titulo de eleitor é irregular
        self.assertIs(verify_situation(voter_id), False)#mudar para false

        voter_id = "123456789017" #caso onde o título de eleitor é irregular
        self.assertIs(verify_situation(voter_id), False)#mudar para false



    def valid_and_irregular(self):
        voter_id = '217633460930' #caso onde o título de eleitor é válido e não é regular
        self.assertIs(verify_situation(voter_id), False)
        
        voter_id = '183475722801' #caso onde o título de eleitor é válido e não é regular
        self.assertIs(verify_situation(voter_id), False)
    
    
    def valid_and_regular(self):
        voter_id = '460230490124'
        self.assertIs(verify_situation(voter_id), True)



    


