import os
from backend_categories import *

def limpiar_pantalla(): os.system('cls' if os.name == 'nt' else 'clear')

def menu_gestion_categorias():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Categorías ===")
        print("1. Agregar una categoría")
        print("2. Editar una categoría")
        print("3. Eliminar una categoría")
        print("4. Observar estadísticas generales")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_categoria_menu()
        elif opcion == "2":
            editar_categoria_menu()
        elif opcion == "3":
            eliminar_categoria_menu()
        elif opcion == "4":
            print("Función pendiente de desarrollo. Presione Enter para continuar...")
            input()
        elif opcion == "5":
            print("Saliendo del menú de Gestión de Categorías...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")


def agregar_categoria_menu():
    limpiar_pantalla()
    print("=== Agregar una Categoría ===")
    while True:
        nombre = input("Ingrese el nombre de la nueva categoría: ").strip()
        if nombre:
            break
        else:
            print("El nombre de la categoría no puede estar vacío. Intente nuevamente.")
    while True:
        descripcion = input("Ingrese una descripción para la categoría: ").strip()
        if descripcion:
            break
        else:
            print("La descripción de la categoría no puede estar vacía. Intente nuevamente.")
    agregar_categoria(nombre, descripcion)
    input("Presione Enter para continuar...")


def editar_categoria_menu():
    limpiar_pantalla()
    print("=== Editar una Categoría ===")
    print("Categorías disponibles:")
    mostrar_categorias()
    while True:
        try:
            cod_categoria = int(input("Seleccione el código de la categoría a editar: "))
            break
        except ValueError:
            print("Debe ingresar un número válido. Intente nuevamente.")
    limpiar_pantalla()
    print(f"=== Categoría {cod_categoria} ===")
    print("1. Editar nombre")
    print("2. Editar descripción")
    opcion_editar = input("Seleccione una opción: ")
    if opcion_editar == "1":
        while True:
            nuevo_nombre = input("Ingrese el nuevo nombre para la categoría: ").strip()
            if nuevo_nombre:
                break
            else:
                print("El nombre no puede estar vacío. Intente nuevamente.")
        editar_nombre_categoria(cod_categoria, nuevo_nombre)
    elif opcion_editar == "2":
        while True:
            nueva_descripcion = input("Ingrese la nueva descripción para la categoría: ").strip()
            if nueva_descripcion:
                break
            else:
                print("La descripción no puede estar vacía. Intente nuevamente.")
        editar_descripcion_categoria(cod_categoria, nueva_descripcion)
    else:
        print("Opción no válida. Intente nuevamente.")
    input("Presione Enter para continuar...")

def eliminar_categoria_menu():
    limpiar_pantalla()
    print("=== Eliminar una Categoría ===")
    print("Categorías disponibles:")
    mostrar_categorias()
    while True:
        try:
            cod_categoria = int(input("Seleccione el código de la categoría a eliminar: "))
            break
        except ValueError:
            print("Debe ingresar un número válido. Intente nuevamente.")
    confirmar = input(f"¿Está seguro de que desea eliminar la categoría con código {cod_categoria}? (s/n): ").lower()
    if confirmar == "s":
        eliminar_categoria(cod_categoria)
    else:
        print("Operación cancelada.")
    input("Presione Enter para continuar...")