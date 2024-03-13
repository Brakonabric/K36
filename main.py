from tkinter import *
import keyboard
from data.player import WhoPlayFirst
from data.alg import UsingAlgorithm


def button_click():
    keyboard.send("*")


def on_click_exit():
    root.destroy()


def about(mode):
    def close_about():
        about_fake_button.destroy()

    about_fake_button = Button(root, width=800, height=600, command=close_about, border=0, relief='sunken')
    if mode == "main":
        about_fake_button.config(image=Assets.main_about_preview_img)
    else:
        about_fake_button.config(image=Assets.main_about_preview_img)
    about_fake_button.place(x=-1.5, y=-1.5)


def game_menu(turn, mode, start):
    def finish(won):
        info_bar.destroy()
        x2_button.destroy()
        x3_button.destroy()
        finish_menu(won)

    if turn == 'human':
        background.create_image(0, 0, image=Assets.in_game_human_bg, anchor=NW)
    else:
        background.create_image(0, 0, image=Assets.in_game_ai_bg, anchor=NW)

    info_bar = Canvas(root, width=400, height=64, highlightthickness=0, border=0)
    info_bar.create_image(0, 0, image=Assets.in_game_window, anchor=NW)
    info_bar.place(x=200, y=264)

    x3_button = Button(root, image=Assets.in_game_x3, border=0, command=lambda: finish("human"))
    x2_button = Button(root, image=Assets.in_game_x2, border=0, command=lambda: finish("ai"))

    x3_button.place(x=412, y=349)
    x2_button.place(x=286, y=349)


def finish_menu(mode):
    def to_preset_menu():
        background.create_image(0, 0, image=Assets.preset_back_img, anchor=NW)
        start_again_button.destroy()
        exit_button.destroy()
        menu_bar.destroy()
        preset_menu()

    def to_main():
        start_again_button.destroy()
        menu_bar.destroy()
        exit_button.destroy()
        main_menu()

    if mode == "human":
        background.create_image(0, 0, image=Assets.final_victory_bg_img, anchor=NW)
    elif mode == "ai":
        background.create_image(0, 0, image=Assets.final_defeat_bg_img, anchor=NW)
    else:
        background.create_image(0, 0, image=Assets.final_draw_bg_img, anchor=NW)

    exit_button = Button(root, image=Assets.final_exit_img, border=0, command=lambda: on_click_exit())
    start_again_button = Button(root, image=Assets.final_start_img, border=0, command=lambda: to_preset_menu())
    menu_bar = Button(root, image=Assets.final_menu_img, border=0, command=lambda: to_main())

    start_again_button.place(x=500, y=270)
    menu_bar.place(x=500, y=330)
    exit_button.place(x=500, y=390)


def preset_menu():
    first_player = WhoPlayFirst()
    used_algorithm = UsingAlgorithm()

    def check_rules():
        player_state = first_player.current_player()
        alg_state = used_algorithm.current_alg()
        if player_state is not None and alg_state is not None:
            start_button.destroy()
            alg_button.destroy()
            who_starts_button.destroy()
            start_on = input_line.get()
            input_box.destroy()
            input_line.destroy()
            about_button.destroy()
            game_menu(player_state, alg_state, start_on)
        else:
            print(False)
            print(player_state)
            print(alg_state)

    def change_player():
        first_player.change_player(False)
        if first_player.current_player() == "human":
            who_starts_button.config(image=Assets.preset_human_img)
        elif first_player.current_player() == "ai":
            who_starts_button.config(image=Assets.preset_ai_img)
        else:
            return

    def change_alg():
        used_algorithm.change_alg(False)
        if used_algorithm.current_alg() == "Alfa-beta":
            alg_button.config(image=Assets.preset_alg_ab_img)
        elif used_algorithm.current_alg() == "Minimax":
            alg_button.config(image=Assets.preset_alg_mm_img)
        else:
            return

    start_button = Button(root, image=Assets.main_menu_start_img, border=0, command=check_rules)
    start_button.place(x=275, y=263)
    alg_button = Button(root, image=Assets.preset_algorithm_img, border=0, command=lambda: change_alg())
    alg_button.place(x=502, y=352)
    who_starts_button = Button(root, image=Assets.preset_who_starts_img, border=0, command=lambda: change_player())
    who_starts_button.place(x=150, y=352)
    input_box = Canvas(root, width=100, height=50, highlightthickness=0)
    input_box.create_image(0, 0, image=Assets.preset_number_img, anchor=NW)
    input_box.place(x=350, y=350)
    input_line = Entry(input_box, width=2, border=0, justify="center", font=('Terminal', 25, 'bold'))
    input_line.place(x=24, y=8)
    about_button = Button(root, image=Assets.main_menu_about_img, border=0, background='white',
                          activebackground='white', command=lambda: about("preset"))
    about_button.place(x=375, y=485)


def main_menu():
    def to_preset_menu():
        background.create_image(0, 0, image=Assets.preset_back_img, anchor=NW)
        start_button.destroy()
        exit_button.destroy()
        about_button.destroy()
        preset_menu()

    background.create_image(0, 0, image=Assets.main_menu_bg_img, anchor=NW)
    start_button = Button(root, image=Assets.main_menu_start_img, border=0, command=lambda: to_preset_menu())
    start_button.place(x=275, y=263)
    exit_button = Button(root, image=Assets.main_menu_exit_img, border=0, command=lambda: on_click_exit())
    exit_button.place(x=300, y=350)
    about_button = Button(root, image=Assets.main_menu_about_img, border=0, background='white',
                          activebackground='white', command=lambda: about("main"))
    about_button.place(x=375, y=485)


# Main but not def
root = Tk()
root.title('K36 GAMES')
root.geometry('800x600')
root.resizable(width=False, height=False)
from data.assets import LoadAssets as Assets

background = Canvas(root, width=800, height=600)
background.pack()
main_menu()
root.mainloop()
