from tkinter import *
from random import *

colors = ['Red', 'Green', 'Blue', 'Orange', 'Yellow', 'Black', 'Gray', 'White', 'Pink', 'Purple']
text = ['White', 'Black', 'White', 'Black', 'Black', 'White', 'Black', 'Black', 'Black', 'White']
score = 0
seconds = 30
value = 0
wrong = 0


def start(event):
    global value, wrong
    if seconds == 30:
        timer()
        value = randint(0, 9)
        root.config(bg=colors[value].lower())
        sc.config(bg=colors[value].lower(), fg=text[value].lower())
        tm.config(bg=colors[value].lower(), fg=text[value].lower())
        wr = Label(bg=colors[value].lower(), fg=text[value].lower(), text=wrong, font=('Consolas', 50))
        wr.place(x=200, y=0)
    next()


def next():
    global score, value, wrong
    if seconds > 0:
        if en.get().lower() == colors[value].lower():
            score += 1
            sc.config(text=score)
            value = randint(0, 9)
            root.config(bg=colors[value].lower())
            sc.config(bg=colors[value].lower(), fg=text[value].lower())
            tm.config(bg=colors[value].lower(), fg=text[value].lower())
            wr = Label(bg=colors[value].lower(), fg=text[value].lower(), text=wrong, font=('Consolas', 50))
            wr.place(x=200, y=0)
            en.delete(0, END)
        
        elif en.get().lower() != colors[value].lower() and len(en.get()) > 0 :
            wrong += 1
            wr = Label(bg=colors[value].lower(), fg=text[value].lower(), text=wrong, font=('Consolas', 50))
            wr.place(x=200, y=0)

        else:
            en.delete(0, END)
            


def timer():
    global seconds
    if seconds > 0:
        seconds -= 1
        tm.config(text=seconds)
        tm.after(1000, timer)


root = Tk()
root.title('ИГРА В ЦВЕТА')
root.geometry('450x250')

sc = Label(text=score, font=('Consolas', 50))
sc.place(relx=0.2, rely=0.2)

wr = Label(text=wrong, font=('Consolas', 50))
wr.place(x=200, y=0)

tm = Label(text=seconds, font=('Consolas', 50))
tm.place(relx=0.65, rely=0.2)

en = Entry(width=20, justify=CENTER, font=('Consolas', 30), insertontime=0)
en.focus()
en.place(relx=0.5, rely=0.7, anchor=CENTER)

root.bind('<Return>', start)
root.mainloop()
