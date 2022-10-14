import csv

file_name = ''


def init(name):
    global file_name
    file_name = f'{name}.csv'


def write_to_file(users, columns):
    with open(file_name, "w", newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(users)
