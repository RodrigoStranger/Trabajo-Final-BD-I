from fronted_users import menu_gestion_personal 
from fronted_contracts import menu_gestion_contratos
from fronted_categories import menu_gestion_categorias
from fronted_suppliers import menu_gestion_proveedores
from fronted_productos import menu_gestion_productos
import os

def limpiar_pantalla(): os.system('cls' if os.name == 'nt' else 'clear')

def menu_admin():
    while True:
        limpiar_pantalla()
        print("     === FabiaNatura ===")
        print("=== Administración General ===")
        print("1. Gestión de Ventas")
        print("2. Gestión del Personal")
        print("3. Gestión de Contratos")
        print("4. Gestión de Categorias")
        print("5. Gestión de Proveedores")
        print("6. Gestión de Productos")
        print("7. Gestión de Reportes")
        print("8. Salir del sistema")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("Función pendiente de desarrollo. Presione Enter para continuar...")
            input()
        elif opcion == "2":
            menu_gestion_personal()
        elif opcion == "3":
            menu_gestion_contratos()
        elif opcion == "4":
            menu_gestion_categorias()
        elif opcion == "5":
            menu_gestion_proveedores()
        elif opcion == "6":
            menu_gestion_productos()
        if opcion == "7":
            print("Función pendiente de desarrollo. Presione Enter para continuar...")
            input()
        elif opcion == "8":
            print("Saliendo del sistema.....")
            input("Presione Enter para continuar...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")