import tkinter as tk
from resources.colors import colors_list
from random import choice, randint


class _Label:
    def __init__(self, x, y, size, step, bg_color):
        self.x = x
        self.y = y
        self.size = size
        self.step = step
        self.bg_color = bg_color

        self.label = tk.Label(bg=self.bg_color)
        self.place()

    def place(self):
        self.label.place(x=self.x, y=self.y, width=self.size, height=self.size)

    def will_collide_screen(self, align):
        if align == "right":
            if self.x + self.size + self.step > screen_right_hitwall:
                return True

        if align == "left":
            if self.x - self.step < screen_left_hitwall:
                return True

        if align == "down":
            if self.y + self.size + self.step > screen_bot_hitwall:
                return True

        if align == "up":
            if self.y - self.step < screen_top_hitwall:
                return True

    def x_in_obj(self, obj):
        if self.x + self.size > obj.x and self.x < obj.x + obj.size:
            return True

    def y_in_obj(self, obj):
        if self.y < obj.y + obj.size and self.y + self.size > obj.y:
            return True

    def will_collide_obj(self, side, obj):
        if side == "up":
            if self.y - self.step < obj.y + obj.size:
                if self.x_in_obj(obj):
                    return True

        if side == "right":
            if self.x + self.size + self.step > obj.x:
                if self.y_in_obj(obj):
                    return True

        if side == "left":
            if self.x - self.step < obj.x + obj.size:
                if self.y_in_obj(obj):
                    return True

        if side == "down":
            if self.y + self.size + self.step > obj.y:
                if self.x_in_obj(obj):
                    return True

    def move(self, side, obj):
        if side == "up":
            if not self.will_collide_obj(side, obj):
                if not self.will_collide_screen(side):
                    self.y -= self.step
                    self.update(50)
                    return True

        elif side == "right":
            if not self.will_collide_obj(side, obj):
                if not self.will_collide_screen(side):
                    self.x += self.step
                    self.update(50)
                    return True

        elif side == "left":
            if not self.will_collide_obj(side, obj):
                if not self.will_collide_screen(side):
                    self.x -= self.step
                    self.update(50)
                    return True

        elif side == "down":
            if not self.will_collide_obj(side, obj):
                if not self.will_collide_screen(side):
                    self.y += self.step
                    self.update(50)
                    return True

    def update(self, ms):
        self.place()
        root.update()
        if self != player:
            root.after(ms)


root = tk.Tk()
width, height = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2
root.geometry(f"{width}x{height}")

screen_top_hitwall = 0
screen_bot_hitwall = height
screen_left_hitwall = 0
screen_right_hitwall = width

player = _Label(x=300, y=300, size=35, step=5, bg_color="green")
obstacle = _Label(x=100, y=0, size=35, step=5, bg_color="black")
enemy = _Label(x=0, y=0, size=35, step=5, bg_color="red")

root.bind("<Right>", lambda event: player.move("right", obstacle))
root.bind("<Left>", lambda event: player.move("left", obstacle))
root.bind("<Up>", lambda event: player.move("up", obstacle))
root.bind("<Down>", lambda event: player.move("down", obstacle))

def enemy_found_player():
    if (enemy.x + enemy.size > player.x and enemy.y + enemy.size > player.y) or enemy.y_in_obj(player) and enemy.x_in_obj(player):
        return True

def enemy_searching():
    while True:
        if enemy_found_player():
            root.destroy()
            break

        while enemy.x < player.x:
            if not enemy.move("right", obstacle):
                enemy.move("down", obstacle)

        while enemy.x > player.x:
            if not enemy.move("left", obstacle):
                enemy.move("up", obstacle)

        while enemy.y < player.y:
            if not enemy.move("down", obstacle):
                enemy.move("right", obstacle)

        while enemy.y > player.y:
            if not enemy.move("up", obstacle):
                enemy.move("up", obstacle)


enemy_searching()
