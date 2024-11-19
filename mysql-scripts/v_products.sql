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
CREATE VIEW ProductosVendidos AS
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

-- SELECT * FROM ProductosVendidos;