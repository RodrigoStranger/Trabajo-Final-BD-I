import os
from functions_users import *

def limpiar_pantalla(): os.system('cls' if os.name == 'nt' else 'clear')

def menu_gestion_personal():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Personal ===")
        print("1. Gestión de Vendedores")
        print("2. Gestión de Asesores")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_vendedores()
        elif opcion == "2":
            menu_asesores()
        elif opcion == "3":
            print("Saliendo del sistema...")
            print("¡Gracias por usar FabiaNatura!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def menu_vendedores():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Vendedores ===")
        print("1. Insertar Vendedor")
        print("2. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            insertar_vendedor_menu()
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def menu_asesores():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Asesores ===")
        print("1. Insertar Asesor")
        print("2. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            insertar_asesor_menu()
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def insertar_vendedor_menu():
    """Lógica para insertar un vendedor."""
    limpiar_pantalla()
    print("=== Inserción de Vendedor ===")
    dni = input("Ingrese el DNI del vendedor: ")
    telefono = input("Ingrese el teléfono del vendedor: ")
    rol = input("Ingrese el rol del vendedor: ")
    insertar_vendedor(dni, telefono, rol)
    input("Presione Enter para continuar...")

def insertar_asesor_menu():
    limpiar_pantalla()
    print("=== Inserción de Asesor ===")
    dni = input("Ingrese el DNI del asesor: ")
    telefono = input("Ingrese el teléfono del asesor: ")
    experiencia = int(input("Ingrese la experiencia (en años) del asesor: "))
    especialidad = input("Ingrese la especialidad del asesor: ")
    insertar_asesor(dni, telefono, experiencia, especialidad)
    input("Presione Enter para continuar...")