from backend_general import *
from backend_api import *
from tabulate import tabulate # pip install tabulate 

def obtener_ultima_factura():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        cursor.execute("SELECT ObtenerUltimaFactura();")
        resultado = cursor.fetchone()
        if resultado and resultado[0] is not None:
            print(f"El último código de factura es: {resultado[0]}")
            return resultado[0]
        else:
            print("No hay facturas en la base de datos.")
            return None
    except Exception as e:
        print(f"Error al obtener el último código de factura: {e}")
        return None
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def eliminar_factura(cod_factura):
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        cursor.callproc('EliminarFactura', [cod_factura])
        conexion.commit()
        print(f"Factura con código {cod_factura} eliminada exitosamente.")
    except Exception as e:
        print(f"Error al eliminar la factura: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
