# Лабораторная работа №3: CLI для алгоритмов и структур данных

## Введение
Данная лабораторная работа реализует интерфейс командной строки для тестирования алгоритмов сортировки, работы со структурами данных (стек, очередь) и выполнения математических функций. Программа предоставляет бенчмаркинговые сравнения производительности различных алгоритмов.

## Структура проекта

<pre>
    lab3/
    ├── src/
    │   ├── cli.py
    │   ├── sorts.py
    │   ├── structure_data.py
    │   ├── test_generators.py
    │   ├── math_functions.py
    │   ├── benchmark.py
    │   └── __init__.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_bubble_sort.py
    │   ├── test_bucket_sort.py
    │   ├── test_count_sort.py
    │   ├── test_factorial_default.py
    │   ├── test_factorial_recurs.py
    │   ├── test_fib_default.py
    │   ├── test_fib_recurs.py
    │   ├── test_queue.py
    │   ├── test_quick_sort.py
    │   ├── test_radix_sort.py
    │   ├── test_stack.py
    │   └── __pycache__/
    ├── uv.lock
    ├── report.pdf
    ├── .gitignore
    ├── .pre-commit-config.yaml
    └── README.md
</pre>

## Описание файлов

### Основные модули:
- **cli.py** - Главный модуль, содержащий класс SortingCLI с реализацией командного интерфейса
- **sorts.py** - Класс MultiSorter с реализацией алгоритмов сортировки (bubble, quick, radix, bucket, count)
- **structure_data.py** - Классы Stack и Queue для работы со структурами данных
- **test_generators.py** - Функции для генерации тестовых массивов (случайные, почти отсортированные, с дубликатами, обратный порядок)
- **math_functions.py** - Математические функции (факториал, числа Фибоначчи) в рекурсивной и итеративной реализациях
- **benchmark.py** - Модуль для проведения бенчмаркинга алгоритмов сортировки

### Тесты:
- **test_bubble_sort.py** - Unit тесты для сортировки пузырьком, включая тесты на корректность и граничные случаи
- **test_bucket_sort.py** - Тесты блочной сортировки
- **test_count_sort.py** - Тесты сортировки подсчетом
- **test_factorial_default.py** - Тесты итеративной реализации факториала
- **test_factorial_recurs.py** - Тесты рекурсивной реализации факториала
- **test_fib_default.py** - Тесты итеративных чисел Фибоначчи
- **test_fib_recurs.py** - Тесты рекурсивных чисел Фибоначчи
- **test_queue.py** - Тесты для структуры данных Queue, проверяющие все операции
- **test_quick_sort.py** - Тесты быстрой сортировки
- **test_radix_sort.py** - Тесты поразрядной сортировки
- **test_stack.py** - Тесты для структуры данных Stack, проверяющие все операции

## Как запустить программу на любом устройстве

### Требования:
- Python 3.8 или выше
- Операционная система: Windows, macOS, Linux

### Прямой запуск (универсальный)
```bash
# Перейдите в директорию проекта
cd <путь_к_проекту>

# Запустите CLI
python -c 'from src.cli import main; main()'

# Или если используется python3
python3 -c 'from src.cli import main; main()'
