USE FabiaNatura;

-- mostrar todas las categorias
CREATE VIEW MostrarProveedores AS
SELECT 
    ruc AS RUC, 
    nombre AS Nombre
FROM Proveedores
ORDER BY nombre ASC;

-- SELECT * FROM VistaProveedores;