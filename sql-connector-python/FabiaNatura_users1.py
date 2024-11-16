from FabiaNatura_functions import obtener_siguiente_codigo
from FabiaNatura_functions import conectar_base_datos
from FabiaNatura_api_functions import generar_datos_dni
from FabiaNatura_contracts import gestionar_actualizar_contrato_por_dni_desactivar_activar

from mysql.connector import Error
from datetime import datetime

def obtener_codigo_empleado_por_dni(cursor, dni):
    query = """
        SELECT cod_empleado 
        FROM Empleados
        WHERE dni = %s
    """
    cursor.execute(query, (dni,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]  # Retorna el código del empleado si existe
    else:
        print(f"No se encontró ningún empleado con DNI {dni}.")
        return None
    
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

def insertar_empleado(cursor, dni, estado = "activo"):
    cod_empleado = obtener_siguiente_codigo(cursor, "Empleados", "cod_empleado", "EMP")
    query_empleado = """INSERT INTO Empleados (cod_empleado, dni, estado) 
                        VALUES (%s, %s, %s)"""
    valores_empleado = (cod_empleado, dni, estado)
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
        datos_persona = generar_datos_dni(dni)
        if datos_persona:
            nombre = datos_persona["nombre"]
            apellido_paterno = datos_persona["apellido_paterno"]
            apellido_materno = datos_persona["apellido_materno"]
            fecha_nacimiento = datos_persona["fecha_nacimiento"]
            if not es_mayor_de_edad(fecha_nacimiento):
                print("No se puede insertar el cliente: La persona es menor de 18 años.")
                return
            conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                insertar_persona(cursor, dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
                conexion.commit()
                cod_empleado = insertar_empleado(cursor, dni)
                conexion.commit()
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
        datos_persona = generar_datos_dni(dni) 
        if datos_persona:
            nombre = datos_persona["nombre"]
            apellido_paterno = datos_persona["apellido_paterno"]
            apellido_materno = datos_persona["apellido_materno"]
            fecha_nacimiento = datos_persona["fecha_nacimiento"]
            if not es_mayor_de_edad(fecha_nacimiento):
                print("No se puede insertar el cliente: La persona es menor de 18 años.")
                return
            conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                insertar_persona(cursor, dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
                conexion.commit()
                cod_empleado = insertar_empleado(cursor, dni)
                conexion.commit()
                cod_asesor = insertar_asesor(cursor, cod_empleado, anios_experiencia, especialidad)
                conexion.commit()
                print(f"Asesor insertado correctamente con código: {cod_empleado, cod_asesor}")
        else: print("No se pudieron obtener los datos de la persona.")    
    except Error as e: print(f"Error al insertar datos: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def gestionar_insercion_cliente(dni, tipo_cliente="Cliente normal"):
    try:
        datos_persona = generar_datos_dni(dni)
        if datos_persona:
            nombre = datos_persona["nombre"]
            apellido_paterno = datos_persona["apellido_paterno"]
            apellido_materno = datos_persona["apellido_materno"]
            fecha_nacimiento = datos_persona["fecha_nacimiento"]
            if not es_mayor_de_edad(fecha_nacimiento):
                print("No se puede insertar el cliente: La persona es menor de 18 años.")
                return
            conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                insertar_persona(cursor, dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
                conexion.commit()
                insertar_cliente(cursor, dni, tipo_cliente)
                conexion.commit()
                print(f"Cliente insertado correctamente con DNI: {dni}")
        else: print("No se pudieron obtener los datos de la persona.")
    except Error as e: print(f"Error al insertar datos: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

# DESACTIVAR o ACTIVAR 
def desactivar_activar_empleado(cursor, dni, estado):
    cod_empleado = obtener_codigo_empleado_por_dni(cursor, dni)
    if not cod_empleado:
        print(f"No se encontró ningún empleado con DNI {dni}.")
        return
    query_verificar_estado = "SELECT estado FROM Empleados WHERE cod_empleado = %s"
    cursor.execute(query_verificar_estado, (cod_empleado,))
    estado_actual = cursor.fetchone()
    if estado_actual and estado_actual[0] == estado:
        print(f"El empleado con DNI {dni} ya está en estado '{estado}'.")
        return
    query_actualizar_estado = "UPDATE Empleados SET estado = %s WHERE cod_empleado = %s"
    cursor.execute(query_actualizar_estado, (estado, cod_empleado))
    print(f"Empleado con DNI {dni} cambiado a estado '{estado}' correctamente.")

def gestionar_cambio_estado_empleado_y_contrato(dni, estado):
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            desactivar_activar_empleado(cursor, dni, estado)
            gestionar_actualizar_contrato_por_dni_desactivar_activar(dni, estado)
            conexion.commit()
    except Error as e: print(f"Error al actualizar el estado del empleado o contrato: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def imprimir_todos_los_empleados():
    """
    Imprime todos los empleados con su información básica, roles (vendedor, asesor, o ambos) y código de contrato.
    """
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            query = """
            SELECT 
                Empleados.cod_empleado,
                Empleados.dni,
                Personas.nombre,
                Personas.apellido_paterno,
                Personas.apellido_materno,
                Empleados.estado,
                Vendedores.cod_vendedor,
                Asesores.cod_asesor,
                Asesores.anios_experiencia,
                Asesores.especialidad,
                Vendedores.rol,
                Contratos.cod_contrato,
                Contratos.fecha_inicio,
                Contratos.fecha_fin,
                Contratos.salario_men,
                Contratos.observaciones
            FROM 
                Empleados
            JOIN 
                Personas ON Empleados.dni = Personas.dni
            LEFT JOIN 
                Vendedores ON Empleados.cod_empleado = Vendedores.cod_empleado
            LEFT JOIN 
                Asesores ON Empleados.cod_empleado = Asesores.cod_empleado
            LEFT JOIN 
                Contratos ON Empleados.cod_empleado = Contratos.cod_empleado;
            """
            cursor.execute(query)
            empleados = cursor.fetchall()
            for empleado in empleados:
                (cod_empleado, dni, nombre, apellido_paterno, apellido_materno, estado, 
                 cod_vendedor, cod_asesor, anios_experiencia, especialidad, rol,
                 cod_contrato, fecha_inicio, fecha_fin, salario_men, observaciones) = empleado
                print(f"Código Empleado: {cod_empleado}")
                print(f"DNI: {dni}")
                print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno}")
                print(f"Estado: {estado}")
                # Determinar y mostrar el rol
                if cod_vendedor:
                    print(f"Rol: Vendedor")
                    print(f"  Código Vendedor: {cod_vendedor}")
                    print(f"  Rol Específico: {rol}")
                if cod_asesor:
                    print(f"Rol: Asesor")
                    print(f"  Código Asesor: {cod_asesor}")
                    print(f"  Años de Experiencia: {anios_experiencia}")
                    print(f"  Especialidad: {especialidad}")
                if not cod_vendedor and not cod_asesor:
                    print("Rol: Empleado sin rol específico")
                # Mostrar detalles del contrato si existe
                if cod_contrato:
                    print(f"Código de Contrato: {cod_contrato}")
                    print(f"  Fecha Inicio: {fecha_inicio}")
                    print(f"  Fecha Fin: {fecha_fin}")
                    print(f"  Salario Mensual: {salario_men}")
                    print(f"  Observaciones: {observaciones}")
                else:
                    print("Contrato: Sin contrato asociado")
                print("-" * 30)
    except Error as e: print(f"Error al realizar la consulta: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def imprimir_detalles_empleado_por_dni(dni):
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            query = """
            SELECT 
                Empleados.cod_empleado,
                COALESCE(Vendedores.cod_vendedor, Asesores.cod_asesor) AS codigo_rol,
                Personas.nombre,
                Personas.apellido_paterno,
                Personas.apellido_materno,
                Empleados.estado
            FROM 
                Empleados
            JOIN 
                Personas ON Empleados.dni = Personas.dni
            LEFT JOIN 
                Vendedores ON Empleados.cod_empleado = Vendedores.cod_empleado
            LEFT JOIN 
                Asesores ON Empleados.cod_empleado = Asesores.cod_empleado
            WHERE 
                Empleados.dni = %s;
            """
            cursor.execute(query, (dni,))
            empleado = cursor.fetchone()
            if empleado:
                codigo_empleado, codigo_rol, nombre, apellido_paterno, apellido_materno, estado = empleado
                rol = "Vendedor" if codigo_rol and "VEND" in codigo_rol else "Asesor" if codigo_rol else "Empleado sin rol específico"
                print(f"Código Empleado: {codigo_empleado}")
                print(f"Código Rol: {codigo_rol}")
                print(f"Rol: {rol}")
                print(f"Nombre Completo: {nombre} {apellido_paterno} {apellido_materno}")
                print(f"Estado: {estado}")
            else: print(f"No se encontró ningún empleado con DNI {dni}.")    
    except Error as e: print(f"Error al realizar la consulta: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def imprimir_todos_los_clientes():
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            query = """
            SELECT 
                Clientes.dni,
                Personas.nombre,
                Personas.apellido_paterno,
                Personas.apellido_materno,
                Clientes.tipo_cliente
            FROM 
                Clientes
            JOIN 
                Personas ON Clientes.dni = Personas.dni;
            """
            cursor.execute(query)
            clientes = cursor.fetchall()
            for cliente in clientes:
                dni, nombre, apellido_paterno, apellido_materno, tipo_cliente = cliente
                print(f"DNI: {dni}")
                print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno}")
                print(f"Tipo de Cliente: {tipo_cliente}")
                print("-" * 30)
    except Error as e:  print(f"Error al realizar la consulta: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()


def imprimir_detalles_cliente_por_dni(dni):
    try:
        conexion = conectar_base_datos("LocalHost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            query = """
            SELECT 
                Clientes.dni,
                Personas.nombre,
                Personas.apellido_paterno,
                Personas.apellido_materno,
                Clientes.tipo_cliente
            FROM 
                Clientes
            JOIN 
                Personas ON Clientes.dni = Personas.dni
            WHERE 
                Clientes.dni = %s;
            """
            cursor.execute(query, (dni,))
            cliente = cursor.fetchone()
            if cliente:
                dni, nombre, apellido_paterno, apellido_materno, tipo_cliente = cliente
                print(f"DNI: {dni}")
                print(f"Nombre Completo: {nombre} {apellido_paterno} {apellido_materno}")
                print(f"Tipo de Cliente: {tipo_cliente}")
            else:
                print(f"No se encontró ningún cliente con DNI {dni}.")
    except Error as e: print(f"Error al realizar la consulta: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()