USE FabiaNatura;

-- mostrar empleados
CREATE VIEW MostrarEmpleados AS
SELECT 
    p.dni AS DNI,
    e.cod_empleado AS CodigoEmpleado,
    p.nombre AS Nombre,
    p.apellido_paterno AS ApellidoPaterno,
    p.apellido_materno AS ApellidoMaterno,
    CASE 
        WHEN c.cod_contrato IS NOT NULL THEN 'Sí'
        ELSE 'No'
    END AS TieneContrato
FROM 
    Personas p
JOIN 
    Empleados e ON p.dni = e.dni
LEFT JOIN 
    Contratos c ON e.cod_empleado = c.cod_empleado
ORDER BY 
    e.cod_empleado ASC;


-- SELECT * FROM MostrarEmpleados;

-- mostrar vendedores
CREATE VIEW MostrarVendedores AS
SELECT 
    p.dni AS DNI,
    v.cod_vendedor AS CodigoVendedor,
    p.nombre AS Nombre,
    p.apellido_paterno AS ApellidoPaterno,
    p.apellido_materno AS ApellidoMaterno,
    v.rol AS Rol,
    CASE 
        WHEN c.cod_contrato IS NOT NULL THEN 'Sí'
        ELSE 'No'
    END AS TieneContrato
FROM 
    Personas p
JOIN 
    Empleados e ON p.dni = e.dni
JOIN 
    Vendedores v ON e.cod_empleado = v.cod_empleado
LEFT JOIN 
    Contratos c ON e.cod_empleado = c.cod_empleado
ORDER BY 
    v.cod_vendedor ASC;

    
-- SELECT * FROM MostrarVendedores;

-- mostrar asesores
CREATE VIEW MostrarAsesores AS
SELECT 
    p.dni AS DNI,
    a.cod_asesor AS CodigoAsesor,
    p.nombre AS Nombre,
    p.apellido_paterno AS ApellidoPaterno,
    p.apellido_materno AS ApellidoMaterno,
    a.especialidad AS Especialidad,
    a.experiencia AS Experiencia,
    CASE 
        WHEN c.cod_contrato IS NOT NULL THEN 'Sí'
        ELSE 'No'
    END AS TieneContrato
FROM 
    Personas p
JOIN 
    Empleados e ON p.dni = e.dni
JOIN 
    Asesores a ON e.cod_empleado = a.cod_empleado
LEFT JOIN 
    Contratos c ON e.cod_empleado = c.cod_empleado
ORDER BY 
    a.cod_asesor ASC;

-- SELECT * FROM MostrarAsesores;