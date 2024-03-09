import tkinter as tk

WHITE = '#FFFFFF'
RED = '#FF0000'
KEYBOARD_LINES = 3
letters = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
special_keys = ['<-', '○']
class KeyLabel(tk.Label):
    def __init__(self, key, font=("Roboto", 15, "bold")):
        self.key_text = key
        self.font = font
        tk.Label.__init__(self)
        self.configure(text=self.key_text, font=self.font)
        self.configure(bg=WHITE)

    def light_in(self):
        self.configure(bg=RED)

    def light_out(self):
        self.configure(bg=WHITE)

def onKeyPress(event):
    try:
        keys[event.char].light_in()
        text['text'] = "You pressed " + event.char
        input_window['text'] += event.char
    except KeyError:
        return
def event_handle(event):
    try:
        keys[event.char].light_out()
        text['text'] = "You released " + event.char
    except KeyError:
        return

def escape(event):
    root.destroy()

def backspace(event):
    if len(input_window['text']) > 0:
        input_window['text'] = input_window['text'][:-1]

root = tk.Tk()
root.geometry('300x200')


keys = {letter:KeyLabel(key=letter) for letter in letters}
for key in special_keys:
    keys[key] = KeyLabel(key=key)

row = 1
column = 1
for key in keys.values():
    key.grid(row=row, column=column)
    column += 1
    if column > len(letters)//3:
        column = 1
        row += 1

text = tk.Label(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.grid(row=row+1, columnspan=10)

input_window = tk.Label(root, background='black', foreground='white', font=('Comic Sans MS', 12))
input_window.grid(row=0, columnspan=10)

root.bind('<BackSpace>', backspace)
root.bind('<Escape>', escape)

root.bind('<KeyPress>', onKeyPress)
root.bind('<KeyRelease>', event_handle)
root.mainloop()
