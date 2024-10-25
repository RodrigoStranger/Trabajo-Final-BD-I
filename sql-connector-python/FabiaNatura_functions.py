import mysql.connector
from mysql.connector import Error

def obtener_siguiente_codigo(cursor, tabla, columna, prefijo):
    query = f"SELECT {columna} FROM {tabla} ORDER BY {columna} DESC LIMIT 1"
    cursor.execute(query)
    resultado = cursor.fetchone()
    if resultado:
        ultimo_codigo = resultado[0]
        numero = int(ultimo_codigo[len(prefijo):])  # Obtiene la parte numérica del código
        siguiente_numero = numero + 1
    else:
        siguiente_numero = 1  # Si no hay registros, comienza en el primer número
    return f"{prefijo}{siguiente_numero:02d}"  # Formato con prefijo y dos dígitos

def conectar_base_datos(host, database, user, password):
    try:
        conexion = mysql.connector.connect(host=host, database=database, user=user, password=password)
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None