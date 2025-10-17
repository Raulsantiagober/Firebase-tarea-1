from data import firebase_service

class CuentaVM:
    def __init__(self, cuenta):
        self.cuenta = cuenta

    def guardar(self):
        data = {
            "numero": self.cuenta.numero,
            "titular": self.cuenta.titular,
            "saldo": self.cuenta.saldo
        }
        firebase_service.crear_cuenta(data)
