from tkinter import *

import keyboard

from data.player import WhoPlayFirst
from data.alg import UsingAlgorithm


def button_click():
    keyboard.press("Enter")


def on_click_exit():
    root.destroy()


def change_player():
    FirstPlayer.change_player(False)
    if FirstPlayer.current_player() == "human":
        who_starts_button.config(image=preset_human_img)
    elif FirstPlayer.current_player() == "ai":
        who_starts_button.config(image=preset_ai_img)
    else:
        return


def change_alg():
    UseAlgorithm.change_alg(False)
    if UseAlgorithm.current_alg() == "Alfa-beta":
        alg_button.config(image=preset_alg_ab_img)
    elif UseAlgorithm.current_alg() == "Minimax":
        alg_button.config(image=preset_alg_mm_img)
    elif UseAlgorithm.current_alg() == "Heuristic evaluation":
        alg_button.config(image=preset_alg_hf_img)
    else:
        return


def about(mode):
    def close_about():
        about_fake_button.destroy()

    about_fake_button = Button(root, width=800, height=600, command=close_about, border=0, relief='sunken')
    if mode == "main":
        about_fake_button.config(image=main_about_preview_img)
    else:
        about_fake_button.config(image=main_about_preview_img)
    about_fake_button.place(x=-1.5, y=-1.5)


def game_menu(window, turn, mode, start):
    def finish(won):
        if won == "human":
            print()
        elif won == "ai":
            print()
        else:
            print()
        info_bar.destroy()
        x2_button.destroy()
        x3_button.destroy()

    if turn == 'human':
        background.create_image(0, 0, image=in_game_human_bg, anchor=NW)
    else:
        background.create_image(0, 0, image=in_game_ai_bg, anchor=NW)

    info_bar = Canvas(window, width=400, height=64, highlightthickness=0, border=0)
    info_bar.create_image(0, 0, image=in_game_window, anchor=NW)
    info_bar.place(x=200, y=264)

    x3_button = Button(window, image=in_game_x3, border=0, command=lambda: finish("human"))
    x3_button.place(x=412, y=349)
    x2_button = Button(window, image=in_game_x2, border=0, command=lambda: finish("ai"))
    x2_button.place(x=286, y=349)


def preset_menu(window):
    def check_rules():
        player_state = FirstPlayer.current_player()
        alg_state = UseAlgorithm.current_alg()
        if player_state is not None and alg_state is not None:
            start_button.destroy()
            alg_button.destroy()
            who_starts_button.destroy()
            start_on = input_line.get()
            input_box.destroy()
            input_line.destroy()
            about_button.destroy()
            game_menu(window, player_state, alg_state, start_on)
        else:
            print(False)
            print(player_state)
            print(alg_state)

    start_button = Button(window, image=main_menu_start_img, border=0, command=check_rules)
    start_button.place(x=275, y=263)
    alg_button.place(x=502, y=352)
    who_starts_button.place(x=150, y=352)
    input_box = Canvas(window, width=100, height=50, highlightthickness=0)
    input_box.create_image(0, 0, image=preset_number_img, anchor=NW)
    input_box.place(x=350, y=350)
    input_line = Entry(input_box, width=2, border=0, justify="center", font=('Terminal', 25, 'bold'))
    input_line.place(x=24, y=8)
    about_button = Button(window, image=main_menu_about_img, border=0, background='white', activebackground='white',
                          command=lambda: about("preset"))
    about_button.place(x=375, y=485)


def main_menu(window):
    def to_preset_menu():
        background.create_image(0, 0, image=preset_back_img, anchor=NW)
        start_button.destroy()
        exit_button.destroy()
        about_button.destroy()
        preset_menu(window)

    background.create_image(0, 0, image=main_menu_bg_img, anchor=NW)
    start_button = Button(window, image=main_menu_start_img, border=0, command=to_preset_menu)
    start_button.place(x=275, y=263)
    exit_button = Button(window, image=main_menu_exit_img, border=0, command=on_click_exit)
    exit_button.place(x=300, y=350)
    about_button = Button(window, image=main_menu_about_img, border=0, background='white', activebackground='white',
                          command=lambda: about("main"))
    about_button.place(x=375, y=485)


# Main but not def
FirstPlayer = WhoPlayFirst()
UseAlgorithm = UsingAlgorithm()
root = Tk()
root.title('K36 GAMES')
root.geometry('800x600')
root.resizable(width=False, height=False)

main_menu_bg_img = PhotoImage(file='assets/main/main_menu_background.png')
main_menu_start_img = PhotoImage(file='assets/main/main_menu_start.png')
main_menu_exit_img = PhotoImage(file='assets/main/main_menu_exit.png')
main_menu_about_img = PhotoImage(file='assets/main/main_menu_about.png')
main_about_preview_img = PhotoImage(file='assets/main/about_preview.png')

preset_back_img = PhotoImage(file='assets/preset/preset_background.png')
preset_number_img = PhotoImage(file='assets/preset/preset_number.png')
preset_who_starts_img = PhotoImage(file='assets/preset/preset_who_starts.png')
preset_human_img = PhotoImage(file='assets/preset/preset_who_starts_human.png')
preset_ai_img = PhotoImage(file='assets/preset/preset_who_starts_ai.png')

preset_algorithm_img = PhotoImage(file='assets/preset/preset_alg.png')
preset_alg_ab_img = PhotoImage(file='assets/preset/preset_alg_alpha_beta.png')
preset_alg_mm_img = PhotoImage(file='assets/preset/preset_alg_minimax.png')
preset_alg_hf_img = PhotoImage(file='assets/preset/preset_alg_hf.png')

in_game_human_bg = PhotoImage(file='assets/game/game_human_background.png')
in_game_ai_bg = PhotoImage(file='assets/game/game_computer_background.png')
in_game_window = PhotoImage(file='assets/game/game_window.png')
in_game_x3 = PhotoImage(file='assets/game/game_x3.png')
in_game_x2 = PhotoImage(file='assets/game/game_x2.png')

background = Canvas(root, width=800, height=600)
background.pack()
who_starts_button = Button(root, image=preset_who_starts_img, border=0, command=change_player)
alg_button = Button(root, image=preset_algorithm_img, border=0, command=change_alg)

main_menu(root)
root.mainloop()
