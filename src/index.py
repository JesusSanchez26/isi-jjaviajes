from flask import Flask, render_template,request,redirect
from string import Template
""" import mysql """

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login/login.html')

@app.route('/buscar')
def buscar():
    return render_template('home.html')

@app.route('/buscar_vuelos', methods=['POST'])
def buscar_vuelos():
    # Obtener los valores del formulario
    origen = request.form['origen']
    destino = request.form['destino']
    fecha = request.form['fecha']

    # Conectar a la base de datos
    conexion = mysql.connector.connect(user= 'AÑADIR USUARIO', 
                                    password='AÑADIR CONTRASEÑA', 
                                    host='AÑADIR HOST',
                                    database='AÑADIR NOMBRE BASE DE DATOS',
                                    port='AÑADIR PUERTO')

    # Ejecutar una consulta
    mycursor = conexion.cursor()
    sql = "SELECT columna1, columna2, columna3, columna4, columna5 FROM vuelo WHERE columna1=%s AND columna2=%s AND DATE(columna4)=%s"
    valores = (origen, destino, fecha)
    mycursor.execute(sql, valores)
    datos = mycursor.fetchall()

    # Cerrar la conexión a la base de datos
    conexion.close()

    # Renderizar el resultado en un archivo HTML
    with open("resultado.html", "r") as f:
        html_template = Template(f.read())
    rendered_html = html_template.render(datos=datos)
    with open("resultado_busqueda.html", "w") as f:
        f.write(rendered_html)

    # Redirigir al usuario al archivo HTML renderizado
    return redirect('/resultado_busqueda.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
