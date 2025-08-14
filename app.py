from flask import Flask, render_template, request
from pprint import pprint

app = Flask(__name__) #Creando el objeto aplicacion
 
@app.route('/') #Decorador Ruta principal
def holamundo(): #Funcion que retorna un mensaje de bienvenida
    return 'Bienvenido a Flask PRACTICAS DE PROFESIONALIZACION'

@app.route('/home')
def home():
    return 'Pagina principal, bienvenido!'

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

