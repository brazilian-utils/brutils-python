from brutils.legal_process import (
    remove_symbols,
)
from unittest import TestCase, main


class TestLegalProcess(TestCase):
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
