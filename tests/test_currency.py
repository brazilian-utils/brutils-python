from decimal import Decimal
from unittest import TestCase

from brutils.currency import format_currency


class TestFormatCurrency(TestCase):
    def test_when_value_is_a_decimal_value(self):
        assert format_currency(Decimal("123236.70")) == "R$ 123.236,70"

    def test_when_value_is_a_float_value(self):
        assert format_currency(123236.70) == "R$ 123.236,70"

    def test_when_value_is_negative(self):
        assert format_currency(-123236.70) == "R$ -123.236,70"

    def test_when_value_is_zero(self):
        print(format_currency(0))
        assert format_currency(0) == "R$ 0,00"

    def test_value_decimal_replace_rounding(self):
        assert format_currency(-123236.7676) == "R$ -123.236,77"

    def test_when_value_is_not_a_valid_currency(self):
        assert format_currency("not a number") is None
        assert format_currency("09809,87") is None
        assert format_currency("897L") is None
