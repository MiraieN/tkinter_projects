from tkinter import *
import ttkbootstrap as ttk
# from tkinter import ttk

# root = Tk()
# root.geometry("430x180+40+10")
# root.configure(bg="white")
# root.title("Demo")
# root.iconbitmap("icon.ico")
#
# Label(text="Miles to kilometers", bg="white", font=("Arial", 30, "bold")).\
#     grid(row=0, pady=10, columnspan=2, padx=30)
#
# new_entry = Entry(font=12, relief="sunken")
# new_entry.grid(row=1, column=0, sticky="e", ipady=4)
#
# Button(text="convert", fg="white", font=("", 11, "bold"), bg="#FA8072",
#        command=lambda: new_label.config(text=round(int(new_entry.get())*1.609, 1)))\
#     .grid(row=1, column=1, sticky="w", padx=5)
#
# new_label = Label(text="16.1", font=("Calibri", 26), bg="white")
# new_label.grid(row=2, pady=6, columnspan=2)


# тут пошукай другі теми
root = ttk.Window(themename='darkly')
root.geometry("300x150+40+10")
root.configure()
root.title("Demo")
root.iconbitmap("icon.ico")

label = ttk.Label(master=root, text="Miles to kilometers", font="Calibri 24 bold")
label.pack()

frame = ttk.Frame(master=root)
entry = ttk.Entry(master=frame, background="white")
button = ttk.Button(master=frame, text="convert",
                command=lambda: out_label.config(text=round(int(entry.get())*1.609, 1)))

entry.pack(side='left', padx=10)
button.pack(side='left')
frame.pack(pady=10)

out_label = ttk.Label(text="", font="Calibri 24 bold")
out_label.pack(pady=5)

root.mainloop()


# https://youtu.be/mop6g-c5HEY?t=1282


