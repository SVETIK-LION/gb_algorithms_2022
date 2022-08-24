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

Это файл для второго скрипта
"""


from collections import namedtuple
from recordclass import recordclass
import sys


def avg_profit_1():
    result_profit = {}
    amount = int(input('Введите количество предриятий для рассчета прибыли: '))
    companies_nt = namedtuple('Company', 'name quarter_1 quarter_2 quarter_3 quarter_4')
    for i in range(amount):
        company = companies_nt(name=input('Введиите название предприятия: '),
                               quarter_1=int(input('Введите прибыль предприятия за первый квартал: ')),
                               quarter_2=int(input('Введите прибыль предприятия за второй квартал: ')),
                               quarter_3=int(input('Введите прибыль предприятия за третий квартал: ')),
                               quarter_4=int(input('Введите прибыль предприятия за четвертый квартал: ')))

        result_profit[company.name] = (company.quarter_1 + company.quarter_2 +
                                       company.quarter_3 + company.quarter_4) / 4

    total_avg_profit = 0
    for val in result_profit.values():
        total_avg_profit += val
        total_avg_profit = total_avg_profit / amount

    print(f'Средняя годовая прибыль всех предприятий: {total_avg_profit}')

    for key, val in result_profit.items():
        if val > total_avg_profit:
            print(f'Предприятия, с прибылью выше среднего значения: {key}')
        elif val < total_avg_profit:
            print(f'Предприятия, с прибылью ниже среднего значения: {key}')

    print(f'Объем занимаемой памяти объектом namedtuple: {sys.getsizeof(companies_nt)}')


avg_profit_1()


def avg_profit_2():
    result_profit = {}
    amount = int(input('Введите количество предриятий для рассчета прибыли: '))
    companies_rec = recordclass('Company', 'name quarter_1 quarter_2 quarter_3 quarter_4')
    for i in range(amount):
        company = companies_rec(name=input('Введиите название предприятия: '),
                                quarter_1=int(input('Введите прибыль предприятия за первый квартал: ')),
                                quarter_2=int(input('Введите прибыль предприятия за второй квартал: ')),
                                quarter_3=int(input('Введите прибыль предприятия за третий квартал: ')),
                                quarter_4=int(input('Введите прибыль предприятия за четвертый квартал: ')))

        result_profit[company.name] = (company.quarter_1 + company.quarter_2 +
                                       company.quarter_3 + company.quarter_4) / 4

    total_avg_profit = 0
    for val in result_profit.values():
        total_avg_profit += val
        total_avg_profit = total_avg_profit / amount

    print(f'Средняя годовая прибыль всех предприятий: {total_avg_profit}')

    for key, val in result_profit.items():
        if val > total_avg_profit:
            print(f'Предприятия, с прибылью выше среднего значения: {key}')
        elif val < total_avg_profit:
            print(f'Предприятия, с прибылью ниже среднего значения: {key}')

    print(f'Объем занимаемой памяти объектом recordclass: {sys.getsizeof(companies_rec)}')


avg_profit_2()

# Объем занимаемой памяти объектом namedtuple: 904
# Объем занимаемой памяти объектом recordclass: 1072