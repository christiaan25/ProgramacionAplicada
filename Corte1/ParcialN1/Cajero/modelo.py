class Cuenta:
    def __init__(self, titular: str, saldo: int = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto: int):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero.")
        self.saldo += monto

    def retirar(self, monto: int):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero.")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes para realizar el retiro.")
        self.saldo -= monto

    def obtener_saldo(self):
        return self.saldo
