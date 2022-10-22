import view
import create_db
import print_db
import change_db
import os


def button_click(task):
    match task:
        case 1:
            create_db.create_db()
        case 2:
            print_db.print_table()
        case 3:
            id = view.get_worker_id()
            print_db.print_worker(id)
        case 4:
            id = view.get_worker_id()
            txt = view.get_new_name()
            change_db.change_name(id, txt)
        case 5:
            id = view.get_worker_id()
            change_db.delete_by_id(id)
        case 6:
            txt = view.get_new_name()
            pos = view.get_new_position()
            birth_day = view.get_new_birth_day()
            phone = view.get_new_phone()
            change_db.add_name(txt, pos, birth_day, phone)

