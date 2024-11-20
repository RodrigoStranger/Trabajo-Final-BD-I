from backend_general import *
from tabulate import tabulate # pip install tabulate 

def mostrar_proveedores():
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM VistaProveedores;"
        cursor.execute(query)
        proveedores = cursor.fetchall()
        if proveedores:
            headers = ["RUC", "Nombre"]
            print(tabulate(proveedores, headers=headers, tablefmt="grid"))
        else: print("No hay proveedores disponibles.")
    except Error as e: print(f"Error al consultar los proveedores: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def telefono_existe_proveedores(telefono):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            query = f"SELECT VerificarTelefonoExisteProveedores('{telefono}') AS ExisteTelefono;"
            cursor.execute(query)
            resultado = cursor.fetchone()
            return resultado[0] == 1  # Retorna True si existe, False si no
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def agregar_proveedor(ruc, nombre, telefono):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('AgregarProveedor', [ruc, nombre, telefono])
            conexion.commit()
            print(f"Proveedor '{nombre}' con RUC {ruc} creado exitosamente.")
    except Error as e:
        print(f"Error al agregar el proveedor: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_telefono_proveedor(ruc, nuevo_telefono):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarTelefonoProveedor', [ruc, nuevo_telefono])
            conexion.commit()
            print(f"Teléfono del proveedor con RUC {ruc} actualizado correctamente.")
    except Error as e:
        print(f"Error al actualizar el teléfono del proveedor: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def eliminar_proveedor(ruc):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EliminarProveedor', [ruc])
            conexion.commit()
            print(f"Proveedor con RUC {ruc} eliminado correctamente.")
    except Error as e:
        print(f"Error al eliminar el proveedor: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()