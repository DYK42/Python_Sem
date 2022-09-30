# 4.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

pos = []
file = open('file.txt', 'r')
pos = file.read().split()
print(pos)

num = int(input('Введите целое число: '))
l = [random.randrange(-num, num + 1) for i in range(num)]
print(l)

multi = 1
for i in pos:
    j = int(i)
    if j < len(l):
        print(f'i = {j}; value = {l[j]}')
        multi *= l[j]

print(f'Произведение элементов равно: {multi}')
