import pytest
from src.math_functions import factorial_default


class TestFactorialDefault:
    def test_factorial_zero(self):
        assert factorial_default(0) == 1

    def test_factorial_one(self):
        assert factorial_default(1) == 1

    def test_factorial_two(self):
        assert factorial_default(2) == 2

    def test_factorial_three(self):
        assert factorial_default(3) == 6

    def test_factorial_four(self):
        assert factorial_default(4) == 24

    def test_factorial_five(self):
        assert factorial_default(5) == 120

    def test_factorial_six(self):
        assert factorial_default(6) == 720

    def test_factorial_ten(self):
        assert factorial_default(10) == 3628800

    def test_factorial_twenty(self):
        assert factorial_default(20) == 2432902008176640000

    def test_factorial_large(self):
        result = factorial_default(15)
        assert result == 1307674368000
