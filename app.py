from flask import Flask, render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
from pprint import pprint

app = Flask(__name__) #Creando el objeto aplicacion

app.secret_key = 'appsecretkey' #Clave secreta para la sesion

mysql=MySQL() #Inicializando la extension de MySQL

# conexion de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ventas'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql.init_app(app)

@app.route('/') #Decorador Ruta principal
def inicio(): #Funcion que retorna un mensaje de bienvenida
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/admin')
def admin  ():
    return render_template('admin.html')

# FUNCION DE ACCESO A LOGIN
@app.route('/accesologin', methods=['GET', 'POST'])
def accesologin():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        
        # Aquí puedes agregar la lógica para verificar las credenciales del usuario
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['logueado'] = True
            session['id'] = user['id']
            
            session['id_rol'] = user['id_rol']
            if user['id_rol'] == 1:
                return render_template('admin.html')
            elif user['id_rol'] == 2:
                return render_template('usuario.html')
            
        else:
            return render_template('login.html', error='Usuario y contraseña incorrectos')


""" 
@app.route('/home')
def home():
    return 'Pagina principal, bienvenido!' """

@app.route('/parametros/<nombre>') #Ruta de parametros
def parametros(nombre):
    return 'La pagina el parametro es: %s' %nombre

@app.route('/usuario/<nombre>') #Ruta de parametros con un variable
def parametros_uno(nombre):
    return 'Hola, {} ¿como estas?'.format(nombre)

@app.route('/parametros1/<id>/<nombre>') #Ruta de parametros con dos variables
def parametros_dos(id, nombre):
    return 'La pagina el parametro es: %s y el nombre es: %s' %(id, nombre)

@app.route('/edad/<int:edad>') #Ruta de parametros con un variable entero
def edad(edad):
    return 'Tiene {} años'.format(edad)

@app.route('/suma/<int:num1>/<int:num2>') #Ruta de parametros con dos variables enteras
def suma(num1, num2):
    resultado = num1 + num2
    return 'La suma de {} y {} es: {}'.format(num1, num2, resultado)
 
@app.route('/edadvalor/<int:edad>') #Ruta de parametros con un variable entero
def edadvalor(edad):
    if edad < 18:
            return 'Eres menor de edad'
    elif edad >= 18 and edad < 65:
        return 'Eres mayor de edad tienes {} años'.format(edad)
    else:
        return 'Eres un adulto mayor, tienes {} años'.format(edad)

@app.route('/index') #Ruta para renderizar una plantilla HTML
def index():
    return render_template('index.html')

#Metodo GET
""" @app.route('/registro', methods=['GET']) #Ruta para renderizar una plantilla HTML
def registro():
    user = { # Diccionario para almacenar la información del usuario
        'name': '',
        'email': '',
        'mensaje': ''
    }
    if request.method == 'GET':
        user['name'] = request.args.get('nombre', '')
        user['email'] = request.args.get('email', '')
        user['mensaje'] = request.args.get('mensaje', '')
    return render_template('contactoget.html', usuario=user) """

 #Metodo POST
@app.route('/registro1', methods=['GET', 'POST']) #Ruta para renderizar una plantilla HTML
def contacto_post():
    user = {
        'name': '',
        'email': '',
        'mensaje': ''
    }
    if request.method == 'POST':
        user['name'] = request.form['nombre']
        user['email'] = request.form['email']
        user['mensaje'] = request.form['mensaje']

    return render_template('usuario.html', usuario=user)


@app.route('/contacto', methods=['GET', 'POST']) #Ruta para renderizar una plantilla HTML
def contacto():
    if request.method == 'POST':
        # Aquí podrías manejar el formulario enviado
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        pprint(request.form)
        pprint(f'Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}')
        return 'Mensaje enviado!.'
    else:
        return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)

