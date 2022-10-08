# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1, 10))


# рисует и обновляет решетку
def draw_board(lst):
    print('-------------')
    for i in range(3):
        print(f'| {lst[0 + i * 3]} | {lst[1 + i * 3]} | {lst[2 + i * 3]} |')
        print('-------------')


# Ввод и запись Х или 0 в ячейку
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(f'Куда поставим {player_token}? ')
        if player_answer.isdigit():
            player_answer = int(player_answer)
        else:
            print("Некорректный ввод. Вы ввели не целое число!")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) in "XO":
                print("Эта клеточка уже занята")
            else:
                print(player_answer)
                board[player_answer - 1] = player_token
                valid = True
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


# Проверяет на наличие выигрышной комбинации Х или 0
def check_win(lst):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if lst[each[0]] == lst[each[1]] == lst[each[2]]:
            return lst[each[0]]
    return False


# сама Игра
def main(lst):
    counter = 0
    while counter < 9:
        draw_board(lst)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('0')
        counter += 1
        if counter > 4:
            tmp = check_win(lst)
            if tmp:
                print(f'Игрок <{tmp}>, выиграл!')
                break
        if counter == 9:
            print('Ничья!')
            break
    draw_board(lst)


main(board)
