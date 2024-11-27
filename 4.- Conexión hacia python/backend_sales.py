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

def insertar_factura(dni, cod_vendedor, cod_asesor):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('AgregarFactura', [dni, cod_vendedor, cod_asesor])
            conexion.commit()
    except Error as e:
        print("Error al agregar la factura:", e)
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

def insertar_detalle_factura(cod_factura, cod_producto, cantidad):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('InsertarDetalleFactura', [cod_factura, cod_producto, cantidad])
            conexion.commit()
            for result in cursor.stored_results():
                error_message = result.fetchone()
                if error_message:
                    print(f"Error: {error_message[0]}")
                else:
                    print("Detalle de factura insertado correctamente.") 
            cursor.close()
    except Error as e:
        print(f"Error en la conexión a la base de datos: {e}")
    
    finally:
        if conexion.is_connected():
            conexion.close()

def cancelar_factura(cod_factura):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('CancelarFactura', [cod_factura])
            conexion.commit()
            cursor.close()
    except Error as e:
        print(f"Error en la conexión a la base de datos: {e}")
    finally:
        if conexion.is_connected():
            conexion.close()

def calcular_subtotal(cod_factura):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute("SELECT CalcularSubtotal(%s)", (cod_factura,))
            subtotal = cursor.fetchone()[0]
            return subtotal
    except Error as e:
        print(f"Error en la conexión a la base de datos: {e}")
        return None
    finally:
        if conexion.is_connected():
            conexion.close()

def mostrar_boleta_venta(cod_factura):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('MostrarBoletaVenta', [cod_factura])
            for result in cursor.stored_results():
                data = result.fetchall()
                headers = ["Producto", "Cantidad", "Precio Unitario", "Total Producto"]
                print(tabulate(data, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
    except Error as e:
        print(f"Error al ejecutar el procedimiento: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()