"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и выводящий результат на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        number = enter_num % 10
        revers_num = (revers_num + number / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        number = enter_num % 10
        revers_num = (revers_num + number / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


num = 1234567890
print(timeit("revers(num)", globals=globals(), number=10000))
print(timeit("revers_2(num)", globals=globals(), number=10000))
print(timeit("revers_3(num)", globals=globals(), number=10000))
print(timeit('revers_4(num)', globals=globals(), number=10000))


"""
Самая эффективная реализация из четырех - третья. 
"""
