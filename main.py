from tkinter import *
import tkinter as ttk
from tkinter import PhotoImage

root = Tk()  # Primāra loga inicijalizacija ar nosaukumu root.
root.title('K36 GAMES')
root.geometry('800x600')  # Primāra loga izmērs.
root.resizable(width=False, height=False)

bg = PhotoImage(file='assets/main_menu_background.png')
background = Canvas(root, width=800, height=600)
background.pack()
background.create_image(0, 0, image=bg, anchor=NW)
root.mainloop()
