from tkinter import *
import random

def event_no(event):
    btn_no.place(x=random.randint(0, 400), y=random.randint(0, 400))

def event_yes(i=1):
    i += 1
    if i == 500:
        print('thanks for watch')
        return
    heart = '\U0001f493'
    label_heart = Label(root, text=heart, font=('Consolas', 30), bg='white', fg='red')
    label_heart.place(x=random.randint(0, 500), y=random.randint(0, 500))
    label_heart.after(10, event_yes, i)

root = Tk()
root.title('Hello')
root.geometry('500x500')
root.resizable(False, False)

label = Label(root, text='Do you want to my girlfriend?', font=('Consolas', 20))
label.pack(pady=80)

btn_yes = Button(root, text='Yes', font=('Consolas', 20), width=5, command=event_yes)
btn_yes.place(x=100, y=200)

btn_no = Button(root, text='No', font=('Consolas', 20), width=5)
btn_no.place(x=300, y=200)
btn_no.bind('<Enter>', event_no)

root.mainloop()