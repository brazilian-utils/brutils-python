from unittest import TestCase
from brutils.types.boleto import Boleto
from brutils.boleto import format_boleto  

class TestBoleto(TestCase):
    def test_format_boleto(self):
        boleto: Boleto = {
            "bank_issuing": 237,   
            "coin_type": 9,       
            "due_date": "300125",  
            "amount": 1500.75,    
            "our_number": "12345678901",
            "free_field": "1",     
            "barcode": "23791800000015007500012345678901"
        }

        formatted_boleto = format_boleto(boleto)

        expected_boleto = '23791.80000 01500.750000 12345.678901 1 10010000055000'

        self.assertEqual(formatted_boleto, expected_boleto)
