from tkinter import *


def button_click():
    print("Button clicked!")


def on_button_click():
    print("Button clicked!")
    root.destroy()


root = Tk()
root.title('K36 GAMES')
root.geometry('800x600')
root.resizable(width=False, height=False)

bg_img = PhotoImage(file='assets/main_menu_background.png')
start_img = PhotoImage(file='assets/main_menu_start.png')
exit_img = PhotoImage(file='assets/main_menu_exit.png')
about_img = PhotoImage(file='assets/main_menu_about.png')


def main_menu(window):
    background = Canvas(window, width=800, height=600)
    background.pack()
    background.create_image(0, 0, image=bg_img, anchor=NW)
    start_button = Button(window, highlightthickness=0, image=start_img, border=0, command=button_click)
    start_button.place(x=275, y=263)
    exit_button = Button(window, image=exit_img, highlightthickness=0, border=0, command=on_button_click)
    exit_button.place(x=300, y=350)
    about_button = Button(window, image=about_img, highlightthickness=0, border=0, background='white',
                          activebackground='white', takefocus=1)
    about_button.place(x=375, y=470)


# Main but not def
main_menu(root)
root.mainloop()
