import mysql.connector

conexion =  mysql.connector.connect(user= 'AÑADIR USUARIO', 
                                    password='AÑADIR CONTRASEÑA', 
                                    host='AÑADIR HOST',
                                    database='AÑADIR NOMBRE BASE DE DATOS',
                                    port='AÑADIR PUERTO')


# Crear la tabla vuelo (solo una vez)

"""
cursor = conexion.cursor()
sql = "CREATE TABLE vuelo (id INT AUTO_INCREMENT PRIMARY KEY, columna1 VARCHAR(255), columna2 VARCHAR(255), columna3 VARCHAR(255), columna4 VARCHAR(255), columna5 VARCHAR(255))"
cursor.execute(sql)
conexion.close()
"""

# Prueba de inserción de datos

mycursor = conexion.cursor()
valores = ("valor1", "valor2", "valor3", "valor4", "valor5")
sql = "INSERT INTO vuelo (columna1, columna2, columna3, columna4, columna5) VALUES (%s, %s, %s, %s, %s)"
mycursor.execute(sql, valores)
conexion.commit()


print(mycursor.rowcount, "fila insertada.")
print(conexion)