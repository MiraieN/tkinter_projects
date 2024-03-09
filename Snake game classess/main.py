from tkinter import *
from random import randint, choice
from resources.colors import colors_list

root = Tk()
width, height = int(root.winfo_screenwidth()/2), int(root.winfo_screenheight()/2)
root.geometry(f"{width}x{height}+{int(width/2)}+{int(height/2)}")
root.resizable(False, False)

# color_head = choice(colors_list)
# color_body = choice(colors_list)
#
# part_count = 0
#
# temp_x, temp_y = 0, 0
#
# size = 30
#
# step = 10
# move = {'move_up': False,
#         'move_left': False,
#         'move_down': False,
#         'move_right': False}
#
# def up():
#     body_parts['body0'].y -= step
#     for key in move.keys():
#         move[key] = False
#     move['move_up'] = True
#
# def left():
#     body_parts['body0'].x -= step
#     for key in move.keys():
#         move[key] = False
#     move['move_left'] = True
#
#
# Button(text="↑", command=up).place(x=430, y=450)
# Button(text="←", command=left).place(x=380, y=500)
#
#
# class Part:
#     def __init__(self, bg=color_body):
#         Label(bg=bg)
#         self.x = 100
#         self.y = 100
#
#     def place(self, x, y):
#         self.place(x=x, y=y)
#
#     def get_x(self):
#         return self.x
#
#
# body_parts = {f'body{+part_count}': Part(bg=color_head)}
# body_parts['body0'].place(x=100, y=100)
# part_count += 1
#
# body_parts[f'body{+part_count}'] = Part()
# body_parts[f'body{+part_count}'].place(x=body_parts['body0'].x+size, y=body_parts['body0'].y)
# part_count += 1
# body_parts[f'body{+part_count}'] = Part()
# body_parts[f'body{+part_count}'].place(x=body_parts['body1'].x+size, y=body_parts['body1'].y)
# part_count += 1
#
# while body_parts['body0'].x < width:
#     part_count = 0
#     for key in body_parts.keys():
#         if key == 'body0':
#             body_parts[key].place(x=body_parts['body0'].x, y=body_parts['body0'].y)
#         else:
#             body_parts[key].place(x=body_parts[f'{key}{-part_count}'], y=body_parts[f'{key}{-part_count}'])
#             part_count += 1
#
#         root.update()
#         root.after(50)
#
#
# mainloop()

canvas = Canvas(bg="#000000", width=width, height=height)

color = "#00FF00"
size = 30
coordinates = [(100, 100)]
squares = []

for x, y in coordinates:
    square = canvas.create_rectangle(x, y, x + size, y + size, fill=color)
    squares.append(square)

x, y = coordinates[0]
square = canvas.create_rectangle(x, y, x + size, y + size, fill=color)
squares.insert(0, square)

mainloop()
