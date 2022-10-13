# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

from enum import Enum


class Prior(Enum):
    PLUS = 1
    MINUS = 1
    MULTI = 2
    DIV = 2
    POW = 3

exp = '(3 + 5) * ((7 - 9) / 3)'
# exp = '((12 + 23 * 2 - 43) * 31) * 10'  #   = 4650
# exp = input('Введите арифметическое выражение: ')
lst = exp.split()

print(exp)

result = 0
size = len(lst)
i = 0

while i < size:
    if not lst[i].isdigit():
        # print(f'{i} {lst[i]}')
        if len(lst[i]) > 1:
            if '(' in lst[i]:
                temp = lst[i][1:]
                lst[i] = '('
                lst.insert(i + 1, temp)
                size += 1
            if ')' in lst[i]:
                # print(lst[i])
                temp = lst[i][:-1]
                lst[i] = temp
                lst.insert(i + 1, ')')
                size += 1
    i += 1

print(lst)


def operation(op, val):
    match op:
        case '-':
            return float(val[0]) - float(val[1])
        case '+':
            return float(val[0]) + float(val[1])
        case '*':
            return float(val[0]) * float(val[1])
        case '/':
            return float(val[0]) / float(val[1])
        case '^':
            return float(val[0]) ** float(val[1])


char = []
num = []
i = 0
result = 0

while i < len(lst):
    # print(num)
    # print(char)
    if lst[i].isdigit():
        num.append(lst[i])
    else:
        match lst[i]:
            case '+':
                if len(char) > 0:
                    if char[-1] in '-*/':
                        if len(num) > 1:
                            val = num[-2:]
                            num = num[:-2]
                            num.append(operation(char[-1], val))
                            char.pop()
                            i -= 1
                        else:
                            char.append(lst[i])
                    else:
                        char.append(lst[i])
                else:
                    char.append(lst[i])
            case '-':
                if len(char) > 0:
                    if char[-1] in '+*/':
                        if len(num) > 1:
                            val = num[-2:]
                            num = num[:-2]
                            num.append(operation(char[-1], val))
                            char.pop()
                            i -= 1
                        else:
                            char.append(lst[i])
                    else:
                        char.append(lst[i])
                else:
                    char.append(lst[i])
            case '*':
                if len(char) > 0:
                    if char[-1] in '*/':
                        if len(num) > 1:
                            val = num[-2:]
                            num = num[:-2]
                            num.append(operation(char[-1], val))
                            char.pop()
                            i -= 1
                        else:
                            char.append(lst[i])
                    else:
                        char.append(lst[i])
                else:
                    char.append(lst[i])
            case '/':
                if len(char) > 0:
                    if char[-1] in '*/':
                        if len(num) > 1:
                            val = num[-2:]
                            num = num[:-2]
                            num.append(operation(char[-1], val))
                            char.pop()
                            i -= 1
                        else:
                            char.append(lst[i])
                    else:
                        char.append(lst[i])
                else:
                    char.append(lst[i])
            case '(':
                char.append(lst[i])
            case ')':
                if len(num) > 1:
                    val = num[-2:]
                    num = num[:-2]
                    num.append(operation(char[-1], val))
                    char = char[:-2]
                    # i -= 1
    # print(lst)
    # print(num)
    # print(char)
    if i == len(lst) - 1:
        while len(num) > 1:
            # print(f'{num} {len(num)}')
            # print(char)
            val = num[-2:]
            num = num[:-2]
            num.append(operation(char[-1], val))
            char = char[:-1]
        else:
            result = num[0]
            break
    else:
        i += 1
    # print(num)

# print(num)
# print(char)
print(result)
print(eval(exp))
