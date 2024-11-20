import os
from backend_products import *
from backend_suppliers import mostrar_proveedores
from backend_categories import mostrar_categorias

def limpiar_pantalla(): os.system('cls' if os.name == 'nt' else 'clear')





def agregar_producto_menu():
    limpiar_pantalla()
    print("=== Agregar un Producto ===")
    print("Categorías disponibles:")
    mostrar_categorias()
    while True:
        cod_categoria = input("Ingrese el código de la categoría (presione Enter si desea omitir): ").strip()
        if cod_categoria == "":
            cod_categoria = None
            break
        elif cod_categoria.isdigit():
            break
        else:
            print("Debe ingresar un número válido para el código de la categoría o presione Enter para omitir.")
    limpiar_pantalla()
    print("Proveedores disponibles:")
    mostrar_proveedores()
    while True:
        ruc = input("Ingrese el RUC del proveedor (presione Enter si desea omitir): ").strip()
        if ruc == "":
            ruc = None
            break
        elif len(ruc) == 11 and ruc.isdigit():
            break
        else:
            print("Debe ingresar un ruc válido de 11 dígitos o presione Enter para omitir.")
    limpiar_pantalla()
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        else:
            print("El nombre del producto no puede estar vacío. Intente nuevamente.")
    linea = input("Ingrese la línea del producto (presione Enter si desea omitir): ").strip()
    if linea == "":
        linea = None
    descripcion = input("Ingrese la descripción del producto (presione Enter si desea omitir): ").strip()
    if descripcion == "":
        descripcion = None
    while True:
        try:
            precio_compra = float(input("Ingrese el precio de compra: "))
            if precio_compra > 0:
                break
            else:
                print("El precio de compra debe ser mayor a 0. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido para el precio de compra. Intente nuevamente.")
    while True:
        try:
            precio_venta = float(input("Ingrese el precio de venta: "))
            if precio_venta > precio_compra:
                break
            else:
                print(f"El precio de venta debe ser mayor al precio de compra ({precio_compra}). Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido para el precio de venta. Intente nuevamente.")
    while True:
        try:
            stock = int(input("Ingrese el stock del producto: "))
            if stock > 0:
                break
            else:
                print("El stock debe ser mayor a 0. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido para el stock. Intente nuevamente.")
    agregar_producto(cod_categoria, ruc, nombre, linea, descripcion, precio_compra, precio_venta, stock)
    input("Presione Enter para continuar...")