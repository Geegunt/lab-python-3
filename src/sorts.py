class MultiSorter:
    '''
    Класс реализующий алгоритмы сортировки
    '''
    def bubble_sort(self, arr):
        if not arr:
            return arr
        n = len(arr)
        result = arr.copy()
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
            if not swapped:
                break

        return result

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr.copy()

        support = arr[len(arr) // 2]
        left = []
        middle = []
        right = []

        for x in arr:
            if x < support:
                left.append(x)
            elif x == support:
                middle.append(x)
            else:
                right.append(x)
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def radix_sort(self, arr):
        if not arr:
            return arr.copy()

        if any(x < 0 for x in arr):
            raise ValueError("Radix sort принимает только неотрицательные целые числа")

        result = arr.copy()
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

    def bucket_sort(self, arr):
        if not arr:
            return arr.copy()

        n = len(arr)
        if n <= 1:
            return arr.copy()

        bucket_count = max(1, n // 2)
        buckets = [[] for _ in range(bucket_count)]

        min_val = arr[0]
        max_val = arr[0]
        for num in arr:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num

        if min_val == max_val:
            return arr.copy()
        for num in arr:
            index = int((num - min_val) / (max_val - min_val) * (bucket_count - 1))
            buckets[index].append(num)

        for i in range(bucket_count):
            if buckets[i]:
                bucket = buckets[i]
                bucket_len = len(bucket)
                for j in range(bucket_len):
                    for k in range(0, bucket_len - j - 1):
                        if bucket[k] > bucket[k + 1]:
                            bucket[k], bucket[k + 1] = bucket[k + 1], bucket[k]

        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result