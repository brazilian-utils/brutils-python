import unittest
from brutils.titulo_eleitoral import (
    is_valid_titulo_eleitoral,
    _get_titulo_eleitoral_parts,
    _calculate_dv1,
    _verify_length,
    _verify_dv1,
    _verify_dv2,
    generate_titulo_eleitoral,
)


class TestIsValidTituloEleitoral(unittest.TestCase):
    def test_valid_titulo_eleitoral(self):
        # test a valid titulo eleitoral number
        valid_titulo = "217633460930"
        self.assertTrue(is_valid_titulo_eleitoral(valid_titulo))

    def test_invalid_titulo_eleitoral(self):
        # test an invalid titulo eleitoral number (dv1 & UF fail)
        invalid_titulo = "123456789011"
        self.assertFalse(is_valid_titulo_eleitoral(invalid_titulo))
    
    def test_invalid_length(self):
        # Test an invalid length for titulo eleitoral
        invalid_length_short = "12345678901"
        invalid_length_long = "1234567890123"
        self.assertFalse(is_valid_titulo_eleitoral(invalid_length_short))
        self.assertTrue(is_valid_titulo_eleitoral(invalid_length_long))

    def test_invalid_characters(self):
        # Test titulo eleitoral with non-numeric characters
        invalid_characters = "ABCD56789012"
        invalid_characters_space = "217633 460 930"
        self.assertFalse(is_valid_titulo_eleitoral(invalid_characters))
        self.assertFalse(is_valid_titulo_eleitoral(invalid_characters_space))

    def test_valid_special_case(self):
        # Test a valid edge case (SP & MG with 13 digits)
        valid_special = "3244567800167"
        self.assertTrue(is_valid_titulo_eleitoral(valid_special))


class TestSplitString(unittest.TestCase):
    def test_get_titulo_eleitoral_parts(self):
        input_string = "12345678AB12"
        (
            tit_sequence,
            tit_unid_fed,
            tit_dig_verifiers,
        ) = _get_titulo_eleitoral_parts(input_string)
        self.assertEqual(tit_sequence, "12345678")
        self.assertEqual(tit_unid_fed, "AB")
        self.assertEqual(tit_dig_verifiers, "12")


class TestVerifyLength(unittest.TestCase):
    def test_valid_length(self):
        numero_titulo = "123456789012"
        tit_unid_fed = "AB"
        self.assertTrue(_verify_length(numero_titulo, tit_unid_fed))

    def test_invalid_length(self):
        numero_titulo = "12345678AB123"  # Invalid length
        tit_unid_fed = "AB"
        self.assertFalse(_verify_length(numero_titulo, tit_unid_fed))


class TestVerifyDv1(unittest.TestCase):
    def test_verify_dv1(self):
        # test dv1 converts from 10 to 0 and UF is "01" (SP)
        self.assertTrue(_verify_dv1(10, "01", "01")[0])
        # test dv1 converts from 10 to 0 and UF is "02" (MG)
        self.assertTrue(_verify_dv1(10, "02", "01")[0])

    def test_dv1_ten_edge_case(self):
        # test dv1 is 10, which should be treated as 0
        self.assertTrue(_verify_dv1(10, "04", "05")[0])

    def test_dv1_zero_edge_case(self):
        # test dv1 is 0, declare as 1 instead with SP or MG as UF
        self.assertTrue(_verify_dv1(0, "01", "16")[0])
        self.assertTrue(_verify_dv1(0, "02", "15")[0])


class TestVerifyDv2(unittest.TestCase):
    def test_verify_dv2(self):
        self.assertTrue(_verify_dv2("03", 6, "01"))

    def test_dv2_zero_edge_case(self):
        # edge case: if UF is "01" or "02" (for SP & MG) AND dv2 == 0
        # declare dv2 as 1 instead
        self.assertTrue(_verify_dv2("01", 9, "01"))
        self.assertTrue(_verify_dv2("01", 4, "41"))


class TestGenerateTituloEleitoral(unittest.TestCase):
    def test_generate(self):
        # Is valid
        self.assertIsNotNone(
            is_valid_titulo_eleitoral(generate_titulo_eleitoral())
        )
        self.assertIsNotNone(
            is_valid_titulo_eleitoral(generate_titulo_eleitoral(state="SP"))
        )
        self.assertIsNotNone(
            is_valid_titulo_eleitoral(generate_titulo_eleitoral(state="AC"))
        )

        # Validate if the UFs digits are correct

        self.assertEqual(generate_titulo_eleitoral(state="SP")[8:10], "01")

        self.assertEqual(generate_titulo_eleitoral(state="MG")[8:10], "02")

        self.assertEqual(generate_titulo_eleitoral()[8:10], "28")

        # Validate digits

        self.assertNotEqual(_calculate_dv1(_get_titulo_eleitoral_parts(
            generate_titulo_eleitoral(state="MG"))[0]), "0")
        
        self.assertNotEqual(_calculate_dv1(_get_titulo_eleitoral_parts(
            generate_titulo_eleitoral(state="SP"))[0]), "0")
        
        self.assertNotEqual(_calculate_dv1(_get_titulo_eleitoral_parts(
            generate_titulo_eleitoral(state="AC"))[0]), "10")   
        
        self.assertNotEqual(_calculate_dv1(_get_titulo_eleitoral_parts(
            generate_titulo_eleitoral())[0]), "10")
        
        actual = generate_titulo_eleitoral(state='sp')
        dv1 = _calculate_dv1(_get_titulo_eleitoral_parts(actual)[0])
        dig = _get_titulo_eleitoral_parts(actual)[2]
          
        self.assertTrue(_verify_dv1(dv1, "01", dig)[0])
        self.assertTrue(_verify_dv2("01", _verify_dv1(dv1, "01", dig)[1], dig))
        
        actual = generate_titulo_eleitoral(state='mg')
        dv1 = _calculate_dv1(_get_titulo_eleitoral_parts(actual)[0])
        dig = _get_titulo_eleitoral_parts(actual)[2]
          
        self.assertTrue(_verify_dv1(dv1, "02", dig)[0])
        self.assertTrue(_verify_dv2("02", _verify_dv1(dv1, "02", dig)[1], dig))

        actual = generate_titulo_eleitoral()
        dv1 = _calculate_dv1(_get_titulo_eleitoral_parts(actual)[0])
        dig = _get_titulo_eleitoral_parts(actual)[2]
          
        self.assertTrue(_verify_dv1(dv1, "28", dig)[0])
        self.assertTrue(_verify_dv2("28", _verify_dv1(dv1, "28", dig)[1], dig))
                
if __name__ == "__main__":
    unittest.main()
