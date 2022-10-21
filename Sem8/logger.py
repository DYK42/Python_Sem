from datetime import datetime


def LOG(func):
    def wrapper(*args):
        func(*args)
        with open('log.csv', 'a', encoding='utf-8') as log:
            log.write(
                f'Запущена функция "{func.__name__}": {func.__doc__}. {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}\n')

    return wrapper
