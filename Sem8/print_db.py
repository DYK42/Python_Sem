import sqlite3
import variables
from logger import LOG

path = variables.path
name = variables.name

conn = sqlite3.connect(f'{path}/{name}')


@LOG
def print_table():
    '''Вывод списка сотрудников компании в консоль'''
    global conn
    cur = conn.cursor()
    cur.execute('SELECT workers_id, first_name, last_name FROM workers')
    rows = cur.fetchall()
    for row in rows:
        print(*row)


@LOG
def print_worker(num):
    '''Вывод полной информации о сотруднике компании по ID в консоль'''
    if num <=0  or num >= variables.workers:
        print('Сотрудник с таким ID не определен!')
    else:
        global conn
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM workers WHERE workers_id = {num}')
        rows = list(cur.fetchall())
        cur.execute(f'SELECT position_id, hire_date FROM workers_post WHERE workers_id = {num}')
        rows += list(cur.fetchall())
        result = []
        for i, row in enumerate(rows):
            row = list(row)
            if i > 0:
                row[0] = variables.positions[int(row[0])]
            result += row
        # print(*variables.columns_workers)
        print(*result)


if __name__ == '__main__':
    # print_table()
    print_worker(6)
