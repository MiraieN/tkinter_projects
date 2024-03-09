from tkinter import *
from resources.colors import colors_list
from random import choice

root = Tk()
width, height = root.winfo_screenwidth()//2, root.winfo_screenheight()//2
root.geometry(f"{width}x{height}")

x, y = 40, 10
label_size_x = 35
label_size_y = 35

def moving(event):
    global x, y, colors_ind

    x_step = 3
    y_step = 3
    colors_step = 1
    colors_len = len(colors_list)
    multiple_step = 1.05

    while True:
        if x_step > 100:
            multiple_step = 1
        if x > width-label_size_x or x < 0:
            x_step *= -1
            x_step *= multiple_step
            y_step *= multiple_step
        if y > height-label_size_y or y < 0:
            y_step *= -1
            x_step *= multiple_step
            y_step *= multiple_step
        if colors_ind > colors_len-2:
            colors_ind = 0

        label["background"] = colors_list[colors_ind]

        x += x_step
        y += y_step

        colors_ind += colors_step

        label.place(x=x, y=y)
        Label(background=colors_list[colors_ind]).place(x=x, y=y, width=label_size_x, height=label_size_y)

        root.after(1)
        root.update()

colors_ind = 1
label = Label(font=("comic sans ms", 30), background=choice(colors_list))
label.place(x=x, y=y, width=label_size_x, height=label_size_y)
label.bind("<Button-1>", moving)

mainloop()

