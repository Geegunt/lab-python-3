import sys
import time

from src.benchmark import benchmark_sorts, print_benchmark_results, timeit_once
from src.math_functions import (factorial_default, factorial_recurs,
                                fib_default, fib_recurs)
from src.sorts import MultiSorter
from src.structure_data import Queue, Stack
from src.test_generators import (many_duplicates, nearly_sorted,
                                 rand_int_array, reverse_sorted)


class SortingCLI:
    def __init__(self):
        self.test_size = 1000
        self.stack = None
        self.queue = None
        self.running = True

    def benchmark_sort(self, algo_name, algo_func):
        print(f"\n{algo_name}")

        tests = {
            "Случайный": rand_int_array(self.test_size, 1, 1000),
            "Почти отсортированный": nearly_sorted(
                self.test_size, self.test_size // 100
            ),
            "Много дубликатов": many_duplicates(self.test_size, 10),
            "Обратный порядок": reverse_sorted(self.test_size),
        }

        total = 0
        for name, arr in tests.items():
            elapsed = timeit_once(algo_func, arr.copy()) * 1000
            print(f"{name:<25} {elapsed:>8.2f} мс")
            total += elapsed

        print(f"{'Итого:':<25} {total:>8.2f} мс\n")

    def sort_bubble(self, *args):
        self.benchmark_sort("Bubble Sort", lambda arr: MultiSorter(arr).bubble_sort())

    def sort_quick(self, *args):
        self.benchmark_sort("Quick Sort", lambda arr: MultiSorter(arr).quick_sort())

    def sort_radix(self, *args):
        self.benchmark_sort("Radix Sort", lambda arr: MultiSorter(arr).radix_sort())

    def sort_bucket(self, *args):
        self.benchmark_sort("Bucket Sort", lambda arr: MultiSorter(arr).bucket_sort())

    def sort_count(self, *args):
        self.benchmark_sort("Count Sort", lambda arr: MultiSorter(arr).count_sort())

    def sort_heap(self, *args):
        self.benchmark_sort("Heap Sort", lambda arr: MultiSorter(arr).heap_sort())

    def sort_all(self, *args):
        print(f"\nСравнение всех алгоритмов (размер: {self.test_size})")

        arr = rand_int_array(self.test_size, 1, 1000)

        algos = {
            "Bubble Sort": lambda a: MultiSorter(a).bubble_sort(),
            "Quick Sort": lambda a: MultiSorter(a).quick_sort(),
            "Radix Sort": lambda a: MultiSorter(a).radix_sort(),
            "Bucket Sort": lambda a: MultiSorter(a).bucket_sort(),
            "Count Sort": lambda a: MultiSorter(a).count_sort(),
            "Heap Sort": lambda a: MultiSorter(a).heap_sort(),
            "Python Sort": lambda a: sorted(a),
        }

        results = []
        for name, func in algos.items():
            start = time.time()
            func(arr.copy())
            elapsed = (time.time() - start) * 1000
            results.append((name, elapsed))

        results.sort(key=lambda x: x[1])

        for i, (name, t) in enumerate(results, 1):
            print(f"{i}. {name:<20} {t:>8.2f} мс")
        print()

    def set_size(self, *args):
        if not args:
            print("Укажите размер: SetSize <N>\n")
            return
        try:
            self.test_size = int(args[0])
            print(f"Установлен размер: {self.test_size}\n")
        except:
            print("Некорректный ввод\n")

    def stack_create(self, *args):
        capacity = 100
        if args:
            try:
                capacity = int(args[0])
            except:
                pass
        self.stack = Stack(capacity)
        print(f"Стек создан: {capacity}\n")

    def stack_push(self, *args):
        if not self.stack:
            print("Создайте стек командой StackCreate\n")
            return
        if not args:
            print("Укажите значение: StackPush <val>\n")
            return
        try:
            value = int(args[0])
            self.stack.push(value)
            print(f"Добавлено: {value}, размер: {self.stack.size()}\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")

    def stack_pop(self, *args):
        if not self.stack:
            print("Создайте стек командой StackCreate\n")
            return
        try:
            value = self.stack.pop()
            print(f"Извлечено: {value}, размер: {self.stack.size()}\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")

    def stack_peek(self, *args):
        if not self.stack:
            print("Создайте стек командой StackCreate\n")
            return
        try:
            print(f"Верхний элемент: {self.stack.peek()}\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")

    def stack_show(self, *args):
        if not self.stack:
            print("Создайте стек командой StackCreate\n")
            return
        print(f"\nСтек ({self.stack.size()}/{self.stack.capacity}):")
        if self.stack.is_empty():
            print("  Пуст")
        else:
            for i in range(self.stack.top - 1, -1, -1):
                print(f"  {self.stack.data[i]}")
        print()

    def stack_test(self, *args):
        print("\nТест Stack:")
        for size in [100, 1000, 10000]:
            s = Stack(size)

            start = time.time()
            for i in range(size):
                s.push(i)
            push_time = (time.time() - start) * 1000

            start = time.time()
            for i in range(size):
                s.pop()
            pop_time = (time.time() - start) * 1000

            print(f"  {size} элементов: push {push_time:.2f} мс, pop {pop_time:.2f} мс")
        print()

    def queue_create(self, *args):
        capacity = 10
        if args:
            try:
                capacity = int(args[0])
            except:
                pass
        self.queue = Queue(capacity)
        print(f"Очередь создана: {capacity}\n")

    def queue_enqueue(self, *args):
        if not self.queue:
            print("Создайте очередь командой QueueCreate\n")
            return
        if not args:
            print("Укажите значение: QueueEnqueue <val>\n")
            return
        try:
            value = int(args[0])
            self.queue.enquene(value)
            print(f"Добавлено: {value}, размер: {self.queue.size()}\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")

    def queue_dequeue(self, *args):
        if not self.queue:
            print("Создайте очередь командой QueueCreate\n")
            return
        try:
            value = self.queue.dequene()
            print(f"Извлечено: {value}, размер: {self.queue.size()}\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")

    def queue_peek(self, *args):
        if not self.queue:
            print("Создайте очередь командой QueueCreate\n")
            return
        try:
            print(f"Первый элемент: {self.queue.peek()}\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")

    def queue_show(self, *args):
        if not self.queue:
            print("Создайте очередь командой QueueCreate\n")
            return
        print(f"\nОчередь ({self.queue.size()}/{self.queue.capacity}):")
        if self.queue.is_empty():
            print("  Пуста")
        else:
            current = self.queue.head
            for i in range(self.queue.size()):
                print(f"  {self.queue.data[current]}")
                current = (current + 1) % self.queue.capacity
        print()

    def queue_test(self, *args):
        print("\nТест Queue:")
        for size in [100, 1000, 10000]:
            q = Queue(size)

            start = time.time()
            for i in range(size):
                q.enquene(i)
            enq_time = (time.time() - start) * 1000

            start = time.time()
            for i in range(size):
                q.dequene()
            deq_time = (time.time() - start) * 1000

            print(
                f"  {size} элементов: enqueue {enq_time:.2f} мс, dequeue {deq_time:.2f} мс"
            )
        print()

    def math_factorial_recurs(self, *args):
        n = int(args[0])
        result = factorial_recurs(n)
        print(f"{n}! (рекурсивно) = {result}\n")

    def math_factorial_default(self, *args):
        n = int(args[0])
        result = factorial_default(n)
        print(f"{n}! (итеративно) = {result}\n")

    def math_fib_recurs(self, *args):
        n = int(args[0])
        result = fib_recurs(n)
        print(f"Fib({n}) (рекурсивно) = {result}\n")

    def math_fib_default(self, *args):
        n = int(args[0])
        result = fib_default(n)
        print(f"Fib({n}) (итеративно) = {result}\n")

    def run_benchmark(self, *args):
        print("\nЗапуск бенчмарков из benchmark.py\n")

        test_arrays = {
            "Случайный (1000)": rand_int_array(1000, 1, 1000),
            "Почти отсортированный (1000)": nearly_sorted(1000, 10),
            "Много дубликатов (1000)": many_duplicates(1000, 10),
        }

        algorithms = {
            "Python Sort": lambda arr: arr.sort(),
            "Bubble Sort": lambda arr: MultiSorter(arr).bubble_sort(),
            "Quick Sort": lambda arr: MultiSorter(arr).quick_sort(),
            "Radix Sort": lambda arr: MultiSorter(arr).radix_sort(),
            "Bucket Sort": lambda arr: MultiSorter(arr).bucket_sort(),
            "Count Sort": lambda arr: MultiSorter(arr).count_sort(),
            "Heap Sort": lambda arr: MultiSorter(arr).heap_sort(),
        }

        results = benchmark_sorts(test_arrays, algorithms)
        print_benchmark_results(results)
        print()

    def show_help(self, *args):
        print("\nКоманды:")
        print("SortBubble, SortQuick, SortRadix, SortBucket, SortCount, SortHeap")
        print("SortAll - сравнить все алгоритмы")
        print("SetSize <N> - установить размер массива")
        print(
            "StackCreate [N], StackPush <val>, StackPop, StackPeek, StackShow, StackTest"
        )
        print(
            "QueueCreate [N], QueueEnqueue <val>, QueueDequeue, QueuePeek, QueueShow, QueueTest"
        )
        print("FactorialRecurs <n>, FactorialDefault <n>")
        print("FibRecurs <n>, FibDefault <n>")
        print("Бенчмарки:")
        print("Benchmark - запустить бенчмарки из benchmark.py")
        print("Help, Exit")

    def run(self):
        print("CLI для алгоритмов и структур данных (ввод через stdin)")
        print("Введите Help для списка команд\n")

        commands = {
            "sortbubble": self.sort_bubble,
            "sortquick": self.sort_quick,
            "sortradix": self.sort_radix,
            "sortbucket": self.sort_bucket,
            "sortcount": self.sort_count,
            "sortheap": self.sort_heap,
            "sortall": self.sort_all,
            "setsize": self.set_size,
            "stackcreate": self.stack_create,
            "stackpush": self.stack_push,
            "stackpop": self.stack_pop,
            "stackpeek": self.stack_peek,
            "stackshow": self.stack_show,
            "stacktest": self.stack_test,
            "queuecreate": self.queue_create,
            "queueenqueue": self.queue_enqueue,
            "queuedequeue": self.queue_dequeue,
            "queuepeek": self.queue_peek,
            "queueshow": self.queue_show,
            "queuetest": self.queue_test,
            "factorialrecurs": self.math_factorial_recurs,
            "factorialdefault": self.math_factorial_default,
            "fibrecurs": self.math_fib_recurs,
            "fibdefault": self.math_fib_default,
            "benchmark": self.run_benchmark,
            "help": self.show_help,
            "exit": lambda *a: setattr(self, "running", False),
            "quit": lambda *a: setattr(self, "running", False),
        }

        for line in sys.stdin:
            parts = line.strip().split()
            if not parts:
                continue

            cmd = parts[0].lower()
            args = parts[1:]

            if cmd in commands:
                try:
                    commands[cmd](*args)
                except Exception as e:
                    print(f"Ошибка выполнения команды: {e}")
            else:
                print(f"Неизвестная команда: {cmd}")

            if not self.running:
                break

        print("До свидания!")


def main():
    cli = SortingCLI()
    cli.run()
