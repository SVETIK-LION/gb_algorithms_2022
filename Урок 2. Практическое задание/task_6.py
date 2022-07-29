"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""


from random import randint


def guess_number(number, attempts_count):
    """
    Игра "Угадай число"
    :param number: Загаданное число
    :param attempts_count: Число попыток
    :return: Результат угадывания
    """
    print(f'Попытка № {attempts_count}')
    user_number = int(input('Введите целое число от 0 до 100: '))
    if user_number == number:
        print(f'Вы угадали! Это число {number}')
    elif attempts_count == 10:
        print(f'Попытки закончились. Это было число {number}')
    else:
        if user_number < number:
            print(f'Число {user_number} меньше, чем загаданное')
            return guess_number(number, attempts_count + 1)
        elif user_number > number:
            print(f'Число {user_number} больше, чем загаданное')
            return guess_number(number, attempts_count + 1)


try:
    guess_number(randint(0, 100), 1)
except ValueError:
    print('Неверное значение. Введите целое число от 0 до 100')
