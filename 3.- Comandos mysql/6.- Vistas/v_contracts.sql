USE FabiaNatura;

-- Cantidad de Contratos Activos e Inactivos por Tipo de Empleado
CREATE VIEW MostrarContratosPorEstadoYTipo AS
SELECT 
    CASE 
        WHEN EXISTS (SELECT 1 FROM Vendedores v WHERE v.cod_empleado = c.cod_empleado) THEN 'Vendedor'
        WHEN EXISTS (SELECT 1 FROM Asesores a WHERE a.cod_empleado = c.cod_empleado) THEN 'Asesor'
        ELSE 'Otro'
    END AS TipoEmpleado,
    c.estado AS EstadoContrato,
    COUNT(*) AS TotalContratos
FROM Contratos c
GROUP BY TipoEmpleado, c.estado;

-- Promedio de Salarios por Tipo de Contrato
CREATE VIEW MostrarPromedioSalariosPorEstadoYTipo AS
SELECT 
    CASE 
        WHEN EXISTS (SELECT 1 FROM Vendedores v WHERE v.cod_empleado = c.cod_empleado) THEN 'Vendedor'
        WHEN EXISTS (SELECT 1 FROM Asesores a WHERE a.cod_empleado = c.cod_empleado) THEN 'Asesor'
        ELSE 'Otro'
    END AS TipoEmpleado,
    c.estado AS EstadoContrato,
    AVG(c.salario_men) AS SalarioPromedio
FROM Contratos c
GROUP BY TipoEmpleado, c.estado;

-- Duración Promedio de los Contratos por Empleado
CREATE VIEW MostrarDuracionPromedioContratosPorEmpleado AS
SELECT 
    e.cod_empleado AS CodigoEmpleado,
    CONCAT(p.nombre, ' ', p.apellido_paterno, ' ', p.apellido_materno) AS NombreEmpleado,
    AVG(DATEDIFF(IFNULL(c.fecha_fin, CURDATE()), c.fecha_inicio)) AS DuracionPromedioDias
FROM Contratos c
JOIN Empleados e ON c.cod_empleado = e.cod_empleado
JOIN Personas p ON e.dni = p.dni
GROUP BY e.cod_empleado, NombreEmpleado;