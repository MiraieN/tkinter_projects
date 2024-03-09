import tkinter as tk

root = tk.Tk()
root.geometry(f"{800}x{600}")
canvas = tk.Canvas(bg="black")
canvas_x = 50
canvas_y = 50
canvas_width = 600
canvas_height = 400
canvas.place(x=canvas_x, y=canvas_y, width=canvas_width, height=canvas_height)
label = tk.Label(canvas, bg="white")
label_step_x = 3
label_step_y = 3
label_x = 100
label_y = 100
label_width = 30
label_height = 30
label.place(x=label_x, y=label_y, width=label_width, height=label_height)

while True:
    if label_x + label_width > canvas_width or label_x < 0:
        label_step_x *= -1
        label_x += label_step_x
        canvas_width -= 3
        if label_x < canvas_x + canvas_width // 2:
            canvas_x += 3


    if label_y + label_height > canvas_height or label_y < 0:
        label_step_y *= -1
        label_y += label_step_y
        canvas_height -= 3
        if label_y < canvas_y + canvas_height // 2:
            canvas_y += 3


    canvas.place(x=canvas_x, y=canvas_y, width=canvas_width, height=canvas_height)

    label_x += label_step_x
    label_y += label_step_y

    label.place(x=label_x, y=label_y, width=label_width, height=label_height)

    tk.Label(canvas, bg="white").place(x=label_x, y=label_y, width=label_width, height=label_height)



    root.update()
    root.after(1)
