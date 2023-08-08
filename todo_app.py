import tkinter as tk
from tkinter import messagebox
from tkinter import *

def addition():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter a task!")

def removing():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def updating():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        updated_task = task_entry.get()
        if updated_task:
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task!")
    else:
        messagebox.showwarning("Warning", "Please select a task to update!")

def clearing():
    tasks_listbox.delete(0, tk.END)

root = Tk()
root.geometry("340x400")
root.title("Todo app")
task_entry = tk.Entry(root, width=28, font="time 15", bg="light green")
task_entry.place(x=10,y=10)
add_button = tk.Button(root, text="Add Task", command=addition,font="time 10", bg = "light green")
add_button.place(x=10, y=45)
tasks_listbox = tk.Listbox(root, width=52, height=18, bg="light green")
tasks_listbox.place(x =10, y=90)
remove_button = tk.Button(root, text="Remove Task", command=removing, font="time 10")
remove_button.place(x=80, y=45)
update_button = tk.Button(root, text="Update Task", command=updating, font="time 10")
update_button.place(x=172, y=45)
clear_button = tk.Button(root, text="Clear All", command=clearing, font="time 10", bg="light pink")
clear_button.place(x=260, y=45)
root.mainloop()
