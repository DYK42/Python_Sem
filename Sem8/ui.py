import view
import controller


def start():
    while True:
        task = view.get_task()
        if 0 < task < 8:
            if task != 7:
                controller.button_click(task)
            else:
                view.end()
                break
        else:
            view.error()
            view.end()
            break
