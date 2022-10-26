import tkinter as tk
import variables as vr
import click_button


def create_window():
    window = tk.Tk()
    frame_game = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    frame_game.pack(fill=tk.BOTH, expand=True)

    frame_ui = tk.Frame(master=window, height=40, relief=tk.RAISED, borderwidth=1)
    frame_ui.pack(fill=tk.BOTH)

    index = 0

    for i in range(3):
        for j in range(3):
            frame_game.columnconfigure(i, weight=1, minsize=75)
            frame_game.rowconfigure(i, weight=1, minsize=60)

            frame_btn_game = tk.Frame(master=frame_game,
                                      relief=tk.RAISED,
                                      borderwidth=1)
            frame_btn_game.grid(row=i, column=j, sticky="nsew")
            vr.btn_game.append(tk.Button(master=frame_btn_game, command=lambda m=index: click_button.game_command(m)))
            vr.btn_game[index].pack(fill=tk.BOTH, expand=True)
            index += 1

        frame_btn_ui = tk.Frame(master=frame_ui, relief=tk.RAISED, borderwidth=1, bg='red', width=5)
        frame_btn_ui.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        vr.btn_ui.append(tk.Button(master=frame_btn_ui, bg='red', width=10, text=vr.but_ui[i],
                                   command=lambda m=(10 + i): click_button.ui_command(m)))
        vr.btn_ui[i].pack(fill=tk.BOTH, expand=True)
        if i < 1:
            continue
        if not vr.game_mode:
            vr.btn_ui[0]['fg'] = 'yellow'
            vr.btn_ui[1]['fg'] = 'SystemButtonText'
        else:
            vr.btn_ui[1]['fg'] = 'yellow'
            vr.btn_ui[0]['fg'] = 'SystemButtonText'

    window.mainloop()


def reset_window():
    vr.counter = 0
    for x in range(9):
        vr.btn_game[x]['bg'] = 'SystemButtonFace'
        vr.btn_game[x]['fg'] = 'SystemButtonText'
        vr.btn_game[x]['text'] = ''
