"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


from random import randint
from timeit import timeit


m = 1000
my_list = [randint(0, 100) for i in range(2 * m + 1)]


def not_sort(lst: list):
    for i in range(len(lst) // 2):
        lst.remove(max(lst))
    return max(lst)


print(f'Медиана: {not_sort(my_list)}')
print(f'Время выполнения: {timeit("not_sort(my_list[:])", globals=globals(), number=100)}')


# Время выполнения 10: 0.0001703750021988526
# Время выполнения 100: 0.007357624999713153
# Время выполнения 1000: 0.38284125000063796
