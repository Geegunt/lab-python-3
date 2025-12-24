class MultiSorter:
    """
    Класс реализующий алгоритмы сортировки
    """

    def __init__(self, arr, key=None, reverse=False):
        self.arr = arr
        self.key = key
        self.reverse = reverse

    def _compare(self, a, b):
        if self.key:
            a_key = self.key(a)
            b_key = self.key(b)
        else:
            a_key = a
            b_key = b

        if self.reverse:
            return a_key < b_key
        return a_key > b_key

    def bubble_sort(self):
        if not self.arr:
            return self.arr
        n = len(self.arr)
        result = self.arr.copy()
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self._compare(result[j], result[j + 1]):
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
            if not swapped:
                break

        return result

    def quick_sort(self, arr=None):
        if arr is None:
            arr = self.arr

        if len(arr) <= 1:
            return arr.copy()

        support = arr[len(arr) // 2]
        left = []
        middle = []
        right = []

        for x in arr:
            if self._compare(x, support):
                right.append(x)
            elif self._compare(support, x):
                left.append(x)
            else:
                middle.append(x)

        return self.quick_sort(left) + middle + self.quick_sort(right)

    def radix_sort(self):
        if not self.arr:
            return self.arr.copy()

        if self.key:
            raise ValueError(
                "Radix sort не поддерживает произвольные ключи, только неотрицательные целые числа"
            )

        if any(x < 0 for x in self.arr):
            raise ValueError("Radix sort принимает только неотрицательные целые числа")

        result = self.arr.copy()
        max_num = max(result)
        exp = 1
        while max_num // exp > 0:
            buckets = [[] for _ in range(10)]

            for num in result:
                digit = (num // exp) % 10
                buckets[digit].append(num)

            result = []
            for bucket in buckets:
                result.extend(bucket)

            exp *= 10

        return result

    def bucket_sort(self):
        if not self.arr:
            return self.arr.copy()

        n = len(self.arr)
        if n <= 1:
            return self.arr.copy()

        bucket_count = max(1, n // 2)
        buckets = [[] for _ in range(bucket_count)]

        min_val = self.key(self.arr[0]) if self.key else self.arr[0]
        max_val = self.key(self.arr[0]) if self.key else self.arr[0]
        for num in self.arr:
            num_key = self.key(num) if self.key else num
            if num_key > max_val:
                max_val = num_key
            if num_key < min_val:
                min_val = num_key

        if min_val == max_val:
            return self.arr.copy()
        for num in self.arr:
            num_key = self.key(num) if self.key else num
            index = int((num_key - min_val) / (max_val - min_val) * (bucket_count - 1))
            buckets[index].append(num)

        for i in range(bucket_count):
            if buckets[i]:
                bucket = buckets[i]
                bucket_len = len(bucket)
                for j in range(bucket_len):
                    for k in range(0, bucket_len - j - 1):
                        if self._compare(bucket[k], bucket[k + 1]):
                            bucket[k], bucket[k + 1] = bucket[k + 1], bucket[k]

        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result

    def count_sort(self):
        if not self.arr:
            return self.arr.copy()

        if self.key:
            raise ValueError(
                "Count sort не поддерживает произвольные ключи, только неотрицательные целые числа"
            )

        if any(x < 0 for x in self.arr):
            raise ValueError(
                "Сортировка подсчетом принимает только неотрицательные целые числа"
            )
        max_val = max(self.arr)
        count = [0] * (max_val + 1)
        for num in self.arr:
            count[num] += 1
        result = []
        for value in range(len(count)):
            result.extend([value] * count[value])
        return result

    def heap_sort(self):
        if not self.arr:
            return self.arr.copy()

        result = self.arr.copy()
        n = len(result)

        def get_key(item):
            if hasattr(self, 'keys') and self.keys:
                return self.keys[0](item) if self.keys[0] else item
            return self.key(item) if self.key else item

        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n:
                left_key = get_key(arr[left])
                largest_key = get_key(arr[largest])
                if (not self.reverse and left_key > largest_key) or (self.reverse and left_key < largest_key):
                    largest = left

            if right < n:
                right_key = get_key(arr[right])
                largest_key = get_key(arr[largest])
                if (not self.reverse and right_key > largest_key) or (self.reverse and right_key < largest_key):
                    largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(result, n, i)

        for i in range(n - 1, 0, -1):
            result[0], result[i] = result[i], result[0]
            heapify(result, i, 0)

        return result


class EnhancedMultiSorter(MultiSorter):
    def __init__(self, arr, key=None, reverse=False, comparator=None, keys=None):
        super().__init__(arr, key=key, reverse=reverse)
        self.comparator = comparator
        if keys:
            self.keys = keys if isinstance(keys, list) else [keys]
        else:
            self.keys = []

    def _compare(self, a, b):
        if self.comparator:
            result = self.comparator(a, b)
            return not result if self.reverse else result

        if self.keys:
            for key in self.keys:
                a_key = key(a) if key else a
                b_key = key(b) if key else b
                if a_key < b_key:
                    return True if self.reverse else False
                elif a_key > b_key:
                    return False if self.reverse else True
            return False

        return super()._compare(a, b)
