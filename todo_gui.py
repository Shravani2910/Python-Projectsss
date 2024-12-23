import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()