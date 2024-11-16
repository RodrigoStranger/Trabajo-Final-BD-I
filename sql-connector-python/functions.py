import mysql.connector
from mysql.connector import Error

def conectar_base_datos(host, database, user, password):
    try:
        conexion = mysql.connector.connect(host=host, database=database, user=user, password=password)
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None