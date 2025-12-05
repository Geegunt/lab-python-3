import pytest
from src.sorts import MultiSorter


class TestBucketSort:
    def test_basic_floats(self):
        sorter = MultiSorter([0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51])
        result = sorter.bucket_sort()
        assert result == sorted([0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51])
    
    def test_integers(self):
        sorter = MultiSorter([3, 1, 2, 7, 9])
        assert sorter.bucket_sort() == [1, 2, 3, 7, 9]
    
    def test_empty(self):
        sorter = MultiSorter([])
        assert sorter.bucket_sort() == []
    
    def test_single(self):
        sorter = MultiSorter([5])
        assert sorter.bucket_sort() == [5]
    
    def test_with_key(self):
        data = [{'val': 3}, {'val': 1}, {'val': 2}]
        sorter = MultiSorter(data, key=lambda x: x['val'])
        result = sorter.bucket_sort()
        assert [item['val'] for item in result] == [1, 2, 3]
    
    def test_duplicates(self):
        sorter = MultiSorter([3, 1, 2, 1, 3])
        assert sorter.bucket_sort() == [1, 1, 2, 3, 3]
    
    def test_already_sorted(self):
        sorter = MultiSorter([1, 2, 3, 4, 5])
        assert sorter.bucket_sort() == [1, 2, 3, 4, 5]
    
    def test_reverse_sorted(self):
        sorter = MultiSorter([5, 4, 3, 2, 1])
        assert sorter.bucket_sort() == [1, 2, 3, 4, 5]
    
    def test_all_same(self):
        sorter = MultiSorter([5, 5, 5, 5])
        assert sorter.bucket_sort() == [5, 5, 5, 5]
