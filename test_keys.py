#!/usr/bin/env python3
from src.sorts import MultiSorter

# Тестовые данные
people = [
    {"name": "Alice", "age": 30, "salary": 5000},
    {"name": "Bob", "age": 25, "salary": 3000},
    {"name": "Charlie", "age": 35, "salary": 7000},
    {"name": "Diana", "age": 28, "salary": 4000},
]

numbers = [5, 2, 8, 1, 9, 3]

print("=== Тестирование поддержки ключей ===")

# 1. Сортировка по возрасту
print("\n1. Сортировка людей по возрасту:")
sorter = MultiSorter(people, key=lambda x: x["age"])
sorted_by_age = sorter.bubble_sort()
for person in sorted_by_age:
    print(f"{person['name']}: {person['age']}")

# 2. Сортировка по зарплате в обратном порядке
print("\n2. Сортировка людей по зарплате (обратный порядок):")
sorter = MultiSorter(people, key=lambda x: x["salary"], reverse=True)
sorted_by_salary = sorter.quick_sort()
for person in sorted_by_salary:
    print(f"{person['name']}: {person['salary']}")

# 3. Сортировка чисел по модулю
print("\n3. Сортировка чисел с отрицательными по модулю:")
numbers_with_neg = [5, -2, 8, -1, 9, -3]
sorter = MultiSorter(numbers_with_neg, key=abs)
sorted_by_abs = sorter.bubble_sort()
print(f"Исходный: {numbers_with_neg}")
print(f"Отсортированный по модулю: {sorted_by_abs}")

# 4. Сортировка строк по длине
print("\n4. Сортировка строк по длине:")
strings = ["apple", "banana", "kiwi", "strawberry", "fig"]
sorter = MultiSorter(strings, key=len)
sorted_by_length = sorter.quick_sort()
print(f"Исходный: {strings}")
print(f"Отсортированный по длине: {sorted_by_length}")

# 5. Тестирование bucket sort с ключами
print("\n5. Bucket sort с ключом (по возрасту):")
sorter = MultiSorter(people, key=lambda x: x["age"])
sorted_by_age_bucket = sorter.bucket_sort()
for person in sorted_by_age_bucket:
    print(f"{person['name']}: {person['age']}")

print("\n=== Тестирование ограничений ===")

# 6. Radix sort с ключом - должно выдать ошибку
try:
    sorter = MultiSorter(numbers, key=lambda x: x * 2)
    result = sorter.radix_sort()
    print("Radix sort с ключом сработал (неожиданно)")
except ValueError as e:
    print(f"Radix sort с ключом вызвал ошибку: {e}")

# 7. Count sort с ключом - должно выдать ошибку
try:
    sorter = MultiSorter(numbers, key=lambda x: x * 2)
    result = sorter.count_sort()
    print("Count sort с ключом сработал (неожиданно)")
except ValueError as e:
    print(f"Count sort с ключом вызвал ошибку: {e}")

print("\n=== Тестирование reverse ===")

# 8. Обратная сортировка чисел
print("\n8. Обратная сортировка чисел:")
sorter = MultiSorter(numbers, reverse=True)
reverse_sorted = sorter.bubble_sort()
print(f"Исходный: {numbers}")
print(f"Обратный порядок: {reverse_sorted}")

# 9. Комбинированная сортировка: по длине имени в обратном порядке
print("\n9. Сортировка людей по длине имени (обратный порядок):")
sorter = MultiSorter(people, key=lambda x: len(x["name"]), reverse=True)
sorted_by_name_length = sorter.quick_sort()
for person in sorted_by_name_length:
    print(f"{person['name']}: {len(person['name'])}")
