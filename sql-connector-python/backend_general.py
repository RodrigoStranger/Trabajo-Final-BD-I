import mysql.connector
from mysql.connector import Error

def conectar_base_datos():
    try:
        conexion = mysql.connector.connect(host="localhost", database="FabiaNatura", user="rodrigo", password="ubnt")
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None  