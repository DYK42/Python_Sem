# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random

num = int(input('Введите размер списка: '))
l = [round(random.random() + random.randint(0, 100), 2) for i in range(num)]
print(l)

max = 0.0
min = 1.0

for elem in l:
    num = round(elem - int(elem), 2)
    print(num)
    if max < num:
        max = num
    if min > num:
        min = num

print(f'Разница между максимальным {max} и минимальным {min} значениями дробной части элементов равна: {round(max - min, 2)}')
