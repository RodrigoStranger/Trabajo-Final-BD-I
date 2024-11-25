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

-- mostrar los vendedores con más ventas
CREATE VIEW MostrarTopVendedores AS
SELECT 
    v.cod_vendedor AS Codigo,
    CONCAT(p.nombre, ' ', p.apellido_paterno, ' ', p.apellido_materno) AS Vendedor,
    COUNT(f.cod_factura) AS TotalVentas,
    FORMAT(SUM(df.cantidad * pr.precio_venta), 2) AS TotalIngresosGenerados
FROM 
    Vendedores v
INNER JOIN 
    Empleados e ON v.cod_empleado = e.cod_empleado
INNER JOIN 
    Personas p ON e.dni = p.dni
INNER JOIN 
    Facturas f ON v.cod_vendedor = f.cod_vendedor
INNER JOIN 
    Detalle_Facturas df ON f.cod_factura = df.cod_factura
INNER JOIN 
    Productos pr ON df.cod_producto = pr.cod_producto
GROUP BY 
    v.cod_vendedor, p.nombre, p.apellido_paterno, p.apellido_materno
ORDER BY 
    SUM(df.cantidad * pr.precio_venta) DESC;

-- MostrarVendedoresConMenosVentas
CREATE VIEW MostrarVendedoresConMenosVentas AS
SELECT 
    v.cod_vendedor AS CodigoVendedor,
    CONCAT(p.nombre, ' ', p.apellido_paterno, ' ', p.apellido_materno) AS NombreVendedor,
    COUNT(f.cod_factura) AS TotalFacturas
FROM 
    Vendedores v
INNER JOIN 
    Empleados e ON v.cod_empleado = e.cod_empleado
INNER JOIN 
    Personas p ON e.dni = p.dni
LEFT JOIN 
    Facturas f ON v.cod_vendedor = f.cod_vendedor
GROUP BY 
    v.cod_vendedor, NombreVendedor
ORDER BY 
    TotalFacturas ASC;

CREATE VIEW MostrarProductosMasVendidosPorVendedor AS
SELECT 
    v.cod_vendedor AS CodigoVendedor,
    CONCAT(p.nombre, ' ', p.apellido_paterno, ' ', p.apellido_materno) AS NombreVendedor,
    pr.nombre AS ProductoMasVendido,
    SUM(df.cantidad) AS UnidadesVendidas
FROM 
    Vendedores v
INNER JOIN 
    Empleados e ON v.cod_empleado = e.cod_empleado
INNER JOIN 
    Personas p ON e.dni = p.dni
INNER JOIN 
    Facturas f ON v.cod_vendedor = f.cod_vendedor
INNER JOIN 
    Detalle_Facturas df ON f.cod_factura = df.cod_factura
INNER JOIN 
    Productos pr ON df.cod_producto = pr.cod_producto
GROUP BY 
    v.cod_vendedor, NombreVendedor, pr.nombre
ORDER BY 
    v.cod_vendedor, UnidadesVendidas DESC;

CREATE VIEW MostrarClientesAtendidosPorVendedor AS
SELECT 
    v.cod_vendedor AS CodigoVendedor,
    CONCAT(p.nombre, ' ', p.apellido_paterno, ' ', p.apellido_materno) AS NombreVendedor,
    COUNT(DISTINCT f.dni) AS ClientesUnicos
FROM 
    Vendedores v
INNER JOIN 
    Empleados e ON v.cod_empleado = e.cod_empleado
INNER JOIN 
    Personas p ON e.dni = p.dni
INNER JOIN 
    Facturas f ON v.cod_vendedor = f.cod_vendedor
GROUP BY 
    v.cod_vendedor, NombreVendedor
ORDER BY 
    ClientesUnicos DESC;
