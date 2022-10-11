# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

import random

lst = [random.randrange(0, 10) for i in range(10)]
print(lst)

unique = [x for x in lst if lst.count(x) < 2]
print(f'Cписок уникальных элементов заданной последовательности: {unique}')

no_duplicate = list(set(lst))
print(f'Cписок без дубликатов заданной последовательности: {no_duplicate}')

duplicate = list(set(filter(lambda x: lst.count(x) > 1, lst)))
print(f'Cписок дубликатов заданной последовательности: {duplicate}')
