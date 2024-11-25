USE FabiaNatura;

-- mostrar todas las categorias
CREATE VIEW MostrarProveedores AS
SELECT 
    ruc AS RUC, 
    nombre AS Nombre
FROM Proveedores
ORDER BY nombre ASC;

-- SELECT * FROM VistaProveedores;

-- Proveedores con Mayor Contribución al Inventario
CREATE VIEW MostrarProveedoresMayorContribucion AS
SELECT 
    p.ruc AS RUC,
    p.nombre AS NombreProveedor,
    SUM(pr.stock) AS TotalStockContribuido
FROM 
    Proveedores p
LEFT JOIN 
    Productos pr ON p.ruc = pr.ruc
GROUP BY 
    p.ruc, p.nombre
ORDER BY 
    TotalStockContribuido DESC;

-- Proveedores con Mayor Valor de Productos
CREATE VIEW MostrarProveedoresMayorValor AS
SELECT 
    p.ruc AS RUC,
    p.nombre AS NombreProveedor,
    SUM(pr.stock * pr.precio_venta) AS ValorTotalProductos
FROM 
    Proveedores p
LEFT JOIN 
    Productos pr ON p.ruc = pr.ruc
GROUP BY 
    p.ruc, p.nombre
ORDER BY 
    ValorTotalProductos DESC;

-- Proveedores con Productos Más Vendidos
CREATE VIEW MostrarProveedoresProductosMasVendidos AS
SELECT 
    p.ruc AS RUC,
    p.nombre AS NombreProveedor,
    pr.nombre AS ProductoMasVendido,
    SUM(df.cantidad) AS UnidadesVendidas
FROM 
    Proveedores p
LEFT JOIN 
    Productos pr ON p.ruc = pr.ruc
LEFT JOIN 
    Detalle_Facturas df ON pr.cod_producto = df.cod_producto
GROUP BY 
    p.ruc, p.nombre, pr.cod_producto, pr.nombre
ORDER BY 
    UnidadesVendidas DESC;

-- Cantidad Promedio de Productos por Proveedor
CREATE VIEW MostrarPromedioProductosPorProveedor AS
SELECT 
    AVG(TotalProductos) AS PromedioProductosPorProveedor
FROM (
    SELECT 
        p.ruc,
        COUNT(pr.cod_producto) AS TotalProductos
    FROM 
        Proveedores p
    LEFT JOIN 
        Productos pr ON p.ruc = pr.ruc
    GROUP BY 
        p.ruc
) AS SubConsulta;