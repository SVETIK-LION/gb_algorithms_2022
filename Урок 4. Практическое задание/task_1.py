"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


numbers = [elem for elem in range(10000)]
print(f'Результат работы функции func_1: {func_1(numbers)}')
print(f'Время выполнения: {timeit("func_1(numbers)", globals=globals(), number=10000)}')


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(f'Результат работы оптимизированной функции func_2: {func_2(numbers)}')
print(f'Время выполнения: {timeit("func_2(numbers)", globals=globals(), number=10000)}')


"""
Оптимизировала функцию с помощью list comprehension. Программа стала выполняться быстрее примерно на 19%.
Это достигается за счет того, что в list comprehension не вызывается метод append.
"""
