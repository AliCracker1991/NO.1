from tkinter import *
import random
from tkinter import messagebox
import tkinter.messagebox

colors = ['red', 'yellow', 'black', 'white', 'brown', 'blue', 'purple', 'orange','green','pink',]
score = 0
timeleft = 30
game_started = False

def startgame(event=None):
    global game_started
    if not game_started:
        game_started = True
        countdown()
        nextcolor()

        root.unbind('<Return>')
        root.bind('<Return>', nextcolor)

def nextcolor(event=None):
    global score
    global timeleft
    if timeleft > 0:
        user_input = j.get().lower()

        if user_input == label.cget('fg'):
            score += 1
            scorelb.config(text="امتیاز شما: " + str(score))
        
        j.delete(0, END)
        random.shuffle(colors)

        label.config(text=str(colors[0]), fg=str(colors[1]))
    else:
        j.config(state='disabled')
        messagebox.showinfo("پایان بازی", f"بازی تمام شد!\nامتیاز نهایی: {score}")

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timelb.config(text="زمان باقی‌مانده: " + str(timeleft))
        timelb.after(1000, countdown)
    else:
        j.config(state='disabled')
        messagebox.showinfo("پایان بازی", f"بازی تمام شد!\nامتیاز نهایی: {score}")

root = Tk()
root.title('بازی تشخیص رنگ')
root.geometry('400x400')

lbl = Label(root, text="رنگ نمایش داده شده را وارد کنید )", font=('Tahoma', 12))
lbl.pack(pady=10)

scorelb = Label(root, text="امتیاز: 0", font=('Tahoma', 12, 'bold'))
scorelb.pack()

timelb = Label(root, text="زمان باقی‌مانده: 30", font=('Tahoma', 12, 'bold'))
timelb.pack()

label = Label(root, font=('Comic Sans MS', 40, 'bold'))
label.pack(pady=20)

j = Entry(root, width=20, font=('Tahoma', 14))
j.pack(pady=10)
j.focus_set()


root.bind('<Return>', startgame)

root.mainloop()

