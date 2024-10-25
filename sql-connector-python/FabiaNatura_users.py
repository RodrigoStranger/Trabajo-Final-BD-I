from FabiaNatura_functions import obtener_siguiente_codigo
from FabiaNatura_functions import conectar_base_datos

from mysql.connector import Error

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
    query_asesor = """INSERT INTO Asesores (cod_asesor, cod_empleado, años_experiencia, especialidad) 
                      VALUES (%s, %s, %s, %s)"""
    valores_asesor = (cod_asesor, cod_empleado, años_experiencia, especialidad)
    cursor.execute(query_asesor, valores_asesor)
    return cod_asesor

def insertar_cliente(cursor, dni, tipo_cliente):
    query_cliente = """INSERT INTO Clientes (dni, tipo_cliente) 
                       VALUES (%s, %s)"""
    valores_cliente = (dni, tipo_cliente)
    cursor.execute(query_cliente, valores_cliente)

def gestionar_insercion_vendedor(dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, rol):
    try: 
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
    except Error as e: print(f"Error al insertar datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def gestionar_insercion_asesor(dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, años_experiencia, especialidad):
    try:
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
            cod_asesor = insertar_asesor(cursor, cod_empleado, años_experiencia, especialidad)
            conexion.commit()
            print(f"Asesor insertado correctamente con código: {cod_empleado, cod_asesor}")
    except Error as e: print(f"Error al insertar datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def gestionar_insercion_cliente(dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, tipo_cliente):
    try:
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
    except Error as e: print(f"Error al insertar datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

