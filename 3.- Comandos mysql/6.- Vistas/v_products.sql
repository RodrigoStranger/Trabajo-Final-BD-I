USE FabiaNatura;

-- Vista para poder mostrar los productos disponibles
CREATE VIEW MostrarProductosDisponibles AS
SELECT 
    cod_producto AS Codigo,
    nombre AS Nombre,
    linea AS Linea,
    precio_venta AS Precio,
    stock AS Disponible
FROM Productos
WHERE estado = 'disponible'
ORDER BY stock DESC;

-- SELECT * FROM MostrarProductosDisponibles;

-- Vista para poder mostrar los productos agotados
CREATE VIEW MostrarProductosAgotados AS
SELECT 
    cod_producto AS Codigo,
    nombre AS Nombre,
    linea AS Linea,
    precio_venta AS Precio,
    stock AS Disponible
FROM Productos
WHERE estado = 'agotado'
ORDER BY cod_producto DESC;

-- SELECT * FROM MostrarProductosAgotados;

-- Vista para poder mostrar que productos han sido vendidos, con su cantidad vendida y monto recaudado
CREATE VIEW MostrarProductosVendidos AS
SELECT 
    p.cod_producto AS CodigoProducto,
    p.nombre AS NombreProducto,
    c.nombre AS Categoria,
    p.linea AS Linea,
    SUM(df.cantidad) AS CantidadVendida,
    ROUND(SUM(df.cantidad * p.precio_venta), 2) AS TotalVenta
FROM 
    Detalle_Facturas df
JOIN 
    Productos p ON df.cod_producto = p.cod_producto
LEFT JOIN 
    Categorias c ON p.cod_categoria = c.cod_categoria
GROUP BY 
    p.cod_producto, p.nombre, c.nombre, p.linea
ORDER BY 
    TotalVenta DESC;

-- SELECT * FROM MostrarProductosVendidos;

-- Productos más vendidos
CREATE VIEW MostrarProductosMasVendidos AS
SELECT 
    p.cod_producto AS CodigoProducto,
    p.nombre AS NombreProducto,
    SUM(df.cantidad) AS TotalVendidos,
    FORMAT(SUM(df.cantidad * p.precio_venta), 2) AS TotalIngresos
FROM 
    Productos p
INNER JOIN 
    Detalle_Facturas df ON p.cod_producto = df.cod_producto
GROUP BY 
    p.cod_producto, p.nombre
ORDER BY 
    TotalVendidos DESC;

-- Productos menos vendidos
CREATE VIEW MostrarProductosMenosVendidos AS
SELECT 
    p.cod_producto AS CodigoProducto,
    p.nombre AS NombreProducto,
    IFNULL(SUM(df.cantidad), 0) AS TotalVendidos,
    FORMAT(IFNULL(SUM(df.cantidad * p.precio_venta), 0), 2) AS TotalIngresos
FROM 
    Productos p
LEFT JOIN 
    Detalle_Facturas df ON p.cod_producto = df.cod_producto
GROUP BY 
    p.cod_producto, p.nombre
ORDER BY 
    TotalVendidos ASC;

-- Productos agotados
CREATE VIEW MostrarProductosAgotados AS
SELECT 
    p.cod_producto AS CodigoProducto,
    p.nombre AS NombreProducto,
    p.stock AS Stock,
    p.estado AS Estado
FROM 
    Productos p
WHERE 
    p.estado = 'agotado'
ORDER BY 
    p.cod_producto;

-- Ingresos generados por productos
CREATE VIEW MostrarIngresosPorProducto AS
SELECT 
    p.cod_producto AS CodigoProducto,
    p.nombre AS NombreProducto,
    FORMAT(SUM(df.cantidad * p.precio_venta), 2) AS TotalIngresos,
    SUM(df.cantidad) AS TotalVendidos
FROM 
    Productos p
INNER JOIN 
    Detalle_Facturas df ON p.cod_producto = df.cod_producto
GROUP BY 
    p.cod_producto, p.nombre
ORDER BY 
    TotalIngresos DESC;

-- Productos con mayor margen de ganancia
CREATE VIEW MostrarProductosMayorMargenGanancia AS
SELECT 
    p.cod_producto AS CodigoProducto,
    p.nombre AS NombreProducto,
    FORMAT(p.precio_venta - p.precio_compra, 2) AS MargenGanancia,
    FORMAT((p.precio_venta - p.precio_compra) / p.precio_compra * 100, 2) AS PorcentajeGanancia,
    p.precio_compra AS PrecioCompra,
    p.precio_venta AS PrecioVenta,
    p.stock AS Stock
FROM 
    Productos p
WHERE 
    p.precio_venta > p.precio_compra
ORDER BY 
    MargenGanancia DESC;