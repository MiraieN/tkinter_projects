import tkinter as tk
from resources.colors import colors_list
from random import choice, randint

class _Label:
    def __init__(self, x, y, size, step_x, step_y, bg_color, top_hitwall, bot_hitwall, left_hitwall, right_hitwall):
        self.x = x
        self.y = y
        self.size = size
        self.step_x = step_x
        self.step_y = step_y
        self.bg_color = bg_color
        self.step_multiplying = 1.05
        self.top_hitwall = top_hitwall
        self.bot_hitwall = bot_hitwall
        self.left_hitwall = left_hitwall
        self.right_hitwall = right_hitwall

        self.label = tk.Label(bg=self.bg_color)
        self.hue = randint(1, colors_list_len)
        self.place()

    def place(self):
        self.label.place(x=self.x, y=self.y, width=self.size, height=self.size)

    def stamp(self):
        tk.Label(bg=self.get_bg_color()).place(x=self.x, y=self.y, width=self.size, height=self.size)

    def collide_screen(self, align):
        if align == "right":
            if self.x + self.size > self.right_hitwall:
                return True
        if align == "left":
            if self.x < self.left_hitwall:
                return True
        if align == "down":
            if self.y + self.size * 1.5 > self.bot_hitwall:
                return True
        if align == "up":
            if self.y < self.top_hitwall:
                return True

    def multiplying_steps(self, step):
        if step == "x":
            self.step_x *= -1
        elif step == "y":
            self.step_y *= -1
        self.step_x *= self.step_multiplying
        self.step_y *= self.step_multiplying

    def next_color(self):
        if self.hue > colors_list_len:
            self.hue = 0
        color = colors_list[self.hue]
        # # tried change hsv to rgb to use colorsys
        # rgb = colorsys.hsv_to_rgb(self.hue, 1, 1)
        # color = "#%02x%02x%02x" % rgb
        self.label['bg'] = color
        self.bg_color = color
        self.hue += 1

    def move(self):
        self.x += self.step_x
        self.y += self.step_y
        self.place()

    def get_bg_color(self):
        return self.bg_color

colors_list_len = len(colors_list) - 1

root = tk.Tk()
width, height = root.winfo_screenwidth()//2, root.winfo_screenheight()//2
root.geometry(f"{width}x{height}")

player_1 = _Label(x=0, y=0, size=35, step_x=5, step_y=5, bg_color=choice(colors_list),
                  top_hitwall=0, bot_hitwall=height/2, left_hitwall=0, right_hitwall=width)
player_2 = _Label(x=0, y=height-55, size=35, step_x=5, step_y=5, bg_color=choice(colors_list),
                  top_hitwall=height/2, bot_hitwall=height, left_hitwall=0, right_hitwall=width)
player_3 = _Label(x=0, y=400, size=35, step_x=5, step_y=5, bg_color=choice(colors_list),
                  top_hitwall=0, bot_hitwall=height, left_hitwall=0, right_hitwall=width)


def moving():
    while True:
        for obj in (player_1, player_2, player_3):
            if obj.step_x > 100:
                obj.step_multiplying = 1
            if obj.collide_screen("right") or obj.collide_screen("left"):
                obj.multiplying_steps('x')
            if obj.collide_screen("up") or obj.collide_screen("down"):
                obj.multiplying_steps('y')

            obj.next_color()

            obj.move()

            obj.stamp()

            root.after(1)
            root.update()

moving()
# def moving(event):
#     global x, y, colors_ind
#
#     x_step = 3
#     y_step = 3
#     colors_step = 1
#     colors_len = len(colors_list)
#     multiple_step = 1.05
#
#     while True:
#         if x_step > 100:
#             multiple_step = 1
#         if x > width-label_size_x or x < 0:
#             x_step *= -1
#             x_step *= multiple_step
#             y_step *= multiple_step
#         if y > height-label_size_y or y < 0:
#             y_step *= -1
#             x_step *= multiple_step
#             y_step *= multiple_step
#         if colors_ind > colors_len-2:
#             colors_ind = 0
#
#         label["background"] = colors_list[colors_ind]
#
#         x += x_step
#         y += y_step
#
#         colors_ind += colors_step
#
#         label.place(x=x, y=y)
#         Label(background=colors_list[colors_ind]).place(x=x, y=y, width=label_size_x, height=label_size_y)
#
#         root.after(1)
#         root.update()
#
# colors_ind = 1
# label = Label(font=("comic sans ms", 30), background=choice(colors_list))
# label.place(x=x, y=y, width=label_size_x, height=label_size_y)
# label.bind("<Button-1>", moving)
#
# mainloop()

