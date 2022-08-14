"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.tasks = []

    def __str__(self):
        return str(self.tasks)

    def is_empty(self):
        return self.tasks == []

    def add_task(self, task):
        self.tasks.insert(0, task)

    def del_task(self):
        return self.tasks.pop()

    def tasks_count(self):
        return len(self.tasks)


class TaskBoardClass:
    def __init__(self):
        self.base_queue = QueueClass()  # Базовая очередь
        self.work_queue = QueueClass()  # Очереь на доработку
        self.performed = []             # Выполненные задачи

    def add_to_base(self, task):
        """Добавляем задачу в базовую очередь"""
        self.base_queue.add_task(task)

    def perform_task(self):
        """Отмечаем текущую задачу выполненной"""
        task = self.base_queue.del_task()
        self.performed.append(task)

    def send_to_work(self):
        """Отправляем задачу на доработку"""
        task = self.base_queue.del_task()
        self.work_queue.add_task(task)

    def from_work_to_base(self):
        """Отправляем из доработки в базовую очередь"""
        task = self.work_queue.del_task()
        self.base_queue.add_task(task)

    def work_task(self):
        """Задача в дорботке"""
        return self.work_queue.tasks[len(self.work_queue.tasks) - 1]

    def current_task(self):
        """Текущая задача"""
        return self.base_queue.tasks[len(self.base_queue.tasks) - 1]


if __name__ == '__main__':
    task_board = TaskBoardClass()
    # Добавим несколько задач
    task_board.add_to_base('Breakfast')
    task_board.add_to_base('Workout')
    task_board.add_to_base('Work')
    task_board.add_to_base('Meditation')
    # Список задач в базовой очереди
    print(task_board.base_queue.tasks)
    # Текущая задача
    print(task_board.current_task())
    # Отметим задачу выполненной
    task_board.perform_task()
    # Список выполненных задач
    print(task_board.performed)
    # Отправим задачу на доработку
    task_board.send_to_work()
    # Список задач на доработку
    print(task_board.work_queue.tasks)
    # Отправим задачу из доработки в базовую очередь
    task_board.from_work_to_base()
    # Базовая очередь
    print(task_board.base_queue.tasks)
