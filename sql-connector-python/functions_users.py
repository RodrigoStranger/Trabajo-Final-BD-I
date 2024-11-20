from functions import *
from api import *

def persona_existe(dni):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            query = f"SELECT VerificarPersonaExiste('{dni}') AS Existe;"
            cursor.execute(query)
            resultado = cursor.fetchone()
            existe = resultado[0]  # 1 para TRUE, 0 para FALSE
            return True if existe == 1 else False
    except Error as e: 
        print(f"Error al conectar con la base de datos: {e}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def telefono_existe(telefono):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            query = f"SELECT VerificarTelefonoExiste('{telefono}') AS ExisteTelefono;"
            cursor.execute(query)
            resultado = cursor.fetchone()
            return resultado[0] == 1  # Retorna True si existe, False si no
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def insertar_cliente(dni, telefono):
    datos = generar_datos_completos(dni)
    if datos:
        try:
            conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
            if not conexion:
                print("No se pudo establecer conexión con la base de datos.")
                return
            cursor = conexion.cursor()
            cursor.callproc('AgregarCliente', [
                dni,
                datos["nombre"],
                datos["apellido_paterno"],
                datos["apellido_materno"],
                datos["fecha_nacimiento"],
                telefono,
                datos["direccion"]
            ])
            conexion.commit()
            print(f"Cliente {datos['nombre']} insertado correctamente.")
        except Error as e: print(f"Error al insertar el cliente: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
    else: print("No se pudieron obtener los datos del cliente desde la API.")

def insertar_vendedor(dni, telefono, rol):
    datos = generar_datos_completos(dni)
    if datos:
        try:
            conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
            if not conexion:
                print("No se pudo establecer conexión con la base de datos.")
                return
            cursor = conexion.cursor()
            cursor.callproc('AgregarVendedor', [dni,
                datos["nombre"],
                datos["apellido_paterno"],
                datos["apellido_materno"],
                datos["fecha_nacimiento"],
                telefono,
                datos["direccion"],
                rol
            ])
            conexion.commit()
            print(f"Vendedor {datos['nombre']} insertado correctamente.")
        except Error as e: print(f"Error al insertar el vendedor: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
    else: print("No se pudieron obtener los datos del vendedor desde la API.")

def insertar_asesor(dni, telefono, experiencia, especialidad):
    datos = generar_datos_completos(dni)
    if datos:
        try:
            conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
            if not conexion:
                print("No se pudo establecer conexión con la base de datos.")
                return
            cursor = conexion.cursor()
            cursor.callproc('AgregarAsesor', [
                dni,
                datos["nombre"],
                datos["apellido_paterno"],
                datos["apellido_materno"],
                datos["fecha_nacimiento"],
                telefono,
                datos["direccion"],
                experiencia,
                especialidad
            ])
            conexion.commit()
            print(f"Asesor {datos['nombre']} insertado correctamente.")
        except Error as e: print(f"Error al insertar el asesor: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
    else: print("No se pudieron obtener los datos del asesor desde la API.")


def editar_telefono(dni, telefono_nuevo):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarTelefono', [dni, telefono_nuevo])
            conexion.commit()
            print(f"Teléfono actualizado correctamente para el dni {dni}.")
    except Exception as e:
        print(f"Error al actualizar el teléfono: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_direccion(dni, direccion_nueva):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarDireccion', [dni, direccion_nueva])
            conexion.commit()
            print(f"Dirección actualizada correctamente para el dni {dni}.")
    except Exception as e:
        print(f"Error al actualizar la dirección: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_especialidad_asesor(dni, especialidad_nueva):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarEspecialidadAsesor', [dni, especialidad_nueva])
            conexion.commit()
            print(f"Especialidad actualizada correctamente para el dni {dni}.")
    except Exception as e:
        print(f"Error al actualizar la especialidad: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_experiencia_asesor(dni, experiencia_nueva):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarExperienciaAsesor', [dni, experiencia_nueva])
            conexion.commit()
            print(f"Experiencia actualizada correctamente para el dni {dni}.")
    except Exception as e:
        print(f"Error al actualizar la experiencia: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_rol_vendedor(dni, rol_nuevo):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('EditarRolVendedor', [dni, rol_nuevo])
            conexion.commit()
            print(f"Rol actualizado correctamente para el dni {dni}.")
    except Exception as e:
        print(f"Error al actualizar el rol: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def cambiar_estado_asesor(dni, nuevo_estado):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('CambiarEstadoAsesor', [dni, nuevo_estado])
            conexion.commit()
            print(f"Estado del asesor con dni {dni} cambiado a {nuevo_estado}.")
    except Exception as e:
        print(f"Error al cambiar el estado del asesor: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def cambiar_estado_vendedor(dni, nuevo_estado):
    try:
        conexion = conectar_base_datos("localhost", "FabiaNatura", "rodrigo", "ubnt")
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.callproc('CambiarEstadoVendedor', [dni, nuevo_estado])
            conexion.commit()
            print(f"Estado del vendedor con dni {dni} cambiado a {nuevo_estado}.")
    except Exception as e:
        print(f"Error al cambiar el estado del vendedor: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()