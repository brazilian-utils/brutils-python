from unittest import TestCase, main
from unittest.mock import patch

from brutils.cnpj import (
    _checksum,
    _checksum_alphanumeric,
    _hashdigit,
    _hashdigit_alphanumeric,
    ascii_value,
    display,
    format_cnpj,
    generate,
    is_valid,
    is_alphanumeric_cnpj,
    remove_symbols,
    sieve,
    validate,
)


class TestCNPJ(TestCase):
    # -------------------------------------------------------------------------
    # LEGACY TESTS (numeric CNPJ)
    # -------------------------------------------------------------------------

    def test_sieve(self):
        self.assertEqual(sieve("00000000000"), "00000000000")
        self.assertEqual(sieve("12.345.678/0001-90"), "12345678000190")
        self.assertEqual(sieve("134..2435/.-1892.-"), "13424351892")
        self.assertEqual(sieve("abc1230916*!*&#"), "abc1230916*!*&#")
        self.assertEqual(
            sieve("ab.c1.--.2-3/09.-1-./6/-.*.-!*&#"), "abc1230916*!*&#"
        )
        self.assertEqual(sieve("/...---.../"), "")

    def test_display_numeric_valid(self):
        # Traditional numeric CNPJ
        self.assertEqual(display("12345678000195"), "12.345.678/0001-95")

    def test_display_alphanumeric_valid(self):
        # Alphanumeric CNPJ (valid from 2026)
        formatted = display("12ABC34501DE35")
        self.assertEqual(formatted, "12.ABC.345/01DE-35")

    def test_display_invalid_cases(self):
        # Too short
        self.assertIsNone(display("1234567890123"))
        # All same character
        self.assertIsNone(display("AAAAAAAAAAAAAA"))
        # Empty string
        self.assertIsNone(display(""))

    def test_format_cnpj_numeric_valid(self):
        # Numeric CNPJ should format properly
        self.assertEqual(format_cnpj("03560714000142"), "03.560.714/0001-42")

    def test_format_cnpj_alphanumeric_valid(self):
        # Alphanumeric CNPJ with computed DV
        base = "12ABC34501DE"
        dv = _checksum_alphanumeric(base)
        valid_cnpj = base + dv
        formatted = format_cnpj(valid_cnpj)
        self.assertEqual(formatted, "12.ABC.345/01DE-" + dv)

    def test_format_cnpj_invalid_returns_none(self):
        # Invalid numeric
        self.assertIsNone(format_cnpj("12345678000100"))
        # Invalid alphanumeric (wrong DV)
        self.assertIsNone(format_cnpj("12ABC34501DE99"))


    def test_validate(self):
        self.assertIs(validate("34665388000161"), True)
        self.assertIs(validate("52599927000100"), False)
        self.assertIs(validate("00000000000"), False)

    def test_is_valid(self):
        # When CNPJ is not string, returns False
        self.assertIs(is_valid(1), False)

        # When CNPJ's len is different of 14, returns False
        self.assertIs(is_valid("1"), False)

        # When CNPJ does not contain only digits, returns False
        self.assertIs(is_valid("1112223334445-"), False)

        # When CNPJ has only the same digit, returns false
        self.assertIs(is_valid("11111111111111"), False)

        # When rest_1 is lt 2 and the 13th digit is not 0, returns False
        self.assertIs(is_valid("1111111111315"), False)

        # When rest_1 is gte 2 and the 13th digit is not (11 - rest), returns
        # False
        self.assertIs(is_valid("1111111111115"), False)

        # When rest_2 is lt 2 and the 14th digit is not 0, returns False
        self.assertIs(is_valid("11111111121205"), False)

        # When rest_2 is gte 2 and the 14th digit is not (11 - rest), returns
        # False
        self.assertIs(is_valid("11111111113105"), False)

        # When CNPJ is valid
        self.assertIs(is_valid("34665388000161"), True)
        self.assertIs(is_valid("01838723000127"), True)

    def test_generate(self):
        for _ in range(1000):
            cnpj = generate()
            self.assertTrue(validate(cnpj))
            self.assertIsNotNone(display(cnpj))

    def test__hashdigit(self):
        self.assertEqual(_hashdigit("00000000000000", 13), 0)
        self.assertEqual(_hashdigit("00000000000000", 14), 0)
        self.assertEqual(_hashdigit("52513127000292", 13), 9)
        self.assertEqual(_hashdigit("52513127000292", 14), 9)

    def test__checksum(self):
        self.assertEqual(_checksum("00000000000000"), "00")
        self.assertEqual(_checksum("52513127000299"), "99")

    # -------------------------------------------------------------------------
    # NEW TESTS (alphanumeric CNPJ - 2026 format)
    # -------------------------------------------------------------------------

    def test_is_alphanumeric_cnpj(self):
        self.assertTrue(is_alphanumeric_cnpj("12AB345C0001D5"))
        self.assertFalse(is_alphanumeric_cnpj("12345678000195"))

    def test_ascii_value_conversion(self):
        # Digits: ASCII(0–9) → 48–57 → minus 48 → 0–9
        self.assertEqual(ascii_value("0"), 0)
        self.assertEqual(ascii_value("9"), 9)
        # Letters: ASCII(A) = 65 → minus 48 → 17
        self.assertEqual(ascii_value("A"), 17)
        self.assertEqual(ascii_value("Z"), 42)
        self.assertEqual(ascii_value("b"), 18)  # lowercase also works

    def test_hashdigit_alphanumeric(self):
        # Simple test to ensure deterministic checksum generation
        result = _hashdigit_alphanumeric("12ABC34501DE", 13)
        self.assertIsInstance(result, int)
        self.assertTrue(0 <= result <= 9)

    def test_checksum_alphanumeric(self):
        # Ensure it returns exactly 2 digits as string
        base = "12ABC34501DE"
        dv = _checksum_alphanumeric(base)
        self.assertEqual(len(dv), 2)
        self.assertTrue(dv.isdigit())

    def test_validate_cnpj_alphanumeric(self):
        base = "12ABC34501DE"
        dv = _checksum_alphanumeric(base)
        valid_cnpj = base + dv

        # Should be valid
        self.assertTrue(validate(valid_cnpj))
        self.assertTrue(is_valid(valid_cnpj))

        # Invalid if DV altered
        invalid_cnpj = valid_cnpj[:-1] + "9"
        self.assertFalse(validate(invalid_cnpj))

    def test_generate_alphanumeric(self):
        # Generates and validates 100 random new-format CNPJs
        for _ in range(200):
            cnpj = generate(new_format=True)
            self.assertEqual(len(cnpj), 14)
            self.assertTrue(any(c.isalpha() for c in cnpj[:12]))
            self.assertTrue(cnpj[-2:].isdigit())
            self.assertTrue(is_valid(cnpj))

    def test_generate_branch_numeric_still_valid(self):
        # Backward compatible
        cnpj = generate(branch=9999)
        self.assertTrue(is_valid(cnpj))
        self.assertFalse(any(c.isalpha() for c in cnpj))


@patch("brutils.cnpj.sieve")
class TestRemoveSymbols(TestCase):
    def test_remove_symbols(self, mock_sieve):
        # When call remove_symbols, it calls sieve
        remove_symbols("12.345.678/0001-90")
        mock_sieve.assert_called()


@patch("brutils.cnpj.is_valid")
class TestIsValidToFormat(TestCase):
    def test_when_cnpj_is_valid_returns_true_to_format(self, mock_is_valid):
        mock_is_valid.return_value = True

        # When cnpj is_valid, returns formatted cnpj
        self.assertEqual(format_cnpj("01838723000127"), "01.838.723/0001-27")

        # Checks if function is_valid_cnpj is called
        mock_is_valid.assert_called_once_with("01838723000127")

    def test_when_cnpj_is_not_valid_returns_none(self, mock_is_valid):
        mock_is_valid.return_value = False

        # When cnpj isn't valid, returns None
        self.assertIsNone(format_cnpj("01838723000127"))


if __name__ == "__main__":
    main()
