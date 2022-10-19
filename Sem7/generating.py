import random
from datetime import datetime, timedelta


def get_random_datetime(min_year=1900, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year - 10
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


columns = ['id', 'first_name', 'last_name', 'birthday', 'work', 'phone']


def get_phone_directory(num):
    lst = []
    for x in range(num):
        # lst.append({'id': x, 'first_name': f'FirstName{x}', 'last_name': f'LastName{x}',
        #             'birthday': get_random_datetime().strftime("%d/%m/%Y"), 'work': f'Work{x}',
        #             'phone': [random.randrange(100000, 1000000) for i in range(random.randrange(1, 3))]})
        lst.append({a: f'{a.upper().replace("_", "")}{x}'
        if not 'phone' in a else [random.randrange(100000, 1000000)
                                  for i in range(random.randrange(1, 3))] for a in columns})
    return lst


def print_phone_directory(lst):
    for x in lst:
        print(x)


if __name__ == '__main__':
    users = get_phone_directory(10)
