from tkinter import *
from random import randint, choice
from resources.colors import colors_list, colors_dict

def click_in_time():
    global x, y, colors_ind
    root = Tk()
    width, height = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2
    root.geometry(f"{width}x{height}")

    x, y = 40, 10
    label_size_x = 70
    label_size_y = 70

    box_label_size = 70
    box_x = width // 2 - 200  # to test up collision. It stucks
    box_y = height // 2

    box_left_hitwall = box_x
    box_right_hitwall = box_x + box_label_size
    box_up_hitwall = box_y
    box_down_hitwall = box_y + box_label_size

    def moving(event):
        global x, y, colors_ind

        def x_in_box():
            if box_left_hitwall < label_left_hitwall < box_right_hitwall or \
                    box_right_hitwall > label_right_hitwall > box_left_hitwall:
                return True

        def y_in_box():
            if box_down_hitwall > label_up_hitwall > box_up_hitwall or \
                    box_up_hitwall < label_down_hitwall < box_down_hitwall:
                return True

        def got_it(event):
            global game
            if y_in_box() and x_in_box():
                print("got it")
                game = False
                return "got it"

        x_step = 3
        y_step = 3
        colors_step = 1
        colors_len = len(colors_list)
        multiple_step = 1.05

        root.bind("<space>", got_it)
        game = True
        while game:
            label_left_hitwall = x
            label_right_hitwall = x + label_size_x
            label_up_hitwall = y
            label_down_hitwall = y + label_size_y

            if x_step > 100:
                multiple_step = 1
            if label_right_hitwall > width or label_left_hitwall < 0:
                x_step *= -1
                x_step *= multiple_step
                y_step *= multiple_step
            if label_down_hitwall > height or label_up_hitwall < 0:
                y_step *= -1
                x_step *= multiple_step
                y_step *= multiple_step
            if colors_ind > colors_len - 2:
                colors_ind = 0

            label["background"] = colors_list[colors_ind]

            x += x_step
            y += y_step

            colors_ind += colors_step

            label.place(x=x, y=y)

            root.after(1)
            root.update()
        root.destroy()

    colors_ind = 1
    label = Label(background=choice(colors_list))
    label.place(x=x, y=y, width=label_size_x, height=label_size_y)
    label.bind("<Button-1>", moving)

    Box = Label(background=choice(colors_list))
    Box.place(x=box_x, y=box_y, width=box_label_size, height=box_label_size)

    mainloop()

if __name__ == '__main__':
    click_in_time()
