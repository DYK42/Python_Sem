# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.


import random

num = int(input('Введите размер списка: '))
lst = [random.randrange(1, 10) for i in range(num)]

result = [elem for elem in lst if lst.count(elem) == 1]

print(lst)
print(f'Список неповторяющихся элементов исходной последовательности: {result}')
