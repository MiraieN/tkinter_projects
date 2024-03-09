# video course slots https://youtu.be/th4OBktqK1I?t=1466

import tkinter as tk
import glob
from random import choice

bg = "#bfbfbf"

root = tk.Tk()
width, height = 800, 600
root.geometry(f"{width}x{height}")
# root.configure(bg=bg)

images = [str(s) for s in glob.glob(pathname="pics\*.png")]


images = {tk.PhotoImage(file=img): img[5:-4] for img in images}
images_list = list(images.keys())

label1 = tk.Label()
label1.place(x=100, y=100)
label2 = tk.Label()
label2.place(x=300, y=100)
label3 = tk.Label()
label3.place(x=500, y=100)

def slide(lab):
    global x
    x += 200
    c = 30
    while True:
        img = choice(images_list)
        # image = tk.PhotoImage(file=img)
        lab['image'] = img
        root.update()
        root.after(c)
        c += 3
        if c > 100:
            c += 5
        if c > 300:
            c += 10
        # if c > 400:
        #     c += 20
        if c > 400:
            root.after(1000)
            tk.Label(image=img).place(x=x, y=100)
            tk.Label(text=images[img], font=("Blackadder ITC", 32)).place(x=x + 40, y=280)
            root.update()
            root.after(3000)
            return


def working():
    global x
    x = -100
    button.configure(state="disabled")
    if label1['image']:
        for x in (100, 300, 500):
            tk.Label().place(x=x, y=100, width=190, height=180)
    for label in (label1, label2, label3):
        # image, x = slide(label)
        # tk.Label(image=image).place(x=x, y=100)
        slide(label)
    root.update()
    button.configure(state="normal")


button = tk.Button(text="Spin!", font=("Blackadder ITC", 32), command=working, relief='solid')
button.place(x=350, y=400)

root.mainloop()
