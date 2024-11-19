from functions import *
from api import *

def insertar_cliente(dni, telefono):
    datos = generar_datos_completos(dni)
    if datos:
        try:
            conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
            if not conexion:
                print("No se pudo establecer conexión con la base de datos.")
                return
            cursor = conexion.cursor()
            cursor.callproc('AgregarCliente', [
                dni,
                datos["nombre"],
                datos["apellido_paterno"],
                datos["apellido_materno"],
                datos["fecha_nacimiento"],
                telefono,
                datos["direccion"]
            ])
            conexion.commit()
            print(f"Cliente {datos['nombre']} insertado correctamente.")
        except Error as e: print(f"Error al insertar el cliente: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
    else: print("No se pudieron obtener los datos del cliente desde la API.")

def insertar_vendedor(dni, telefono, rol):
    datos = generar_datos_completos(dni)
    if datos:
        try:
            conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
            if not conexion:
                print("No se pudo establecer conexión con la base de datos.")
                return
            cursor = conexion.cursor()
            cursor.callproc('AgregarVendedor', [dni,
                datos["nombre"],
                datos["apellido_paterno"],
                datos["apellido_materno"],
                datos["fecha_nacimiento"],
                telefono,
                datos["direccion"],
                rol
            ])
            conexion.commit()
            print(f"Vendedor {datos['nombre']} insertado correctamente.")
        except Error as e: print(f"Error al insertar el vendedor: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
    else: print("No se pudieron obtener los datos del vendedor desde la API.")

def insertar_asesor(dni, telefono, experiencia, especialidad):
    datos = generar_datos_completos(dni)
    if datos:
        try:
            conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
            if not conexion:
                print("No se pudo establecer conexión con la base de datos.")
                return
            cursor = conexion.cursor()
            cursor.callproc('AgregarAsesor', [
                dni,
                datos["nombre"],
                datos["apellido_paterno"],
                datos["apellido_materno"],
                datos["fecha_nacimiento"],
                telefono,
                datos["direccion"],
                experiencia,
                especialidad
            ])
            conexion.commit()
            print(f"Asesor {datos['nombre']} insertado correctamente.")
        except Error as e: print(f"Error al insertar el asesor: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
    else: print("No se pudieron obtener los datos del asesor desde la API.")