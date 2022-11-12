# '5x^3 - 4x^2 - x + 10 = 0'
def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = pol.replace('^', '')
    pol = pol.replace('**', '')
    pol = pol.replace('+', ' + ')
    pol = pol.replace('-', ' - ')
    pol = pol.split(' ')
    pol = [char.split(' ') for char in pol]
    # print(pol)
    for i, x in enumerate(pol):
        if '+' in x or '' in x:
            pol.remove(x)
        if '-' in x:
            pol[i][0] = pol[i][0] + pol[i + 1][0]
            pol.remove(pol[i + 1])
    # print(pol)
    for i in pol:
        if i[0][0] == 'x':
            i.insert(0, 1)
        if len(i) == 1:
            if str(i[0]).find('x') >= 0:
                if str(i[0][-1]) == 'x':
                    i.append(1)
                else:
                    i.append(i[0][-1])
                    i[0] = i[0][:-1]
            else:
                i.append(0)
    # print(pol)
    for j in pol:
        for i, x in enumerate(j):
            m = str(x)
            if m.find('x') >= 0:
                temp = m.replace('x', '')
                if temp == '-':
                    temp += '1'
                j[i] = int(temp)
            else:
                j[i] = int(x)
    # print(pol)
    return pol


def sum_polynom(l, l2):
    i = 0
    j = 0
    sum = 0
    result = []
    if len(l2) > len(l):
        l, l2 = l2, l
    while i < len(l) and j < len(l2):
        if int(l[i][1]) == int(l2[j][1]):
            sum = l[i][0] + l2[j][0]
            if sum != 0:
                result.append([sum, l[i][1]])
            i = i + 1
            j = j + 1
        elif l[i][1] > l2[j][1]:
            result.append((l[i]))
            i = i + 1
        elif l[i][1] < l2[j][1]:
            result.append((l2[j]))
            j = j + 1
    # print(result)
    return result


def get_polynom(l):
    result = ''
    for x in l:
        if x[0] > 0:
            x0 = f' + {x[0]}'
        else:
            x0 = f' - {-1 * x[0]}'
        if x[1] > 1:
            x1 = f'x^{x[1]}'
        elif x[1] > 0:
            x1 = f'x'
        else:
            x1 = ''
        result += x0 + x1

    result += ' = 0'
    # print(result)
    return result


if __name__ == '__main__':
    data = '2x^2+5x-6'
    data2 = '2x^2+5x-6'
    lst = convert_pol(data)
    lst2 = convert_pol(data2)

    list_sum = sum_polynom(lst, lst2)
    s = get_polynom(list_sum)
    print(s)