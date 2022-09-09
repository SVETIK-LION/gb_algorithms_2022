"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""


from random import randint
from timeit import timeit


my_list = [randint(-100, 100) for i in range(100)]


def bubble_sort_desc(lst: list):
    number = 1
    while number < len(lst):
        for i in range(len(lst) - number):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        number += 1
    return lst


def bubble_sort_desc_upgrade(lst: list):
    # Есть перемещения
    moving = True
    while moving:
        moving = False
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                # Совершается перемещение и флаг меняется. Если его не будет, то выход из цикла
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                moving = True
    return lst


# Время выполнения bubble_sort_desc range(6)
print(timeit("bubble_sort_desc(my_list[:])", globals=globals(), number=100))
# 0.000311833995510824

# Время выполнения bubble_sort_desc_upgrade range(6)
print(timeit("bubble_sort_desc_upgrade(my_list[:])", globals=globals(), number=100))
# 0.00016879200120456517

# ---------------------

# Время выполнения bubble_sort_desc range(100)
print(timeit("bubble_sort_desc(my_list[:])", globals=globals(), number=100))
# 0.062236709010903724

# Время выполнения bubble_sort_desc_upgrade range(100)
print(timeit("bubble_sort_desc_upgrade(my_list[:])", globals=globals(), number=100))
# 0.09122887499688659

# ---------------------

# Время выполнения bubble_sort_desc range(1000)
print(timeit("bubble_sort_desc(my_list[:])", globals=globals(), number=100))
# 6.232797000004211

# Время выполнения bubble_sort_desc_upgrade range(1000)
print(timeit("bubble_sort_desc_upgrade(my_list[:])", globals=globals(), number=100))
# 9.985506541997893


"""
Вывод:
На небольших массивах, действительно, по времени выигрывает bubble_sort_desc_upgrade - вариант функции с флагом.
Но когда массив увеличивается, скорость второй функции падает и становится меньше, чем у функции без флага.
"""
