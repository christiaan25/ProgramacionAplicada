
import tkinter as tk

class CalculatorView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Calculadora MVC")
        self.geometry("300x400")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
        self.display.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(expand=True, fill="both")

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', 'C', '+'),
            ('=',)
        ]

        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(row_frame, text=char, font=("Arial", 18), relief=tk.RAISED, bd=4,
                                command=lambda ch=char: self.controller.on_button_click(ch))
                btn.pack(side=tk.LEFT, expand=True, fill="both")

    def get_display(self):
        return self.display.get()

    def set_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, value)
