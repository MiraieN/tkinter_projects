from tkinter import *

root = Tk()
width, height = root.winfo_screenwidth()//2, root.winfo_screenheight()//2
root.geometry(f"{width}x{height}")

x, y = 40, 10
label_size_x = 80
label_size_y = 35

def moving():
    global x, y, colors_ind
    x_step = 3
    y_step = 3
    colors_step = 1
    while True:
        if x > width-label_size_x or x < 0:
            x_step *= -1
            colors_ind += colors_step
        if y > height-label_size_y or y < 0:
            y_step *= -1
            colors_ind += colors_step
        if colors_ind == 5:
            colors_ind *= 0
        label["foreground"] = colors[colors_ind]
        x += x_step
        y += y_step
        label.place(x=x, y=y)
        root.after(1)
        root.update()

# colors = ["#FFC1C1", "#FF6A6A", "#FF6666", "#FF4040", "#FF3333", "#FF3030", "#FF0000", "#CD0000", "#8B0000", "#800000", "#660000", "#330000"]
colors = ["blue", "red", "green", "white", "grey", "black"]
colors_ind = 1
label = Label(text="DVD", font=("comic sans ms", 30))
label.place(x=x, y=y, width=label_size_x, height=label_size_y)
label.bind("<Button-1>", lambda event: moving())

mainloop()

