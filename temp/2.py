from tkinter import *
from random import randint

root = Tk()
width, height = int(root.winfo_screenwidth()/2), int(root.winfo_screenheight()/2)
root.geometry(f"{width}x{height}+{int(width/2)}+{int(height/2)}")
root.resizable(False, False)

lbl_to_click = Label(background="#9d8461")
lbl_to_click.place(x=50, y=50, width=50, height=50)
def change_pos():
    pass

lbl_to_click.bind("<Button-1>", lambda event: change_pos())
