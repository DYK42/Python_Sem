# if __name__ == '__main__':
import random
import string


def get_input(mode='i'):
    value = ''
    match mode:
        case 'i':
            value = input('Введите целое число: ')
            if not value.isdigit():
                return print('Введено не целое число!')
            return int(value)
        case 'f':
            value = input('Введите вещественное число: ')
            if not value.replace('.', '', 1).isdigit():
                return print('Введено не вещественное число!')
            return float(value)
        case 's':
            return input('Введите текст: ')
        case _:
            print('Настройка не задана!')


def get_list(mode='i'):
    match mode:
        case 'i':
            num = int(input('Введите размер списка: '))
            return list(range(num))
        case 'f':
            num = int(input('Введите размер списка: '))
            return [round(random.random() + random.randint(0, 100), 2) for i in range(num)]
        case 's':
            num = int(input('Введите размер списка: '))
            return [''.join(random.choice(string.ascii_letters) for i in range(random.randrange(0, 5))) for j in
                    range(num)]
        case 'h':
            l = []
            while True:
                value = input('Введите элемент списка (Пустое значение для выхода): ')
                if value.isdigit():
                    l.append(int(value))
                elif value.replace('.', '', 1).isdigit():
                    l.append(float(value))
                else:
                    if not value:
                        return l
                    else:
                        l.append(value)
        case _:
            print('Настройка не задана!')




