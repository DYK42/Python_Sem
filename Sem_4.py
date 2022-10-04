import random

import my_func as mf

# N = int(input('N: '))
# lst = [random.randrange(N) for i in range(N)]
# print(lst)
#
# result = []
# print(lst[:(N + 1) // 2], lst[N // 2:][::-1])
#
# for el_1, el_2 in zip(lst[:(N + 1) // 2], lst[N // 2:][::-1]):
#     result.append(el_1 * el_2)
# print(result)

# def tentotwo(n):
#     if n <= 1:
#         return str(n)
#     return tentotwo(n//2) + str(n % 2)
#
# num = int(input('Введите десятичное число '))
# print(tentotwo(num))

# def fib(n):
#     if not n:
#         return 0 # n
#     if n < 0:
#         return (-1) ** (-n + 1) * fib(-n)
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# N = int(input('N: '))
# neg_fib = []
# for i in range(-N, N + 1):
#     neg_fib.append(fib(i))
#
# print(neg_fib)


k = 1
s = 0
for i in range(1000000):
    if i % 2 == 0:
        s += 4 / k
    else:
        s -= 4 / k
    k += 2

print(int(s*1000)/1000)