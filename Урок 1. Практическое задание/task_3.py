"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

# Информация о компаниях
companies = {
    'RobCo Industries': 20937466,
    'Nuka-Cola Corporation': 3948574839,
    'Sunset Sarsaparilla Company': 3464,
    'Brotherhood of steel': 42,
    'Vault-Tec Corporation': 43893849392923
}


# Решение №1:
def three_largest_profit_1(information: dict):
    sorted_values = sorted(information.values(), reverse=True)  # O(n * log(n)) Сортировка значений словаря
    sorted_dict = {}                                    # O(1)

    for i in sorted_values:                             # O(n)
        for j in information.keys():                           # O(n) + O(1)
            if information[j] == i:                            # O(1)
                sorted_dict[j] = information[j]                # O(1)
                break
    return list(sorted_dict.items())[0:3]               # O(1) + O(len(dict)) + (O[0:3] => O(1))
    # Общая сложность: O(n * log(n)) + O(n**2) = O(n**2)


print(three_largest_profit_1(companies))


# Решение №2:
def three_largest_profit_2(information: dict):
    sorted_keys = sorted(information, key=information.get, reverse=True)  # O(n * log(n))
    sorted_dict = {}                        # O(1)

    for i in sorted_keys:                   # O(n)
        sorted_dict[i] = information[i]            # O(1)

    return list(sorted_dict.items())[0:3]   # (O(1) + O(len(dict)) + O[0:3]) => O(1)
    # Общая сложность: O(n * log(n)) + O(n) = O(n * log(n))


print(three_largest_profit_2(companies))

"""
Решения №2 эффективнее, чем решение №1.
Так как скорость алгоритма со сложностью O(n * log(n)) меняется менее значительно при увеличении количества значений,
чем скорость алгоритма со сложностью O(n**2).
"""
