import view
import export_phone
import import_phone
import generating
import os


def button_click():
    task = view.get_task()
    match task:
        case 1:
            size = view.get_size()
            name = view.get_name_export()
            if not name:
                name = 'phone_directory'
            export_phone.init(name)
            export_phone.write_to_file(generating.get_phone_directory(size), generating.columns)
        case 2:
            name = view.get_name_import()
            if not name:
                name = 'phone_directory.csv'
            if not os.path.exists(name):
                print("Указанный файл не существует!")
            else:
                import_phone.init(name)
                import_phone.read_file(generating.columns)
        case _:
            print('Операция не определена!')


if __name__ == '__main__':
    button_click()
