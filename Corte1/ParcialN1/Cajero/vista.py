class VistaCajero:
    def mostrar_mensaje_bienvenida(self):
        print(" Bienvenido al Cajero Virtual ChrisIndustries")

    def mostrar_menu(self):
        print("\nSeleccione una opción:")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("4. Salir")

    def solicitar_opcion(self):
        return input("Ingrese el número de la opción: ")

    def solicitar_monto(self, operacion: str):
        try:
            monto = int(input(f"Ingrese el monto a {operacion} (COP): "))
            return monto
        except ValueError:
            raise ValueError("Debe ingresar un número válido.")

    def mostrar_saldo(self, saldo: int):
        print(f"\n Su saldo actual es: COP {saldo:,}")

    def mostrar_mensaje_despedida(self):
        print("\n Gracias por usar el cajero. ¡Hasta pronto!")

    def mostrar_error(self, mensaje: str):
        print(f" Error: {mensaje}")
