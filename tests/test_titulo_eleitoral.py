from brutils.titulo_eleitoral import generate_titulo_eleitoral
from unittest import TestCase, main
from unittest.mock import patch


class TestTituloEleitoral(TestCase):
    def test_generate(self):
        self.assertIsNotNone((generate_titulo_eleitoral()))
        self.assertIsNotNone((generate_titulo_eleitoral(state="SP")))
        self.assertIsNotNone((generate_titulo_eleitoral(state="AC")))


if __name__ == "__main__":
    main()
