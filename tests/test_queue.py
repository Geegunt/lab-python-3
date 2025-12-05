import pytest
from src.structure_data import Queue


class TestQueue:
    def test_enquene_and_dequene(self):
        queue = Queue(5)
        queue.enquene(1)
        queue.enquene(2)
        queue.enquene(3)
        assert queue.dequene() == 1
        assert queue.dequene() == 2
        assert queue.dequene() == 3

    def test_is_empty(self):
        queue = Queue(5)
        assert queue.is_empty() is True
        queue.enquene(1)
        assert queue.is_empty() is False

    def test_peek(self):
        queue = Queue(5)
        queue.enquene(1)
        queue.enquene(2)
        assert queue.peek() == 1

    def test_overflow(self):
        queue = Queue(2)
        queue.enquene(1)
        queue.enquene(2)
        with pytest.raises(OverflowError):
            queue.enquene(3)

    def test_underflow(self):
        queue = Queue(5)
        with pytest.raises(IndexError):
            queue.dequene()
