# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def get_multiplication_numbers(num):
    l = []
    temp = 1
    for i in range(1, num + 1):
        l.append(i * temp)
        temp *= i
    return l

number = int(input('Введите целое число: '))
print(f'Набор произведений чисел {number} будет: {get_multiplication_numbers(number)}')