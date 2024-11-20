from backend_general import *

def agregar_producto(cod_categoria, ruc, nombre, linea, descripcion, precio_compra, precio_venta, stock):
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo establecer conexión con la base de datos.")
            return
        cursor = conexion.cursor()
        cursor.callproc('AgregarProducto', [cod_categoria, ruc, nombre, linea, descripcion, precio_compra, precio_venta, stock])
        conexion.commit()
        print(f"Producto {nombre} agregado correctamente.")
    except mysql.connector.Error as e:
        if e.errno == 1644:
            print(f"Error: {e.msg}")
        else:
            print(f"Error al agregar el producto: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()


