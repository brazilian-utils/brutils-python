import unittest

from datetime import datetime
from brutils.legal_process import (
    format_processo_juridico,
    remove_symbols,
    generate_processo_juridico,
    _checksum as checksum,
)


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

    def test_generate_processo_juridico(self):
        self.assertEqual(
            generate_processo_juridico()[9:13], str(datetime.now().year)
        )
        self.assertEqual(generate_processo_juridico(ano=3000)[9:13], "3000")
        self.assertEqual(generate_processo_juridico(orgao=4)[13:14], "4")
        self.assertEqual(
            generate_processo_juridico(ano=3000, orgao=4)[13:14], "4"
        )
        self.assertEqual(
            generate_processo_juridico(ano=3000, orgao=4)[9:13], "3000"
        )

    def test_check_sum(self):
        self.assertEqual(checksum(546611720238150014), "77")
        self.assertEqual(checksum(403818720238230498), "50")


if __name__ == "__main__":
    unittest.main()
