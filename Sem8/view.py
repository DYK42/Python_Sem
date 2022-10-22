import variables


def get_task():
    return int(input('\n1) сгенерировать базу данных сотрудников'
                     '\n2) просмотреть список сотрудников '
                     '\n3) получить информацию о сотруднике'
                     '\n4) изменить информацию о сотруднике'
                     '\n5) удалить информацию о сотруднике'
                     '\n6) добавить нового сотрудника'
                     '\n7) выход'
                     '\nЧто желаете: '))


def end():
    print('Завершение программы.')


def error():
    print('Команда не определена!')


def get_worker_id():
    return int(input('Введите ID сотрудника: '))


def get_new_name():
    return input('Введите имя и фамилию сотрудника: ')


def get_new_birth_day():
    return input('Введите день рождения сотрудника: ')

def get_new_phone():
    return input('Введите телефон сотрудника: ')


def get_new_position():
    for i, x in enumerate(variables.positions):
        print(f'{i}: {x}')
    return input('Введите цифру должности сотрудника: ')
