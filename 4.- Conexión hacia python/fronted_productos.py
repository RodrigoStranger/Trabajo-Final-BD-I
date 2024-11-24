import os
from backend_products import *
from backend_suppliers import mostrar_proveedores
from backend_categories import mostrar_categorias

def limpiar_pantalla(): os.system('cls' if os.name == 'nt' else 'clear')

def menu_gestion_productos():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Producto===")
        print("1. Agregar un producto")
        print("2. Editar un producto")
        print("3. Cambiar el estado de un producto")
        print("4. Observar estadísticas generales")
        print("5. Salir al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto_menu()
        elif opcion == "2":
            menu_editar_producto()
        elif opcion == "3":
            menu_cambiar_estado_producto()
        elif opcion == "4":
            print("Función pendiente de desarrollo. Presione Enter para continuar...")
            input()
        elif opcion == "5":
            print("Saliendo del menú de Gestión de Proveedores...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

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

def menu_editar_producto():
    while True:
        limpiar_pantalla()
        print("=== Edición de Productos ===")
        while True:
            print("¿Qué desea hacer?")
            print("1. Buscar un producto por nombre o parte del nombre.")
            print("2. Ingresar directamente el código de un producto.")
            opcion_inicial = input("Seleccione una opción: ")
            if opcion_inicial == "1":
                while True:
                    busqueda = input("Ingrese el nombre o parte del nombre del producto: ").strip()
                    if not busqueda:
                        print("Debe ingresar un criterio de búsqueda. Intente nuevamente.")
                        continue
                    buscar_productos(busqueda)
                    print("¿Qué desea hacer ahora?")
                    print("1. Intentar buscar nuevamente.")
                    print("2. Ingresar el código de un producto encontrado.")
                    opcion_busqueda = input("Seleccione una opción: ")
                    if opcion_busqueda == "1":
                        continue
                    elif opcion_busqueda == "2":
                        try:
                            cod_producto = int(input("Ingrese el código del producto: "))
                            break
                        except ValueError:
                            print("Debe ingresar un código válido.")
                    else:
                        print("Opción no válida. Intente nuevamente.")
            elif opcion_inicial == "2":
                try:
                    cod_producto = int(input("Ingrese el código del producto: "))
                    break
                except ValueError:
                    print("Debe ingresar un código válido.")
            else:
                print("Opción no válida. Intente nuevamente.")
        while True:
            limpiar_pantalla()
            print(f"=== Edición del Producto {cod_producto} ===")
            print("1. Editar precio de compra")
            print("2. Editar precio de venta")
            print("3. Editar descripción")
            print("4. Editar línea")
            print("5. Editar stock")
            print("6. Salir al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                try:
                    precio_compra = float(input("Ingrese el nuevo precio de compra (mayor a 0): "))
                    if precio_compra > 0:
                        editar_precio_compra_producto(cod_producto, precio_compra)
                    else:
                        print("El precio de compra debe ser mayor a 0.")
                except ValueError:
                    print("Debe ingresar un número válido para el precio de compra.")
            elif opcion == "2":
                try:
                    precio_venta = float(input("Ingrese el nuevo precio de venta (mayor a 0): "))
                    if precio_venta > 0:
                        editar_precio_venta_producto(cod_producto, precio_venta)
                    else:
                        print("El precio de venta debe ser mayor a 0.")
                except ValueError:
                    print("Debe ingresar un número válido para el precio de venta.")
            elif opcion == "3":
                descripcion = input("Ingrese la nueva descripción (puede dejarse en blanco): ").strip()
                editar_descripcion_producto(cod_producto, descripcion)
            elif opcion == "4":
                linea = input("Ingrese la nueva línea (puede dejarse en blanco): ").strip()
                editar_linea_producto(cod_producto, linea)
            elif opcion == "5":
                while True:
                    try:
                        stock = int(input("Ingrese el nuevo stock del producto (no puede ser menor a 0): "))
                        if stock >= 0:
                            editar_stock_producto(cod_producto, stock)
                            break
                        else:
                            print("El stock no puede ser menor a 0.")
                    except ValueError:
                        print("Debe ingresar un número válido para el stock.")
            elif opcion == "6":
                return
            else:
                print("Opción no válida. Intente nuevamente.")

def menu_cambiar_estado_producto():
    while True:
        limpiar_pantalla()
        print("=== Cambiar Estado de un Producto ===")
        while True:
            print("¿Qué desea hacer?")
            print("1. Buscar un producto por nombre o parte del nombre.")
            print("2. Ingresar directamente el código de un producto.")
            opcion_inicial = input("Seleccione una opción: ")
            if opcion_inicial == "1":
                while True:
                    busqueda = input("Ingrese el nombre o parte del nombre del producto: ").strip()
                    if not busqueda:
                        print("Debe ingresar un criterio de búsqueda. Intente nuevamente.")
                        continue
                    buscar_productos(busqueda)
                    print("¿Qué desea hacer ahora?")
                    print("1. Intentar buscar nuevamente.")
                    print("2. Ingresar el código de un producto encontrado.")
                    opcion_busqueda = input("Seleccione una opción: ")
                    if opcion_busqueda == "1":
                        continue
                    elif opcion_busqueda == "2":
                        try:
                            cod_producto = int(input("Ingrese el código del producto: "))
                            break
                        except ValueError:
                            print("Debe ingresar un código válido.")
                    else:
                        print("Opción no válida. Intente nuevamente.")
            elif opcion_inicial == "2":
                try:
                    cod_producto = int(input("Ingrese el código del producto: "))
                    break
                except ValueError:
                    print("Debe ingresar un código válido.")
            else:
                print("Opción no válida. Intente nuevamente.")
        while True:
            limpiar_pantalla()
            print(f"=== Cambiar Estado del Producto {cod_producto} ===")
            print("1. Cambiar a disponible")
            print("2. Cambiar a agotado")
            print("3. Regresar al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                while True:
                    try:
                        stock = int(input("Ingrese el stock para cambiar el estado a 'disponible' (mayor a 0): "))
                        if stock > 0:
                            cambiar_estado_producto(cod_producto, 'disponible', stock)
                            break
                        else:
                            print("El stock debe ser mayor a 0.")
                    except ValueError:
                        print("Debe ingresar un número válido para el stock.")
            elif opcion == "2":
                while True:
                    try:
                        stock = int(input("Ingrese el stock para cambiar el estado a 'agotado' (debe ser 0): "))
                        if stock == 0:
                            cambiar_estado_producto(cod_producto, 'agotado', stock)
                            break
                        else:
                            print("El stock debe ser 0 para cambiar a 'agotado'.")
                    except ValueError:
                        print("Debe ingresar un número válido para el stock.")
            elif opcion == "3":
                return
            else:
                print("Opción no válida. Intente nuevamente.")