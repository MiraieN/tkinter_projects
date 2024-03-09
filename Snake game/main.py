from tkinter import *
from random import randint, choice
from resources.colors import colors_list

root = Tk()
width, height = int(root.winfo_screenwidth()/2), int(root.winfo_screenheight()/2)
root.geometry(f"{width}x{height}+{int(width/2)}+{int(height/2)}")
root.resizable(False, False)

def start():
    global body_count, head_x, head_y
    start_button.destroy()
    temp_step = head_size

    while True:
        temp_x, temp_y = head_x, head_y
        head_x += step_x
        head_y += step_y

        for key, value in snake_body.items():
            temp_x, temp_y = head_x, head_y
            temp_step += head_size
            temp_x += temp_step
            snake_body[key].place(x=temp_x, y=temp_y)

        root.update()
        root.after(50)

start_button_x = 60
start_button_y = 35
start_button = Button(text="Start", font=("comic sans ms", 27), command=start)
start_button.place(width=width//2-start_button_x, height=height//2-start_button_y)

head_color = choice(colors_list)

snake_body = {"head": Label(bg=head_color)}
head_x, head_y = 100, 100
head_size = 30
step_x, step_y = 10, 0

snake_body['head'].place(x=head_x, y=head_y, width=head_size, height=head_size)
body_count = 0

snake_body[f'body{+body_count}'] = Label(text="123")
snake_body['body0'].place(x=head_x+head_size, y=head_y)

mainloop()
