

class CalculatorModel:
    def __init__(self):
        self.result = 0

    def evaluate_expression(self, expression):
        try:
            self.result = eval(expression)
            return self.result
        except Exception:
            return "Error"
