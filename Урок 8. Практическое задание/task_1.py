"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""


# Алгоритм Хаффмана
from collections import Counter, deque


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def get_tree(string: str):
    # Считаем, сколько раз в строке встречается каждый символ
    count_string = Counter(string)
    # Преобразуем словарь в список кортежей, сортируем по значеню и записываем в дек
    sorted_string = deque(sorted(count_string.items(), key=lambda items: item[1]))
    # Если в деке содержится больше одного кортежа, то суммируем первые два значения кортежа. Это будет вес узла
    while len(sorted_string) > 1:
        weight = sorted_string[0][1] + sorted_string[1][1]
        # Создаем левую и правую ветки
        node = Node(left=sorted_string.popleft()[0], right=sorted_string.popleft()[0])
        #
        for i, item in enumerate(sorted_string):
            if weight > item[1]:
                continue
            else:
                sorted_string.insert(i, (node, weight))
                break
        else:
            sorted_string.append((node, weight))

    return sorted_string[0][0]


code_table = dict()


def coding(tree, path=''):
    if not isinstance(tree, Node):
        code_table[tree] = path
    else:
        coding(tree.left, path=f'{path}0')
        coding(tree.right, path=f'{path}1')


# def decoding():
#

my_string = "beep boop beer!"

coding(get_tree(my_string))

for i in my_string:

    print(code_table[i], end=' ')

print()
