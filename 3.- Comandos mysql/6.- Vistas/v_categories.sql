USE FabiaNatura;

-- mostrar todas las categorias
CREATE VIEW MostrarCategorias AS
SELECT 
    cod_categoria AS Codigo, 
    nombre AS Nombre
FROM Categorias
ORDER BY cod_categoria ASC;

-- SELECT * FROM VistaCategorias;

-- Categorías con más productos
CREATE VIEW MostrarCategoriasConMasProductos AS
SELECT 
    c.cod_categoria AS CodigoCategoria,
    c.nombre AS NombreCategoria,
    COUNT(p.cod_producto) AS TotalProductos
FROM 
    Categorias c
LEFT JOIN 
    Productos p ON c.cod_categoria = p.cod_categoria
GROUP BY 
    c.cod_categoria, c.nombre
ORDER BY 
    TotalProductos DESC;

-- Categorías con productos más vendidos
CREATE VIEW MostrarCategoriasConProductosMasVendidos AS
SELECT 
    c.cod_categoria AS CodigoCategoria,
    c.nombre AS NombreCategoria,
    SUM(df.cantidad) AS TotalUnidadesVendidas
FROM 
    Categorias c
JOIN 
    Productos p ON c.cod_categoria = p.cod_categoria
JOIN 
    Detalle_Facturas df ON p.cod_producto = df.cod_producto
GROUP BY 
    c.cod_categoria, c.nombre
ORDER BY 
    TotalUnidadesVendidas DESC;

-- Categorías con productos agotados
CREATE VIEW MostrarCategoriasConProductosAgotados AS
SELECT 
    c.cod_categoria AS CodigoCategoria,
    c.nombre AS NombreCategoria,
    COUNT(p.cod_producto) AS ProductosAgotados
FROM 
    Categorias c
JOIN 
    Productos p ON c.cod_categoria = p.cod_categoria
WHERE 
    p.estado = 'agotado'
GROUP BY 
    c.cod_categoria, c.nombre
ORDER BY 
    ProductosAgotados DESC;

-- Categorías con mayor cantidad de productos disponibles
CREATE VIEW MostrarCategoriasConProductosDisponibles AS
SELECT 
    c.cod_categoria AS CodigoCategoria,
    c.nombre AS NombreCategoria,
    COUNT(p.cod_producto) AS ProductosDisponibles
FROM 
    Categorias c
JOIN 
    Productos p ON c.cod_categoria = p.cod_categoria
WHERE 
    p.estado = 'disponible'
GROUP BY 
    c.cod_categoria, c.nombre
ORDER BY 
    ProductosDisponibles DESC;

--  Categorías con más ventas por cliente
CREATE VIEW MostrarCategoriasConMasVentasPorCliente AS
SELECT 
    c.cod_categoria AS CodigoCategoria,
    c.nombre AS NombreCategoria,
    COUNT(DISTINCT f.dni) AS ClientesUnicos
FROM 
    Categorias c
JOIN 
    Productos p ON c.cod_categoria = p.cod_categoria
JOIN 
    Detalle_Facturas df ON p.cod_producto = df.cod_producto
JOIN 
    Facturas f ON df.cod_factura = f.cod_factura
GROUP BY 
    c.cod_categoria, c.nombre
ORDER BY 
    ClientesUnicos DESC;