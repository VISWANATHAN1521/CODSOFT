import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []


def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)


def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "[✓] " if task["done"] else "[ ] "
        listbox.insert(tk.END, status + task["task"])


def add_task():
    task_text = entry.get()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        entry.delete(0, tk.END)
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        update_listbox()
        save_tasks()
    else:
        messagebox.showinfo("Selection Error", "Please select a task.")


def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        update_listbox()
        save_tasks()
    else:
        messagebox.showinfo("Selection Error", "Please select a task.")

root = tk.Tk()
root.title("To-Do List App")

tasks = load_tasks()

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

done_btn = tk.Button(root, text="Mark as Done", command=mark_done)
done_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

update_listbox()
root.mainloop()
