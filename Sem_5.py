# def is_prime(N):
#     if N in (2, 3):
#         return True
#     div = 3
#     while div <= N ** (1 / 2):
#         if N % div == 0:
#             return False
#             div += 1
#         else:
#             return True
#
#
# if __name__ == '__main__':
#     N = int(input('Введите число: '))
#     prime_div = []
#     div = 2
#     while N != 1:
#         # print(N)
#         if is_prime(div) and N % div == 0:
#             prime_div.append(div)
#             N //= div
#             div = 2
#         else:
#             div += 1
#
# print(prime_div)

# Задана натуральная степень k. Сформировать
# случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import numpy as np
from random import randint
from sympy import Symbol, expand

k = randint(2, 5)


def get_ratios(k):
    ratios = [randint(0, 100) for i in range(k + 1)]
    return ratios


#ratios = get_ratios(k)
ratios=[4,12,0]
print(ratios)
p = np.poly1d(ratios)
print(p)
x = Symbol('x')

with open('Polynomial.txt', 'w') as data:
    data.write(str(expand(p(x))).replace('**', '^')+" = 0")
