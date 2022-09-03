"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""


from collections import defaultdict
import functools


def hex_calc():
    """
    Возвращает сумму и произведение чисел в шестнадцатеричной системе\n
    :return:list
    """
    numbers = defaultdict(list)
    conver_nums = []

    digit_1 = input(f'Введите первое натуральное шестнадцатеричное число: ')
    digit_2 = input(f'Введите второе натуральное шестнадцатеричное число: ')
    numbers[digit_1] = list(digit_1)
    numbers[digit_2] = list(digit_2)

    for val in numbers.values():
        conver_digit = int(''.join(val), 16)  # Преобразуем в 10-ю систему
        conver_nums.append(conver_digit)

    sum_nums_10 = sum(conver_nums)
    mult_nums_10 = functools.reduce(lambda a, b: a * b, conver_nums)

    sum_nums_16 = list(hex(sum_nums_10).upper()[2:])    # Переводим обратно в 16-ю систему
    mult_nums_16 = list(hex(mult_nums_10).upper()[2:])

    return f'Сумма чисел: {sum_nums_16}\nПроизведение: {mult_nums_16}'


print(hex_calc())
