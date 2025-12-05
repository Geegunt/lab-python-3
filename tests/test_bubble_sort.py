import pytest
from src.sorts import MultiSorter, EnhancedMultiSorter


class TestBubbleSort:
    def test_basic(self):
        sorter = MultiSorter([3, 1, 2, 7, 9])
        assert sorter.bubble_sort() == [1, 2, 3, 7, 9]

    def test_empty(self):
        sorter = MultiSorter([])
        assert sorter.bubble_sort() == []

    def test_single(self):
        sorter = MultiSorter([5])
        assert sorter.bubble_sort() == [5]

    def test_reverse(self):
        sorter = MultiSorter([3, 1, 2, 7, 9], reverse=True)
        assert sorter.bubble_sort() == [9, 7, 3, 2, 1]

    def test_with_key(self):
        data = [{'val': 3}, {'val': 1}, {'val': 2}]
        sorter = MultiSorter(data, key=lambda x: x['val'])
        result = sorter.bubble_sort()
        assert [item['val'] for item in result] == [1, 2, 3]

    def test_duplicates(self):
        sorter = MultiSorter([3, 1, 2, 1, 3])
        assert sorter.bubble_sort() == [1, 1, 2, 3, 3]

    def test_already_sorted(self):
        sorter = MultiSorter([1, 2, 3, 4, 5])
        assert sorter.bubble_sort() == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        sorter = MultiSorter([5, 4, 3, 2, 1])
        assert sorter.bubble_sort() == [1, 2, 3, 4, 5]


class TestBubbleSortEnhanced:
    def test_with_multiple_keys(self):
        data = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 20},
            {'name': 'Charlie', 'age': 25}
        ]
        sorter = EnhancedMultiSorter(data, keys=[lambda x: x['age'], lambda x: x['name']])
        result = sorter.bubble_sort()
        assert result[0]['name'] == 'Bob'
        assert result[1]['name'] == 'Alice'
        assert result[2]['name'] == 'Charlie'

    def test_with_comparator(self):
        data = ['a', 'bbb', 'cc']
        sorter = EnhancedMultiSorter(data, comparator=lambda a, b: len(a) > len(b))
        result = sorter.bubble_sort()
        assert result == ['a', 'cc', 'bbb']
