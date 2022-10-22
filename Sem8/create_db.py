from datetime import datetime, timedelta
import sqlite3
import os
import random
import variables
from logger import LOG


@LOG
def create_db():
    '''Создание базы данных сотрудников компании '''
    path = variables.path
    name = variables.name

    if not os.path.exists(path):
        os.mkdir(path)

    conn = sqlite3.connect(f'{path}/{name}')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS workers(
                workers_id INT PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                birth_day DATE,
                phone INT);
                """)

    cur.execute("""CREATE TABLE IF NOT EXISTS positions(
                position_id INT PRIMARY KEY,
                position TEXT,
                salary REAL);
                """)

    cur.execute('DROP table if exists workers_post')
    cur.execute("""CREATE TABLE IF NOT EXISTS workers_post(
                workers_id INT,
                position_id INT,
                hire_date DATE,
                FOREIGN KEY (workers_id) REFERENCES workers(workers_id),
                FOREIGN KEY (position_id) REFERENCES position(position_id));
                """)

    def get_random_datetime(min_year=1950, max_year=datetime.now().year):
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year - 10
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random.random()

    def get_workers(num, col):
        lst = []
        for x in range(num):
            temp = []
            for a in col:
                if 'id' in a:
                    temp.append(x)
                elif 'birth_day' in a:
                    temp.append(get_random_datetime(1950, 1990).strftime("%d/%m/%Y"))
                elif 'phone' in a:
                    temp.append(random.randrange(100000, 1000000))
                elif 'first_name' in a:
                    temp.append(variables.first_name[x])
                elif 'last_name' in a:
                    temp.append(variables.last_name[x])
            lst.append(temp)
        return lst

    def get_positions(num, col):
        lst = []
        salary = [random.randrange(100000, 1000000) for x in range(num)]
        salary.sort(reverse=True)
        for x in range(num):
            temp = []
            for a in col:
                if 'id' in a:
                    temp.append(x)
                elif 'position' in a:
                    temp.append(variables.positions[x])
                elif 'salary' in a:
                    temp.append(salary[x])

            lst.append(temp)
        return lst

    def get_workers_by_positions(num, col):
        lst = []
        for x in range(num):
            temp = []
            for a in col:
                if 'workers' in a:
                    temp.append(x)
                elif 'position' in a:
                    temp.append(random.randrange(0, len(variables.positions)))
                else:
                    temp.append(get_random_datetime(1990).strftime("%d/%m/%Y"))

            lst.append(temp)
        return lst

    lst = get_workers(variables.workers, variables.columns_workers)
    cur.executemany("INSERT OR IGNORE INTO workers VALUES(?, ?, ?, ?, ?);", lst)

    pos = get_positions(len(variables.positions), variables.columns_position)
    cur.executemany("INSERT OR IGNORE INTO positions VALUES(?, ?, ?);", pos)

    worker_pos = get_workers_by_positions(variables.workers, variables.columns_work_position)
    cur.executemany("INSERT INTO workers_post VALUES(?, ?, ?);", worker_pos)

    conn.commit()
    conn.close()
