# data/firebase_service.py
import os
from dotenv import load_dotenv
load_dotenv()
print("CREDENCIALES:", os.getenv("FIREBASE_CREDENTIALS_JSON"))
print("URL:", os.getenv("FIREBASE_DB_URL"))
import firebase_admin
from firebase_admin import credentials, db

# Inicializa firebase una sola vez
if not firebase_admin._apps:
    cred_path = os.getenv("FIREBASE_CREDENTIALS_JSON")
    db_url = os.getenv("FIREBASE_DB_URL")
    if not cred_path or not db_url:
        raise Exception("Debes definir FIREBASE_CREDENTIALS_JSON y FIREBASE_DB_URL en .env")
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {"databaseURL": db_url})

root = db.reference("cuentas")

def crear_cuenta(data):
    ref = db.reference("cuentas")
    ref.child(data["numero"]).set(data)
    print("✅ Cuenta guardada correctamente.")


def leer_cuenta(numero):
    return root.child(str(numero)).get()

def actualizar_cuenta(numero, nuevos_datos):
    root.child(str(numero)).update(nuevos_datos)

def eliminar_cuenta(numero):
    root.child(str(numero)).delete()

def listar_cuentas():
    return root.get() or {}
