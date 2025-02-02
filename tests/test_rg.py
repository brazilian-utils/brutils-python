from unittest import TestCase
from brutils.rg import is_valid_rg

class TestRG(TestCase):
    # Base do Github
    # def test_is_valid_rg(self):
    #     # Testes para RGs válidos
    #     self.assertTrue(is_valid_rg('12.345.678-9', 'SP'))
    #     self.assertTrue(is_valid_rg('MG-12.345.678', 'MG'))
    #     self.assertTrue(is_valid_rg('123456789', 'RJ'))
    #
    #     # Testes para RGs inválidos
    #     self.assertFalse(is_valid_rg('A12345678', 'SP'))  # Letras não permitidas
    #     self.assertFalse(is_valid_rg('1234567890', 'SP'))  # RG longo demais
    #     self.assertFalse(is_valid_rg('12.345.678-10', 'SP'))  # Dígito verificador incorreto
    #
    #     # Testes para entradas malformadas
    #     self.assertFalse(is_valid_rg('', 'SP'))  # Entrada vazia
    #     self.assertFalse(is_valid_rg('12.345.678', 'SP'))  # Formato incorreto sem dígito verificador
    #     self.assertFalse(is_valid_rg('12.345.678-9', 'XX'))  # UF inválida

    def test_valid_rg_sp(self):
        # Testes para SP (São Paulo) – validação com dígito verificador
        self.assertTrue(is_valid_rg("12.345.678-9", "SP"))
        # Exemplo com dígito calculado: "11.111.111-0" (1*2+1*3+...+1*9 = 44; 44 % 11 = 0)
        self.assertTrue(is_valid_rg("11.111.111-0", "SP"))
        # Dígito verificador incorreto
        self.assertFalse(is_valid_rg("11.111.111-1", "SP"))
        # Formato incorreto: falta o hífen
        self.assertFalse(is_valid_rg("12.345.6789", "SP"))

    def test_valid_rg_mg(self):
        # Testes para MG (Minas Gerais) – somente verificação de formato
        self.assertTrue(is_valid_rg("MG-12.345.678", "MG"))
        # Ausência do prefixo "MG-"
        self.assertFalse(is_valid_rg("12.345.678", "MG"))
        # Formato sem hífen após o prefixo
        self.assertFalse(is_valid_rg("MG12.345.678", "MG"))

    def test_valid_rg_rj(self):
        # Testes para RJ (Rio de Janeiro) – somente RG composto por 9 dígitos
        self.assertTrue(is_valid_rg("123456789", "RJ"))
        # Formatação não permitida para RJ
        self.assertFalse(is_valid_rg("12.345.678-9", "RJ"))
        # Contém caractere não numérico
        self.assertFalse(is_valid_rg("12345678A", "RJ"))

    def test_valid_rg_norte(self):
        # Estados da Região Norte: AC, AP, AM, PA, RO, RR, TO (padrão "2_3_groups_dash")
        for uf in ["AC", "AP", "AM", "PA", "RO", "RR", "TO"]:
            with self.subTest(uf=uf):
                self.assertTrue(is_valid_rg("12.345.678-9", uf))
                # Formato incorreto: ausência do hífen
                self.assertFalse(is_valid_rg("12.345.6789", uf))

    def test_valid_rg_nordeste(self):
        # Estados com padrão "2_3_groups_dash": AL, CE, MA, PE, PI, RN
        for uf in ["AL", "CE", "MA", "PE", "PI", "RN"]:
            with self.subTest(uf=uf):
                self.assertTrue(is_valid_rg("12.345.678-9", uf))
                # Formato sem formatação adequada (apenas dígitos)
                self.assertFalse(is_valid_rg("123456789", uf))
        # BA utiliza o padrão "8_digits_dash": exemplo "12345678-9"
        self.assertTrue(is_valid_rg("12345678-9", "BA"))
        self.assertFalse(is_valid_rg("12.345.678-9", "BA"))
        # PB e SE usam o padrão "9_digits"
        for uf in ["PB", "SE"]:
            with self.subTest(uf=uf):
                self.assertTrue(is_valid_rg("123456789", uf))
                self.assertFalse(is_valid_rg("12.345.678-9", uf))

    def test_valid_rg_centro_oeste(self):
        # Estados: DF, GO, MT, MS (padrão "2_3_groups_dash")
        for uf in ["DF", "GO", "MT", "MS"]:
            with self.subTest(uf=uf):
                self.assertTrue(is_valid_rg("12.345.678-9", uf))
                # Formato sem formatação esperada
                self.assertFalse(is_valid_rg("123456789", uf))

    def test_valid_rg_sudeste(self):
        # ES utiliza o padrão "2_3_groups_dash"
        self.assertTrue(is_valid_rg("12.345.678-9", "ES"))
        self.assertFalse(is_valid_rg("123456789", "ES"))
        # RJ e SP já foram testados separadamente e possuem regras próprias

    def test_valid_rg_sul(self):
        # PR utiliza o padrão "3_groups_dash" (igual a SP, mas sem a validação do dígito verificador)
        self.assertTrue(is_valid_rg("12.345.678-9", "PR"))
        self.assertFalse(is_valid_rg("123456789", "PR"))
        # RS utiliza o padrão "7_10_digits" – aceita RG com 7 ou 8 dígitos formatados com pontos
        self.assertTrue(is_valid_rg("1.234.567", "RS"))
        self.assertTrue(is_valid_rg("12.345.678", "RS"))
        self.assertFalse(is_valid_rg("12.345.678-9", "RS"))
        # SC utiliza o padrão "3_groups": formato exato de três grupos de três dígitos
        self.assertTrue(is_valid_rg("123.456.789", "SC"))
        self.assertFalse(is_valid_rg("12.345.678-9", "SC"))

    def test_invalid_inputs(self):
        # Teste para entradas malformadas e UFs inválidas
        self.assertFalse(is_valid_rg("", "SP"))  # Entrada vazia
        self.assertFalse(is_valid_rg("   ", "RJ"))  # Somente espaços
        self.assertFalse(
            is_valid_rg("12.345.678", "SP")
        )  # Falta dígito verificador
        self.assertFalse(is_valid_rg("12.345.678-9", "XX"))  # UF não mapeada

        # Testando parâmetros None: esperamos que ocorra um erro de tipo
        self.assertFalse(is_valid_rg(None, "SP"))
        self.assertFalse(is_valid_rg("12.345.678-9", None))
