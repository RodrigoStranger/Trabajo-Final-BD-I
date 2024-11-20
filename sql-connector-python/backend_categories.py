from backend_general import *
from tabulate import tabulate # pip install tabulate 

def mostrar_categorias():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM VistaCategorias;"
        cursor.execute(query)
        categorias = cursor.fetchall()
        if categorias:
            headers = ["Código", "Nombre"]
            print(tabulate(categorias, headers=headers, tablefmt="grid"))
        else: print("No hay categorías disponibles.")
    except Error as e: print(f"Error al consultar las categorías: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def agregar_categoria(nombre, descripcion):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('AgregarCategoria', [nombre, descripcion])
            conexion.commit()
            print(f"La categoría {nombre} fue creada exitosamente.")
    except Error as e:
        print(f"Error al agregar la categoría: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_nombre_categoria(cod_categoria, nuevo_nombre):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarNombreCategoria', [cod_categoria, nuevo_nombre])
            conexion.commit()
            print(f"El nombre de la categoría con código {cod_categoria} fue actualizado a '{nuevo_nombre}'.")
    except Error as e:
        print(f"Error al editar el nombre de la categoría: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_descripcion_categoria(cod_categoria, nueva_descripcion):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarDescripcionCategoria', [cod_categoria, nueva_descripcion])
            conexion.commit()
            print(f"La descripción de la categoría con código {cod_categoria} fue actualizada.")
    except Error as e:
        print(f"Error al editar la descripción de la categoría: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def eliminar_categoria(cod_categoria):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EliminarCategoria', [cod_categoria])
            conexion.commit()
            print(f"La categoría con código {cod_categoria} fue eliminada exitosamente.")
    except Error as e:
        print(f"Error al eliminar la categoría: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()