"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# Учетные записи пользователей
users = {
    'Korben Dallas': ('Korben123', 'activated'),
    'Leeloo': ('dhcyrb4jbd', 'activated'),
    'Ruby Rhood': ('yesBaby#@!', 'activated'),
    'Aknot': ('Arrr', 'not_activated'),
    'Emanuel Zorg': ('StoNeS', 'not_activated'),
    'Diva Plavalaguna': ('SingTheSong', 'activated')
}


# Решение №1
def autentification_1(login: str, password: str):
    if login in users:
        if password == list(users.get(login))[0] and list(users.get(login))[1] == 'activated':
            return f'{login}, добро пожаловать на сайт!'
        elif password == list(users.get(login))[0] and list(users.get(login))[1] == 'not_activated':
            return f'{login}, пожалуйста, активируйте Вашу учетную запись'
        else:
            return 'Неверный пароль'
    else:
        return 'Вы еще не зарегистрированы в системе или ввели неверный логин'


# Проверка:
print(autentification_1('Korben Dallas', 'Korben123'))
print(autentification_1('Aknot', 'Arrr'))
print(autentification_1('Lelo', 'dhcyrb4jbd'))
print(autentification_1('Leeloo', 'dcyrbjd'))


# Решение №2
def autentification_2(login: str, password: str):
    for name in users:
        if login == name and users.get(name) == (password, 'activated'):
            return f'{login}, добро пожаловать на сайт!'
        elif login == name and users.get(name) == (password, 'not_activated'):
            return f'{login}, пожалуйста, активируйте Вашу учетную запись'
        elif login == name and list(users.get(name))[0] != password:
            return 'Неверный пароль'
    if login not in users:
        return 'Вы еще не зарегистрированы в системе или ввели неверный логин'


# Проверка:
print(autentification_2('Leeloo', 'dhcyrb4jbd'))
print(autentification_2('Emanuel Zorg', 'StoNeS'))
print(autentification_2('Aknot', 'Mrrr'))
print(autentification_2('user', '12345'))

