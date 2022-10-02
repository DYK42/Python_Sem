# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


number = int(input('Введите целое число: '))

l = []
l2 = []

for i in range(number + 1):
    if i < 2:
        l.append(i)
        l2.append(i)
    else:
        l.append(l[i - 1] + l[i - 2])
        l2.append(l2[i - 2] - l2[i - 1])

l2.reverse()
l2.pop()

result = l2 + l

print(result)
