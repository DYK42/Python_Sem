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

# def checkPredicate(x, y, z):
#     return (not (x or y or z)) == (not x and not y and not z)
#
# x = int(input('Введите целое число X: '))
# y = int(input('Введите целое число Y: '))
# z = int(input('Введите целое число Z: '))
#
# if checkPredicate(x, y, z):
#     print('Утверждение истинно!')
# else:
#     print('Утверждение ложно!')

# 3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# def get_sector(x, y):
#     if x != 0 and y != 0:
#         if x > 0 and y > 0:
#             print('Четверть № 1')
#         elif x < 0 and y > 0:
#             print('Четверть № 2')
#         elif x < 0 and y < 0:
#             print('Четверть № 3')
#         elif x > 0 and y < 0:
#             print('Четверть № 4')
#     else:
#         if x != 0 and y == 0:
#             print('Ось Y')
#         elif x == 0 and y != 0:
#             print('Ось X')
#         else:
#             print('Точка начала координат')
#
# x = int(input('Введите координату X: '))
# y = int(input('Введите координату Y: '))
# get_sector(x, y)

# 4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

# def get_range_sector(num):
#     if 0 < num < 5:
#         match num:
#             case 1:
#                 print('Диапазон (+x; +y)')
#             case 2:
#                 print('Диапазон (-x; +y)')
#             case 3:
#                 print('Диапазон (-x; -y)')
#             case 4:
#                 print('Диапазон (+x; -y)')
#     else:
#         print("Превышение количества. Число может быть задано от 1 до 4.")
#
# number = int(input('Введите номер четверти: '))
# get_range_sector(number)

# 5
# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.


def get_length_segment(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)

def set_coordinates(num):
    l = []
    coord = ['X', 'Y']
    for i in range(num):
        while True:
            try:
                number = int(input(f"Введите координату по оси {coord[i]}: "))
                l.append(number)
                break
            except ValueError:
                print("Введите целое число!")
    return l

print("Введите координаты точки А")
a = set_coordinates(2)

print("Введите координаты точки B")
b = set_coordinates(2)

print(f"Расстояние между точками A и B равно: {format(get_length_segment(a, b), '.2f')}")