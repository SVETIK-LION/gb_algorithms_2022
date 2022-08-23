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


class HexCalc:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return list(hex(int(''.join(self.num_1), 16) + int(''.join(other.num_2), 16)).upper())[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_1), 16) * int(''.join(other.num_2), 16)).upper())[2:]


number_1 = input('Введите первое натуральное шестнадцатеричное число: ')
number_2 = input('Введите второе натуральное шестнадцатеричное число: ')

sum_nums = HexCalc(number_1, number_2) + HexCalc(number_1, number_2)
mul_nums = HexCalc(number_1, number_2) * HexCalc(number_1, number_2)

print(f'Сумма чисел: {sum_nums}\nПроизведение: {mul_nums}')
