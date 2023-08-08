from tkinter import *
import random
import pyperclip
import string

root = Tk()
root.geometry("600x400")
root.title("Password generator app")
value = StringVar()

def generate():
    password = ""
    num = int(entry.get())
    s_lower = string.ascii_lowercase
    s_upper = string.ascii_uppercase
    s_digits = string.digits
    s_punctuation = string.punctuation
    s = []
    s.extend(list(s_lower))
    s.extend(list(s_upper))
    s.extend(list(s_digits))
    s.extend(list(s_punctuation))
    random.shuffle(s)
    for i in range(num):
        password += s[i]
    l_p = Label(root, text="Password: ", font="Arial")
    l_p.place(x=70, y=80)
    l_gp = Label(root, text = password, font="Arial", bg ="green")
    l_gp.place(x=250, y=80)
    value.set(password)

def copy():
    to_copy = value.get()
    temp = ""
    for i in to_copy:
        temp += i
    pyperclip.copy(temp)

l_pl = Label(root, text = "Password length: ", font = "Arial")
l_pl.place(x = 70, y = 20)
entry = Entry(root, width = 26,  font = 'time 13 bold')
entry.place(x = 250, y=24)
btn_gp = Button(root, text = "Generate Password", font="time 13 bold"
                ,width = 20, command = generate, bg = "green")
btn_gp.place(x = 180, y=250)
btn_copy = Button(root, text = "Copy Password", font="time 13 bold"
                ,width = 20, command = copy, bd=4)
btn_copy.place(x = 180, y=290)
root.mainloop()
