from unittest import TestCase
from brutils.boleto import is_valid


class Boleto(TestCase):
    def test_is_valid(self):
        ## When boleto's len is different than 47 and 48, returns false
        self.assertFalse(is_valid("1"))
        self.assertTrue(is_valid(47 * "1"))
        self.assertTrue(is_valid(48 * "1"))
        ## When boleto is not string, returns False
        self.assertFalse(is_valid(1))
        ##verificação  -> fazer
        #    A linha é composta por 47 ou 48 dígitos que são distribuídos em 5 campos:
        #         | campo 1   |  campo 2   |  campo 3   |4|    campo 5    |
        #          1112X.XXXX3.XXXXX.XXXXX3.XXXXX.XXXXX3.4.5555.6666666666
        #           *5*   *5*   *5*   *6*    *5*   *6*  *1* *4*   *10*
        # 1 - Os três primeiros números da linha digitável identificam o código
        #      do banco que emitiu o boleto.
        # 2 - O quarto dígito indica a moeda. No caso do real será sempre o número 9.
        # 3 - Esse número representa o dígito verificador do boleto. Existe um dígito
        #      verificador no primeiro campo da linha, outro no segundo campo e outro
        #      no terceiro campo.
        # 4 - O único número do campo 4 representa o dígito verificador geral.
        # 5 - Os quatro números que aparecem depois do dígito verificador geral
        #      representam o fator de vencimento do boleto. Importante ressaltar
        #      que não será apresentado na forma de dia, mês e ano. Aparecerá a
        #      quantidade de dias que se passaram desde a data-base estipulada pelo
        #      Banco Central (7 de outubro de 1997). Ou seja, um boleto com vencimento
        #      em 05/09/2022 serão apresentados os números 9099.
        # 6 - Os 10 últimos números indicam o valor do documento, sem descontos. Ou seja,
        #      se o valor da conta é R$ 1,00 o final da sua linha digitável será 0000000100.
        # * - Os demais campos representados na imagem na cor cinza, são chamados de campos
        #      livres. Nesses campos cada banco pode definir de uma forma, como por exemplo,
        #      trazendo as informações do cliente (número da agência, número identificador
        #      do boleto, etc).
        #
        # SOURCE: https://forum.casadodesenvolvedor.com.br/topic/45002-quais-dados-est%C3%A3o-contidos-no-c%C3%B3digo-de-barras-do-boleto/
