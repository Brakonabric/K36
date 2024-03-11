from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from style import

root = Tk()  # Primāra loga inicijalizacija ar nosaukumu root.
root['bg'] = '#2a374a'  # Primāra loga fona krāsa.
root.title('K36 GAMES')
root.geometry('800x600')  # Primāra loga izmērs.
root.resizable(width=False, height=False)

rootHeader = Canvas(root, MainMenu.start() ).place(x=300, y=242)

root.mainloop()