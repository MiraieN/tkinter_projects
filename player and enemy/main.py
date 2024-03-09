from tkinter import *
from resources.colors import colors_list
from random import choice


def update_hitboxes():
    global player_left_hitbox, player_right_hitbox, player_up_hitbox, player_down_hitbox
    player_left_hitbox = x
    player_right_hitbox = x + player_size
    player_up_hitbox = y
    player_down_hitbox = y + player_size


def update_enemy_hitboxes():
    global enemy_left_hitbox, enemy_right_hitbox, enemy_up_hitbox, enemy_down_hitbox
    enemy_left_hitbox = enemy_x
    enemy_right_hitbox = enemy_x + enemy_size
    enemy_up_hitbox = enemy_y
    enemy_down_hitbox = enemy_y + enemy_size


def x_in_box(box_left_hitwall, box_right_hitwall):
    if box_left_hitwall < player_left_hitbox < box_right_hitwall or \
            box_right_hitwall > player_right_hitbox > box_left_hitwall:
        return True


def y_in_box(box_up_hitwall, box_down_hitwall):
    if box_down_hitwall > player_up_hitbox > box_up_hitwall or \
            box_up_hitwall < player_down_hitbox < box_down_hitwall:
        return True


def move(txt):
    global x, y

    update_hitboxes()

    if txt == "←":
        possible = True
        for coll_x, coll_y in coors:
            if coll_x[0] < player_left_hitbox - player_step < coll_x[1]:
                if y_in_box(coll_y[0], coll_y[1]):
                    possible = False
        if possible:
            x -= player_step

    elif txt == "→":
        possible = True
        for coll_x, coll_y in coors:
            if coll_x[0] < player_right_hitbox + player_step < coll_x[1]:
                if y_in_box(coll_y[0], coll_y[1]):
                    possible = False
        if possible:
            x += player_step

    elif txt == "↑":
        possible = True
        for coll_x, coll_y in coors:
            if coll_y[0] < player_up_hitbox - player_step < coll_y[1]:
                if x_in_box(coll_x[0], coll_x[1]):
                    possible = False
        if possible:
            y -= player_step

    elif txt == "↓":
        possible = True
        for coll_x, coll_y in coors:
            if coll_y[0] < player_down_hitbox + player_step < coll_y[1]:
                if x_in_box(coll_x[0], coll_x[1]):
                    possible = False
        if possible:
            y += player_step

    player_label.place(x=x, y=y)

    update_hitboxes()


def enemy_x_in_box(box_left_hitwall, box_right_hitwall):
    if enemy_left_hitbox - step_x < box_right_hitwall and enemy_right_hitbox + step_x > box_left_hitwall:
        return True


def enemy_y_in_box(box_up_hitwall, box_down_hitwall):
    if box_down_hitwall > enemy_up_hitbox - step_y and box_up_hitwall < enemy_down_hitbox + step_y:
        return True


def moving_enemy():
    global enemy_x, enemy_y, x, y
    # prev_x, prev_y = enemy_x, enemy_y
    while True:
        if x > enemy_x:
            possible = True
            for coll_x, coll_y in coors:
                if enemy_right_hitbox + step_x > coll_x[0] and enemy_y_in_box(coll_y[0], coll_y[1]):
                    possible = False
                    break
            if possible:
                enemy_x += step_x

            if y > enemy_y:
                possible = True
                for coll_x, coll_y in coors:
                    if enemy_x_in_box(coll_x[0], coll_x[1]) and enemy_down_hitbox + step_y > coll_y[0]:
                        possible = False
                        break
                if possible:
                    enemy_y += step_y

            if y < enemy_y:
                possible = True
                for coll_x, coll_y in coors:
                    if enemy_x_in_box(coll_x[0], coll_x[1]) and enemy_up_hitbox - step_y < coll_y[1]:
                        possible = False
                        break
                if possible:
                    enemy_y -= step_y

        if x < enemy_x:
            possible = True
            for coll_x, coll_y in coors:
                if enemy_y_in_box(coll_y[0], coll_y[1]) and enemy_left_hitbox - step_x < coll_x[1]:
                    possible = False
                    break
            if possible:
                enemy_x -= step_x

            if y > enemy_y:
                possible = True
                for coll_x, coll_y in coors:
                    if enemy_x_in_box(coll_x[0], coll_x[1]) and enemy_down_hitbox + step_y > coll_y[0]:
                        possible = False
                        break
                if possible:
                    enemy_y += step_y

            if y < enemy_y:
                possible = True
                for coll_x, coll_y in coors:
                    if enemy_x_in_box(coll_x[0], coll_x[1]) and enemy_up_hitbox - step_y < coll_y[1]:
                        possible = False
                        break
                if possible:
                    enemy_y -= step_y

        if y > enemy_y:
            possible = True
            for coll_x, coll_y in coors:
                if enemy_x_in_box(coll_x[0], coll_x[1]) and enemy_down_hitbox + step_y > coll_y[0]:
                    possible = False
                    break
            if possible:
                enemy_y += step_y

            if x < enemy_x:
                possible = True
                for coll_x, coll_y in coors:
                    if enemy_y_in_box(coll_y[0], coll_y[1]) and enemy_left_hitbox - step_x < coll_x[1]:
                        possible = False
                        break
                if possible:
                    enemy_x -= step_x

            if x > enemy_x:
                possible = True
                for coll_x, coll_y in coors:
                    if enemy_right_hitbox + step_x > coll_x[0] and enemy_y_in_box(coll_y[0], coll_y[1]):
                        possible = False
                        break
                if possible:
                    enemy_x += step_x

        if y < enemy_y:
            possible = True
            for coll_x, coll_y in coors:
                if enemy_x_in_box(coll_x[0], coll_x[1]) and enemy_up_hitbox - step_y < coll_y[1]:
                    possible = False
                    break
            if possible:
                enemy_y -= step_y

            if x < enemy_x:
                possible = True
                for coll_x, coll_y in coors:
                    if enemy_y_in_box(coll_y[0], coll_y[1]) and enemy_left_hitbox - step_x < coll_x[1]:
                        possible = False
                        break
                if possible:
                    enemy_x -= step_x

            if x > enemy_x:
                possible = True
                for coll_x, coll_y in coors:
                    if enemy_right_hitbox + step_x > coll_x[0] and enemy_y_in_box(coll_y[0], coll_y[1]):
                        possible = False
                        break
                if possible:
                    enemy_x += step_x

        if x == enemy_x and y == enemy_y:
            root.destroy()
            break

        enemy.place(x=enemy_x, y=enemy_y)
        root.after(40)
        root.update()

        update_enemy_hitboxes()

        # if prev_x == enemy_x and prev_y == enemy_y:
        #     print("checking")
        #     for coll_x, coll_y in coors:
        #         if enemy_right_hitbox > coll_x[0] and enemy_y_in_box(coll_y[0], coll_y[1]) \
        #                 and enemy_x_in_box(coll_x[0], coll_x[1]) and enemy_down_hitbox + step_y > coll_y[0]:
        #             print("checking 2")
        #             enemy_x -= step_x
        #             enemy_y -= step_y
        #         if enemy_right_hitbox > coll_x[0] and enemy_y_in_box(coll_y[0], coll_y[1]) \
        #                 and enemy_x_in_box(coll_x[0], coll_x[1]) and enemy_up_hitbox - step_y < coll_y[1]:
        #             enemy_x -= step_x
        #             enemy_y += step_y
        #         if enemy_y_in_box(coll_y[0], coll_y[1]) and enemy_left_hitbox - step_x < coll_x[1] \
        #                 and enemy_x_in_box(coll_x[0], coll_x[1]) and enemy_down_hitbox + step_y > coll_y[0]:
        #             enemy_x += step_x
        #             enemy_y -= step_y
        #         if enemy_y_in_box(coll_y[0], coll_y[1]) and enemy_left_hitbox - step_x < coll_x[1] \
        #                 and enemy_x_in_box(coll_x[0], coll_x[1]) and enemy_up_hitbox - step_y < coll_y[1]:
        #             enemy_x += step_x
        #             enemy_y += step_y

root = Tk()
width, height = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2  # 960 540
root.geometry(f"{width}x{height}")

size = 30
color = choice(colors_list)
player_size = 15
player_step = 10

coors = []
x, y = 850, 440
step_x, step_y = 1, 1

player_left_hitbox = x
player_right_hitbox = x + player_size
player_up_hitbox = y
player_down_hitbox = y + player_size

enemy_size = 10
enemy_x, enemy_y = 70, 125

enemy_left_hitbox = enemy_x
enemy_right_hitbox = enemy_x + enemy_size
enemy_up_hitbox = enemy_y
enemy_down_hitbox = enemy_y + enemy_size

for raw in range(size, width - size, size * 2):
    for column in range(size, height - size, size * 2):
        new_label = Label(background=color)
        new_label.place(x=raw, y=column, width=size, height=size)
        coors.append(((raw, raw + size), (column, column + size)))

root.configure(background="#E6E6E6")

player_label = Label(background=choice(colors_list))
player_label.place(x=x, y=y, width=player_size, height=player_size)

# # arrows buttons creation
# def create_button(ind):
#     Button(text=arrows[ind], command=lambda: move(arrows[ind])).\
#         place(x=buttons_coors[ind][0], y=buttons_coors[ind][1], width=40, height=40)
# buttons_coors = ((380, 500), (480, 500), (430, 450), (430, 500))
# arrows = "←→↑↓"
# for i in range(len(arrows)):
#     create_button(i)

root.bind('<Left>', lambda event: move('←'))
root.bind('<Right>', lambda event: move('→'))
root.bind('<Up>', lambda event: move('↑'))
root.bind('<Down>', lambda event: move('↓'))

enemy = Label(background=choice(colors_list))
enemy.place(x=enemy_x, y=enemy_y, width=enemy_size, height=enemy_size)

moving_enemy()

mainloop()
