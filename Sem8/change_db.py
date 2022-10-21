import datetime
import sqlite3
import variables
from logger import LOG

path = variables.path
name = variables.name

conn = sqlite3.connect(f'{path}/{name}')


@LOG
def change_name(num, txt):
    '''Изменение имени сотрудника компании по ID'''
    global conn
    cur = conn.cursor()
    lst = txt.split()
    cur.execute(f'UPDATE workers SET first_name = "{lst[0]}" WHERE workers_id = {num}')
    if len(lst) > 1:
        cur.execute(f'UPDATE workers SET last_name = "{lst[1]}" WHERE workers_id = {num}')
    conn.commit()

def delete_by_id(num):
    '''Удаление из базы данных сотрудника компании по ID'''
    global conn
    cur = conn.cursor()
    cur.execute(f'DELETE FROM workers WHERE workers_id = {num}')
    cur.execute(f'DELETE FROM workers_post WHERE workers_id = {num}')
    conn.commit()

@LOG
def add_name(txt, pos, bday, phone):
    '''Добавление нового сотрудника компании'''
    global conn
    cur = conn.cursor()
    lst = txt.split()
    cur.execute('SELECT workers_id FROM workers')
    num = cur.fetchall()
    # print(max(num))
    # print(int(max(num)[0]))
    id = int(max(num)[0]) + 1
    print(id)
    cur.execute("INSERT INTO workers VALUES(?, ?, ?, ?, ?);", (id, lst[0], lst[1], bday, phone))
    cur.execute(f"INSERT INTO workers_post VALUES(?, ?, ?);", (id, pos, datetime.datetime.now()))
    conn.commit()

if __name__ == '__main__':
    add_name('jjjj jjjjjjj', 4, datetime.datetime.now(), 555555555)