import pytest
from src.math_functions import fib_default


class TestFibDefault:
    def test_fib_zero(self):
        assert fib_default(0) == 1

    def test_fib_one(self):
        assert fib_default(1) == 1

    def test_fib_two(self):
        assert fib_default(2) == 1

    def test_fib_three(self):
        assert fib_default(3) == 2

    def test_fib_four(self):
        assert fib_default(4) == 3

    def test_fib_five(self):
        assert fib_default(5) == 5

    def test_fib_six(self):
        assert fib_default(6) == 8

    def test_fib_seven(self):
        assert fib_default(7) == 13

    def test_fib_ten(self):
        assert fib_default(10) == 55

    def test_fib_fifteen(self):
        assert fib_default(15) == 610

    def test_fib_twenty(self):
        assert fib_default(20) == 6765

    def test_fib_thirty(self):
        assert fib_default(30) == 832040
