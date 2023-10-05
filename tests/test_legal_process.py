import unittest
from unittest.mock import patch

from brutils.legal_process import (
    sieve,
    display,
    format_processo_juridico,
    remove_symbols,
)


class TestLegalProcess(unittest.TestCase):
    def test_sieve(self):
        self.assertEqual(
            sieve("23141945820055070079"), ("23141945820055070079")
        )
        self.assertEqual(
            sieve("2314194-58.2005.5.07.0079"), ("23141945820055070079")
        )
        self.assertEqual(
            sieve("2314194--58..2005..5..07..0079"), ("23141945820055070079")
        )
        self.assertEqual(
            sieve("2314$$$-^|.2005.5.0%.***%"), ("2314$$$^|200550%***%")
        )
        self.assertEqual(
            sieve("2314$$$*^|(2005)5&0%#***%"), ("2314$$$*^|(2005)5&0%#***%")
        )
        self.assertEqual(sieve("...---..."), "")

    def test_remove_symbols(self):
        with patch("brutils.legal_process.sieve") as mock_sieve:
            remove_symbols("123.456.789-10")
            mock_sieve.assert_called()

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
