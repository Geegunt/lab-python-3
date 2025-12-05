import pytest
from src.math_functions import fib_recurs


class TestFibRecurs:
    def test_fib_zero(self):
        assert fib_recurs(0) == 0

    def test_fib_one(self):
        assert fib_recurs(1) == 1

    def test_fib_two(self):
        assert fib_recurs(2) == 1

    def test_fib_three(self):
        assert fib_recurs(3) == 2

    def test_fib_four(self):
        assert fib_recurs(4) == 3

    def test_fib_five(self):
        assert fib_recurs(5) == 5

    def test_fib_six(self):
        assert fib_recurs(6) == 8

    def test_fib_seven(self):
        assert fib_recurs(7) == 13

    def test_fib_ten(self):
        assert fib_recurs(10) == 55

    def test_fib_sequence(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected_val in enumerate(expected):
            assert fib_recurs(i) == expected_val

    def test_fib_negative(self):
        with pytest.raises(ValueError):
            fib_recurs(-1)

    def test_fib_negative_large(self):
        with pytest.raises(ValueError):
            fib_recurs(-5)
