from domain.account import Cuenta
from presentation.account_vm import CuentaVM
from data import firebase_service

def menu():
    print(" \n=== MENÚ DE CUENTAS === ")
    print("|1. Crear cuenta            |")
    print("|2. Consultar cuenta        |")
    print("|3. Actualizar saldo        |")
    print("|4. Eliminar cuenta         |")
    print("|5. Listar cuentas          |")
    print("|0. Salir                   |")

def iniciar_cli():
    while True:
        menu()
        op = input("Opción: ")

        if op == "1":
            num = input("Número de cuenta: ")
            nom = input("Titular: ")
            saldo = float(input("Saldo inicial: "))
            cuenta = Cuenta(num, nom, saldo)
            vm = CuentaVM(cuenta)
            vm.guardar()
            print(" Cuenta creada.")

        elif op == "2":
            num = input("Número de cuenta: ")
            print(firebase_service.leer_cuenta(num))

        elif op == "3":
            num = input("Número de cuenta: ")
            nuevo = float(input("Nuevo saldo: "))
            firebase_service.actualizar_cuenta(num, {"saldo": nuevo})
            print(" Saldo actualizado.")

        elif op == "4":
            num = input("Número de cuenta: ")
            firebase_service.eliminar_cuenta(num)
            print(" Cuenta eliminada.")

        elif op == "5":
            cuentas = firebase_service.listar_cuentas()
            print(cuentas)

        elif op == "0":
            print(" Adiós")
            break

        else:
            print("Opción inválida.")
