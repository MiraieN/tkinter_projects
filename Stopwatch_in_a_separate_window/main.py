import tkinter as t

class Stopwatch:
    def __init__(self):
        self.alive = True

        self.window = t.Tk()
        self.window.geometry(f"{width//2}x{height//2}+{width//4}+{height//4}")
        self.window.resizable(False, False)

        self.Canvas = t.Canvas(self.window, relief="solid")
        self.MinSecCanvas = t.Canvas(self.Canvas)

        self.MinutesEntry = t.Entry(self.MinSecCanvas)
        self.SecondsEntry = t.Entry(self.MinSecCanvas)
        self.ok_button = t.Button(self.Canvas, text="ok", command=self.create_label)
        self.time_lab = t.Label(self.Canvas, text="", font="Arial 32 bold")

        self.Canvas.pack(ipady=height//8)
        self.MinSecCanvas.pack(ipady=20)
        self.MinutesEntry.pack(ipady=20, ipadx=10, side="left")
        self.SecondsEntry.pack(ipady=20, ipadx=10, side="right")
        self.time_lab.pack(ipady=20, side="bottom")
        self.ok_button.pack(pady=20, side="bottom")

    def create_label(self):
        minutes_entry, seconds_entry = 0, 0
        if self.MinutesEntry.get() != "":
            minutes_entry = int(self.MinutesEntry.get())
        if self.SecondsEntry.get() != "":
            seconds_entry = int(self.SecondsEntry.get())


        full_time = minutes_entry * 60 + seconds_entry
        while True:
            minn = full_time//60
            sec = full_time - minn * 60

            if len(str(sec)) == 1:
                self.time_lab['text'] = f"{full_time//60}:0{full_time - full_time//60*60}"
            else:
                self.time_lab['text'] = f"{full_time // 60}:{full_time - full_time // 60 * 60}"
            if minn == 0 and sec == 0:
                from tkinter import messagebox
                messagebox.showinfo(message="Type is up!")
            full_time -= 1

            self.window.update()
            self.window.after(1000)


    def destroy(self):
        self.alive = False
        self.window.destroy()

    def is_alive(self):
        return True if self.alive else False



root = t.Tk()
width, height = root.winfo_screenwidth()//2, root.winfo_screenheight()//2
root.geometry(f"{width}x{height}+{int(width/2)}+{int(height/2)}")

def check_func(event):
    global timer
    if not check_var.get():
        timer = Stopwatch()
    elif check_var.get():
        if timer.is_alive():
            timer.destroy()

    root.update()

timer = ''
check_var = t.IntVar()
check = t.Checkbutton(text="Stopwatch", variable=check_var)
check.pack()
check.bind('<Button-1>', check_func)


root.mainloop()