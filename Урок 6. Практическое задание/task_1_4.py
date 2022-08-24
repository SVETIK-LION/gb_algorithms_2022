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

Это файл для четвертого скрипта
"""


from timeit import timeit
from pympler import asizeof
from numpy import array


numbers = [elem for elem in range(1000)]


# Урок 4 задание 1
def func_1(nums):
    new_arr_1 = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return asizeof.asizeof(new_arr_1)


print(f'Занимает объект 1: {func_1(numbers)}')
print(f'Время выполнения func_1: {timeit("func_1(numbers)", globals=globals(), number=10000)}')


def func_2(nums):
    new_arr_2 = array([i for i in range(len(nums)) if nums[i] % 2 == 0])
    return asizeof.asizeof(new_arr_2)


print(f'Занимает объект 2: {func_2(numbers)}')
print(f'Время выполнения func_2: {timeit("func_2(numbers)", globals=globals(), number=10000)}')


# Занимает объект 1: 20208
# Время выполнения func_1: 6.575020874995971
# Занимает объект 2: 4128
# Время выполнения func_2: 0.9490602919977391

# Вывод:
# После использования arrov из модуля numpy, объект стал занимать меньше памяти.
