from tkinter import *


def calculator(buttons, font_size, bg, but_color, x_y):
    window = Tk()
    window.title("daa")
    window.geometry(f'{x_y[0]}x{x_y[1]}')

    def def_text(elem):
        if entre.get() == "error":
            clear_f()
        main_text.set(entre.get() + elem)

    main_text = StringVar()

    def clear_f():
        main_text.set("")

    def solve_f():
        try:
            main_text.set(eval(entre.get()))
        except:
            main_text.set("error")

    entre = Entry(font=("comic sans ms", font_size), textvariable=main_text)  # state="disabled"
    entre.grid(row=0, columnspan=4, ipady=20, pady=4)

    but7 = Button(text=buttons[0], command=lambda: def_text("7"), font=("comic sans ms", font_size))
    but7.grid(row=1, column=0, padx=4, pady=4)

    but8 = Button(text=buttons[1], command=lambda: def_text("8"), font=("comic sans ms", font_size))
    but8.grid(row=1, column=1, padx=4, pady=4)

    but9 = Button(text=buttons[2], command=lambda: def_text("9"), font=("comic sans ms", font_size))
    but9.grid(row=1, column=2, padx=4, pady=4)

    butD = Button(text=buttons[3], command=lambda: def_text("-"), font=("comic sans ms", font_size))
    butD.grid(row=1, column=3, padx=4, pady=4)

    butG = Button(text=buttons[4], command=lambda: def_text("4"), font=("comic sans ms", font_size))
    butG.grid(row=2, column=0, padx=4, pady=4)

    but5 = Button(text=buttons[5], command=lambda: def_text("5"), font=("comic sans ms", font_size))
    but5.grid(row=2, column=1, padx=4, pady=4)

    but6 = Button(text=buttons[6], command=lambda: def_text("6"), font=("comic sans ms", font_size))
    but6.grid(row=2, column=2, padx=4, pady=4)

    butT = Button(text=buttons[7], command=lambda: def_text("+"), font=("comic sans ms", font_size))
    butT.grid(row=2, column=3, padx=4, pady=4)

    but0 = Button(text=buttons[8], command=lambda: def_text("1"), font=("comic sans ms", font_size))
    but0.grid(row=3, column=0, padx=4, pady=4)

    but1 = Button(text=buttons[9], command=lambda: def_text("2"), font=("comic sans ms", font_size))
    but1.grid(row=3, column=1, padx=4, pady=4)

    but2 = Button(text=buttons[10], command=lambda: def_text("3"), font=("comic sans ms", font_size))
    but2.grid(row=3, column=2, padx=4, pady=4)

    but3 = Button(text=buttons[11], command=lambda: def_text("0"), font=("comic sans ms", font_size))
    but3.grid(row=3, column=3, padx=4, pady=4)

    butC = Button(text=buttons[12], command=clear_f, font=("comic sans ms", font_size))
    butC.grid(row=4, column=0, padx=4, pady=4)

    butH = Button(text=buttons[13], command=lambda: def_text("*"), font=("comic sans ms", font_size))
    butH.grid(row=4, column=1, padx=4, pady=4)

    butF = Button(text=buttons[14], command=solve_f, font=("comic sans ms", font_size))
    butF.grid(row=4, column=2, padx=4, pady=6)

    butV = Button(text=buttons[15], command=lambda: def_text("/"), font=("comic sans ms", font_size))
    butV.grid(row=4, column=3, padx=4, pady=4)

    mainloop()


buttons = ("7", "8", "9", "-", "4", "5", "6", "+", "1", "2", "3", "0", "C", "*", "=", "/")  # всі кнопки 15 штук
calculator(buttons, 14, "red", 'grey', (240, 300))
