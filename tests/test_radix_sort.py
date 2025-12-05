import pytest
from src.sorts import MultiSorter


class TestRadixSort:
    def test_basic(self):
        sorter = MultiSorter([170, 45, 75, 90, 802, 24, 2, 66])
        assert sorter.radix_sort() == [2, 24, 45, 66, 75, 90, 170, 802]
    
    def test_empty(self):
        sorter = MultiSorter([])
        assert sorter.radix_sort() == []
    
    def test_single(self):
        sorter = MultiSorter([42])
        assert sorter.radix_sort() == [42]
    
    def test_with_key_raises(self):
        sorter = MultiSorter([1, 2, 3], key=lambda x: x)
        with pytest.raises(ValueError):
            sorter.radix_sort()
    
    def test_negative_raises(self):
        sorter = MultiSorter([1, -2, 3])
        with pytest.raises(ValueError):
            sorter.radix_sort()
    
    def test_all_zeros(self):
        sorter = MultiSorter([0, 0, 0])
        assert sorter.radix_sort() == [0, 0, 0]
    
    def test_large_numbers(self):
        sorter = MultiSorter([1000, 1, 100, 10])
        assert sorter.radix_sort() == [1, 10, 100, 1000]
    
    def test_duplicates(self):
        sorter = MultiSorter([5, 2, 5, 1, 2])
        assert sorter.radix_sort() == [1, 2, 2, 5, 5]
