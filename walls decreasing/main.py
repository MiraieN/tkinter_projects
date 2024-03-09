import tkinter as tk

class Square(tk.Label):
    def __init__(self, master, color, width, height, x, y):
        self.master = master
        self.x, self.y = x, y
        self.color = color
        self.width = width
        self.height = height
        self.step_x = 5
        self.step_y = 5

        tk.Label.__init__(self, master=self.master, bg=self.color)

        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

    def stamp(self):
        tk.Label(master=self.master, bg=self.color).place(x=self.x, y=self.y, width=self.width, height=self.height)

    def collision(self, win):
        if self.x + self.width > win.width or self.x < 0:
            self.step_x *= -1
            self.x += self.step_x * 2
            win.decrease_width()
            if self.x < win.x + win.width / 2:
                win.decreased_left()
            else:
                win.decreased_right()

        if self.y + self.height > win.height or self.y < 0:
            self.step_y *= -1
            self.y += self.step_y * 2
            win.decrease_height()
            if self.y < win.y + win.height / 2:
                win.decreased_up()
            else:
                win.decreased_down()

    def moving(self):
        self.stamp()
        self.x += self.step_x
        self.y += self.step_y
        self.place(x=self.x, y=self.y)

class Canvas(tk.Canvas):
    def __init__(self, color, width, height, x, y):
        self.x, self.y = x, y
        self.color = color
        self.width = width
        self.height = height
        self.decreaser = 5

        tk.Canvas.__init__(self, bg=self.color)

        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

    def decrease_width(self):
        self.width -= self.decreaser
        self.place(x=self.x + self.decreaser, y=self.y, width=self.width, height=self.height)

    def decrease_height(self):
        self.height -= self.decreaser
        self.place(x=self.x, y=self.y + self.decreaser, width=self.width, height=self.height)

    def decreased_left(self):
        self.x += self.decreaser
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

    def decreased_up(self):
        self.y += self.decreaser
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

    def decreased_right(self):
        self.x -= self.decreaser
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

    def decreased_down(self):
        self.y -= self.decreaser
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

    def move(self):
        self.x += 0.5
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

class Window(tk.Tk):
    def __init__(self, width, height):
        tk.Tk.__init__(self)
        self.width = width
        self.height = height
        self.geometry(f"{self.width}x{self.height}")

window = Window(1200, 500)
big_lbl = Canvas("black", 400, 300, 20, 20)
lbl = Square(big_lbl, "white", 30, 30, 100, 100)
big_lbl2 = Canvas("black", 300, 400, 420, 20)
lbl2 = Square(big_lbl2, "white", 30, 30, 20, 100)

while True:
    for obj1, obj2 in ((lbl, big_lbl), (lbl2, big_lbl2)):
        obj1.moving()
        obj1.collision(obj2)
        obj2.move()
        window.after(10)
        window.update()