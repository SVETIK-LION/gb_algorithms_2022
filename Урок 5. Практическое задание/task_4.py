"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from collections import OrderedDict
from timeit import timeit


di = {}
or_di = OrderedDict()
n = 100000


# 1) Добавление элемента
def adding_elem_di(dictionary):
    for i in range(n):
        dictionary[i] = i
    return dictionary


def adding_elem_or_di(order_dictionary):
    for i in range(n):
        order_dictionary[i] = i
    return order_dictionary


# 2) Изменение элемента
def change_elem_di(dictionary):
    for i in range(n):
        dictionary[i] = 'meow'
    return dictionary


def change_elem_or_di(order_dictionary):
    for i in range(n):
        order_dictionary[i] = 'moooow'
    return order_dictionary


# 3) Удаление элемента
def del_elem_di(dictionary):
    for i in range(n):
        dictionary.pop(i)
    return dictionary


def del_elem_or_di(order_dictionary):
    for i in range(n):
        order_dictionary.pop(i)
    return order_dictionary


# 1)
print(f'adding_elem_di {timeit("adding_elem_di(di)", globals=globals(), number=100)}')
print(f'adding_elem_or_di {timeit("adding_elem_or_di(or_di)", globals=globals(), number=100)}')


# 2)
print(f'change_elem_di {timeit("change_elem_di(di)", globals=globals(), number=100)}')
print(f'change_elem_or_di {timeit("change_elem_or_di(or_di)", globals=globals(), number=100)}')


# 3)
print(f'del_elem_di {timeit("del_elem_di(di)", globals=globals(), number=1)}')
print(f'del_elem_or_di {timeit("del_elem_or_di(or_di)", globals=globals(), number=1)}')


# Результаты:
# 1)
# adding_elem_di 0.5018004580051638
# adding_elem_or_di 0.6773198750015581

# 2)
# change_elem_di 0.46167091700044693
# change_elem_or_di 0.640619666002749

# 3)
# del_elem_di 0.0068648750020656735
# del_elem_or_di 0.01258850000158418


"""
Обычный словарь dict работает быстрее, чем упорядоченный OrderedDict.
Поэтому лучше использовать его, если не нужены функции move_to_end и popitem.
Тем более в новых версиях Python в обычном словаре порядок элементов тоже запоминается.
"""
