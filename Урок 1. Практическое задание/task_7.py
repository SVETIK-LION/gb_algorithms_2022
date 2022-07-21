"""
Задание 7. На закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром и в таких строках (включающих пробелы)

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""


class DecueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        self.elems = []

    def add_to_start(self, el):
        self.elems.insert(0, el)

    def add_to_end(self, el):
        self.elems.append(el)

    def del_start(self):
        return self.elems.pop(0)

    def del_end(self):
        return self.elems.pop()

    def elems_amount(self):
        return len(self.elems)


# Проверка на палиндром
def is_palindrome(string: str):
    pal_decue = DecueClass()

    for el in string.lower().replace(' ', ''):
        pal_decue.add_to_start(el)

    equal = True

    while pal_decue.elems_amount() > 1 and equal:
        start_el = pal_decue.del_start()
        end_el = pal_decue.del_end()
        if start_el != end_el:
            equal = False

    return equal


if __name__ == '__main__':
    my_deque = DecueClass()
    # Добавим несколько элементов в начало дека
    my_deque.add_to_start('Дикий гуль')
    my_deque.add_to_start('Брамин')
    my_deque.add_to_start('Коготь смерти')
    my_deque.add_to_start('Кротокрыс')
    print(my_deque.elems)
    # Добавим элемент в конец дека
    my_deque.add_to_end('Радскорпион')
    print(my_deque.elems)
    # Удалим два элемента из начала дека
    my_deque.del_start()
    my_deque.del_start()
    print(my_deque.elems)
    # Удалим элемент из конца дека
    my_deque.del_end()
    print(my_deque.elems)
    # Количество элементов в деке
    print(my_deque.elems_amount())
    # Проверим палиндром
    print(is_palindrome('молоко делили ледоколом'))
