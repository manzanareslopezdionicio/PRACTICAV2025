from werkzeug.security import generate_password_hash, check_password_hash

texto = "x?1_P-1M.4!eM"
# Hashear con diferentes métodos
texto_encriptado1 = generate_password_hash(texto)
texto_encriptado4 = generate_password_hash(texto, 'pbkdf2:sha256')
texto_encriptado5 = generate_password_hash(texto, 'pbkdf2:sha256', 30)
texto_encriptado6 = generate_password_hash(texto, 'pbkdf2:sha256:30', 30)
print(texto_encriptado1)
print(texto_encriptado4)
print(texto_encriptado5)
print(texto_encriptado6)

# Desencriptar (verificar)
print(check_password_hash(texto_encriptado1, texto))
print(check_password_hash(texto_encriptado4, texto))
print(check_password_hash(texto_encriptado5, texto))
print(check_password_hash(texto_encriptado6, texto))
