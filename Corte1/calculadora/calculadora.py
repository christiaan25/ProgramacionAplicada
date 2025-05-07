
# Clase que define operaciones matemáticas básicas
class Calculator:
    def __init__(self):
        # Constructor vacío, no se necesita inicialización de atributos por ahora
        pass

    def add(self, a, b):
        # Devuelve la suma de a y b
        return a + b

    def substract(self, a, b):
        # Devuelve la resta de a menos b
        return a - b

    def multiply(self, a, b):
        # Devuelve la multiplicación de a por b
        return a * b

    def divide(self, a, b):
        try:
            # Intenta dividir a entre b
            return a / b
        except ZeroDivisionError:
            # Maneja el error si b es cero
            return "Error: División entre cero no permitida."

    def modulo(self, a, b):
        try:
            # Intenta calcular el residuo de a entre b
            return a % b
        except ZeroDivisionError:
            # Maneja el error si b es cero
            return "Error: Módulo entre cero no permitido."

# Clase que maneja la interacción con el usuario
class CalculatorApp:
    def __init__(self):
        # Crea una instancia de la calculadora
        self.calculator = Calculator()

    def run(self):
        print("Bienvenido a la Calculadora en Consola con POO\n")
        
        # Menú de operaciones
        print("Operaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo")

        # se le Solicita al usuario que seleccione una operación
        opcion = input("Seleccione una opción (1-5): ")

        # se le Solicita al usuario los dos números para operar
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Ingrese solo números válidos.")
            return

        # Ejecuta la operación correspondiente
        if opcion == "1":
            print("Resultado:", self.calculator.add(a, b))
        elif opcion == "2":
            print("Resultado:", self.calculator.substract(a, b))
        elif opcion == "3":
            print("Resultado:", self.calculator.multiply(a, b))
        elif opcion == "4":
            print("Resultado:", self.calculator.divide(a, b))
        elif opcion == "5":
            print("Resultado:", self.calculator.modulo(a, b))
        else:
            print("Opción inválida.")

# Punto de entrada del programa
if __name__ == "__main__":
    app = CalculatorApp()  # Crea la aplicación
    app.run()              # Ejecuta la aplicación
