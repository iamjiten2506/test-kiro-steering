import tkinter as tk
from tkinter import messagebox
from calculator import calculate


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x600")
        self.root.resizable(False, False)
        
        self.current = ""
        self.operation = None
        self.first_number = None
        self.history = []
        self.secret_code = ""  # Easter egg tracker
        
        # History display
        self.history_frame = tk.Frame(root, bg="#e0e0e0")
        self.history_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="ew")
        
        tk.Label(self.history_frame, text="History:", font=("Arial", 10, "bold"), bg="#e0e0e0").pack(anchor="w")
        
        self.history_text = tk.Text(self.history_frame, height=5, font=("Arial", 9), bg="#f5f5f5", state="disabled")
        self.history_text.pack(fill="both", expand=True)
        
        # Display
        self.display = tk.Entry(root, font=("Arial", 20), bd=10, justify="right", bg="#f0f0f0")
        self.display.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        # Button layout
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('C', 6, 0), ('←', 6, 1), ('CH', 6, 2)
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
            elif text == 'CH':
                btn = tk.Button(root, text=text, font=("Arial", 12), bg="#2196F3", fg="white",
                               command=self.clear_history)
            else:
                btn = tk.Button(root, text=text, font=("Arial", 16),
                               command=lambda t=text: self.append_number(t))
            
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew", ipadx=20, ipady=20)
        
        # Configure grid weights
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
    
    def append_number(self, num):
        self.current += str(num)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current)
        
        # Easter egg: Check for secret code "1337"
        self.secret_code += str(num)
        if len(self.secret_code) > 4:
            self.secret_code = self.secret_code[-4:]
        
        if self.secret_code == "1337":
            self.open_dice_game()
            self.secret_code = ""
    
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
                
                # Add to history
                history_entry = f"{self.first_number} {self.operation} {second_number} = {result}"
                self.history.append(history_entry)
                self.update_history_display()
                
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
    
    def update_history_display(self):
        self.history_text.config(state="normal")
        self.history_text.delete(1.0, tk.END)
        for entry in self.history[-5:]:  # Show last 5 entries
            self.history_text.insert(tk.END, entry + "\n")
        self.history_text.config(state="disabled")
    
    def clear_history(self):
        self.history = []
        self.update_history_display()
    
    def open_dice_game(self):
        from dice_game import DiceSimulator
        dice_window = tk.Toplevel(self.root)
        DiceSimulator(dice_window)


def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
