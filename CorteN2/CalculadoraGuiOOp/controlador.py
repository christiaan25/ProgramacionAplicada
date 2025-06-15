

from modelo import CalculatorModel
from vista import CalculatorView

class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self)

    def run(self):
        self.view.mainloop()

    def on_button_click(self, char):
        if char == "=":
            expression = self.view.get_display()
            result = self.model.evaluate_expression(expression)
            self.view.set_display(str(result))
        elif char == "C":
            self.view.set_display("")
        else:
            current = self.view.get_display()
            self.view.set_display(current + char)
