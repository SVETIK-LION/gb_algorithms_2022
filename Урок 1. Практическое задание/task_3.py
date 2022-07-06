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
    sorted_values = sorted(dict.values(), reverse=True) # O(n * log(n)) Сортировка значений словаря
    sorted_dict = {}                                    # O(1)

    for i in sorted_values:                             # O(n)
        for j in dict.keys():                           # O(n) + O(1)
            if dict[j] == i:                            # O(1)
                sorted_dict[j] = dict[j]                # O(1)
                break
    return list(sorted_dict.items())[0:3]               # O(1) + O(len(dict)) + (O[0:3] => O(1))
    # Общая сложность: O(n * log(n)) + O(n**2) = O(n**2)

print(three_largest_profit_1(companies))


# Решение 2:
def three_largest_profit_2(dict):
    sorted_keys = sorted(dict, key=dict.get, reverse=True) # O(n * log(n)) Сортировка ключей по их значениям в порядке убывания
    sorted_dict = {}                        # O(1)

    for i in sorted_keys:                   # O(n)
        sorted_dict[i] = dict[i]            # O(1)

    return list(sorted_dict.items())[0:3]   # (O(1) + O(len(dict)) + O[0:3]) => O(1)
    # Общая сложность: O(n * log(n)) + O(n) = O(n * log(n))

print(three_largest_profit_2(companies))


# Решение 3:
def three_largest_profit_3(dict):
    largest_profit = {}                                                       # O(1)
    count = 0                                                                 # O(1)

    for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True): # O(n) + O(n * log(n))
        if count < 3:                                                         # O(len(count))
            largest_profit.setdefault(k, v)                                   # O(1)
        count += 1                                                            # O(1)

    return largest_profit                                                     # O(1)
    # Общая сложность: O(n * log(n))

print(three_largest_profit_3(companies))

"""
Решения №2 и 3 самые эффективные из представленных выше.

"""

