from FabiaNatura_functions import conectar_base_datos
from FabiaNatura_functions import obtener_siguiente_codigo
from mysql.connector import Error

def obtener_cod_empleado_por_dni(cursor, dni):
    query = "SELECT cod_empleado FROM Empleados WHERE dni = %s"
    cursor.execute(query, (dni,))
    resultado = cursor.fetchone()
    if resultado: return resultado[0]
    else:
        print(f"No se encontró ningún empleado con DNI {dni}.")
        return None

def obtener_codigo_contrato(cursor, cod_empleado):
    query = "SELECT cod_contrato FROM Contratos WHERE cod_empleado = %s"
    cursor.execute(query, (cod_empleado,))
    resultado = cursor.fetchone()
    if resultado: return resultado[0]  # Retorna el código del contrato si existe
    else:
        print(f"El empleado con código {cod_empleado} no tiene un contrato existente.")
        return None

def obtener_codigo_contrato_por_dni(cursor, dni):
    query = """
        SELECT Contratos.cod_contrato 
        FROM Contratos
        INNER JOIN Empleados ON Contratos.cod_empleado = Empleados.cod_empleado
        WHERE Empleados.dni = %s
    """
    cursor.execute(query, (dni,))
    resultado = cursor.fetchone()
    if resultado: 
        return resultado[0]  # Retorna el código del contrato si existe
    else:
        print(f"No se encontró ningún contrato asociado al empleado con DNI {dni}.")
        return None
       
def verificar_contrato_existente(cursor, cod_empleado):
    query = "SELECT cod_contrato FROM Contratos WHERE cod_empleado = %s"
    cursor.execute(query, (cod_empleado,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"El empleado con código {cod_empleado} ya tiene un contrato: {resultado[0]}. No se puede insertar otro contrato.")
        return True  # Ya tiene contrato
    return False  # No tiene contrato

# CREATE CONTRATO
def insertar_contrato(cursor, cod_empleado, fecha_inicio, fecha_fin, salario_men, observaciones):
    # Verificamos si el empleado ya tiene un contrato
    if verificar_contrato_existente(cursor, cod_empleado): return  # Si ya tiene contrato, no se inserta otro
    # Usamos la función genérica para obtener el siguiente código de contrato
    cod_contrato = obtener_siguiente_codigo(cursor, "Contratos", "cod_contrato", "CONT")
    # Insertar el contrato
    query_contrato = """INSERT INTO Contratos (cod_contrato, cod_empleado, fecha_inicio, fecha_fin, salario_men, observaciones) 
                        VALUES (%s, %s, %s, %s, %s, %s)"""
    valores_contrato = (cod_contrato, cod_empleado, fecha_inicio, fecha_fin, salario_men, observaciones)
    cursor.execute(query_contrato, valores_contrato)
    print(f"Contrato insertado correctamente para el empleado con código {cod_empleado}.")

def gestionar_insercion_contrato(dni, fecha_inicio, fecha_fin, salario_men, observaciones):
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            # Buscar código de empleado por el DNI
            cod_empleado = obtener_cod_empleado_por_dni(cursor, dni)
            if not cod_empleado: return  # Si no se encuentra el empleado, no se continúa
            # Insertar contrato si el empleado no tiene uno
            insertar_contrato(cursor, cod_empleado, fecha_inicio, fecha_fin, salario_men, observaciones)
            conexion.commit()
    except Error as e: print(f"Error al insertar datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# UPDATE CONTRATO
def actualizar_contrato_por_dni(cursor, dni, fecha_inicio, fecha_fin, salario_men, observaciones):
    # Utilizamos la función obtener_codigo_contrato_por_dni para buscar el contrato
    cod_contrato = obtener_codigo_contrato_por_dni(cursor, dni)
    if cod_contrato:
        # Actualizar el contrato con los nuevos datos
        query_update_contrato = """UPDATE Contratos 
                                   SET fecha_inicio = %s, fecha_fin = %s, salario_men = %s, observaciones = %s
                                   WHERE cod_contrato = %s"""
        valores_update = (fecha_inicio, fecha_fin, salario_men, observaciones, cod_contrato)
        cursor.execute(query_update_contrato, valores_update)
        print(f"Contrato actualizado correctamente para el empleado con DNI {dni}.")
    else: print(f"No se encontró ningún contrato asociado al empleado con DNI {dni}.")

def gestionar_actualizacion_contrato(dni, fecha_inicio, fecha_fin, salario_men, observaciones):
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            # Actualizar contrato usando solo el DNI
            actualizar_contrato_por_dni(cursor, dni, fecha_inicio, fecha_fin, salario_men, observaciones)
            conexion.commit()
    except Error as e: print(f"Error al actualizar el contrato: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# READ
def obtener_contratos_y_empleados():
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            # Consulta para obtener contratos, empleados y nombres
            query = """
            SELECT 
                Contratos.cod_contrato,
                Contratos.fecha_inicio,
                Contratos.fecha_fin,
                Contratos.salario_men,
                Contratos.observaciones,
                Empleados.cod_empleado,
                Empleados.dni,
                Personas.nombre AS nombre_empleado
            FROM 
                Contratos
            JOIN 
                Empleados ON Contratos.cod_empleado = Empleados.cod_empleado
            JOIN 
                Personas ON Empleados.dni = Personas.dni;
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            for contrato in resultados:
                print(f"Nombre de Empleado: {contrato[7]}")
                print(f"Dni de Empleado: {contrato[6]}")
                print(f"Código de Empleado: {contrato[5]}")
                print(f"Código de Contrato: {contrato[0]}")
                print(f"Fecha Inicio: {contrato[1]}")
                print(f"Fecha Fin: {contrato[2]}")
                print(f"Salario Mensual: {contrato[3]}")
                print(f"Observaciones: {contrato[4]}")
                print("-" * 30)
    except Error as e: print(f"Error al realizar la consulta: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def obtener_detalles_contrato_por_dni(dni):
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            # Obtener el código de contrato usando el DNI
            cod_contrato = obtener_codigo_contrato_por_dni(cursor, dni)
            if not cod_contrato:
                return  # Si no se encuentra el contrato, la función termina
            # Consulta para obtener detalles del contrato y el empleado
            query = """
            SELECT 
                Contratos.cod_contrato,
                Contratos.fecha_inicio,
                Contratos.fecha_fin,
                Contratos.salario_men,
                Contratos.observaciones,
                Empleados.cod_empleado,
                Empleados.dni,
                Personas.nombre AS nombre_empleado
            FROM 
                Contratos
            JOIN 
                Empleados ON Contratos.cod_empleado = Empleados.cod_empleado
            JOIN 
                Personas ON Empleados.dni = Personas.dni
            WHERE 
                Contratos.cod_contrato = %s;
            """
            cursor.execute(query, (cod_contrato,))
            resultado = cursor.fetchone()
            # Mostrar los detalles del contrato si se encontró
            if resultado:
                print(f"Código de Contrato: {resultado[0]}")
                print(f"Fecha Inicio: {resultado[1]}")
                print(f"Fecha Fin: {resultado[2]}")
                print(f"Salario Mensual: {resultado[3]}")
                print(f"Observaciones: {resultado[4]}")
                print(f"Código de Empleado: {resultado[5]}")
                print(f"DNI de Empleado: {resultado[6]}")
                print(f"Nombre de Empleado: {resultado[7]}")
            else: print("No se encontró ningún detalle para el contrato especificado.")
    except Error as e: print(f"Error al realizar la consulta: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()