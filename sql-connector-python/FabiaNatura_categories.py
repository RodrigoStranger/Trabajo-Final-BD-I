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

def actualizar_categoria(cursor, cod_categoria, nombre, descripcion):
    query_actualizar = """UPDATE Categorias SET nombre = %s, descripcion = %s WHERE cod_categoria = %s"""
    valores_actualizar = (nombre, descripcion, cod_categoria)
    cursor.execute(query_actualizar, valores_actualizar)
    print(f"Categoria con código {cod_categoria} actualizada correctamente.")

def gestionar_actualizacion_categoria(cod_categoria, nombre, descripcion):
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            actualizar_categoria(cursor, cod_categoria, nombre, descripcion)
            conexion.commit()
    except Error as e:
        print(f"Error al actualizar datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def eliminar_categoria(cursor, cod_categoria=None, nombre=None):
    if cod_categoria:
        query_eliminar = "DELETE FROM Categorias WHERE cod_categoria = %s"
        valor_eliminar = (cod_categoria,)
    elif nombre:
        query_eliminar = "DELETE FROM Categorias WHERE nombre = %s"
        valor_eliminar = (nombre,)
    else:
        print("Debe proporcionar un código o nombre para eliminar la categoría.")
        return
    cursor.execute(query_eliminar, valor_eliminar)
    print(f"Categoria eliminada correctamente.")

def gestionar_eliminacion_categoria(cod_categoria=None, nombre=None):
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            eliminar_categoria(cursor, cod_categoria, nombre)
            conexion.commit()  
    except Error as e: print(f"Error al eliminar la categoría: {e}")  
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_categoria_con_productos(cursor, cod_categoria=None, nombre=None):
    query_categoria_productos = """
        SELECT c.cod_categoria, c.nombre AS categoria_nombre, p.nombre AS producto_nombre, p.descripcion
        FROM Categorias c
        LEFT JOIN Productos p ON c.cod_categoria = p.cod_categoria
        WHERE c.cod_categoria = %s OR c.nombre = %s
    """
    valores = (cod_categoria, nombre)
    cursor.execute(query_categoria_productos, valores)
    resultados = cursor.fetchall()
    if resultados:
        print("Categoría y productos asociados:")
        for resultado in resultados:
            cod_cat, categoria_nombre, producto_nombre, descripcion = resultado
            print(f"Categoría: {categoria_nombre} (Código: {cod_cat})")
            if producto_nombre:
                print(f" - Producto: {producto_nombre}, Descripción: {descripcion}")
            else:
                print(" - Sin productos asociados.")
    else: print("Categoría no encontrada o no tiene productos asociados.")

def gestionar_mostrar_categoria_con_productos(cod_categoria=None, nombre=None):
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            mostrar_categoria_con_productos(cursor, cod_categoria, nombre)
    except Error as e:
        print(f"Error al mostrar la categoría y productos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_todas_categorias(cursor):
    query_todas_categorias = "SELECT cod_categoria, nombre, descripcion FROM Categorias"
    cursor.execute(query_todas_categorias)
    categorias = cursor.fetchall()
    if categorias:
        print("Todas las categorías:")
        for categoria in categorias:
            cod_cat, nombre, descripcion = categoria
            print(f"Código: {cod_cat}, Nombre: {nombre}, Descripción: {descripcion}")
    else:
        print("No hay categorías registradas.")

def gestionar_mostrar_todas_categorias():
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            mostrar_todas_categorias(cursor)
    except Error as e:
        print(f"Error al mostrar las categorías: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()