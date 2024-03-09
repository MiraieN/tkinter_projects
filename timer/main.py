### Timer ###
from tkinter import *
from tkinter import messagebox

root = Tk()
width = 730
height = 510

root.title("Timer")
root.geometry(f'{width}x{height}+500+0')
# root.eval('tk::PlaceWindow . center')
root.configure(background="white")


def vars_to_zero():
    hourVar.set('00')
    minnVar.set('00')
    secVar.set('00')
    milsecVar.set('00')

def clicked():
    global stop_running

    buts["ok"]['state'] = 'disabled'
    hour['state'] = 'disabled'
    minn['state'] = 'disabled'
    sec['state'] = 'disabled'
    try:
        amount = int(hour.get()) * 3600 + int(minn.get()) * 60 + int(sec.get())
        for elem in (hour.get(), minn.get(), sec.get()):
            if len(elem) > 2:
                raise ValueError
    except ValueError:
        messagebox.showerror(message="Incorrect input")
        amount = 0

    hourlbl = Label(width=2, font=('futura', 90, 'bold'), textvariable=hourVar, background="white", borderwidth=0)
    minnlbl = Label(width=2, font=('futura', 90, 'bold'), textvariable=minnVar, background="white", borderwidth=0)
    seclbl = Label(width=2, font=('futura', 90, 'bold'), textvariable=secVar, background="white", borderwidth=0)

    hourlbl.grid(row=0, column=0)
    minnlbl.grid(row=0, column=2)
    seclbl.grid(row=0, column=4)

    while amount > -1:
        if hourVar.get() == "00" and minnVar.get() == "00" and secVar.get() == "00":
            break

        if stop_running:
            break

        for milsec in range(10, 5, -1):
            milsecVar.set(str(milsec))
            root.update()
            root.after(100)
        # root.after(500)

        dots1['text'] = ''
        dots2['text'] = ''
        root.update()

        for milsec in range(5, 0, -1):
            milsecVar.set(str(milsec))
            root.update()
            root.after(100)
        # root.after(500)

        dots1['text'] = ':'
        dots2['text'] = ':'
        root.update()

        amount -= 1

        temp = amount
        hourVar.set(str(amount // 3600))
        if hourVar.get() == '0':
            hourVar.set('00')
        amount %= 3600

        minnVar.set(str(amount // 60))
        if minnVar.get() == '0':
            minnVar.set('00')
        amount %= 60

        secVar.set(str(amount))
        amount = temp

        for which in (hourVar, minnVar, secVar):
            if len(which.get()) == 1:
                which.set('0' + which.get())

    vars_to_zero()

    if hourVar.get() == "00" and minnVar.get() == "00" and secVar.get() == "00":
        messagebox.showinfo(message="Time is up")

    buts["ok"]["state"] = 'normal'
    hour['state'] = 'normal'
    minn['state'] = 'normal'
    sec['state'] = 'normal'
    for lbl in (hourlbl, minnlbl, seclbl):
        lbl.destroy()

    stop_running = False

def to_stop():
    global stop_running
    vars_to_zero()
    stop_running = True

def to_loop():
    global count, height, width, height_maxed
    if not height_maxed:
        height += 140
    root.geometry(f'{width}x{height}+500+0')
    Label(width=2, font=('futura', 90, 'bold'), text=hourVar.get(), background="white", borderwidth=0).grid(row=count, column=0)
    Label(width=2, font=('futura', 90, 'bold'), text=minnVar.get(), background="white", borderwidth=0).grid(row=count, column=2)
    Label(width=2, font=('futura', 90, 'bold'), text=secVar.get(), background="white", borderwidth=0).grid(row=count, column=4)
    Label(width=2, font=('futura', 45, 'bold'), text=milsecVar.get(), background="white", borderwidth=0).grid(row=count, column=5, sticky='se', padx=20)

    Label(text=":", font=('futura', 90, 'bold'), width=1, background="white").grid(row=count, column=1)
    Label(text=":", font=('futura', 90, 'bold'), width=1, background="white").grid(row=count, column=3)

    count += 1

    if count == 5:
        height_maxed = True
        count = 2


buts = {}
height_maxed = False
stop_running = False
count = 2

hourVar = StringVar()
minnVar = StringVar()
secVar = StringVar()
milsecVar = StringVar()

vars_to_zero()

lab = Label(background="white")
lab.place(x=0, y=0, width=1000, height=1000)

hour = Entry(textvariable=hourVar, width=2, font=('futura', 90, 'bold'), background="white", borderwidth=0)
minn = Entry(textvariable=minnVar, width=2, font=('futura', 90, 'bold'), background="white", borderwidth=0)
sec = Entry(textvariable=secVar, width=2, font=('futura', 90, 'bold'), background="white", borderwidth=0)

milseclbl = Label(text="00", width=2, font=('futura', 45, 'bold'), textvariable=milsecVar, background="white", borderwidth=0)

dots1 = Label(text=":", font=('futura', 90, 'bold'), width=1, background="white")
dots2 = Label(text=":", font=('futura', 90, 'bold'), width=1, background="white")

buts["ok"] = Button(text="pognali", font=('ComicSans', 55, 'bold'), background="#F2F2F2", relief="flat", command=clicked)

buts["loop"] = Button(text="loop", font=('ComicSans', 25, 'bold'), background="#F2F2F2", relief="flat", command=to_loop)

buts["stop"] = Button(text="stop", font=('ComicSans', 25, 'bold'), background="#F2F2F2", relief="flat", command=to_stop)


def show(name):
    buts[name]['background'] = "#B7B7B7"


def deshow(event):
    for but in buts.keys():
        if buts[but]['background'] != "#F2F2F2":
            buts[but]['background'] = "#F2F2F2"

def bind_to_show(but):
    buts[but].bind('<Motion>', lambda event: show(but))

for but in buts.keys():
    bind_to_show(but)

lab.bind('<Motion>', deshow)

hour.grid(row=0, column=0, padx=10)
dots1.grid(row=0, column=1)
minn.grid(row=0, column=2)
dots2.grid(row=0, column=3)
sec.grid(row=0, column=4)
milseclbl.grid(row=0, column=5, sticky='se', padx=20)

buts["ok"].grid(columnspan=5, row=10, pady=20, ipady=10)
buts["stop"].grid(column=1, row=11)
buts["loop"].grid(columnspan=2, column=2, row=11)

mainloop()