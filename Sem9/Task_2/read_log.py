
def read_log():
    with open('log.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        file.close()
        print(data)
        return data


if __name__ == '__main__':
    read_log()