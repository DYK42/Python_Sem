# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import os

dir = 'files'  # вернуть текущую папку
txt_files = [file for file in os.listdir(dir) if file.endswith(".txt")]  # список всех .txt файлов

# print(txt_files)

result = {}  # пустой словарь с результатом сложения полиномов.

for txt_file in txt_files:
    with open(f'{dir}\\{txt_file}', encoding='utf-8') as data:
        polynom = filter(lambda x: x not in ('+', '=', '0'), data.read().split())
    # print(polynom)
    for term in polynom:
        if 'x^' in term:
            ratio, power = map(lambda x: int(x) if x else 1, term.split('x^'))
            result[power] = result.get(power, 0) + ratio
        elif 'x' in term:
            ratio, _ = map(lambda x: int(x) if x else 1, term.split('x'))
            result[1] = result.get(1, 0) + ratio
        else:
            result[0] = result.get(0, 0) + int(term)

# print(result)

result = sorted(result.items(), reverse=True)
# print(result)
terms = []
for power, ratio in result:
    ratio = ratio if power == 0 else '' if ratio == 1 else ratio
    power = 'x' if power == 1 else '' if power == 0 else f'x^{power}'
    term = f'{ratio}{power}'

    terms.append(term)

# print(terms)
sum_polynom = ' + '.join(terms) + ' = 0'
print(sum_polynom)
