#main y interfaz.py 

from calc import Calculadora

def mostrar_menu():
    print("\n=== CALCULADORA EN CONSOLA CON POO ===")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Módulo")
    print("6. Salir")

def solicitar_valores():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        return a, b
    except ValueError:
        print(" Error: Ingrese solo números válidos.")
        return None, None

def main():
    calc = Calculadora()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "6":
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        a, b = solicitar_valores()
        if a is None or b is None:
            continue

        try:
            if opcion == "1":
                resultado = calc.add(a, b)
            elif opcion == "2":
                resultado = calc.substract(a, b)
            elif opcion == "3":
                resultado = calc.multiply(a, b)
            elif opcion == "4":
                resultado = calc.divide(a, b)
            elif opcion == "5":
                resultado = calc.modulo(a, b)
            else:
                print(" Opción inválida.")
                continue

            print(f" Resultado: {resultado}")
        except ZeroDivisionError as e:
            print(f" {e}")

if __name__ == "__main__":
    main()
