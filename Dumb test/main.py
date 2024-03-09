from tkinter import *
from random import randint
from tkinter import messagebox

def remove(event):
    lbl.place(x=randint(0, 700), y=randint(0, 370))
    root.update()

def show_txt(event):
    messagebox.showwarning(message="I always knew that :D")
    root.destroy()

root = Tk()

root.geometry("800x400+600+200")

lbl = Label(text="Click me if u r smart!", font=("comic sans ms", 12), background="grey")
lbl.place(x=300, y=100)

lbl.bind("<Motion>", remove)

lbl1 = Label(text="Click me if u r dumb!", font=("comic sans ms", 12), background="grey")
lbl1.place(x=300, y=200)

lbl1.bind("<Button-1>", show_txt)
mainloop()
