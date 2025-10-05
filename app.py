from flask import Flask, render_template, request, redirect, url_for, Response, session, flash
from flask_mysqldb import MySQL
from functools import wraps #decorador

#from pprint import pprint

app = Flask(__name__) #Creando el objeto aplicacion
app.secret_key = 'appsecretkey' #Clave secreta para la sesion

mysql=MySQL() #Inicializando la extension de MySQL

# conexion de la base de datos
app.config['MYSQL_HOST'] = 'dmanzanares.mysql.pythonanywhere-services.com'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'dmanzanares'
app.config['MYSQL_PASSWORD'] = 'dionicio147'
app.config['MYSQL_DB'] = 'dmanzanares$ventas'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql.init_app(app)

#funcion de decorador acceso a rutas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'if' not in session:
            flash('Debes iniciar sesión para acceder.','warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

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
#@login_required
def admin():
    usuario = session.get('id')
    return render_template('admin.html', usuario=usuario)

# FUNCION DE ACCESO A LOGIN
@app.route('/accesologin', methods=['GET', 'POST'])
def accesologin(): 
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        
        cursor = mysql.connection.cursor()
        
        # Verificar las credenciales del usuario
        cursor.execute("SELECT * FROM usuario WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()  
        if user:
            session['logueado'] = True
            session['id'] = user['id']
            session['nombre'] = user['nombre']
            session['id_rol'] = user['id_rol']
            
            if user['id_rol'] == 1:
                flash('¡Bienvenido Administrador!', 'success')
                return render_template('admin.html', user=user)
            elif user['id_rol'] == 2:
                flash('¡Bienvenido Usuario!', 'success')
                return render_template('usuario.html')
        else:
            flash('Usuario y contraseña incorrectos', 'danger')
            return render_template('login.html')
        

#REGISTRO DE USUARIOS
@app.route('/crearusuario', methods=['GET', 'POST'])
def crearusuario():
    nombre = request.form['nombre']
    email = request.form['email']
    password = request.form['password']
        
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO usuario (nombre, email, password, id_rol) VALUES (%s, %s, %s, '2')", (nombre, email, password))
    mysql.connection.commit()
    cursor.close()
    #return redirect(url_for('login'))
    flash('Agregado satisfactoriamente', 'success') # MENSAJE DE ALERTA
    return render_template('registro.html')

#INSERTAR USUARIO A LA BASE DE DATOS AL LISTAR USUARIOS
@app.route('/guardar', methods=['Get','POST'])
def guardar():
    if request.method == "POST":
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuario(nombre,email,password, id_rol) VALUES(%s, %s, %s, '2')", (nombre, email, password))
        mysql.connection.commit()
        flash('Agregado satisfactoriamente', 'success') # MENSAJE DE ALERTA
        cur.close()
        return redirect(url_for('listar'))

#-----LISTAR USUARIOS REGISTRADOS-------------
@app.route('/listar')
#@login_required
def listar(): 
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario")
    usuarios = cur.fetchall()
    cur.close()
    return render_template("listar.html", usuarios=usuarios)

#-----LISTAR PRODUCTOS-------------
@app.route('/listar_productos')
def listar_productos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM productos")
    productos = cur.fetchall()
    cur.close()
    return render_template("listarproducto.html", productos=productos)

#-----AGREGAR PRODUCTOS-------------
@app.route('/agregar_producto', methods=['POST', 'GET'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)", (nombre, descripcion, precio))
        mysql.connection.commit()
        cur.close()
        flash('Producto agregado exitosamente', 'success')
        return redirect(url_for('listar_productos_agregados'))
        #return render_template('agregarproducto.html')

#-----listar productos-------------
@app.route('/listar_productos_agregados')
def listar_productos_agregados():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM productos")
    productos = cur.fetchall()
    cur.close()
    return render_template("agregarproducto.html", productos=productos)

#-------- eliminar usuario -------------
@app.route('/borrarUser/<int:id>', methods=['GET'])
def borrarUser(id):
    flash('Sea borrado permanentemente', 'question')
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM usuario WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect(url_for('listar'))

#-------- eliminar PRODUCTOS -------------
@app.route('/borrarproducto/<int:id>', methods=['GET'])
def borrarproducto(id):
    flash('Sea borrado permanentemente', 'question')
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM productos WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect(url_for('listar_productos'))

# --------Actualizar usuario--------------
@app.route('/updateUsuari', methods = ['POST', 'GET'])
def updateUsuari():
    if request.method == "POST":
        id = request.form['id']
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE usuario SET nombre=%s, email=%s, password=%s WHERE id=%s", (nombre, email, password, id))
        flash ("Datos actualizados correctamente")
        return redirect (url_for('listar'))
    
# ACTUALIZAR USUARIO
@app.route('/updateUsuario', methods=['POST'])
def updateUsuario():
    id = request.form['id']
    nombre = request.form['nombre']
    email = request.form['email']
    password = request.form['password']
    sql="UPDATE usuario SET nombre=%s, email=%s, password=%s WHERE id=%s"
    datos=(nombre, email, password, id)
    
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    flash('Se actualizo Satisfactoriamente', 'success')
    return redirect(url_for('listar'))

# ACTUALIZAR PRODUCTO
@app.route('/editproducto', methods=['POST'])
def editproducto():
    id = request.form['id']
    nombre = request.form['nombre']
    precio = request.form['precio']
    descripcion = request.form['descripcion']
    sql="UPDATE productos SET nombre=%s, precio=%s, descripcion=%s WHERE id=%s"
    datos=(nombre, precio, descripcion, id)
    
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    flash('Se actualizo Satisfactoriamente', 'success')
    return redirect(url_for('listar_productos'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('inicio'))

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


@app.route('/agregarproducto')
def agregarproducto():
    return render_template('agregarproducto.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)