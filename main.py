from tkinter import *


def button_click():
    print("Button clicked!")


def on_button_click():
    root.destroy()


def about():
    def close_about():
        about_fake_button.destroy()

    about_fake_button = Button(root, image=main_about_preview_img, width=800, height=600, command=close_about, border=0,
                               relief='sunken')
    about_fake_button.place(x=-1.5, y=-1.5)


def preset_menu(window):
    start_button = Button(window, highlightthickness=0, image=main_menu_start_img, border=0, command=button_click)
    start_button.place(x=275, y=263)
    algo_button = Button(window, highlightthickness=0, image=preset_algorithm_img, border=0, command=button_click)
    algo_button.place(x=575, y=415)
    # who_starts_button = Button(window, highlightthickness=0, image=preset_who_starts_img, border=0,
    #                            command=button_click)
    # input_block = Canvas(window, width=100, height=600)
    # input_block.pack()
    # input_block.create_image(500, 100, image=preset_number_img, anchor=NW)
    # input_space = Entry(window)
    # input_space.pack()


def main_menu(window):
    def to_preset_menu():
        background.create_image(0, 0, image=preset_back_img, anchor=NW)
        start_button.destroy()
        exit_button.destroy()
        about_button.destroy()
        preset_menu(window)

    background = Canvas(window, width=800, height=600)
    background.pack()
    background.create_image(0, 0, image=main_menu_bg_img, anchor=NW)
    start_button = Button(window, highlightthickness=0, image=main_menu_start_img, border=0, command=to_preset_menu)
    start_button.place(x=275, y=263)
    exit_button = Button(window, image=main_menu_exit_img, highlightthickness=0, border=0, command=on_button_click)
    exit_button.place(x=300, y=350)
    about_button = Button(window, image=main_menu_about_img, highlightthickness=0, border=0, background='white',
                          activebackground='white', command=about)
    about_button.place(x=375, y=473)


# Main but not def
root = Tk()
root.title('K36 GAMES')
root.geometry('800x600')
root.resizable(width=False, height=False)

main_menu_bg_img = PhotoImage(file='assets/main_menu_background.png')
main_menu_start_img = PhotoImage(file='assets/main_menu_start.png')
main_menu_exit_img = PhotoImage(file='assets/main_menu_exit.png')
main_menu_about_img = PhotoImage(file='assets/main_menu_about.png')
main_about_preview_img = PhotoImage(file='assets/about_preview.png')

preset_back_img = PhotoImage(file='assets/preset_background.png')
preset_number_img = PhotoImage(file='assets/preset_number.png')
preset_who_starts_img = PhotoImage(file='assets/preset_who_starts.png')
preset_algorithm_img = PhotoImage(file='assets/preset_algorithm.png')

main_menu(root)
root.mainloop()
