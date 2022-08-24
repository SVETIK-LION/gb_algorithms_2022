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

Это файл для третьего скрипта
"""


from pympler import asizeof


# Урок 5. Задание 2.1
# Исходная функция
class HexCalc_1:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return list(hex(int(''.join(self.num_1), 16) + int(''.join(other.num_2), 16)).upper())[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_1), 16) * int(''.join(other.num_2), 16)).upper())[2:]


# number_1 = input('Введите первое натуральное шестнадцатеричное число: ')
# number_2 = input('Введите второе натуральное шестнадцатеричное число: ')
#
# sum_nums_1_1 = HexCalc_1(number_1, number_2) + HexCalc_1(number_1, number_2)
# mul_nums_1_1 = HexCalc_1(number_1, number_2) * HexCalc_1(number_1, number_2)
#
# print(f'Сумма чисел: {sum_nums_1_1}\nПроизведение: {mul_nums_1_1}')

obj_1 = HexCalc_1('A', 'B')
print(asizeof.asizeof(obj_1))


# Оптимизированная функция
class HexCalc_2:
    __slots__ = ['num_1', 'num_2']

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return list(hex(int(''.join(self.num_1), 16) + int(''.join(other.num_2), 16)).upper())[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_1), 16) * int(''.join(other.num_2), 16)).upper())[2:]


# number_1_2 = input('Введите первое натуральное шестнадцатеричное число: ')
# number_2_2 = input('Введите второе натуральное шестнадцатеричное число: ')
#
# sum_nums_2 = HexCalc_2(number_1, number_2) + HexCalc_2(number_1, number_2)
# mul_nums_2 = HexCalc_2(number_1, number_2) * HexCalc_2(number_1, number_2)
#
# print(f'Сумма чисел: {sum_nums_2}\nПроизведение: {mul_nums_2}')

obj_2 = HexCalc_1('A', 'B')
print(asizeof.asizeof(obj_2))

# Вывод: почему-тоо ничего не поменялось
