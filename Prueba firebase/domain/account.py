class Cuenta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"Cuenta({self.numero}, {self.titular}, {self.saldo})"
