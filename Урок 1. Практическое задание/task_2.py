"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


lst_1 = [5, -4, 25, 17, 36]


def min_list_element_1(lst: list):
    for k in range(len(lst) - 1):                    # O(n)
        for i in range(len(lst) - 1):                # O(n)
            if lst[i] > lst[i + 1]:                  # O(1)
                lst[i], lst[i+1] = lst[i+1], lst[i]  # O(1)

    return lst[0]


print(min_list_element_1(lst_1))


lst_2 = [4, 3, -2, 15, 1]


def min_list_element_2(lst: list):
    min_element = lst[0]            # O(1)
    for i in range(len(lst) - 1):   # O(n)
        if lst[i] < min_element:    # O(1)
            min_element = lst[i]    # O(1)

    return min_element


print(min_list_element_2(lst_2))
