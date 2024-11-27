from backend_general import *
from backend_api import *
from tabulate import tabulate # pip install tabulate 

def mostrar_empleados():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarEmpleados;"
        cursor.execute(query)
        empleados = cursor.fetchall()
        if empleados:
            from tabulate import tabulate
            headers = ["DNI", "CodigoEmpleado", "Nombre", "ApellidoPaterno", "ApellidoMaterno", "TieneContrato"]
            print(tabulate(empleados, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No hay empleados disponibles.")
    except Exception as e:
        print(f"Error al consultar empleados: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_vendedores():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarVendedores;"
        cursor.execute(query)
        vendedores = cursor.fetchall()
        if vendedores:
            from tabulate import tabulate
            headers = ["DNI", "CodigoVendedor", "Nombre", "ApellidoPaterno", "ApellidoMaterno", "Rol", "TieneContrato"]
            print(tabulate(vendedores, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No hay vendedores disponibles.")
    except Exception as e:
        print(f"Error al consultar vendedores: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_asesores():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarAsesores;"
        cursor.execute(query)
        asesores = cursor.fetchall()
        if asesores:
            from tabulate import tabulate
            headers = ["DNI", "CodigoAsesor", "Nombre", "ApellidoPaterno", "ApellidoMaterno", "Especialidad", "Experiencia", "TieneContrato"]
            print(tabulate(asesores, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No hay asesores disponibles.")
    except Exception as e:
        print(f"Error al consultar asesores: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()


def persona_existe(dni):
    try:
        conexion = conectar_base_datos()
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
        conexion = conectar_base_datos()
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
            conexion = conectar_base_datos()
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
            conexion = conectar_base_datos()
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
            conexion = conectar_base_datos()
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
        conexion = conectar_base_datos()
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
        conexion = conectar_base_datos()
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
        conexion = conectar_base_datos()
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
        conexion = conectar_base_datos()
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
        conexion = conectar_base_datos()
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
        conexion = conectar_base_datos()
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
        conexion = conectar_base_datos()
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

def mostrar_top_vendedores():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarTopVendedores;"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if resultados:
            from tabulate import tabulate
            headers = ["Codigo", "Vendedor", "Total Ventas", "Total Ingresos Generados"]
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No hay datos disponibles en la vista de vendedores con más ventas.")
    except Exception as e:
        print(f"Error al consultar los vendedores con más ventas: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_vendedores_con_menos_ventas():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarVendedoresConMenosVentas;"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if resultados:
            from tabulate import tabulate
            headers = ["Codigo Vendedor", "Nombre Vendedor", "Total Facturas"]
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No hay datos disponibles en la vista de vendedores con menos ventas.")
    except Exception as e:
        print(f"Error al consultar los vendedores con menos ventas: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_productos_mas_vendidos_por_vendedor():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarProductosMasVendidosPorVendedor;"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if resultados:
            from tabulate import tabulate
            headers = ["Codigo Vendedor", "Nombre Vendedor", "Producto Más Vendido", "Unidades Vendidas"]
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No hay datos disponibles en la vista de productos más vendidos por cada vendedor.")
    except Exception as e:
        print(f"Error al consultar los productos más vendidos por cada vendedor: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_clientes_atendidos_por_vendedor():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarClientesAtendidosPorVendedor;"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if resultados:
            from tabulate import tabulate
            headers = ["Codigo Vendedor", "Nombre Vendedor", "Clientes Únicos"]
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No hay datos disponibles en la vista de clientes atendidos por cada vendedor.")
    except Exception as e:
        print(f"Error al consultar los clientes atendidos por cada vendedor: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_asesores_con_mas_clientes():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarAsesoresConMasClientes;"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if resultados:
            headers = ["CodigoAsesor", "NombreAsesor", "ClientesUnicos"]
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No se encontraron datos.")
    except Exception as e:
        print(f"Error al consultar los asesores con más clientes: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_ingresos_generados_por_asesores():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarIngresosGeneradosPorAsesores;"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if resultados:
            headers = ["CodigoAsesor", "NombreAsesor", "TotalFacturas", "IngresosTotales"]
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No se encontraron datos.")
    except Exception as e:
        print(f"Error al consultar los ingresos generados por asesores: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_productos_mas_recomendados_por_asesores():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarProductosMasRecomendadosPorAsesores;"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if resultados:
            headers = ["CodigoAsesor", "NombreAsesor", "Producto", "TotalRecomendaciones"]
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No se encontraron datos.")
    except Exception as e:
        print(f"Error al consultar los productos más recomendados por asesores: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def mostrar_impacto_experiencia_asesores():
    try:
        conexion = conectar_base_datos()
        if not conexion:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conexion.cursor()
        query = "SELECT * FROM MostrarImpactoDeExperienciaEnAsesores;"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if resultados:
            headers = ["RangoExperiencia", "CantidadAsesores", "PromedioIngresos", "PromedioClientesAtendidos"]
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2f"))
        else:
            print("No se encontraron datos.")
    except Exception as e:
        print(f"Error al consultar el impacto de la experiencia de asesores: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def verificar_vendedor(cod_vendedor):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute("SELECT VerificarVendedor(%s)", (cod_vendedor,))
            resultado = cursor.fetchone()
            return resultado[0] == 1
    except Error as e:
        print("Error al conectar a la base de datos:", e)
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def verificar_asesor(cod_asesor):
    try:
        conexion = conectar_base_datos()
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute("SELECT VerificarAsesor(%s)", (cod_asesor,))
            resultado = cursor.fetchone()
            return resultado[0] == 1
    except Error as e:
        print("Error al conectar a la base de datos:", e)
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
