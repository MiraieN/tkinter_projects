from tkinter import *
from random import randint

root = Tk()
width, height = int(root.winfo_screenwidth()/2), int(root.winfo_screenheight()/2)
root.geometry(f"{width}x{height}+{int(width/2)}+{int(height/2)}")
root.resizable(False, False)

lbl_main = Label(background="#fbeddb")
lbl_main.place(x=0, y=0, width=width, height=height)

lbl_click_me = Label(text="BLACK ME", font=("comic sans ms", 22, "bold"), background="#FFC1C1", foreground="black")
lbl_click_me.place(x=int(width/2.4), y=int(height/2.8), width=180, height=180)

def for_click():
    lbl_click_me.destroy()
    start()
lbl_click_me.bind("<Button-1>", lambda event: for_click())

def start():
    global counter, rect_size, fps, colors_ind

    def create_rect():
        global counter, x, y, x_step, y_step, rect_size

        def change_pos():
            global counter, x, y, x_step, y_step, rect_size, fps, colors_ind
            counter += 1
            x_step *= -1
            y_step *= -1
            if rect_size < 20:
                rect_size -= 1
                fps -= 3
            else:
                rect_size -= 3
            x, y = randint(0, width - 50 - rect_size // 2), randint(0, height - 50 - rect_size // 2)
            lbl_to_click.place(x=x, y=y, width=rect_size, height=rect_size)
            colors_ind += 1
            lbl_to_click['background'] = colors[colors_ind]

        x, y = randint(0, width - rect_size//2), randint(0, height - rect_size//2)

        lbl_to_click = Label(background=colors[0])
        lbl_to_click.place(x=x, y=y, width=rect_size, height=rect_size)
        lbl_to_click.bind("<Button-1>", lambda event: change_pos())

        x_step = 10
        y_step = 10
        while lbl_to_click:
            if x > width - rect_size or x < 0:
                x_step *= -1
            if y > height - rect_size or y < 0:
                y_step *= -1
            x += x_step
            y += y_step
            try:
                lbl_to_click.place(x=x, y=y)
            except TclError:
                exit()
            root.after(1)
            root.update()

    rect_size = 60
    counter = 0
    fps = 40
    colors = ["#FFC1C1", "#FF6A6A", "#FF6666", "#FF4040", "#FF3333", "#FF3030", "#FF0000", "#CD0000", "#8B0000", "#800000", "#660000", "#330000", "#330000", "#330000", "#330000", "#330000", "#330000", "#330000", "#330000", "#330000", "#330000", "#330000"]
    colors_ind = 1
    create_rect()


mainloop()
