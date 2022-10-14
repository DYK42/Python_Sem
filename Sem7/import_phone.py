import csv

file_name = ''


def init(name):
    global file_name
    file_name = name


def read_file(col):
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            txt = ''
            for x in col:
                txt += f"{row[x]} "
            print(txt)
