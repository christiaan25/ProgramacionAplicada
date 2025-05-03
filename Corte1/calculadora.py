
# operaciones matemáticas básicas

class Calculator:
    def __init__(self): #constructor 
        
        pass  # Constructor vacío

    def add(self, a, b): # función sumar.
        return a + b #Devuelve el resultado de sumar a y b.

    def substract(self, a, b):# función restar.
        return a - b #Devuelve a menos b.

    def multiply(self, a, b):  #función multiplicar.
        return a * b  #Devuelve a por b.

    def divide(self, a, b): # función dividir.
        return a / b  #Devuelve a dividido entre b. Esto retorna un número decimal si b es 0 pyton da error 

    def modulo(self, a, b): #Esta función da el residuo de la división
        return a % b #Devuelve el módulo de a entre b.

# Parte principal del programa
if __name__ == "__main__":
    my_calculator = Calculator()  #objeto de la clase Calculator.
    print(my_calculator.add(5, 7))  #  Llama al método add() de la calculadora, pasando los números 5 y 7.
                                     #La calculadora los suma y devuelve 12, que se imprime en pantalla.
                                    
    print(my_calculator.substract(45, 11)) # resta 
    print(my_calculator.multiply(3, 2))   #multiplicacion 
