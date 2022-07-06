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

# Решение 1:
def three_largest_profit_1(dict):
    sorted_values = sorted(dict.values(), reverse=True) # Сортировка значений словаря
    sorted_dict = {}

    for i in sorted_values:
        for j in dict.keys():
            if dict[j] == i:
                sorted_dict[j] = dict[j]
                break
    return list(sorted_dict.items())[0:3]

print(three_largest_profit_1(companies))


# Решение 2:
def three_largest_profit_2(dict):
    sorted_keys = sorted(dict, key=dict.get, reverse=True) # Сортировка ключей по их значениям в порядке убывания
    sorted_dict = {}

    for i in sorted_keys:
        sorted_dict[i] = dict[i]

    return list(sorted_dict.items())[0:3]

print(three_largest_profit_2(companies))


# Решение 3:
def three_largest_profit_3(dict):
    largest_profit = {}
    count = 0

    for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True):
        if count < 3:
            largest_profit.setdefault(k, v)
        count += 1

    return largest_profit

print(three_largest_profit_3(companies))

# Решение № самое эффективное

