
def get_input(mode = 0):
    match mode:
        case 0:
            value = int(input('Введите целое число: '))
            return value
        case 1:
            value = float(input('Введите дробное число: '))
            return value
        case 2:
            value = input('Введите текст: ')
            return value
        case _:
            print('Настройка не задана!')
