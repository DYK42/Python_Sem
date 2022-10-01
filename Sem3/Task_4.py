# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = int(input('Введите целое число: '))

l = []


def get_binary(num):
    l.append(num % 2)
    num //= 2
    if num > 0:
        get_binary(num)
    return l


get_binary(num)
l.reverse()
result = int("".join(map(str, l)))

print(f'Десятичное число {num} в двоичном формате: {result}')
