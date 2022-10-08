# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def degree(n, s='x'):
    res = ''
    if n > 0:
        if n < 2:
            res = s
        else:
            res = f'{s}^{n}'
    return res


k = int(input('Введите натуральную степень: '))

if k < 2:
    print(f'Натуральная степень {k} не удовлетворяет условию!')
else:
    lst = [random.randrange(0, 100) for i in range(6)]
    print(lst)
    s1 = f'{lst[0]}{degree(k)} + {lst[1]}{degree(k - 1)} + {lst[2]} = 0'
    s2 = f'{lst[3]}{degree(k)} + {lst[4]} = 0'
    s3 = f'{lst[5]}{degree(k)} = 0'

    file = open('file.txt', 'w')
    file.write(s1 + '\n')
    file.write(s2 + '\n')
    file.write(s3 + '\n')
    file.close()
