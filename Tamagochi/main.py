from tkinter import *
from random import randint, choice
from resources.colors import colors_list, colors_dict

root = Tk()
width, height = int(root.winfo_screenwidth()/2), int(root.winfo_screenheight()/2)
root.geometry(f"{width}x{height}+{int(width/2)}+{int(height/2)}")
root.resizable(False, False)

gochi = Label(text="alive", font=("comic sans ms", 32))
gochi.place(x=width//2-50, y=height//2)

max_health = 4
health_amount = 4
health_coors = [(20, 20), (40, 20), (60, 20), (80, 20)]
health_size = 15

def update_health(current_health):
    health_color = colors_dict['LightSeaGreen']
    for elem in range(max_health):
        if elem == current_health:
            health_color = '#000000'
        x, y = health_coors[elem]
        Label(bg=health_color).place(x=x, y=y, width=health_size, height=health_size)

food = Button(text="food", font=("comic sans ms", 28))
food.place(x=width-120, y=height//2-40, width=80, height=40)

max_food = 4
food_amount = 4
food_coors = [(20, 40), (40, 40), (60, 40), (80, 40)]
food_size = 15
allowed_to_eat = True

def update_food(current_food):
    food_color = colors_dict['Red Dirt']
    for elem in range(max_food):
        if elem >= current_food:
            food_color = '#000000'
        x, y = food_coors[elem]
        Label(bg=food_color).place(x=x, y=y, width=food_size, height=health_size)

def feed(event):
    global food_amount, allowed_to_eat
    if allowed_to_eat and food_amount != max_food:
        food_amount += 1
        # allowed_to_eat = False

food.bind("<Button-1>", feed)

timer = 0
timer_lbl = Label(text=timer, font=("comic sans ms", 27))
timer_lbl.place(x=width-80, y=height-40, width=len(str(timer_lbl['text']))*20, height=30)

game = True
while game:
    if food_amount > 0 and timer % 10 == 0:
        food_amount -= 1
    update_food(food_amount)
    if food_amount == 0 and timer % 10 == 0:
        health_amount -= 1
    update_health(health_amount)

    timer += 1
    timer_lbl['text'] = timer
    timer_lbl.place(width=len(str(timer_lbl['text'])) * 20, height=30)
    root.update()

    if health_amount == 0:
        gochi['text'] = "Dead"
        game = False

    root.after(100)

mainloop()
