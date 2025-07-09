import unittest

from brutils.tin import validate_tin_angola


class TestTinAngola(unittest.TestCase):
    def calculate_dv(self, base: str) -> str:
        weights = [9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(d) * w for d, w in zip(base, weights))
        resto = soma % 11
        dv = 0 if resto in (0, 1) else 11 - resto
        return str(dv)

    def test_valid_tins(self):
        # pegamos sequências iniciais quaisquer com primeiro dígito válido
        bases = ["12345678", "58641234"]
        for base in bases:
            tin = base + self.calculate_dv(base)
            with self.subTest(tin=tin):
                self.assertTrue(
                    validate_tin_angola(tin), f"{tin} deveria ser válido"
                )

    def test_invalid_tins(self):
        invalid = [
            "023456789",  # primeiro dígito inválido
            "123456780",  # DV incorreto (mesmo base do primeiro teste, mas forçamos 0)
            "12345678",  # muito curto
            "abcdefgh9",  # não numérico
        ]
        for tin in invalid:
            with self.subTest(tin=tin):
                self.assertFalse(
                    validate_tin_angola(tin), f"{tin} deveria ser inválido"
                )


if __name__ == "__main__":
    unittest.main()
