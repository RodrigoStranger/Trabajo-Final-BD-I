from FabiaNatura_functions import conectar_base_datos
from FabiaNatura_functions import obtener_siguiente_codigo
from mysql.connector import Error

def insertar_categoria(cursor, nombre, descripcion):
    query_categoria = """INSERT INTO Categorias (cod_categoria, nombre, descripcion) VALUES (%s, %s, %s)"""
    cod_cat = obtener_siguiente_codigo(cursor, "Categorias", "cod_categoria", "CAT")
    valores_categoria = (cod_cat, nombre, descripcion)
    cursor.execute(query_categoria, valores_categoria)
    print(f"Categoria {nombre} insertada correctamente con código: {cod_cat}")

def gestionar_insercion_categoria(nombre, descripcion):
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            insertar_categoria(cursor, nombre, descripcion)
            conexion.commit()
    except Error as e: print(f"Error al insertar datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

##FALTA
def actualizar_categoria(cursor, nombre, descripcion):
    query_categoria = """INSERT INTO Categorias (cod_categoria, nombre, descripcion) VALUES (%s, %s, %s)"""
    cod_cat = obtener_siguiente_codigo(cursor, "Categorias", "cod_categoria", "CAT")
    valores_categoria = (cod_cat, nombre, descripcion)
    cursor.execute(query_categoria, valores_categoria)
    print(f"Categoria {nombre} insertada correctamente con código: {cod_cat}")
