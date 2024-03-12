from tkinter import *
from data.player import WhoPlayFirst
from data.alg import UsingAlgorithm


def button_click():
    print(+1)


def on_click_exit():
    root.destroy()


def change_player():
    FirstPlayer.change_player(False)
    if get_player() == "human":
        who_starts_button.config(image=preset_human_img)
    elif get_player() == "ai":
        who_starts_button.config(image=preset_ai_img)
    else:
        return


def get_player():
    return FirstPlayer.current_player()


def change_alg():
    UseAlgorithm.change_alg(False)
    if get_alg() == "Alfa-beta":
        alg_button.config(image=preset_alg_ab_img)
    elif get_alg() == "Minimax":
        alg_button.config(image=preset_alg_mm_img)
    elif get_alg() == "Heuristic evaluation":
        alg_button.config(image=preset_alg_hf_img)
    else:
        return


def get_alg():
    return UseAlgorithm.current_alg()


def check_rules():
    player_state = get_player()
    alg_state = get_alg()
    if player_state is not None and alg_state is not None:
        print(True)
        print(player_state)
        print(alg_state)
    else:
        print(False)
        print(player_state)
        print(alg_state)


def about_main():
    def close_about():
        about_fake_button.destroy()

    about_fake_button = Button(root,
                               image=main_about_preview_img,
                               width=800, height=600,
                               command=close_about,
                               border=0,
                               relief='sunken')
    about_fake_button.place(x=-1.5, y=-1.5)


def about_preset():
    def close_about():
        about_fake_button.destroy()

    about_fake_button = Button(root,
                               image=main_about_preview_img,
                               width=800, height=600,
                               command=close_about,
                               border=0,
                               relief='sunken')
    about_fake_button.place(x=-1.5, y=-1.5)


def preset_menu(window):
    def to_game_menu():
        print(window.winfo_screenwidth(), window)

    start_button = Button(window, image=main_menu_start_img, border=0, command=check_rules)
    start_button.place(x=275, y=263)
    alg_button.place(x=502, y=352)
    who_starts_button.place(x=150, y=352)
    input_box = Canvas(window, width=100, height=50, highlightthickness=0)
    input_box.create_image(0, 0, image=preset_number_img, anchor=NW)
    input_box.place(x=350, y=350)
    Entry(input_box, width=2, border=0, justify="center", font=('Terminal', 25, 'bold')).place(x=24, y=8)
    about_button = Button(window, image=main_menu_about_img, border=0, background='white',
                          activebackground='white', command=about_preset)
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
    about_button = Button(window, image=main_menu_about_img, border=0, background='white',
                          activebackground='white', command=about_main)
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


background = Canvas(root, width=800, height=600)

background.pack()

who_starts_button = Button(root, image=preset_who_starts_img, border=0, command=change_player)
alg_button = Button(root, image=preset_algorithm_img, border=0, command=change_alg)

main_menu(root)
root.mainloop()
