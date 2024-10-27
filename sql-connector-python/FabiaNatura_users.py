from FabiaNatura_functions import obtener_siguiente_codigo
from FabiaNatura_functions import conectar_base_datos
from FabiaNatura_api_functions import generar_datos_dni

from mysql.connector import Error
from datetime import datetime

def es_mayor_de_edad(fecha_nacimiento, edad_minima=18):
    """
    Verifica si una persona es mayor de la edad mínima especificada.
    Args:
        fecha_nacimiento (str): Fecha de nacimiento en formato 'YYYY-MM-DD'.
        edad_minima (int): Edad mínima para ser considerado mayor de edad (por defecto es 18).
    Returns:
        bool: True si la persona es mayor de la edad mínima, False en caso contrario.
    """
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad >= edad_minima

def insertar_persona(cursor, dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
    query_persona = """INSERT INTO Personas (dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento) 
                       VALUES (%s, %s, %s, %s, %s)"""
    valores_persona = (dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
    cursor.execute(query_persona, valores_persona)

def insertar_empleado(cursor, dni):
    cod_empleado = obtener_siguiente_codigo(cursor, "Empleados", "cod_empleado", "EMP")
    query_empleado = """INSERT INTO Empleados (cod_empleado, dni) 
                        VALUES (%s, %s)"""
    valores_empleado = (cod_empleado, dni)
    cursor.execute(query_empleado, valores_empleado)
    return cod_empleado

def insertar_vendedor(cursor, cod_empleado, rol):
    cod_vendedor = obtener_siguiente_codigo(cursor, "Vendedores", "cod_vendedor", "VEND")
    query_vendedor = """INSERT INTO Vendedores (cod_vendedor, cod_empleado, rol) 
                        VALUES (%s, %s, %s)"""
    valores_vendedor = (cod_vendedor, cod_empleado, rol)
    cursor.execute(query_vendedor, valores_vendedor)
    return cod_vendedor

def insertar_asesor(cursor, cod_empleado, años_experiencia, especialidad):
    cod_asesor = obtener_siguiente_codigo(cursor, "Asesores", "cod_asesor", "ASE")
    query_asesor = """INSERT INTO Asesores (cod_asesor, cod_empleado, anios_experiencia, especialidad) 
                      VALUES (%s, %s, %s, %s)"""
    valores_asesor = (cod_asesor, cod_empleado, años_experiencia, especialidad)
    cursor.execute(query_asesor, valores_asesor)
    return cod_asesor

def insertar_cliente(cursor, dni, tipo_cliente):
    query_cliente = """INSERT INTO Clientes (dni, tipo_cliente) 
                       VALUES (%s, %s)"""
    valores_cliente = (dni, tipo_cliente)
    cursor.execute(query_cliente, valores_cliente)

def gestionar_insercion_vendedor(dni, rol):
    try:
        # Obtener datos personales usando la función generar_datos_dni
        datos_persona = generar_datos_dni(dni)
        if datos_persona:
            # Extraer los datos necesarios del diccionario
            nombre = datos_persona["nombre"]
            apellido_paterno = datos_persona["apellido_paterno"]
            apellido_materno = datos_persona["apellido_materno"]
            fecha_nacimiento = datos_persona["fecha_nacimiento"]
            if not es_mayor_de_edad(fecha_nacimiento):
                print("No se puede insertar el cliente: La persona es menor de 18 años.")
                return
            # Conectar a la base de datos
            conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                # Insertar persona en la tabla Personas
                insertar_persona(cursor, dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
                conexion.commit()
                # Insertar empleado en la tabla Empleados
                cod_empleado = insertar_empleado(cursor, dni)
                conexion.commit()
                # Insertar vendedor en la tabla Vendedores
                cod_vendedor = insertar_vendedor(cursor, cod_empleado, rol)
                conexion.commit()
                print(f"Vendedor insertado correctamente con código: {cod_empleado, cod_vendedor}")
        else: print("No se pudieron obtener los datos de la persona.")  
    except Error as e: print(f"Error al insertar datos: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def gestionar_insercion_asesor(dni, anios_experiencia, especialidad):
    try:
        # Obtener datos personales usando la función generar_datos_dni
        datos_persona = generar_datos_dni(dni) 
        if datos_persona:
            # Extraer los datos necesarios del diccionario
            nombre = datos_persona["nombre"]
            apellido_paterno = datos_persona["apellido_paterno"]
            apellido_materno = datos_persona["apellido_materno"]
            fecha_nacimiento = datos_persona["fecha_nacimiento"]
            if not es_mayor_de_edad(fecha_nacimiento):
                print("No se puede insertar el cliente: La persona es menor de 18 años.")
                return            
            # Conectar a la base de datos
            conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                # Insertar persona en la tabla Personas
                insertar_persona(cursor, dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
                conexion.commit()
                # Insertar empleado en la tabla Empleados
                cod_empleado = insertar_empleado(cursor, dni)
                conexion.commit()
                # Insertar asesor en la tabla Asesores
                cod_asesor = insertar_asesor(cursor, cod_empleado, anios_experiencia, especialidad)
                conexion.commit()
                print(f"Asesor insertado correctamente con código: {cod_empleado, cod_asesor}")
        else: print("No se pudieron obtener los datos de la persona.")    
    except Error as e: print(f"Error al insertar datos: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def gestionar_insercion_cliente(dni, tipo_cliente):
    try:
        # Obtener datos personales usando la función generar_datos_dni
        datos_persona = generar_datos_dni(dni)
        if datos_persona:
            # Extraer los datos necesarios del diccionario
            nombre = datos_persona["nombre"]
            apellido_paterno = datos_persona["apellido_paterno"]
            apellido_materno = datos_persona["apellido_materno"]
            fecha_nacimiento = datos_persona["fecha_nacimiento"]
            if not es_mayor_de_edad(fecha_nacimiento):
                print("No se puede insertar el cliente: La persona es menor de 18 años.")
                return
            # Conectar a la base de datos
            conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                # Insertar persona en la tabla Personas
                insertar_persona(cursor, dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
                conexion.commit()
                # Insertar cliente en la tabla Clientes
                insertar_cliente(cursor, dni, tipo_cliente)
                conexion.commit()
                print(f"Cliente insertado correctamente con DNI: {dni}")
        else:
            print("No se pudieron obtener los datos de la persona.")
    except Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()