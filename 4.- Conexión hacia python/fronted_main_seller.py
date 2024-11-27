import os
from fronted_sales import menu_realizar_venta
def limpiar_pantalla(): os.system('cls' if os.name == 'nt' else 'clear')

def menu_seller():
    while True:
        limpiar_pantalla()
        print("     === FabiaNatura ===")
        print("=== Vendedores ===")
        print("1. Realizar una venta")
        print("2. Salir del sistema")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_realizar_venta()
        elif opcion == "2":
            print("Saliendo del sistema.....")
            input("Presione Enter para continuar...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")