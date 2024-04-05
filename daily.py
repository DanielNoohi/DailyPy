import tkinter as tk
from tkinter import messagebox
from datetime import date

def save_tasks():
    tasks = task_text.get("1.0", tk.END)
    today = date.today()
    filename = f"tasks_{today}.txt"
    with open(filename, "w", encoding='utf-8') as file: # Set encoding to utf-8
        file.write(tasks)
    messagebox.showinfo("Tasks Saved", "Tasks saved successfully.")

def clear_tasks():
    task_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Daily Task Manager")

task_text = tk.Text(root, height=10, width=50, font=("Arial", 12)) # Specify font to support Persian characters
task_text.pack(pady=10)

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(root, text="Clear Tasks", command=clear_tasks)
clear_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
