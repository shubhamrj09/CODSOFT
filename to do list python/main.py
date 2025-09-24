import os
import tkinter as tk
from tkinter import ttk, messagebox
import json

class ModernTodo:
    def __init__(self, master):
        self.master = master
        self.master.title("✨ Modern To-Do List")
        self.master.geometry("500x600")
        self.master.configure(bg="#f5f7fa")

        style = ttk.Style()
        style.theme_use("clam")

        # Custom Button Style
        style.configure("TButton",
                        font=('Helvetica', 11, 'bold'),
                        padding=10,
                        relief="flat",
                        background="#4CAF50",
                        foreground="white",
                        borderwidth=0)
        style.map("TButton",
                  background=[("active", "#45a049")])

        # Treeview Style
        style.configure("Treeview",
                        font=('Helvetica', 11),
                        rowheight=30,
                        background="white",
                        fieldbackground="white")
        style.configure("Treeview.Heading",
                        font=('Helvetica', 12, 'bold'),
                        background="#4CAF50",
                        foreground="white")
        style.map("Treeview",
                  background=[("selected", "#d1f2eb")])

        # Top Header
        self.header = tk.Frame(self.master, bg="#4CAF50", height=70)
        self.header.pack(fill="x")

        self.title_label = tk.Label(self.header, text="📝 My Tasks",
                                    font=("Helvetica", 20, "bold"),
                                    bg="#4CAF50", fg="white")
        self.title_label.pack(pady=15)

        # Main Frame
        self.frame = ttk.Frame(self.master, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Task Entry (styled like search bar)
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var,
                                   font=("Helvetica", 12), bd=0,
                                   bg="#ffffff", fg="#333")
        self.task_entry.grid(row=0, column=0, padx=5, pady=10, sticky="ew", ipady=8)
        self.task_entry.configure(highlightthickness=1, highlightbackground="#ccc", highlightcolor="#4CAF50")

        self.add_button = tk.Button(self.frame, text="➕ Add",
                                    font=("Helvetica", 11, "bold"),
                                    bg="#4CAF50", fg="white", bd=0,
                                    activebackground="#45a049",
                                    command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10, sticky="ew", ipadx=5)

        # Task Tree (inside card frame)
        self.tree_frame = tk.Frame(self.frame, bg="white", bd=1, relief="solid")
        self.tree_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=10)

        self.task_tree = ttk.Treeview(self.tree_frame, columns=("Task",), show="headings", height=15)
        self.task_tree.heading("Task", text="Your Tasks")
        self.task_tree.pack(fill="both", expand=True, side="left")

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.task_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.task_tree.configure(yscrollcommand=scrollbar.set)

        # Buttons at bottom
        self.delete_button = tk.Button(self.frame, text="🗑 Delete",
                                       font=("Helvetica", 11, "bold"),
                                       bg="#e74c3c", fg="white", bd=0,
                                       activebackground="#c0392b",
                                       command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=15, sticky="ew")

        self.save_button = tk.Button(self.frame, text="💾 Save",
                                     font=("Helvetica", 11, "bold"),
                                     bg="#3498db", fg="white", bd=0,
                                     activebackground="#2980b9",
                                     command=self.save_tasks)
        self.save_button.grid(row=2, column=1, padx=5, pady=15, sticky="ew")

        # Grid expansion
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

        # Load saved tasks
        self.load_tasks()
        self.apply_row_colors()

    def apply_row_colors(self):
        """Alternate row colors"""
        for index, item in enumerate(self.task_tree.get_children()):
            if index % 2 == 0:
                self.task_tree.item(item, tags=("evenrow",))
            else:
                self.task_tree.item(item, tags=("oddrow",))

        self.task_tree.tag_configure("evenrow", background="#fdfdfd")
        self.task_tree.tag_configure("oddrow", background="#f7f7f7")

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.task_tree.insert("", tk.END, values=(task,))
            self.task_var.set("")
            self.apply_row_colors()
        else:
            messagebox.showwarning("⚠ Warning", "Please enter a task.")

    def delete_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            self.task_tree.delete(selected_item)
            self.apply_row_colors()
        else:
            messagebox.showwarning("⚠ Warning", "Please select a task to delete.")

    def save_tasks(self):
        tasks = [self.task_tree.item(child)['values'][0] for child in self.task_tree.get_children()]
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        messagebox.showinfo("✅ Saved", "Your tasks have been saved successfully.")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                tasks = json.load(f)
            for task in tasks:
                self.task_tree.insert('', tk.END, values=(task,))
            self.apply_row_colors()
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ModernTodo(root)
    root.mainloop()
