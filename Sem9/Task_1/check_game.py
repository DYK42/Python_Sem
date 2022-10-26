import variables as vr


def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if vr.btn_game[each[0]]['text']:
            if vr.btn_game[each[0]]['text'] == vr.btn_game[each[1]]['text'] == \
                    vr.btn_game[each[2]]['text']:
                for i in range(3):
                    vr.btn_game[each[i]]['bg'] = 'blue'
                    vr.btn_game[each[i]]['fg'] = 'yellow'
                return vr.btn_game[each[0]]['text']
    return False


def check_value(button_press):
    if vr.btn_game[button_press]['text'] and vr.btn_game[button_press]['text'] in 'XO':
        print('Данное поле уже занято! Выберите другое.')
        return False
    return True


def take_value(button_press):
    token = 'X' if vr.counter % 2 else 'O'
    vr.btn_game[button_press]['text'] = token
    vr.counter += 1
    vr.btn_game[button_press]['font'] = 'Times 20'
    if vr.counter > 4:
        win_token = check_win()
        # print(win_token)
        if win_token:
            print(f'Winner! "{win_token}"')
            vr.counter = 9
            return True
        else:
            if vr.counter >= 9:
                print('Ничья!')
