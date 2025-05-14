# calc.py

class Calculadora:
    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("División entre cero no permitida.")
        return a / b

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Módulo entre cero no permitido.")
        return a % b
