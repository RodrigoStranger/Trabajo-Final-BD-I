from functions import *

def agregar_contrato(dni, fecha_inicio, fecha_fin, salario_mensual, observaciones):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('AgregarContrato', [dni, fecha_inicio, fecha_fin, salario_mensual, observaciones])
            conexion.commit()
            print(f"Contrato para el empleado con dni {dni} creado exitosamente.")
    except Error as e:
        print(f"Error al agregar el contrato: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_contrato_sueldo(dni, nuevo_sueldo):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarContratoSueldo', [dni, nuevo_sueldo])
            conexion.commit()
            print(f"Sueldo actualizado exitosamente para el empleado con dni {dni}.")
    except Error as e:
        print(f"Error al actualizar el sueldo del contrato: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_contrato_fechas(dni, nueva_fecha_inicio, nueva_fecha_fin):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarContratoFechas', [dni, nueva_fecha_inicio, nueva_fecha_fin])
            conexion.commit()
            print(f"Fechas actualizadas exitosamente para el empleado con DNI {dni}.")
    except Error as e:
        print(f"Error al actualizar las fechas del contrato: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_contrato_observacion(dni, nueva_observacion):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarContratoObservacion', [dni, nueva_observacion])
            conexion.commit()
            print(f"Observación actualizada exitosamente para el empleado con DNI {dni}.")
    except Error as e:
        print(f"Error al actualizar la observación del contrato: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def cambiar_estado_contrato(dni, nuevo_estado):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('CambiarEstadoContrato', [dni, nuevo_estado])
            conexion.commit()
            print(f"Estado del contrato actualizado a '{nuevo_estado}' para el empleado con DNI {dni}.")
    except Error as e:
        print(f"Error al cambiar el estado del contrato: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()