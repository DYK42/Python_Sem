from datetime import datetime as dt
import csv

file_name = 'log.csv'


def task_logger(data):
    time = dt.now()
    with open(file_name, "w", newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(users)

    # with open('log.csv', 'a') as file:
    #     file.write('{};pressure;{}\n'
    #                 .format(time, data))