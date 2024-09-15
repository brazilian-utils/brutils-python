from unittest import TestCase, main

from brutils.ibge.municipality import get_municipality_by_code


class TestIBGE(TestCase):
    def test_get_municipality_by_code(self):
        self.assertEqual(
            get_municipality_by_code("3550308"), ("São Paulo", "SP")
        )
        self.assertEqual(
            get_municipality_by_code("3304557"), ("Rio de Janeiro", "RJ")
        )
        self.assertEqual(get_municipality_by_code("5208707"), ("Goiânia", "GO"))
        self.assertIsNone(get_municipality_by_code("1234567"))


if __name__ == "__main__":
    main()
