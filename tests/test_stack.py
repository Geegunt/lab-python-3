import pytest
from src.structure_data import Stack


class TestStack:
    def test_push_and_pop(self):
        stack = Stack(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_is_empty(self):
        stack = Stack(5)
        assert stack.is_empty() is True
        stack.push(1)
        assert stack.is_empty() is False

    def test_peek(self):
        stack = Stack(5)
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2

    def test_overflow(self):
        stack = Stack(2)
        stack.push(1)
        stack.push(2)
        with pytest.raises(OverflowError):
            stack.push(3)

    def test_underflow(self):
        stack = Stack(5)
        with pytest.raises(IndexError):
            stack.pop()
