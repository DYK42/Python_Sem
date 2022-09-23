# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# def check_weekends(num):
#     if 5 < num < 8:
#         print('Да!')
#     elif 0 < num < 6:
#         print('Нет!')
#     else:
#         print('Превышает количество дней недели!')

# number = int(input('Введите целое число: '))
#check_weekends(number)

# 2
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def checkPredicate(x, y, z):
    return (not (x or y or z)) == (not x and not y and not z)

x = int(input('Введите целое число X: '))
y = int(input('Введите целое число Y: '))
z = int(input('Введите целое число Z: '))

if checkPredicate(x, y, z):
    print('Утверждение истинно!')
else:
    print('Утверждение ложно!')