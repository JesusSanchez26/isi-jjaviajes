import json
import mysql.connector
from ryanair import datos_api

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

# Inserción de datos

mycursor = conexion.cursor()
sql = "INSERT INTO vuelo (columna1, columna2, columna3, columna4, columna5) VALUES (%s, %s, %s, %s, %s)"

api_data = datos_api.vuelos()
final_data = json.loads(api_data)

for trip in final_data.values():
    for flight in trip:
        origin_code = flight[0]['origin_code']
        destination_code = flight[0]['destination_code']
        regular_fare = flight[0]['regular_fare']
        departure_datetime_utc = flight[0]['departure_datetime_utc']
        duration_hours = flight[0]['duration_hours']
        valores = (origin_code, destination_code, regular_fare, departure_datetime_utc, duration_hours)
        mycursor.execute(sql, valores)
        conexion.commit()
        print(mycursor.rowcount, "fila insertada.")

print(conexion)