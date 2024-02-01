import tkinter as tk
from tkinter import simpledialog, messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = []

        # GUI Components
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_new_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_selected_task)
        self.remove_button.pack()

        self.show_button = tk.Button(root, text="Show Tasks", command=self.display_all_tasks)
        self.show_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.destroy)
        self.quit_button.pack()

    def add_new_task(self):
        task_input = simpledialog.askstring("Add Task", "Enter a new task:")
        if task_input:
            self.tasks.append(task_input)
            messagebox.showinfo("Task Added", f"Task '{task_input}' added successfully!")

    def remove_selected_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            if 0 <= selected_index < len(self.tasks):
                selected_task = self.tasks.pop(selected_index)
                messagebox.showinfo("Task Removed", "Task '{selected_task}' removed successfully!")
                self.display_all_tasks()

    def display_all_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def initiate_app():
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()

if __name__ == "__main__":
    initiate_app()
