from tkinter import *
from random import randint, choice
from resources.colors import colors_list

root = Tk()
width, height = int(root.winfo_screenwidth()/2), int(root.winfo_screenheight()/2)
root.geometry(f"{width}x{height}+{int(width/2)}+{int(height/2)}")
root.resizable(False, False)

years = 18
years_lbl = Label()


mainloop()
