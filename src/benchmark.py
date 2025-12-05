import time
from test_generators import rand_int_array, nearly_sorted, many_duplicates
from src.sorts import MultiSorter

def timeit_once(func, *args, **kwargs) -> float:
    '''
    Замеряет время выполнения функции один раз
    :param func:
    :param args:
    :param kwargs:
    :return:
    '''
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time


def benchmark_sorts(arrays:  dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]:
    '''
    Бенчмарк сортировок на разных массивах
    :param arrays:
    :param algos:
    :return:
    '''
    results = {}

    for array_name, array in arrays.items():
        results[array_name] = {}

        for algo_name, algo_func in algos.items():
            arr_copy = array.copy()
            exec_time = timeit_once(algo_func, arr_copy)
            results[array_name][algo_name] = exec_time

    return results

def print_benchmark_results(results: dict[str, dict[str, float]]):
    '''
    Красиво выводит результаты бенчмарка
    :param results:
    :return:
    '''
    print("результаты бенчмарка")

    for array_name, timings in results.items():
        print(f"\n {array_name}:")
        sorted_timings = sorted(timings.items(), key=lambda x: x[1])
        for algo_name, exec_time in sorted_timings:
            print(f" {algo_name:20s}: {exec_time*1000:8.4f} мс")


if __name__ == "__main__":
    def python_sort(arr):
        arr.sort()
        return arr

    def multisorter_bubble(arr):
        sorter = MultiSorter(arr)
        return sorter.bubble_sort()

    def multisorter_quick(arr):
        sorter = MultiSorter(arr)
        return sorter.quick_sort()

    def multisorter_radix(arr):
        sorter = MultiSorter(arr)
        return sorter.radix_sort()

    def multisorter_bucket(arr):
        sorter = MultiSorter(arr)
        return sorter.bucket_sort()

    def multisorter_count(arr):
        sorter = MultiSorter(arr)
        return sorter.count_sort()

    test_arrays = {
        "Случайный (1000)": rand_int_array(1000, 1, 1000),
        "Почти отсортированный (1000)": nearly_sorted(1000, 10),
        "Много дубликатов (1000)": many_duplicates(1000, unique_values_count=10),
    }

    algorithms = {
        "Python Sort": python_sort,
        "MultiSorter Bubble": multisorter_bubble,
        "MultiSorter Quick": multisorter_quick,
        "MultiSorter Radix": multisorter_radix,
        "MultiSorter Bucket": multisorter_bucket,
        "MultiSorter Count": multisorter_count,
    }

    results = benchmark_sorts(test_arrays, algorithms)
    print_benchmark_results(results)