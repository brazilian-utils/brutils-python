from unittest import TestCase, main
import brutils
from brutils.phone import return_region_from_ddd

class TestDDD(TestCase):
    def test_invalid_Number(self):
        # Caso onde o ddd não existe
        invalid_phone= [
            '123',            # Número muito curto
            '12345678901234', # Número Muito longo
            'abcdefghijk',     # Número contém caracteres não numéricos
        ]
        for phone in invalid_phone:
            with self.subTest(phone=phone):
                self.assertIs(return_region_from_ddd(phone), None)  # Assume None para formatos inválidos

    def test_invalid_number_with_invalid_ddd(self):
        # Casos onde o numero é inválido
        phone = '123'
        self.assertIs(return_region_from_ddd(phone), None)

        phone = 'abcdefghijk'
        self.assertIs(return_region_from_ddd(phone), None)

    def test_valid_number_with_invalid_ddd(self):
        # Casos onde o numero é válido e o ddd não
        phone = '23999731703'
        self.assertEqual(return_region_from_ddd(phone), "DDD não existe")

        phone = '5238761234'
        self.assertEqual(return_region_from_ddd(phone), "DDD não existe")

    # Região Sul
    def test_valid_ddd_and_find_regionRS(self):
        phone = '51930001082'
        self.assertEqual(return_region_from_ddd(phone), "Porto Alegre e região")

        phone = '5335887651'
        self.assertEqual(return_region_from_ddd(phone), "Caxias do Sul e região")

        phone = '5442945078'
        self.assertEqual(return_region_from_ddd(phone), "Serra Gaúcha")

        phone = '55924498129'
        self.assertEqual(return_region_from_ddd(phone), "Santa Maria e região")

    def test_valid_ddd_and_find_regionSC(self):
        phone = '4840381307'
        self.assertEqual(return_region_from_ddd(phone), "Florianópolis e região")

        phone = '42955639405'
        self.assertEqual(return_region_from_ddd(phone), "Ponta Grossa e região")

    def test_valid_ddd_and_find_regionPR(self):
        phone = '41973458654'
        self.assertEqual(return_region_from_ddd(phone), "Curitiba e região")

        phone = '42981286906'
        self.assertEqual(return_region_from_ddd(phone), "Ponta Grossa e região")

        phone = '43926724648'
        self.assertEqual(return_region_from_ddd(phone), "Londrina e região")

        phone = '44905858922'
        self.assertEqual(return_region_from_ddd(phone), "Maringá e região")

        phone = '45911215368'
        self.assertEqual(return_region_from_ddd(phone), "Foz do Iguaçu e região")

        phone = '46989326201'
        self.assertEqual(return_region_from_ddd(phone), "Francisco Beltrão e região")

    # Região Sudeste
    def test_valid_ddd_and_find_regionSP(self):
        phone = '11943118548'
        self.assertEqual(return_region_from_ddd(phone), "São Paulo")

        phone = '1256825073'
        self.assertEqual(return_region_from_ddd(phone), "São José dos Campos e região")

        phone = '1357666227'
        self.assertEqual(return_region_from_ddd(phone), "Santos e região")

        phone = '14933246128'
        self.assertEqual(return_region_from_ddd(phone), "Bauru e região")

        phone = '15925000463'
        self.assertEqual(return_region_from_ddd(phone), "Sorocaba e região")

        phone = '1633559157'
        self.assertEqual(return_region_from_ddd(phone), "Ribeirão Preto e região")

        phone = '1749290450'
        self.assertEqual(return_region_from_ddd(phone), "São José do Rio Preto e região")

        phone = '1833764233'
        self.assertEqual(return_region_from_ddd(phone), "Presidente Prudente e região")

        phone = '1926798926'
        self.assertEqual(return_region_from_ddd(phone), "Campinas e região")

    def test_valid_ddd_and_find_regionRJ(self):
        phone = '21999731703'
        self.assertEqual(return_region_from_ddd(phone), "Rio de Janeiro")

        phone = '2234441107'
        self.assertEqual(return_region_from_ddd(phone), "Região dos Lagos (Rio de Janeiro)")

        phone = '2450980685'
        self.assertEqual(return_region_from_ddd(phone), "Região Serrana (Rio de Janeiro)")

    def test_valid_ddd_and_find_regionMG(self):
        phone = '31928188258'
        self.assertEqual(return_region_from_ddd(phone), "Belo Horizonte e região")

        phone = '3230598537'
        self.assertEqual(return_region_from_ddd(phone), "Juiz de Fora e região")

        phone = '3327950073'
        self.assertEqual(return_region_from_ddd(phone), "Teófilo Otoni e região")

        phone = '34917250859'
        self.assertEqual(return_region_from_ddd(phone), "Uberlândia e região")

        phone = '3520597609'
        self.assertEqual(return_region_from_ddd(phone), "Poços de Caldas e região")

        phone = '37950031365'
        self.assertEqual(return_region_from_ddd(phone), "Divinópolis e região")

    def test_valid_ddd_and_find_regionES(self):
        phone = '27999731703'
        self.assertEqual(return_region_from_ddd(phone), "Espírito Santo")

        phone = '2848065584'
        self.assertEqual(return_region_from_ddd(phone), "Região Norte do Espírito Santo")

    # Região Centro-Oeste
    def test_valid_ddd_and_find_regionMS(self):
        phone = '67947863711'
        self.assertEqual(return_region_from_ddd(phone), "Mato Grosso do Sul")

    def test_valid_ddd_and_find_regionGO(self):
        phone = '6127393552'
        self.assertEqual(return_region_from_ddd(phone), "Brasília e região")
        
        phone = '6257053923'
        self.assertEqual(return_region_from_ddd(phone), "Goiânia e região")

        phone = '6435506880'
        self.assertEqual(return_region_from_ddd(phone), "Caldas Novas e região")

    def test_valid_ddd_and_find_regionMT(self):
        phone = '65959496245'
        self.assertEqual(return_region_from_ddd(phone), "Cuiabá e região")

        phone = '6636145678'
        self.assertEqual(return_region_from_ddd(phone), "Rondonópolis e região")

    # Região Norte
    def test_valid_ddd_and_find_regionAM(self):
        phone = '9232550373'
        self.assertEqual(return_region_from_ddd(phone), "Manaus e região")

        phone = '9751347518'
        self.assertEqual(return_region_from_ddd(phone), "Interior do Amazonas")

    def test_valid_ddd_and_find_regionPA(self):
        phone = '91924782874'
        self.assertEqual(return_region_from_ddd(phone), "Belém e região")

        phone = '93991720632'
        self.assertEqual(return_region_from_ddd(phone), "Santarem e região")

        phone = '9432555302'
        self.assertEqual(return_region_from_ddd(phone), "Marabá")

    def test_valid_ddd_and_find_regionRO(self):
        phone = '69962847275'
        self.assertEqual(return_region_from_ddd(phone), "Rondônia")

    def test_valid_ddd_and_find_regionAC(self):
        phone = '6839770628'
        self.assertEqual(return_region_from_ddd(phone), "Acre")

    def test_valid_ddd_and_find_regionRR(self):
        phone = '95901621074'
        self.assertEqual(return_region_from_ddd(phone), "Roraima")

    def test_valid_ddd_and_find_regionTO(self):
        phone = '63940537366'
        self.assertEqual(return_region_from_ddd(phone), "Tocantins")

    # Região Nordeste
    def test_valid_ddd_and_find_regionMA(self):
        phone = '9846786371'
        self.assertEqual(return_region_from_ddd(phone), "São Luís e região")

        phone = '99982293437'
        self.assertEqual(return_region_from_ddd(phone), "Imperatriz e região")

    def test_valid_ddd_and_find_regionPI(self):
        phone = '8624471699'
        self.assertEqual(return_region_from_ddd(phone), "Teresina e região")

        phone = '89900649794'
        self.assertEqual(return_region_from_ddd(phone), "Picos e região")

    def test_valid_ddd_and_find_regionBA(self):
        phone = '71970402789'
        self.assertEqual(return_region_from_ddd(phone), "Salvador e região")

        phone = '73977336050'
        self.assertEqual(return_region_from_ddd(phone), "Porto Seguro e região")
        
        phone = '74975818508'
        self.assertEqual(return_region_from_ddd(phone), "Juazeiro e região")
        
        phone = '7528510745'
        self.assertEqual(return_region_from_ddd(phone), "Alagoinhas e região")
        
        phone = '7734269107'
        self.assertEqual(return_region_from_ddd(phone), "Barreiras e região")

    def test_valid_ddd_and_find_regionCE(self):
        phone = '8538386263'
        self.assertEqual(return_region_from_ddd(phone), "Fortaleza e região")

        phone = '88909363656'
        self.assertEqual(return_region_from_ddd(phone), "Sobral e região")

    def test_valid_ddd_and_find_regionRN(self):
        phone = '8426881088'
        self.assertEqual(return_region_from_ddd(phone), "Rio Grande do Norte")

    def test_valid_ddd_and_find_regionPB(self):
        phone = '8331274076'
        self.assertEqual(return_region_from_ddd(phone), "Paraíba")

    def test_valid_ddd_and_find_regionPE(self):
        phone = '8126267758'
        self.assertEqual(return_region_from_ddd(phone), "Recife e região")

        phone = '8741722384'
        self.assertEqual(return_region_from_ddd(phone), "Petrolina e região")
    
    def test_valid_ddd_and_find_regionAL(self):
        phone = '82901204823'
        self.assertEqual(return_region_from_ddd(phone), "Alagoas")
    
    def test_valid_ddd_and_find_regionSE(self):
        phone = '7945259102'
        self.assertEqual(return_region_from_ddd(phone), "Sergipe")

if __name__ == '__main__':
    main()
