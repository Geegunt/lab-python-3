import pytest
from src.sorts import MultiSorter, EnhancedMultiSorter


class TestHeapSort:
    def test_basic(self):
        sorter = MultiSorter([3, 1, 2, 7, 9])
        assert sorter.heap_sort() == [1, 2, 3, 7, 9]

    def test_empty(self):
        sorter = MultiSorter([])
        assert sorter.heap_sort() == []

    def test_single(self):
        sorter = MultiSorter([5])
        assert sorter.heap_sort() == [5]

    def test_duplicates(self):
        sorter = MultiSorter([3, 1, 2, 1, 3])
        assert sorter.heap_sort() == [1, 1, 2, 3, 3]

    def test_with_key(self):
        data = [{'val': 3}, {'val': 1}, {'val': 2}]
        sorter = MultiSorter(data, key=lambda x: x['val'])
        result = sorter.heap_sort()
        assert [item['val'] for item in result] == [1, 2, 3]

    def test_already_sorted(self):
        sorter = MultiSorter([1, 2, 3, 4, 5])
        assert sorter.heap_sort() == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        sorter = MultiSorter([5, 4, 3, 2, 1])
        assert sorter.heap_sort() == [1, 2, 3, 4, 5]

    def test_all_same(self):
        sorter = MultiSorter([5, 5, 5, 5])
        assert sorter.heap_sort() == [5, 5, 5, 5]

    def test_reverse_order(self):
        sorter = MultiSorter([3, 1, 2, 7, 9], reverse=True)
        assert sorter.heap_sort() == [9, 7, 3, 2, 1]


class TestHeapSortEnhanced:
    def test_with_keys(self):
        data = [{'val': 3}, {'val': 1}, {'val': 2}]
        sorter = EnhancedMultiSorter(data, keys=[lambda x: x['val']])
        result = sorter.heap_sort()
        assert [item['val'] for item in result] == [1, 2, 3]
