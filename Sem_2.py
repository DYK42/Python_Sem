
# num = int(input('Введите целое число: '))
# l = []
# number = 1
#
# for i in range(num):
#     l.append(number)
#     number *= -3
# print(l)

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# d = {a: 3 * a + 1 for a in range(1, num + 1)}
# print(d)

# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

str_1 = input('str_1: ')
str_2 = input('str_2: ')
print(str.count(str_1, str_2))

print(str_1.count(str_2))

inkrement = 0
for i in range(len(str_1)):
    if str_2 in str_1[i: i + len(str_2)]:
        inkrement += 1

print(inkrement)