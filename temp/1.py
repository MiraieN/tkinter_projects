from tkinter import *

root = Tk()
width, height = root.winfo_screenwidth()//2, root.winfo_screenheight()//2
root.geometry(f"{width}x{height}")

a = 40
b = 10

def moving_up():
    global b
    b -= 5
    label.place(x=a, y=b)

def moving_down():
    global b
    b += 5
    label.place(x=a, y=b)

label = Label(text="DVD", font=("comic sans ms", 30))
label.place(x=a, y=b, width=80, height=35)

but = Button(text="up", command=moving_up)
but.place(x=0, y=0)

but1 = Button(text="down", command=moving_down)
but1.place(x=0, y=20)

mainloop()

