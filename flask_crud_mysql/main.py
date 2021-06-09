from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from datetime import datetime
import os 

app = Flask(__name__)
# Settings database connection
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'sistema'
# init extension
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/empleados')
def emp_index():

    sql = "SELECT * FROM `empleados`;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    empleados = cursor.fetchall()

    return render_template('employees/index.html', empleados = empleados)

@app.route('/empleados/create')
def emp_create():
    return render_template('employees/create.html')

@app.route('/empleados/store', methods=['POST'])
def emp_store():
    _nombre = request.form['nombre']
    _correo = request.form['correo']
    # La foto se almacena con información binaria por ende se guarda como files
    _foto = request.files['foto']
    # Tomamos la línea de tiempo actual para almacenar las fotos
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")

    if _foto.filename != '':
        # Concatenamos la línea de tiempo con el nombre de la foto
        nuevoNombrefoto = tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombrefoto)

        datos = (_nombre, _correo, nuevoNombrefoto) # En el caso de la foto almacenamos el nuevo nombre
        sql = "INSERT INTO empleados (nombre, correo, foto) VALUES (%s, %s, %s);"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()
    return render_template('employees/index.html')



if __name__ == '__main__':
    app.run(debug=True)