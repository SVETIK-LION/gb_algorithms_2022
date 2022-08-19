"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""


from collections import deque
from timeit import timeit


my_list = [i for i in range(1000)]
my_deque = deque([i for i in range(1000)])
n = 1000


# 1) append, pop, extend
def append_list(lst):
    for i in range(n):
        lst.append(i)
    return lst


def append_deque(dqe):
    for i in range(n):
        dqe.append(i)
    return dqe


def pop_list(lst):
    for i in range(n):
        lst.pop()
    return lst


def pop_deque(dqe):
    for i in range(n):
        dqe.pop()
    return dqe


def extend_list(lst):
    for i in range(n):
        lst.extend(['meow', 'omnomnom', 'shhhh'])
    return lst


def extend_deque(dqe):
    for i in range(n):
        dqe.extend(['meow', 'omnomnom', 'shhhh'])
    return dqe


# 2) appendleft, popleft, extendleft
def appendleft_list(lst):
    for i in range(n):
        lst.insert(0, i)
    return lst


def appenfleft_deque(dqe):
    for i in range(n):
        dqe.appendleft(i)
    return dqe


def popleft_list(lst):
    for i in range(n):
        lst.pop(i)
    return lst


def popleft_deque(dqe):
    for i in range(n):
        dqe.popleft()
    return dqe


def extendleft_list(lst):
    for i in range(n):
        lst.insert(0, ['ururur', 'mrmrmr', 'hrfrf'])
    return lst


def extendleft_deque(dqe):
    for i in range(n):
        dqe.extendleft(['ururur', 'mrmrmr', 'hrfrf'])
    return dqe


# 3) операции получения элемента списка и дека
def get_element_list(lst):
    for i in range(n):
        lst[i] = i
    return lst


def get_element_deque(dqe):
    for i in range(n):
        dqe[i] = i
    return dqe


# 1)
print(f'append_list {timeit("append_list(my_list)", globals=globals(), number=100)}')
print(f'append_deque {timeit("append_deque(my_deque)", globals=globals(), number=100)}')
print(f'pop_list {timeit("pop_list(my_list)", globals=globals(), number=100)}')
print(f'pop_deque {timeit("pop_deque(my_deque)", globals=globals(), number=100)}')
print(f'extend_list {timeit("extend_list(my_list)", globals=globals(), number=100)}')
print(f'extend_deque {timeit("extend_deque(my_deque)", globals=globals(), number=100)}')


# Результаты 1:
# append_list 0.047495040998910554
# append_deque 0.048215916998742614
# pop_list 0.048307916997146094
# pop_deque 0.050239625001267996
# extend_list 0.09177779099991312
# extend_deque 0.12079112499850453


# 2)
print(f'appendleft_list {timeit("appendleft_list(my_list)", globals=globals(), number=100)}')
print(f'appenfleft_deque {timeit("appenfleft_deque(my_deque)", globals=globals(), number=100)}')
print(f'popleft_list {timeit("popleft_list(my_list)", globals=globals(), number=100)}')
print(f'popleft_deque {timeit("popleft_deque(my_deque)", globals=globals(), number=100)}')
print(f'extendleft_list {timeit("extendleft_list(my_list)", globals=globals(), number=100)}')
print(f'extendleft_deque {timeit("extendleft_deque(my_deque)", globals=globals(), number=100)}')


# Результаты 2:
# appendleft_list 27.02602562499669
# appenfleft_deque 0.005118958004459273
# popleft_list 8.784314374999667
# popleft_deque 0.0047307909990195185
# extendleft_list 27.325117916996533
# extendleft_deque 0.011844332999316975


print(f'get_element_list {timeit("get_element_list(my_list)", globals=globals(), number=100)}')
print(f'get_element_list {timeit("get_element_list(my_deque)", globals=globals(), number=100)}')


# Результаты 3:
# get_element_list 0.0038214590022107586
# get_element_list 0.004483041004277766


"""
Методы для объекта deque модуля collections работают быстрее, чем аналогичные методы для list.
"""
