# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

num = int(input('Введите размер списка: '))
l = list(range(1, num + 1))
print(l)

first = 0
second = len(l) - 1
result = []

while first <= second:
    result.append(l[first] * l[second])
    first += 1
    second -= 1

print(result)
