import unittest

from brutils.legal_process import display, format_processo_juridico


class TestLegalProcess(unittest.TestCase):
    def test_display(self):
        self.assertEqual(
            display("23141945820055070079"), "2314194-58.2005.5.07.0079"
        )
        self.assertIsNone(display("00000000000"))
        self.assertIsNone(display("0000000000a"))
        self.assertIsNone(display("000000000000000000000000000000"))

    def test_format_processo_juridico(self):
        self.assertEqual(
            format_processo_juridico("23141945820055070079"),
            ("2314194-58.2005.5.07.0079"),
        )
        self.assertEqual(
            format_processo_juridico("00000000000000000000"),
            ("0000000-00.0000.0.00.0000"),
        )
        self.assertIsNone(format_processo_juridico("2314194582005507"))
        self.assertIsNone(format_processo_juridico("0000000000000000000000000"))


if __name__ == "__main__":
    unittest.main()
