from backend_sales import *
from backend_users import *
from backend_products import *
import os

def limpiar_pantalla(): os.system('cls' if os.name == 'nt' else 'clear')

def menu_gestion_ventas():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Ventas ===")
        print("1. Realizar una venta")
        print("2. Observar estadísticas generales")
        print("3. Salir al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_realizar_venta()
        elif opcion == "2":
            print("funcion en desarrollo.....")
            input("Presione Enter para continuar...")
        elif opcion == "3":
            print("Saliendo del a la ventana principal...")
            input("Presione Enter para continuar...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

def menu_realizar_venta():
    limpiar_pantalla()
    print("=== Venta ===")
    while True:
        dni = input("Ingrese el DNI del cliente: ")
        if len(dni) == 8 and dni.isdigit():
            if persona_existe(dni):
                print(f"El cliente con DNI {dni} ya existe en la base de datos.")
                input("Presione Enter para continuar...")
                break
            else:
                print("Nuevo cliente :)")
                while True:
                    telefono = input("Ingrese el teléfono del cliente: ")
                    if len(telefono) == 9 and telefono.isdigit():
                        if not telefono_existe(telefono):
                            insertar_cliente(dni, telefono)
                            print(f"Cliente con DNI {dni} y teléfono {telefono} agregado.")
                            input("Presione Enter para continuar...")
                            break
                    else:
                        print("El teléfono debe tener exactamente 9 dígitos numéricos. Intente nuevamente.")
                break
        else:
            print("El DNI debe tener exactamente 8 dígitos numéricos. Intente nuevamente.")
        input("Presione Enter para continuar...")
    while True:
        limpiar_pantalla()
        print("=== Selección del Vendedor ===")
        mostrar_vendedores()
        cod_vendedor = input("Ingrese el código del vendedor: ")
        if verificar_vendedor(cod_vendedor):
            print(f"Vendedor {cod_vendedor} seleccionado.")
            input("Presione Enter para continuar...")
            break
        else:
            print("El vendedor no existe. Ingrese un código válido.")
            input("Presione Enter para continuar...")
    while True:
        opcion = input("¿Desea agregar un asesor? (s/n): ").lower()
        if opcion == 's':
            limpiar_pantalla()
            print("=== Selección del Asesor ===")
            mostrar_asesores()
            cod_asesor = input("Ingrese el código del asesor: ")
            if verificar_asesor(cod_asesor):
                print(f"Asesor {cod_asesor} seleccionado.")
                input("Presione Enter para continuar...")
                break
            else:
                print("El asesor no existe. Ingrese un código válido.")
                input("Presione Enter para continuar...")
        elif opcion == 'n':
            print("No se seleccionará un asesor.")
            cod_asesor = None
            input("Presione Enter para continuar...")
            break
        else:
            print("Opción no válida. Ingrese 's' para sí o 'n' para no.")
            input("Presione Enter para continuar...")
    insertar_factura(dni, cod_vendedor, cod_asesor)
    print("Factura agregada correctamente.")
    limpiar_pantalla()
    print(f"=== Venta de productos para el cliente con DNI {dni} ===")
    print("=== Selección de productos ===")
    producto = input("Buscar producto: ")
    buscar_productos(producto)
    cod_producto = input("Ingrese el código del producto: ")
    cantidad = input("Ingresa la cantidad: ")
    ultimafactura = obtener_ultima_factura()
    reducir_stock_producto(cod_producto, cantidad)
    insertar_detalle_factura(ultimafactura, cod_producto, cantidad)
    while True:
        opcion = input("¿Desea agregar más productos? (s/n): ").lower()
        if opcion == 's':
            limpiar_pantalla()
            producto = input("Buscar otro producto: ")
            buscar_productos(producto)
            cod_producto = input("Ingrese el código del producto: ")
            cantidad = input("Ingresa la cantidad: ")
            reducir_stock_producto(cod_producto, cantidad)
            insertar_detalle_factura(ultimafactura, cod_producto, cantidad)
        elif opcion == 'n':
            limpiar_pantalla()
            print(f"=== Factura para {dni} ==")
            mostrar_boleta_venta(ultimafactura)
            total = calcular_subtotal(ultimafactura)
            print(f"Total a pagar: {total}.")
            input("Presione Enter para continuar...")
            input("Presione Enter para regresar a la Gestión de ventas...")
            break
        else:
            print("Opción no válida. Ingrese 's' para sí o 'n' para no.")

def menu_estadistica_ventas():
    print("en desarrollo")