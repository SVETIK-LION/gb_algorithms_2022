"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


import hashlib


def count_substrings(string: str):
    substrings_set = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] != string:
                 substrings_set.add(hashlib.sha256(string[i:j].encode()).hexdigest())
                 print(string[i:j], end=' ')

    print(f'\nМножество хэшей подстрок: {substrings_set}')
    print(f'Уникальных подстрок в строке "{string}": {len(substrings_set)}')


count_substrings('Zorro')
