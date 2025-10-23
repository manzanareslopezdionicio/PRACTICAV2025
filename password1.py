#flask-bcrypt
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

password_plano = "mi_contraseña_secreta"
hash_password = bcrypt.generate_password_hash(password_plano).decode('utf-8')
print(f"Contraseña encriptada: {hash_password}")

# Para verificar la contraseña
contraseña_interna = "mi_contraseña_secreta"
contraseña_interna = bcrypt.check_password_hash(hash_password, contraseña_interna)
print(f"¿La contraseña es correcta? {contraseña_interna}")