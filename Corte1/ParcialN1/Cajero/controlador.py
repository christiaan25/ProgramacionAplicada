from modelo import Cuenta
from vista import VistaCajero

class ControladorCajero:
    def __init__(self, cuenta: Cuenta, vista: VistaCajero):
        self.cuenta = cuenta
        self.vista = vista

    def iniciar(self):
        self.vista.mostrar_mensaje_bienvenida()

        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.solicitar_opcion()

            try:
                if opcion == "1":
                    monto = self.vista.solicitar_monto("depositar")
                    self.cuenta.depositar(monto)
                    self.vista.mostrar_saldo(self.cuenta.obtener_saldo())
                elif opcion == "2":
                    monto = self.vista.solicitar_monto("retirar")
                    self.cuenta.retirar(monto)
                    self.vista.mostrar_saldo(self.cuenta.obtener_saldo())
                elif opcion == "3":
                    self.vista.mostrar_saldo(self.cuenta.obtener_saldo())
                elif opcion == "4":
                    self.vista.mostrar_mensaje_despedida()
                    break
                else:
                    self.vista.mostrar_error("Opción inválida.")
            except Exception as e:
                self.vista.mostrar_error(str(e))
