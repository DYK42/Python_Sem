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

import re

exp = '((3 +(7-77)*10/(5+25)) *((7- 9) /3))/45 + ((((34+5)*5)+6)/78)'
# exp = input('Введите арифметическое выражение: ')
lst = re.findall(r'\d+|[()+\-*/]', exp)
print(exp)

result = 0
size = len(lst)

# print(lst)


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

while i < len(lst):
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
                    if char[-2] == '(':
                        char = char[:-2]
                    else:
                        char = char[:-1]
                        i -= 1
    if i == len(lst) - 1:
        while len(num) > 1:
            val = num[-2:]
            num = num[:-2]
            num.append(operation(char[-1], val))
            char = char[:-1]
        else:
            result = num[0]
            break
    else:
        i += 1

print('{:10}: {}'.format('Result', result))
print('{:10}: {}'.format('Eval', eval(exp)))
