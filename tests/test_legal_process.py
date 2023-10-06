import unittest

from brutils.legal_process import format_processo_juridico, remove_symbols


class TestLegalProcess(unittest.TestCase):
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

    def test_remove_symbols(self):
        self.assertEqual(
            remove_symbols("6439067-89.2023.4.04.5902"), "64390678920234045902"
        )
        self.assertEqual(
            remove_symbols("4976023-82.2012.7.00.2263"), "49760238220127002263"
        )
        self.assertEqual(
            remove_symbols("4976...-02382-.-2012.-7002--263"),
            "49760238220127002263",
        )
        self.assertEqual(
            remove_symbols("4976023-82.2012.7.00.2263*!*&#"),
            "49760238220127002263*!*&#",
        )
        self.assertEqual(
            remove_symbols("4976..#.-0@2382-.#-2012.#-7002--263@"),
            "4976#0@2382#2012#7002263@",
        )
        self.assertEqual(remove_symbols("@...---...#"), "@#")
        self.assertEqual(remove_symbols("...---..."), "")


if __name__ == "__main__":
    unittest.main()
