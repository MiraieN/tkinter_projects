import tkinter as t


root = t.Tk()
width, height = root.winfo_screenwidth()//2, root.winfo_screenheight()//2
root.geometry(f"{width}x{height}+{int(width/2)}+{int(height/2)}")

canv = t.Canvas()
canv.pack()
t.Label(canv, text="00:", font=('futura', 90, 'bold')).grid(row=0, column=0)
t.Label(canv, text="01:", font=('futura', 90, 'bold')).grid(row=0, column=1)
t.Label(canv, text="02", font=('futura', 90, 'bold')).grid(row=0, column=2)

root.mainloop()