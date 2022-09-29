# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11
import math


def get_sum_number(num):
    sum = 0
    a = int(num)
    b = num - a
    # print(f'a = {a}; b = {b}')

    while a > 1:
        sum += a % 10
        a = a // 10

    while b > 0:
        sum += int((b * 10) % 10)
        b = round((b * 10) - int(b * 10), 2)
        # print(b)
    return sum

number = float(input('Введите вещественное число: '))
print(f'Сумма чисел вещественного числа {number} равна: {get_sum_number(number)}')