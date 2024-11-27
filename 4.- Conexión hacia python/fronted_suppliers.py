import os
from backend_suppliers import *

def limpiar_pantalla(): os.system('cls' if os.name == 'nt' else 'clear')

def menu_gestion_proveedores():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Proveedores ===")
        print("1. Agregar un proveedor")
        print("2. Editar el teléfono de un proveedor")
        print("3. Eliminar un proveedor")
        print("4. Observar estadísticas generales")
        print("5. Salir al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_proveedor_menu()
        elif opcion == "2":
            editar_telefono_proveedor_menu()
        elif opcion == "3":
            eliminar_proveedor_menu()
        elif opcion == "4":
            menu_estadisticas_proveedores()
        elif opcion == "5":
            print("Saliendo del menú de Gestión de Proveedores...")
            input("Presione Enter para continuar...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

def agregar_proveedor_menu():
    limpiar_pantalla()
    print("=== Agregar un Proveedor ===")
    while True:
        ruc = input("Ingrese el RUC del proveedor (11 dígitos): ").strip()
        if len(ruc) == 11 and ruc.isdigit():
            break
        else:
            print("El RUC debe tener exactamente 11 dígitos numéricos. Intente nuevamente.")
    while True:
        nombre = input("Ingrese el nombre del proveedor: ").strip()
        if nombre:
            break
        else:
            print("El nombre del proveedor no puede estar vacío. Intente nuevamente.")
    while True:
        telefono = input("Ingrese el teléfono del proveedor (9 dígitos): ").strip()
        if len(telefono) == 9 and telefono.isdigit():
            if telefono_existe_proveedores(telefono):
                print(f"El teléfono {telefono} ya está registrado. Intente con otro.")
            else:
                break
        else:
            print("El teléfono debe tener exactamente 9 dígitos numéricos. Intente nuevamente.")
    agregar_proveedor(ruc, nombre, telefono)
    input("Presione Enter para continuar...")

def editar_telefono_proveedor_menu():
    limpiar_pantalla()
    print("=== Editar el Teléfono de un Proveedor ===")
    print("Proveedores disponibles:")
    mostrar_proveedores()
    while True:
        ruc = input("Ingrese el RUC del proveedor para editar su teléfono: ").strip()
        if len(ruc) == 11 and ruc.isdigit():
            break
        else:
            print("El RUC debe tener exactamente 11 dígitos numéricos. Intente nuevamente.")
    while True:
        nuevo_telefono = input("Ingrese el nuevo teléfono del proveedor (9 dígitos): ").strip()
        if len(nuevo_telefono) == 9 and nuevo_telefono.isdigit():
            if telefono_existe_proveedores(nuevo_telefono):
                print(f"El teléfono {nuevo_telefono} ya está registrado. Intente con otro.")
            else:
                break
        else:
            print("El teléfono debe tener exactamente 9 dígitos numéricos. Intente nuevamente.")
    editar_telefono_proveedor(ruc, nuevo_telefono)
    input("Presione Enter para continuar...")

def eliminar_proveedor_menu():
    limpiar_pantalla()
    print("=== Eliminar un Proveedor ===")
    print("Proveedores disponibles:")
    mostrar_proveedores()
    while True:
        ruc = input("Ingrese el RUC del proveedor a eliminar: ").strip()
        if len(ruc) == 11 and ruc.isdigit():
            break
        else:
            print("El RUC debe tener exactamente 11 dígitos numéricos. Intente nuevamente.")
    confirmar = input(f"¿Está seguro de que desea eliminar el proveedor con RUC {ruc}? (s/n): ").lower()
    if confirmar == "s":
        eliminar_proveedor(ruc)
    else:
        print("Operación cancelada.")
    input("Presione Enter para continuar...")

def menu_estadisticas_proveedores():
    while True:
        limpiar_pantalla()
        print("=== Estadísticas de Proveedores ===")
        print("1. Mostrar proveedores con mayor contribución al inventario")
        print("2. Mostrar proveedores con mayor valor de productos")
        print("3. Mostrar proveedores con productos más vendidos")
        print("4. Mostrar promedio de productos por proveedor")
        print("5. Regresar a la Gestión de proveedores")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_proveedores_mayor_contribucion()
        elif opcion == "2":
            mostrar_proveedores_mayor_valor()
        elif opcion == "3":
            mostrar_proveedores_productos_mas_vendidos()
        elif opcion == "4":
            mostrar_promedio_productos_por_proveedor()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        input("Presione Enter para continuar...")
