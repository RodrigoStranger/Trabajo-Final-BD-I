from FabiaNatura_users import gestionar_insercion_asesor
from FabiaNatura_users import gestionar_insercion_vendedor
from FabiaNatura_users import gestionar_insercion_cliente
from FabiaNatura_contracts import gestionar_insercion_contrato
from FabiaNatura_contracts import obtener_detalles_contrato_por_dni
from FabiaNatura_contracts import obtener_contratos_y_empleados
from FabiaNatura_functions import cargar_tablas

gestionar_insercion_vendedor(
    dni='73714089',
    nombre='Rodrigo',
    apellido_paterno='Infanzon',
    apellido_materno='Acosta',
    fecha_nacimiento='2004-04-16',
    rol='Gerente de Ventas'
)
gestionar_insercion_contrato(
    dni='73714089',  # DNI del empleado
    fecha_inicio='2024-01-01',
    fecha_fin='2024-12-31',
    salario_men=3000.00,
    observaciones='Contrato a tiempo completo.'
)

#obtener_detalles_contrato_por_dni('73714089')
#obtener_contratos_y_empleados()

#cargar_tablas()