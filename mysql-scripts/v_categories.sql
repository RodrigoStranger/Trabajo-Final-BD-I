USE FabiaNatura;

-- mostrar todas las categorias
CREATE VIEW MostrarCategorias AS
SELECT 
    cod_categoria AS Codigo, 
    nombre AS Nombre
FROM Categorias
ORDER BY cod_categoria ASC;

-- SELECT * FROM VistaCategorias;