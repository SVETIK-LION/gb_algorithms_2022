"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""


from collections import defaultdict
import functools
from memory_profiler import profile


# Урок 5, задание 2_1
# Исходная функция
@profile
def hex_calc_1():
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


print(hex_calc_1())


# Оптимизированная функция
@profile
def hex_calc_2():
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

    del sum_nums_10
    del mult_nums_10
    del conver_nums
    del numbers

    return f'Сумма чисел: {sum_nums_16}\nПроизведение: {mult_nums_16}'


hex_calc_2()


"""
Сделала удаление некоторых элементов с помощью оператора del. Во второй функции стало использоваться меньше памяти.
hex_calc_1: 19.3 MiB
hex_calc_2: 13.8 MiB
"""
# Введите первое натуральное шестнадцатеричное число: A
# Введите второе натуральное шестнадцатеричное число: B
# Filename: /Users/SVETIK/PycharmProjects/gb_algorithms_2022/Урок 6. Практическое задание/task_1_5.py
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     40     19.3 MiB     19.3 MiB           1   @profile
#     41                                         def hex_calc_1():
#     42                                             """
#     43                                             Возвращает сумму и произведение чисел в шестнадцатеричной системе\n
#     44                                             :return:list
#     45                                             """
#     46     19.3 MiB      0.0 MiB           1       numbers = defaultdict(list)
#     47     19.3 MiB      0.0 MiB           1       conver_nums = []
#     48
#     49     19.3 MiB      0.0 MiB           1       digit_1 = input(f'Введите первое натуральное шестнадцатеричное число: ')
#     50     19.3 MiB      0.0 MiB           1       digit_2 = input(f'Введите второе натуральное шестнадцатеричное число: ')
#     51     19.3 MiB      0.0 MiB           1       numbers[digit_1] = list(digit_1)
#     52     19.3 MiB      0.0 MiB           1       numbers[digit_2] = list(digit_2)
#     53
#     54     19.3 MiB      0.0 MiB           3       for val in numbers.values():
#     55     19.3 MiB      0.0 MiB           2           conver_digit = int(''.join(val), 16)  # Преобразуем в 10-ю систему
#     56     19.3 MiB      0.0 MiB           2           conver_nums.append(conver_digit)
#     57
#     58     19.3 MiB      0.0 MiB           1       sum_nums_10 = sum(conver_nums)
#     59     19.3 MiB      0.0 MiB           3       mult_nums_10 = functools.reduce(lambda a, b: a * b, conver_nums)
#     60
#     61     19.3 MiB      0.0 MiB           1       sum_nums_16 = list(hex(sum_nums_10).upper()[2:])    # Переводим обратно в 16-ю систему
#     62     19.3 MiB      0.0 MiB           1       mult_nums_16 = list(hex(mult_nums_10).upper()[2:])
#     63
#     64     19.3 MiB      0.0 MiB           1       return f'Сумма чисел: {sum_nums_16}\nПроизведение: {mult_nums_16}'
#
#
# Сумма чисел: ['1', '5']
# Произведение: ['6', 'E']
# Введите первое натуральное шестнадцатеричное число: A
# Введите второе натуральное шестнадцатеричное число: B
# Filename: /Users/SVETIK/PycharmProjects/gb_algorithms_2022/Урок 6. Практическое задание/task_1_5.py
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     70     19.3 MiB     19.3 MiB           1   @profile
#     71                                         def hex_calc_2():
#     72                                             """
#     73                                             Возвращает сумму и произведение чисел в шестнадцатеричной системе\n
#     74                                             :return:list
#     75                                             """
#     76     19.3 MiB      0.0 MiB           1       numbers = defaultdict(list)
#     77     19.3 MiB      0.0 MiB           1       conver_nums = []
#     78
#     79     14.0 MiB     -5.3 MiB           1       digit_1 = input(f'Введите первое натуральное шестнадцатеричное число: ')
#     80     13.8 MiB     -0.2 MiB           1       digit_2 = input(f'Введите второе натуральное шестнадцатеричное число: ')
#     81     13.8 MiB      0.0 MiB           1       numbers[digit_1] = list(digit_1)
#     82     13.8 MiB      0.0 MiB           1       numbers[digit_2] = list(digit_2)
#     83
#     84     13.8 MiB      0.0 MiB           3       for val in numbers.values():
#     85     13.8 MiB      0.0 MiB           2           conver_digit = int(''.join(val), 16)  # Преобразуем в 10-ю систему
#     86     13.8 MiB      0.0 MiB           2           conver_nums.append(conver_digit)
#     87
#     88     13.8 MiB      0.0 MiB           1       sum_nums_10 = sum(conver_nums)
#     89     13.8 MiB      0.0 MiB           3       mult_nums_10 = functools.reduce(lambda a, b: a * b, conver_nums)
#     90
#     91     13.8 MiB      0.0 MiB           1       sum_nums_16 = list(hex(sum_nums_10).upper()[2:])    # Переводим обратно в 16-ю систему
#     92     13.8 MiB      0.0 MiB           1       mult_nums_16 = list(hex(mult_nums_10).upper()[2:])
#     93
#     94     13.8 MiB      0.0 MiB           1       del sum_nums_10
#     95     13.8 MiB      0.0 MiB           1       del mult_nums_10
#     96     13.8 MiB      0.0 MiB           1       del conver_nums
#     97     13.8 MiB      0.0 MiB           1       del numbers
#     98
#     99     13.8 MiB      0.0 MiB           1       return f'Сумма чисел: {sum_nums_16}\nПроизведение: {mult_nums_16}'
#
#
# """
