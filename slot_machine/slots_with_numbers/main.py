import tkinter as tk
import glob
from random import choice, randint

class Label:
    def __init__(self, text,  font, x, y):
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.default_y = y
        self.default_x = x
        self.label = tk.Label(text=self.text, font=self.font, background=bg)
        self.label.place(x=self.x, y=self.y)
        self.bottom = 160
        self.top = 160
        self.speed = 15
    def change_text(self,text):
        self.text = text
        self.label.configure(text=text)

    def check_bottom(self):
        if self.y > self.bottom:
            self.y = self.default_y
            self.change_text(randint(1, 10))
            self.speed -= 1


    def has_stopped(self):
        if self.speed == 0:
            while self.y != self.bottom - 30:
                self.y += 1
                self.label.place(x=self.default_x, y=self.y)
                root.update()
                root.after(2)
            return True


bg = "#bfbfbf"

root = tk.Tk()
width, height = 800, 600
root.geometry(f"{width}x{height}")
root.configure(bg=bg)


num1 = Label("2", 32, 400, 40)

num2 = Label("7", 32, 480, 40)

num3 = Label("7", 32, 560, 40)

def spin_da_wheel():
    global bank_account
    if bank_account == 0:
        bank_lab['text'] = f"bank: You are broke"
        button.config(state="disabled")
        return
    bank_lab['text'] = f"bank: {bank_account}-{spin_price}"
    bank_account -= spin_price
    button.config(state="disabled")
    for obj in num1, num2, num3:
        while not obj.has_stopped():
            obj.check_bottom()
            obj.label.place(x=obj.x, y=obj.y)
            obj.y += obj.speed
            root.after(2)
            root.update()
    button.config(state="normal")
    bank_lab['text'] = f"bank: {bank_account}"

bank_account = 10
spin_price = 5
button = tk.Button(text="SPIN_DA_WHEEL", font=32, command=spin_da_wheel)
button.place(x=410, y=200)

bank_lab = tk.Label(text=f"bank: {bank_account}", font=32, bg=bg)
bank_lab.place(x=50, y=50)
spin_price_lab = tk.Label(text=f"spin price: 5", font=32, bg=bg)
spin_price_lab.place(x=50, y=70)

root.mainloop()