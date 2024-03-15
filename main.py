from tkinter import *
from algorithm.play_game import Game
from data.player import WhoPlayFirst
from data.alg import UsingAlgorithm


def on_click_exit():
    root.destroy()


def about(src):
    def close_about():
        about_fake_button.destroy()

    about_fake_button = Button(root, width=800, height=600, command=close_about, border=0, relief='sunken')
    if src == "main":
        about_fake_button.config(image=Assets.main_about_preview_img)
    else:
        about_fake_button.config(image=Assets.main_about_preview_img)
    about_fake_button.place(x=-1.5, y=-1.5)


def game_menu(turn, mode, start_score):
    play = Game(turn, mode, start_score, root)

    def play_game(mult):
        def check_game_state():
            if gm_sc >= 1000:
                if hm_sc < ai_sc:
                    finish_menu("human", hm_sc, gm_sc, ai_sc)
                elif hm_sc > ai_sc:
                    finish_menu("ai", hm_sc, gm_sc, ai_sc)
                else:
                    finish_menu("draw", hm_sc, gm_sc, ai_sc)
                destroy()
                return False
            else:
                print(hm_sc, gm_sc, ai_sc)
                print("its okey")
                return True

        def update_game_stats():
            human_score.config(text=f"{hm_sc}")
            ai_score.config(text=f"{ai_sc}")
            game_score.config(text=f"{gm_sc}")

        def destroy():
            human_score.destroy()
            game_score.destroy()
            ai_score.destroy()
            info_bar.destroy()
            x2_button.destroy()
            x3_button.destroy()

        if mult is None:
            play.ai_turn()
            gm_sc, hm_sc, ai_sc = play.get_data("ai")
            update_game_stats()
            background.create_image(0, 0, image=Assets.in_game_human_bg, anchor=NW)

        else:
            if turn == "human":
                play.human_turn(mult)
                gm_sc, hm_sc, ai_sc = play.get_data("human")
                update_game_stats()
                if check_game_state():
                    ai_img = background.create_image(0, 0, image=Assets.in_game_ai_bg, anchor=NW)
                    play.ai_turn()
                    gm_sc, hm_sc, ai_sc = play.get_data("ai")
                    update_game_stats()
                    check_game_state()
                    background.delete(ai_img)
            else:
                ai_img = background.create_image(0, 0, image=Assets.in_game_ai_bg, anchor=NW)
                play.ai_turn()
                gm_sc, hm_sc, ai_sc = play.get_data("ai")
                update_game_stats()
                background.delete(ai_img)
                if check_game_state():
                    play.human_turn(mult)
                    gm_sc, hm_sc, ai_sc = play.get_data("human")
                    update_game_stats()
                    check_game_state()

    info_bar = Canvas(root, width=400, height=64, highlightthickness=0, border=0)
    info_bar.create_image(0, 0, image=Assets.in_game_window, anchor=NW)

    info_bar.place(x=200, y=264)

    human_score = Label(text="0", font=('Terminal', 23, 'bold'), justify="center", width=2, background="white")
    game_score = Label(text=f"{start_score}", font=('Terminal', 23, 'bold'), justify="center", width=4,
                       background="white")
    ai_score = Label(text="0", font=('Terminal', 23, 'bold'), justify="center", width=2, background="white")

    human_score.place(x=224, y=278)
    game_score.place(x=350, y=278)
    ai_score.place(x=520, y=278)

    x3_button = Button(root, image=Assets.in_game_x3, border=0, command=lambda: play_game(3))  # finish("human")
    x2_button = Button(root, image=Assets.in_game_x2, border=0, command=lambda: play_game(2))  # finish("ai")

    x3_button.place(x=412, y=349)
    x2_button.place(x=286, y=349)

    if turn == 'human':
        background.create_image(0, 0, image=Assets.in_game_human_bg, anchor=NW)
    else:
        background.create_image(0, 0, image=Assets.in_game_ai_bg, anchor=NW)
        play_game(None)
    print(turn, mode, start_score)


def finish_menu(mode, hum_sc, game_sc, ai_sc):
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
        bg_img = Assets.final_victory_bg_img
    elif mode == "ai":
        bg_img = Assets.final_defeat_bg_img
    else:
        bg_img = Assets.final_draw_bg_img

    background.create_image(0, 0, image=bg_img, anchor=NW)
    background.create_text(150, 288, text=f"{game_sc}", font=('Terminal', 23, 'bold'), justify="center",
                           width=200, anchor=NW)
    background.create_text(150, 363, text=f"{hum_sc} : {ai_sc}", font=('Terminal', 23, 'bold'), justify="center",
                           width=200, anchor=NW)

    exit_button = Button(root, image=Assets.final_exit_img, border=0, command=lambda: on_click_exit())
    start_again_button = Button(root, image=Assets.final_start_img, border=0, command=lambda: to_preset_menu())
    menu_bar = Button(root, image=Assets.final_menu_img, border=0, command=lambda: to_main())

    start_again_button.place(x=500, y=270)
    menu_bar.place(x=500, y=330)
    exit_button.place(x=500, y=390)


def preset_menu():
    first_player = WhoPlayFirst()
    used_algorithm = UsingAlgorithm()
    start_num = 7

    def modify(operator):
        nonlocal start_num
        if operator == '+':
            if start_num < 15:
                start_num += 1
        else:
            if start_num > 5:
                start_num -= 1
        start_on.config(text=f"{start_num}")

    def check_rules():
        player_state = first_player.current_player()
        alg_state = used_algorithm.current_alg()
        if player_state is not None and alg_state is not None:
            start_button.destroy()
            alg_button.destroy()
            who_starts_button.destroy()
            input_box.destroy()
            start_on.destroy()
            plus_button.destroy()
            minus_button.destroy()
            about_button.destroy()
            game_menu(player_state, alg_state, start_num)
        else:
            pass

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

    start_button = Button(root, image=Assets.main_menu_start_img, border=0, command=lambda: check_rules())
    alg_button = Button(root, image=Assets.preset_algorithm_img, border=0, command=lambda: change_alg())
    who_starts_button = Button(root, image=Assets.preset_who_starts_img, border=0, command=lambda: change_player())
    about_button = Button(root, image=Assets.main_menu_about_img, border=0, background='white',
                          activebackground='white', command=lambda: about("preset"))
    plus_button = Button(root, image=Assets.preset_plus, border=0, command=lambda: modify('+'))
    minus_button = Button(root, image=Assets.preset_minus, border=0, command=lambda: modify('-'))

    input_box = Canvas(root, width=76, height=50, highlightthickness=0)
    input_box.create_image(0, 0, image=Assets.preset_number_img, anchor=NW)
    start_on = Label(text=f"{start_num}", font=('Terminal', 23, 'bold'), justify="center", width=2, background="white")

    start_button.place(x=275, y=263)
    alg_button.place(x=507, y=349)
    who_starts_button.place(x=145, y=349)
    about_button.place(x=375, y=485)
    input_box.place(x=362, y=350)

    minus_button.place(x=303, y=349)
    plus_button.place(x=445, y=349)

    start_on.place(x=370, y=358)


def main_menu():
    def to_preset_menu():
        background.create_image(0, 0, image=Assets.preset_back_img, anchor=NW)
        start_button.destroy()
        exit_button.destroy()
        about_button.destroy()
        preset_menu()

    background.create_image(0, 0, image=Assets.main_menu_bg_img, anchor=NW)
    start_button = Button(root, image=Assets.main_menu_start_img, border=0, command=lambda: to_preset_menu())
    exit_button = Button(root, image=Assets.main_menu_exit_img, border=0, command=lambda: on_click_exit())
    about_button = Button(root, image=Assets.main_menu_about_img, border=0, background='white',
                          activebackground='white', command=lambda: about("main"))

    start_button.place(x=275, y=263)
    exit_button.place(x=300, y=350)
    about_button.place(x=375, y=485)


# Main but not def
root = Tk()
root.wm_attributes('-transparentcolor', 'green')
root.title('K36 GAMES')
root.geometry('800x600')
root.resizable(width=False, height=False)
from data.assets import LoadAssets as Assets

background = Canvas(root, width=800, height=600)
background.pack()
main_menu()
root.mainloop()
