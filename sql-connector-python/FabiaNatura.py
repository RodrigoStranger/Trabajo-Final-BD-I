from FabiaNatura_users import gestionar_insercion_asesor
from FabiaNatura_users import gestionar_insercion_vendedor
from FabiaNatura_users import gestionar_insercion_cliente
from FabiaNatura_contracts import gestionar_insercion_contrato
from FabiaNatura_contracts import gestionar_eliminacion_contrato



gestionar_insercion_contrato(
    dni='73714089',  # DNI del empleado
    fecha_inicio='2024-01-01',
    fecha_fin='2024-12-31',
    salario_men=3000.00,
    observaciones='Contrato a tiempo completo.'
)


#gestionar_eliminacion_contrato(dni="73714089")