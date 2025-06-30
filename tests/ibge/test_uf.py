from unittest import TestCase

from brutils.ibge.uf import convert_code_to_uf, convert_text_to_uf

class TestUF(TestCase):
    def test_convert_code_to_uf(self):
        # Testes para códigos válidos
        self.assertEqual(convert_code_to_uf("12"), "AC")
        self.assertEqual(convert_code_to_uf("33"), "RJ")
        self.assertEqual(convert_code_to_uf("31"), "MG")
        self.assertEqual(convert_code_to_uf("52"), "GO")

        # Testes para códigos inválidos
        self.assertIsNone(convert_code_to_uf("99"))
        self.assertIsNone(convert_code_to_uf("00"))
        self.assertIsNone(convert_code_to_uf(""))
        self.assertIsNone(convert_code_to_uf("AB"))

    def test_convert_text_to_uf(self):
        """Testa a conversão de nomes de estados brasileiros para suas UFs correspondentes."""
        # Testes para nomes válidos (nomes oficiais, com e sem acento, caixa variada)
        self.assertEqual(convert_text_to_uf('São Paulo'), "SP")
        self.assertEqual(convert_text_to_uf('Rio de Janeiro'), "RJ")
        self.assertEqual(convert_text_to_uf('Minas Gerais'), "MG")
        self.assertEqual(convert_text_to_uf('Distrito Federal'), "DF")
        self.assertEqual(convert_text_to_uf('são paulo'), "SP")  # caixa baixa
        self.assertEqual(convert_text_to_uf('riO de janeiRo'), "RJ")  # caixa mista
        self.assertEqual(convert_text_to_uf('minas gerais'), "MG")
        self.assertEqual(convert_text_to_uf('sao paulo'), "SP")  # sem acento
        self.assertEqual(convert_text_to_uf('Acre'), "AC")
        self.assertEqual(convert_text_to_uf('Goias'), "GO")  # sem acento
        self.assertEqual(convert_text_to_uf('goiás'), "GO")  # com acento
        self.assertEqual(convert_text_to_uf('Espírito Santo'), "ES")
        self.assertEqual(convert_text_to_uf('espirito santo'), "ES")  # sem acento
        self.assertEqual(convert_text_to_uf('Maranhão'), "MA")
        self.assertEqual(convert_text_to_uf('maranhao'), "MA")  # sem acento
        self.assertEqual(convert_text_to_uf('Pará'), "PA")
        self.assertEqual(convert_text_to_uf('para'), "PA")  # sem acento
        self.assertEqual(convert_text_to_uf('Rio Grande do Norte'), "RN")
        self.assertEqual(convert_text_to_uf('rio grande do norte'), "RN")
        self.assertEqual(convert_text_to_uf('Rio Grande do Sul'), "RS")
        self.assertEqual(convert_text_to_uf('rIo gRanDe dO sUl'), "RS")  # caixa mista
        self.assertEqual(convert_text_to_uf('   São Paulo   '), "SP")  # espaços extras
        self.assertEqual(convert_text_to_uf('\tMinas Gerais\n'), "MG")  # tabulação e quebra de linha

        # Testes para nomes válidos com entradas pouco usuais (acentuação diferente e caixa alta)
        self.assertEqual(convert_text_to_uf('PARANÁ'), "PR")  # caixa alta e acento
        self.assertEqual(convert_text_to_uf('tocantins'), "TO")  # caixa baixa
        self.assertEqual(convert_text_to_uf('bahia'), "BA")
        self.assertEqual(convert_text_to_uf('Ceará'), "CE")  # acento correto
        self.assertEqual(convert_text_to_uf('ceara'), "CE")  # sem acento

        # Testes para nomes inválidos (nomes inexistentes, vazios, formatos estranhos ou erros de digitação)
        self.assertIsNone(convert_text_to_uf('Estado Inexistente'))  # estado não existe
        self.assertIsNone(convert_text_to_uf(''))  # string vazia
        self.assertIsNone(convert_text_to_uf('123'))  # apenas números
        self.assertIsNone(convert_text_to_uf('São Paulo SP'))  # nome + sigla junto
        self.assertIsNone(convert_text_to_uf('A'))  # muito curto
        self.assertIsNone(convert_text_to_uf('ZZZ'))  # string sem relação
        self.assertIsNone(convert_text_to_uf('Sao-Paulo'))  # hífen não previsto no padrão
        self.assertIsNone(convert_text_to_uf('Amazonass'))  # erro de digitação
        self.assertIsNone(convert_text_to_uf('Santa Catarina do Sul'))  # estado não existe

        # Teste para None como entrada (input nulo)
        self.assertIsNone(convert_text_to_uf(None))

        # Teste para tipos inesperados (entrada que não é string)
        self.assertIsNone(convert_text_to_uf(12345))  # inteiro
        self.assertIsNone(convert_text_to_uf(['São Paulo']))  # lista