import random


def rand_int_array(
    array_size: int,
    minimum_value: int,
    maximum_value: int,
    *,
    distinct=False,
    seed=None,
) -> list[int]:
    """
    Генерирует массив случайных чисел
    :param array_size:
    :param minimum_value:
    :param maximum_value:
    :param distinct:
    :param seed:
    :return:
    """
    if seed is not None:
        random.seed(seed)

    if distinct:
        available_values_count = maximum_value - minimum_value + 1
        if available_values_count < array_size:
            raise ValueError("недостаточно уникальных значений в диапазоне")

        value_range = range(minimum_value, maximum_value + 1)
        return random.sample(value_range, array_size)

    random_numbers = []
    for element_index in range(array_size):
        random_number = random.randint(minimum_value, maximum_value)
        random_numbers.append(random_number)

    return random_numbers


def nearly_sorted(array_size: int, number_of_swaps: int, *, seed=None) -> list[int]:
    """
    Генерирует почти отсортированный массив
    :param array_size:
    :param number_of_swaps:
    :param seed:
    :return:
    """
    if seed is not None:
        random.seed(seed)

    sorted_array = list(range(array_size))

    for swap_iteration in range(number_of_swaps):
        first_random_index = random.randint(0, array_size - 1)
        second_random_index = random.randint(0, array_size - 1)

        first_element = sorted_array[first_random_index]
        second_element = sorted_array[second_random_index]
        sorted_array[first_random_index] = second_element
        sorted_array[second_random_index] = first_element

    return sorted_array


def many_duplicates(array_size: int, unique_values_count=5, *, seed=None) -> list[int]:
    """
    Генерирует массив с большим кол-вом дубликатов
    :param array_size:
    :param uniaue_values_count:
    :param seed:
    :return:
    """
    if seed is not None:
        random.seed(seed)

    array_with_duplicates = []
    for element_position in range(array_size):
        random_value = random.randint(0, unique_values_count - 1)
        array_with_duplicates.append(random_value)

    return array_with_duplicates


def reverse_sorted(array_size: int) -> list[int]:
    """
    Генерирует массив в обратном порядке
    """
    reverse_ordered_array = []
    for current_value in range(array_size - 1, -1, -1):
        reverse_ordered_array.append(current_value)

    return reverse_ordered_array
