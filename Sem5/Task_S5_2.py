# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы
# забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

mode = int(input('Выберите режим игры (1 - человек/человек / 2 - человек/бот): '))

total = 2021
max_count = 28
num_winner_step = max_count + 1
num_first_step = total - ((total // num_winner_step) * num_winner_step)

opponent = random.randrange(0, 100) % 2
print(opponent)
if opponent:
    print('Первый ход за оппонентом')
else:
    print('Первый ход мой!')

num = 0
count = 0


def check_input_int(num):
    if not num.isdigit():
        print('Введено не целое число!')
        return False
    else:
        return True


while total > 0:
    if opponent:
        match mode:
            case 1:
                s = input(
                    f'Оппонент. Введите количество конфет, которые хотите забрать со стола. Максимум 28 конфет. Осталось {total}: ')
                if not check_input_int(s):
                    continue
                else:
                    num = int(s)
                if num > max_count:
                    num = max_count
            case _:
                if not count:
                    num = num_first_step
                elif not count % 2:
                    num = num_winner_step - num
                else:
                    num = random.randrange(1, max_count + 1)
        print(f'opponent: {total} - {num} = {total - num}')
    else:
        if not count:
            num = num_first_step
        elif not count % 2:
            num = num_winner_step - num
        else:
            s = input(
                f'Введите количество конфет, которые хотите забрать со стола. Максимум 28 конфет. Осталось {total}: ')
            if not check_input_int(s):
                continue
            else:
                num = int(s)
            if num > max_count:
                num = max_count
        print(f'I: {total} - {num} = {total - num}')

    total -= num
    count += 1
    if total < 1:
        print(f'{"Оппонент" if opponent else "Я"}, Выиграл !!!')
        break
    opponent = (opponent + 1) % 2
