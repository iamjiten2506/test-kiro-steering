import tkinter as tk
from tkinter import ttk
import random


class DiceSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Title
        title = tk.Label(root, text="🎲 Dice Rolling Simulator 🎲", font=("Arial", 18, "bold"), fg="#2196F3")
        title.pack(pady=20)
        
        # Dice display frame
        self.dice_frame = tk.Frame(root, bg="#f0f0f0", bd=5, relief="ridge")
        self.dice_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.dice_labels = []
        self.dice_values = []
        
        # Number of dice selector
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)
        
        tk.Label(control_frame, text="Number of Dice:", font=("Arial", 12)).pack(side="left", padx=5)
        
        self.dice_count = tk.IntVar(value=2)
        dice_spinner = ttk.Spinbox(control_frame, from_=1, to=6, textvariable=self.dice_count, 
                                   width=5, font=("Arial", 12), command=self.update_dice_display)
        dice_spinner.pack(side="left", padx=5)
        
        # Roll button
        self.roll_button = tk.Button(root, text="🎲 ROLL DICE 🎲", font=("Arial", 16, "bold"),
                                     bg="#4CAF50", fg="white", command=self.roll_dice,
                                     padx=20, pady=10)
        self.roll_button.pack(pady=10)
        
        # Result display
        self.result_label = tk.Label(root, text="Total: 0", font=("Arial", 14, "bold"), fg="#ff9800")
        self.result_label.pack(pady=10)
        
        # History
        self.history_label = tk.Label(root, text="Last 3 rolls:", font=("Arial", 10))
        self.history_label.pack()
        
        self.history_text = tk.Label(root, text="", font=("Arial", 9), fg="#666")
        self.history_text.pack()
        
        self.history = []
        
        # Initialize display
        self.update_dice_display()
    
    def update_dice_display(self):
        # Clear existing dice
        for widget in self.dice_frame.winfo_children():
            widget.destroy()
        
        self.dice_labels = []
        count = self.dice_count.get()
        
        # Create dice display
        for i in range(count):
            dice_label = tk.Label(self.dice_frame, text="?", font=("Arial", 48, "bold"),
                                 bg="white", width=3, height=1, relief="solid", bd=2)
            dice_label.pack(side="left", padx=10, pady=20)
            self.dice_labels.append(dice_label)
    
    def roll_dice(self):
        count = self.dice_count.get()
        self.dice_values = [random.randint(1, 6) for _ in range(count)]
        
        # Animate dice
        for i, label in enumerate(self.dice_labels):
            label.config(text=str(self.dice_values[i]), fg="#2196F3")
        
        # Calculate total
        total = sum(self.dice_values)
        self.result_label.config(text=f"Total: {total}")
        
        # Update history
        roll_str = f"{self.dice_values} = {total}"
        self.history.append(roll_str)
        if len(self.history) > 3:
            self.history.pop(0)
        
        self.history_text.config(text="\n".join(self.history))


def main():
    root = tk.Tk()
    app = DiceSimulator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
