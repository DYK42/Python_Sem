# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os
import sys

path = 'Files'
name_input = 'file_input.txt'
name_output = 'file_output.txt'

if not os.path.exists(path):
    os.mkdir(path)

with open(f'{path}\\{name_input}', 'r', encoding='utf-8') as data:
    txt = data.read()

rle = ''
prev_char = ''
count = 1

for char in txt:
    if char != prev_char:
        if prev_char:
            rle += str(count) + prev_char
        count = 1
        prev_char = char
    else:
        count += 1
rle += str(count) + prev_char

print(f'size: {len(txt)} > {txt}')
print(f'size: {len(rle)} > {rle}')

decode = ''
count = ''

for char in rle:
    if char.isdigit():
        count += char
    else:
        decode += char * int(count)
        count = ''

print(f'size: {len(decode)} > {decode}')

with open(f'{path}\\{name_output}', 'w', encoding='utf-8') as data:
    txt = data.write(decode)
