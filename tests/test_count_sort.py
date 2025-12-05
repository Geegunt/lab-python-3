import pytest
from src.sorts import MultiSorter


class TestCountSort:
    def test_basic(self):
        sorter = MultiSorter([4, 2, 2, 8, 3, 3, 1])
        assert sorter.count_sort() == [1, 2, 2, 3, 3, 4, 8]
    
    def test_empty(self):
        sorter = MultiSorter([])
        assert sorter.count_sort() == []
    
    def test_single(self):
        sorter = MultiSorter([5])
        assert sorter.count_sort() == [5]
    
    def test_with_key_raises(self):
        sorter = MultiSorter([1, 2, 3], key=lambda x: x)
        with pytest.raises(ValueError):
            sorter.count_sort()
    
    def test_negative_raises(self):
        sorter = MultiSorter([1, -2, 3])
        with pytest.raises(ValueError):
            sorter.count_sort()
    
    def test_all_zeros(self):
        sorter = MultiSorter([0, 0, 0])
        assert sorter.count_sort() == [0, 0, 0]
    
    def test_duplicates(self):
        sorter = MultiSorter([5, 2, 5, 1, 2])
        assert sorter.count_sort() == [1, 2, 2, 5, 5]
    
    def test_already_sorted(self):
        sorter = MultiSorter([1, 2, 3, 4, 5])
        assert sorter.count_sort() == [1, 2, 3, 4, 5]
    
    def test_reverse_sorted(self):
        sorter = MultiSorter([5, 4, 3, 2, 1])
        assert sorter.count_sort() == [1, 2, 3, 4, 5]
