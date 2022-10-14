import view
import export_phone
import import_phone
import generating
import os


def button_click():
    task = view.get_task()
    match task:
        case 1:
            size = int(input('Каким размером: '))
            name = input('Под каким именем сохранить: ')
            if not name:
                name = 'phone_directory'
            export_phone.init(name)
            export_phone.write_to_file(generating.get_phone_directory(size), generating.columns)
        case 2:
            name = input('Из какого файла брать данные: ')
            # if not name:
            #     name = 'phone_directory'
            if not os.path.exists(name):
                print("Указанный файл не существует!")
            else:
                import_phone.init(name)
                import_phone.read_file(generating.columns)
        case _:
            print('Операция не определена!')


if __name__ == '__main__':
    button_click()
