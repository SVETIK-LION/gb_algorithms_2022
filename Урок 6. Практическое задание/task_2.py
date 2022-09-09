"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""


from memory_profiler import memory_usage


lst = []  # Список для значений используемой памяти при вызовах рекурсии


def memory_decorator(func):
    """
    Вычисляет память, которая была использована при вызове функции\n
    :param func:
    :return:
    """
    def wrapper(*args, **kvargs):
        result = func(*args, **kvargs)
        lst.append(str(memory_usage()))

        return result

    return wrapper


# Функция из урока 2, задания 4
@memory_decorator
def sum_nums_line(n: int, elem: float, count: int, sum_numbers: float):
    """
    :param n: Количество элементов ряда
    :param elem: Первый элемент ряда
    :param count: Сколько элесентов уже есть в ряде
    :param sum_numbers: Начальная сумма элементов
    :return: Возвращает сумму элементов ряда
    """
    if count == n:
        print(f'Сумма {n} элементов ряда равна: {sum_numbers}')
    else:
        return sum_nums_line(n, elem / 2 * (-1), count + 1, sum_numbers + elem)


try:
    n_elems = int(input('Введите количество элементов ряда(целое положительное число): '))
    sum_nums_line(n_elems, 1, 0, 0)
except ValueError:
    print('Неверное значение. Введите целое положительное число')


print(f'Задействованная память до вызова рекурсивной функции: {str(memory_usage())} MB')
for i, memory in enumerate(list(reversed(lst)), 1):
    print(f'Задействованная память после {i}-го вызова рекурсивной функции: {memory} MB')


"""
При использовании profile, на каждый вызов рекурсии печаталась новая таблица. Это не удобно.
Поэтому можно сделать декорирование функции и сделать замеры с помощью profile для декоратора.
Вызов будет один => таблица с замерами тоже будет одна.
Так же можно сделать декорирование функции другой функцией, в которой использкется memory_usage.
Таким образом, мы сможем замерить используемую память до вызова и после каждого вызова рекурсивной функции.
"""
