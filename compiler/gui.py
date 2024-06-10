import tkinter as tk
from tkinter import filedialog, messagebox
import access

class CompilerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compiler App")

        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load File", command=self.load_file)
        self.load_button.pack(pady=10)

        self.execute_button = tk.Button(self.root, text="Execute", command=self.execute_code)
        self.execute_button.pack(pady=10)

        self.output_text = tk.Text(self.root, height=20, width=80)
        self.output_text.pack(pady=10)

    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            with open(self.file_path, 'r') as file:
                self.input_code = file.read()
            messagebox.showinfo("File Loaded", f"File loaded successfully: {self.file_path}")

    def execute_code(self):
        if hasattr(self, 'input_code'):
            output = access.execute(self.input_code)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output)
        else:
            messagebox.showwarning("No File Loaded", "Please load a file first")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompilerApp(root)
    root.mainloop()
