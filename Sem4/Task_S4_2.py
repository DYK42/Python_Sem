# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import my_func as mf


def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors


num = mf.get_input()
if num is not None:
    lst = factorize(num)
    print(f'Список простых множителей числа {num} состоит из {lst}')
