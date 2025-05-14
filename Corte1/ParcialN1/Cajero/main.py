from modelo import Cuenta
from vista import VistaCajero
from controlador import ControladorCajero

def main():
    cuenta_usuario = Cuenta(titular="Usuario", saldo=50000)  # saldo inicial en COP
    vista = VistaCajero()
    controlador = ControladorCajero(cuenta_usuario, vista)
    controlador.iniciar()

if __name__ == "__main__":
    main()


# cajero/
#modelo.py         # Define los datos y la lógica del cajero 
#vista.py          # Se encarga de la interacción con el usuario
#controlador.py    # Orquesta el flujo entre modelo y vista
#main.py           # Punto de entrada del programa

#Flujo de ejecución:

   #1). main.py crea una cuenta, la vista y el controlador.
   #2). El controlador muestra el menú usando la vista.
   #3). El usuario elige una opción (depositar, retirar, consultar, salir).
   #4). El controlador usa el modelo (Cuenta) para realizar la acción.
   #5). La vista muestra el resultado o errores (como saldo insuficiente).
   #6). El ciclo se repite hasta que el usuario decide salir.