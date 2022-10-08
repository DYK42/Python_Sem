# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# txt = 'Hello world. Hello dear friend!'
txt = input('Введите текст: ')
chars = input('Введите символы, слова содержащие которые нужно удалить: ')

lst = txt.split()
print(lst)

size = len(lst)

for i in range(size):
    count = 0
    for x in chars:
        # print(i)
        # print(f'{x} {lst[i]}')
        if x in lst[i]:
            count += 1
        else:
            break
        if count >= len(chars):
            # print(lst[i])
            lst[i] = ''
            break

print(lst)
txt = ' '.join(list(filter(lambda i: not i == '', lst)))
print(txt)
