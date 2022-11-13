import view
import controller


def start():
    while True:
        task = view.get_task()
        if 0 < task < 5:
            if task != 4:
                controller.button_click(task)
            else:
                view.end()
                break
        else:
            view.error()
            view.end()
            break
