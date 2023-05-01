import tkinter as tk
from tkinter import colorchooser

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.master.geometry("800x600")

        # Create menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Create file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit)

        # Create color menu
        self.color_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Change color", menu=self.color_menu)
        self.color_menu.add_command(label="Text", command=self.change_text_color)
        self.color_menu.add_command(label="Background", command=self.change_bg_color)

        # Create text widget
        self.text_widget = tk.Text(self.master, font=("Arial", 12))
        self.text_widget.pack(fill=tk.BOTH, expand=True)

    def new_file(self):
        self.text_widget.delete("1.0", tk.END)

    def open_file(self):
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert(tk.END, content)

    def save_file(self):
        file_path = tk.filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_widget.get("1.0", tk.END)
                file.write(content)

    def exit(self):
        self.master.destroy()

    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_widget.config(fg=color)

    def change_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_widget.config(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    TextEditor(root)
    root.mainloop()
