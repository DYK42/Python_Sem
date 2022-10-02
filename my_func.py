# if __name__ == '__main__':
import random
import string


def get_input(mode='i'):
    match mode:
        case 'i':
            return int(input('Введите целое число: '))
        case 'f':
            return float(input('Введите вещественное число: '))
        case 's':
            return input('Введите текст: ')
        case _:
            print('Настройка не задана!')


def get_list(mode='i'):
    num = int(input('Введите размер списка: '))
    match mode:
        case 'i':
            return list(range(num))
        case 'f':
            return [round(random.random() + random.randint(0, 100), 2) for i in range(num)]
        case 's':
            return [''.join(random.choice(string.ascii_letters) for i in range(random.randrange(0, 5))) for j in
                    range(num)]
        case _:
            print('Настройка не задана!')
