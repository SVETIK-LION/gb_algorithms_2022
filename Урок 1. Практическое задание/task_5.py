"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class StackPlatesClass:
    def __init__(self, size):
        self.elems = [[]]
        self.size = size      # Размер одной стопки тарелок

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if self.elems[len(self.elems) - 1] == []:
            self.elems.pop()
        result = self.elems[len(self.elems) - 1].pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1]  # Последняя стопка тарелок

    def plates_count(self):  # Тарелок всего
        count = 0
        for p in self.elems:
            count += len(p)
        return count

    def stack_count(self):  # Стопок тарелок всего
        return len(self.elems)


if __name__ == '__main__':
    plates = StackPlatesClass(3)
    print(plates)
    plates.push_in('plate_one')
    plates.push_in('plate_two')
    plates.push_in('plate_three')
    plates.push_in('plate_four')
    plates.push_in('plate_five')
    plates.push_in('plate_six')
    plates.push_in('plate_seven')
    print(plates)
    plates.pop_out()
    plates.pop_out()
    plates.pop_out()
    plates.pop_out()
    plates.pop_out()
    print(plates)
    print(plates.get_val())
    print(plates.plates_count())
    print(plates.stack_count())
