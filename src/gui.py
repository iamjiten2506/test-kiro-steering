import tkinter as tk
from tkinter import messagebox
from calculator import calculate


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        
        self.current = ""
        self.operation = None
        self.first_number = None
        
        # Display
        self.display = tk.Entry(root, font=("Arial", 20), bd=10, justify="right", bg="#f0f0f0")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('←', 5, 1)
        ]
        
        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(root, text=text, font=("Arial", 16), bg="#4CAF50", fg="white",
                               command=self.calculate_result)
            elif text in ['+', '-', '*', '/']:
                btn = tk.Button(root, text=text, font=("Arial", 16), bg="#ff9800", fg="white",
                               command=lambda t=text: self.set_operation(t))
            elif text == 'C':
                btn = tk.Button(root, text=text, font=("Arial", 16), bg="#f44336", fg="white",
                               command=self.clear)
            elif text == '←':
                btn = tk.Button(root, text=text, font=("Arial", 16), bg="#9e9e9e", fg="white",
                               command=self.backspace)
            else:
                btn = tk.Button(root, text=text, font=("Arial", 16),
                               command=lambda t=text: self.append_number(t))
            
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew", ipadx=20, ipady=20)
        
        # Configure grid weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
    
    def append_number(self, num):
        self.current += str(num)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current)
    
    def set_operation(self, op):
        if self.current:
            self.first_number = float(self.current)
            self.operation = op
            self.current = ""
    
    def calculate_result(self):
        if self.current and self.first_number is not None and self.operation:
            try:
                second_number = float(self.current)
                result = calculate(self.first_number, second_number, self.operation)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current = str(result)
                self.first_number = None
                self.operation = None
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.clear()
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.clear()
    
    def clear(self):
        self.current = ""
        self.first_number = None
        self.operation = None
        self.display.delete(0, tk.END)
    
    def backspace(self):
        self.current = self.current[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current)


def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
