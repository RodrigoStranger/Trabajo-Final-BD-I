import mysql.connector
from mysql.connector import Error
import os

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

def cargar_tablas():
    conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
    cursor = conexion.cursor()
    directory = os.path.dirname(__file__)
    sketchfile = 'FabiaNatura - create objects mysql.sql'
    pathfile = os.path.join(directory, '..', 'mysql-scripts', sketchfile)
    with open(pathfile, 'r') as archivo: comandos_sql = archivo.read()
    for comando in comandos_sql.split(';'):
        if comando.strip():
            try:
                cursor.execute(comando)
                #print("Ejecutado:", comando)
            except Exception as err: print(f"Error en el comando: {comando}\n{err}")
    conexion.commit()
    cursor.close()
    print("Tablas cargadas exitosamente.")