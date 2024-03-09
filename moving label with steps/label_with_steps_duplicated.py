from tkinter import *
from resources.colors import colors_list as colors

root = Tk()

width_, height_ = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2
root.geometry(f"{width_}x{height_}")

width, height = width_, height_/2

root.title('DVD logo')

i = 0
x = 0
y = 0
k = 120
j = 50
step_x, step_y = 3, 3
step_multiplying = 1.05

lbl_size_x, lbl_size_y = 30, 30

def cor():
    global x, y,k,j

    x = 0
    y = 0
    k = 120
    j = 50
    lbl_logo_1.place(x=k, y=j, width=70, height=40)
    lbl_logo.place(x=x, y=y, width=70, height=40)


def r():
    global x, y
    global step_x, step_y, i, step_multiplying, lbl_logo,lbl_logo_1

    while True:
        if step_x >= 150:
            step_multiplying = 1
        if x >= width - lbl_size_x or x <= 0:
            step_x *= -1
            step_x *= step_multiplying
            step_y *= step_multiplying
        if y >= height - lbl_size_y/2 or y <= 0:
            step_y *= -1
            step_x *= step_multiplying
            step_y *= step_multiplying

        x += step_x
        y += step_y

        lbl_logo['bg'] = colors[i]
        lbl_logo.place(x=x, y=y, width=lbl_size_x, height=lbl_size_y)

        lbl_logo_1['bg'] = colors[i]
        lbl_logo_1.place(x=x, y=height_-y, width=lbl_size_x, height=lbl_size_y)

        Label(bg=colors[i]).place(x=x, y=y, width=lbl_size_x, height=lbl_size_y)
        Label(bg=colors[i]).place(x=x, y=height_-y, width=lbl_size_x, height=lbl_size_y)

        i += 1
        if i == len(colors) - 1:
            i = 0

        root.after(5)
        root.update()


lbl_logo = Label()
lbl_logo.place(x=0, y=0, width=lbl_size_x, height=lbl_size_y)
lbl_logo_1 = Label()
lbl_logo_1.place(x=0, y=50, width=lbl_size_x, height=lbl_size_y)

Button(text="Right", command=r).pack()

lbl_logo.bind("<Motion>", lambda event: cor())
lbl_logo_1.bind("<Motion>", lambda event: cor())

try:
    mainloop()
except KeyboardInterrupt:
    exit()
