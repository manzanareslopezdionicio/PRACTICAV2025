from flask import Flask
from flask_bcrypt import Bcrypt # Asegúrate de importar Bcrypt de flask_bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app) # Crea una instancia de Bcrypt

# 1. Encriptar una contraseña
password_plana = "mi_contraseña_secreta"
hash_almacenado = bcrypt.generate_password_hash(password_plana).decode('utf-8')
print(f"Contraseña encriptada: {hash_almacenado}")

# 2. Verificar la contraseña
contraseña_intento = "mi_contraseña_secreta"
es_correcta = bcrypt.check_password_hash(hash_almacenado, contraseña_intento)
print(f"La contraseña es correcta: {es_correcta}")

# 2. Verificar una contraseña
contraseña_ingresada = "mi_contraseña_secreta"
contraseña_incorrecta = "contraseña_otra"

# Comprobar si el hash coincide con la contraseña ingresada
if bcrypt.check_password_hash(hash_almacenado, contraseña_ingresada):
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")
