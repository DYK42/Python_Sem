import random

import variables as vr
import check_game
import create_window


def game_command(button_press):
    # print(f'Нажата кнопка № {button_press}')
    if vr.counter < 9:
        if check_game.check_value(button_press):
            if not check_game.take_value(button_press):
                if vr.game_mode:
                    while True:
                        nbr = random.randrange(0, 9)
                        print(nbr)
                        if check_game.check_value(nbr):
                            check_game.take_value(nbr)
                            break
    else:
        print(f'Игра завершена! Победой "{check_game.check_win()}"')


def ui_command(button_press):
    # print(f'Нажата кнопка {vr.but_ui[button_press - 10]}')
    match button_press:
        case 10:
            vr.game_mode = 0
            vr.btn_ui[0]['fg'] = 'yellow'
            vr.btn_ui[1]['fg'] = 'SystemButtonText'
        case 11:
            vr.game_mode = 1
            vr.btn_ui[1]['fg'] = 'yellow'
            vr.btn_ui[0]['fg'] = 'SystemButtonText'
        case 12:
            create_window.reset_window()
