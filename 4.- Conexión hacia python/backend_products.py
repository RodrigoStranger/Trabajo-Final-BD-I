from backend_general import *
from tabulate import tabulate # pip install tabulate 

def buscar_productos(busqueda):
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        cursor.callproc('BuscarProductos', [busqueda])
        resultados = cursor.fetchall()
        if resultados:
            headers = ["Codigo", "Nombre", "Proveedor", "Stock", "PrecioUnitario"]
            print(tabulate(resultados, headers=headers, tablefmt="grid"))
            return resultados
        else:
            print("No se encontraron productos que coincidan con la búsqueda.")
    except Exception as e:
        print(f"Error al buscar productos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            
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

def editar_precio_compra_producto(cod_producto, precio_compra):
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        cursor.callproc('EditarPrecioCompraProducto', [cod_producto, precio_compra])
        conexion.commit()
        print(f"Precio de compra del producto {cod_producto} actualizado a {precio_compra}.")
    except Exception as e:
        print(f"Error al editar el precio de compra: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_precio_venta_producto(cod_producto, precio_venta):
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        cursor.callproc('EditarPrecioVentaProducto', [cod_producto, precio_venta])
        conexion.commit()
        print(f"Precio de venta del producto {cod_producto} actualizado a {precio_venta}.")
    except Exception as e:
        print(f"Error al editar el precio de venta: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_descripcion_producto(cod_producto, descripcion):
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        cursor.callproc('EditarDescripcionProducto', [cod_producto, descripcion])
        conexion.commit()
        print(f"Descripción del producto {cod_producto} actualizada.")
    except Exception as e:
        print(f"Error al editar la descripción del producto: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_linea_producto(cod_producto, linea):
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        cursor.callproc('EditarLineaProducto', [cod_producto, linea])
        conexion.commit()
        print(f"Línea del producto {cod_producto} actualizada.")
    except Exception as e:
        print(f"Error al editar la línea del producto: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_stock_producto(cod_producto, stock):
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        cursor.callproc('EditarStockProducto', [cod_producto, stock])
        conexion.commit()
        print(f"Stock del producto {cod_producto} actualizado a {stock}.")
    except Exception as e:
        print(f"Error al editar el stock del producto: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def cambiar_estado_producto(cod_producto, estado, stock):
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        cursor.callproc('CambiarEstadoProducto', [cod_producto, estado, stock])
        conexion.commit()
        print(f"El estado del producto {cod_producto} ha sido cambiado a {estado} con un stock de {stock}.")
    except Exception as e:
        print(f"Error al cambiar el estado del producto: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

