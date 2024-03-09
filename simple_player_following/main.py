from tkinter import *

def check_collide(txt):
    if txt == "right":
        if enemy_x + enemy_size + enemy_step > obstacle_x:
            return True
        else:
            return False
    elif txt == "left":
        if enemy_x - enemy_step < obstacle_x + obstacle_size:
            return True
        else:
            return False
    elif txt == "down":
        if enemy_y + enemy_size + enemy_step > obstacle_y:
            return True
        else:
            return False
    elif txt == "up":
        if enemy_y - enemy_step < obstacle_y + obstacle_size:
            return True
        else:
            return False

def x_in_box():
    if enemy_x + enemy_size > obstacle_x and enemy_x < obstacle_x + obstacle_size:
        return True

def y_in_box():
    if enemy_y < obstacle_y + obstacle_size and enemy_y + enemy_size > obstacle_y:
        return True

def player_x_in_box():
    if player_x + player_size > obstacle_x and player_x < obstacle_x + obstacle_size:
        return True

def player_y_in_box():
    if player_y < obstacle_y + obstacle_size and player_y + player_size > obstacle_y:
        return True

def player_move(txt):
    global player_x, player_y

    if txt == "up":
        possible = True
        if player_y - player_step < obstacle_y + obstacle_size:
            if player_x_in_box():
                possible = False
        if possible:
            player_y -= player_step

    if txt == "right":
        possible = True
        if player_x + player_size + player_step > obstacle_x:
            if player_y_in_box():
                possible = False
        if possible:
            player_x += player_step

    if txt == "left":
        possible = True
        if player_x - player_step < obstacle_x + obstacle_size:
            if player_y_in_box():
                possible = False
        if possible:
            player_x -= player_step

    if txt == "down":
        possible = True
        if  player_x_in_box():
            if player_y + player_size + player_step > obstacle_y:
                possible = False
        if possible:
            player_y += player_step

    player.place(x=player_x, y=player_y)
    root.update()

root = Tk()
width, height = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2  # 960 540
root.geometry(f"{width}x{height}")

enemy_x, enemy_y = 0, 0
enemy_size = 30
enemy_step = 2

obstacle_x, obstacle_y = 280, 60
obstacle_size = 40

player_x, player_y = 400, 400
player_size = 20
player_step = 15

obstacle = Label(bg="#ffffff")
obstacle.place(x=obstacle_x, y=obstacle_y, width=obstacle_size, height=obstacle_size)

enemy = Label(bg="#a0a0a0")
enemy.place(x=enemy_x, y=enemy_y, width=enemy_size, height=enemy_size)

player = Label(bg="#0f0f0f")
player.place(x=player_x, y=player_y, width=player_size, height=player_size)

root.bind("<Up>", lambda e: player_move("up"))
root.bind("<Down>", lambda e: player_move("down"))
root.bind("<Right>", lambda e: player_move("right"))
root.bind("<Left>", lambda e: player_move("left"))

mainloop()

while True:
    while player_x > enemy_x:
        if not (y_in_box() and check_collide("right")):
            enemy_x += enemy_step
        else:
            enemy_y += enemy_step

        enemy.place(x=enemy_x, y=enemy_y)
        root.after(20)
        root.update()

    while player_x < enemy_x:
        if not (y_in_box() and check_collide("left")):
            enemy_x -= enemy_step
        else:
            enemy_y -= enemy_step

        enemy.place(x=enemy_x, y=enemy_y)
        root.after(20)
        root.update()

    while player_y > enemy_y:
        if not (x_in_box() and check_collide("down")):
            enemy_y += enemy_step
        else:
            enemy_x += enemy_step

        enemy.place(x=enemy_x, y=enemy_y)
        root.after(20)
        root.update()

    while player_y < enemy_y:
        if not (x_in_box() and check_collide("up")):
            enemy_y -= enemy_step
        else:
            enemy_x -= enemy_step

        enemy.place(x=enemy_x, y=enemy_y)
        root.after(20)
        root.update()

    root.update()
