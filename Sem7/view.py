def get_task():
    return int(input('1) cохранить телефонный справочник в файл\n2) загрузить данные из файла телефонного '
                     'справочника\nЧто желаете: '))


def get_name_export():
    name = input('Под каким именем сохранить: ')
    return name


def get_name_import():
    name = input('Из какого файла брать данные: ')
    return name


def get_size():
    size = int(input('Каким размером: '))
    return size
