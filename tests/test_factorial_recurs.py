import pytest
from src.math_functions import factorial_recurs


class TestFactorialRecurs:
    def test_factorial_zero(self):
        assert factorial_recurs(0) == 1
    
    def test_factorial_one(self):
        assert factorial_recurs(1) == 1
    
    def test_factorial_two(self):
        assert factorial_recurs(2) == 2
    
    def test_factorial_three(self):
        assert factorial_recurs(3) == 6
    
    def test_factorial_four(self):
        assert factorial_recurs(4) == 24
    
    def test_factorial_five(self):
        assert factorial_recurs(5) == 120
    
    def test_factorial_six(self):
        assert factorial_recurs(6) == 720
    
    def test_factorial_ten(self):
        assert factorial_recurs(10) == 3628800
    
    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial_recurs(-1)
    
    def test_factorial_negative_large(self):
        with pytest.raises(ValueError):
            factorial_recurs(-5)
