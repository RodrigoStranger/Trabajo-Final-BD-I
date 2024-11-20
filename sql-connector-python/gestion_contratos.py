import os
from functions_users import *
from functions_contracts import *

def limpiar_pantalla(): os.system('cls' if os.name == 'nt' else 'clear')

def menu_gestion_contratos():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Contratos ===")
        print("1. Agregar un contrato")
        print("2. Editar un contrato")
        print("3. Inhabilitar o habilitar un contrato")
        print("4. Observar estadísticas generales")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_contrato_menu()
        elif opcion == "2":
            editar_contrato_menu()
        elif opcion == "3":
            cambiar_estado_contrato_menu()
        elif opcion == "4":
            print("Función pendiente de desarrollo. Presione Enter para continuar...")
            input()
        elif opcion == "5":
            print("Volviendo a la ventana principal...")
            input("Presione Enter para continuar...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

def agregar_contrato_menu():
    limpiar_pantalla()
    print("=== Agregar un Contrato ===")
    while True:
        dni = input("Ingrese el dni del empleado: ")
        if len(dni) == 8 and dni.isdigit():
            if persona_existe(dni):
                break
            else:
                print("El dni ingresado no pertenece a ninguna persona registrada. Intente nuevamente.")
        else:
            print("El dni debe tener exactamente 8 dígitos numéricos. Intente nuevamente.")
    while True:
        try:
            salario = float(input("Ingrese el salario mensual: "))
            if salario > 0:
                break
            else:
                print("El salario debe ser mayor a 0. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un valor numérico válido para el salario. Intente nuevamente.")
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD) (Opcional, puede dejar en blanco): ")
    if fecha_fin.strip() == "":
        fecha_fin = None
    observaciones = input("Ingrese observaciones del contrato: ")
    agregar_contrato(dni, fecha_inicio, fecha_fin, salario, observaciones)
    input("Presione Enter para continuar...")

def editar_contrato_menu():
    limpiar_pantalla()
    print("=== Editar un Contrato ===")
    while True:
        dni = input("Ingrese el DNI del empleado: ")
        if len(dni) == 8 and dni.isdigit():
            if persona_existe(dni):
                break
            else:
                print("El DNI ingresado no pertenece a ninguna persona registrada. Intente nuevamente.")
        else:
            print("El DNI debe tener exactamente 8 dígitos numéricos. Intente nuevamente.")
    limpiar_pantalla()
    print(f"=== Empleado {dni} ===")
    print("1. Editar sueldo")
    print("2. Editar fechas")
    print("3. Editar observaciones")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        while True:
            try:
                nuevo_sueldo = float(input("Ingrese el nuevo sueldo: "))
                if nuevo_sueldo > 0:
                    break
                else:
                    print("El sueldo debe ser mayor a 0. Intente nuevamente.")
            except ValueError:
                print("Debe ingresar un valor numérico válido para el sueldo. Intente nuevamente.")
        editar_contrato_sueldo(dni, nuevo_sueldo)
    elif opcion == "2":
        nueva_fecha_inicio = input("Ingrese la nueva fecha de inicio (YYYY-MM-DD): ")
        nueva_fecha_fin = input("Ingrese la nueva fecha de fin (YYYY-MM-DD) (Opcional, puede dejar en blanco): ")
        if nueva_fecha_fin.strip() == "":
            nueva_fecha_fin = None
        editar_contrato_fechas(dni, nueva_fecha_inicio, nueva_fecha_fin)
    elif opcion == "3":
        nueva_observacion = input("Ingrese la nueva observación: ")
        editar_contrato_observacion(dni, nueva_observacion)
    else:
        print("Opción no válida.")
    input("Presione Enter para continuar...")

def cambiar_estado_contrato_menu():
    limpiar_pantalla()
    print("=== Cambiar Estado de un Contrato ===")
    while True:
        dni = input("Ingrese el DNI del empleado: ")
        if len(dni) == 8 and dni.isdigit():
            if persona_existe(dni):
                break
            else:
                print("El DNI ingresado no pertenece a ninguna persona registrada. Intente nuevamente.")
        else:
            print("El DNI debe tener exactamente 8 dígitos numéricos. Intente nuevamente.")

    while True:
        nuevo_estado = input("Ingrese el nuevo estado ('activo' o 'inactivo'): ").lower()
        if nuevo_estado in ["activo", "inactivo"]:
            break
        else:
            print("Estado inválido. Solo se permite 'activo' o 'inactivo'. Intente nuevamente.")
    cambiar_estado_contrato(dni, nuevo_estado)
    input("Presione Enter para continuar...")