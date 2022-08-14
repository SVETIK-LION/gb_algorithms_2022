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
def autentification_1(users_list: dict, login: str, password: str):
    if login in users_list:                                                                                     # O(n)
        if password == list(users_list.get(login))[0] and list(users_list.get(login))[1] == 'activated':        # O(n)
            return f'{login}, добро пожаловать на сайт!'                                                        # O(1)
        elif password == list(users_list.get(login))[0] and list(users_list.get(login))[1] == 'not_activated':  # O(n)
            return f'{login}, пожалуйста, активируйте Вашу учетную запись'                                      # O(1)
        else:
            return 'Неверный пароль'                                                                            # O(1)
    else:
        return 'Вы еще не зарегистрированы в системе или ввели неверный логин'                                  # O(1)

    # Общая сложность: O(n^2)


# Проверка:
print(autentification_1(users, 'Korben Dallas', 'Korben123'))
print(autentification_1(users, 'Aknot', 'Arrr'))
print(autentification_1(users, 'Lelo', 'dhcyrb4jbd'))
print(autentification_1(users, 'Leeloo', 'dcyrbjd'))


# Решение №2
def autentification_2(users_list: dict, login: str, password: str):
    for key, val in users_list.items():                                         # O(n)
        if key == login:                                                        # O(1)
            if val[0] == password and val[1] == 'activated':                    # O(1)
                return f'{login}, добро пожаловать на сайт!'                    # O(1)
            elif val[0] == password and val[1] == 'not_activated':              # O(1)
                return f'{login}, пожалуйста, активируйте Вашу учетную запись'  # O(1)
            elif val[0] != password:                                            # O(1)
                return 'Неверный пароль'                                        # O(1)

    return 'Вы еще не зарегистрированы в системе или ввели неверный логин'      # O(1)

    # Общая сложность: O(n)


# Проверка:
print('--------------------')
print(autentification_2(users, 'Ruby Rhood', 'yesBaby#@!'))
print(autentification_2(users, 'Emanuel Zorg', 'StoNeS'))
print(autentification_2(users, 'Aknot', 'Mrrr'))
print(autentification_2(users, 'user', '12345'))

"""
Решение №2 эффективнее, так как сложность O(n) меньше, чем сложность O(n^2)
"""
