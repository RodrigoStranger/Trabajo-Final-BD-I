USE FabiaNatura;
-- Total de procedimientos : 

-- CREACIÓN: 
-- Creación de una Categoria
DELIMITER $$
CREATE PROCEDURE AgregarCategoria(
    IN p_nombre VARCHAR(50),
    IN p_descripcion TEXT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error al crear la categoría';
    END;
    START TRANSACTION;
    IF EXISTS (SELECT 1 FROM Categorias WHERE nombre = p_nombre) THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ya existe una categoría con el mismo nombre.';
    END IF;
    INSERT INTO Categorias (nombre, descripcion, fecha_registro) VALUES (p_nombre, p_descripcion, CURRENT_TIMESTAMP);
    COMMIT;
END$$
DELIMITER ;

-- EDICIÓN:
-- Modificar el nombre de una Categoria
-- Modificar la descripcion de una Categoria
DELIMITER $$
CREATE PROCEDURE EditarNombreCategoria(
    IN p_cod_categoria INT,
    IN p_nuevo_nombre VARCHAR(50)
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Categorias WHERE cod_categoria = p_cod_categoria) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La categoría con el código proporcionado no existe.';
    END IF;
    IF EXISTS (SELECT 1 FROM Categorias WHERE nombre = p_nuevo_nombre AND cod_categoria <> p_cod_categoria) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ya existe otra categoría con el mismo nombre.';
    END IF;
    UPDATE Categorias SET nombre = p_nuevo_nombre WHERE cod_categoria = p_cod_categoria;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarDescripcionCategoria(
    IN p_cod_categoria INT,
    IN p_nueva_descripcion TEXT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Categorias WHERE cod_categoria = p_cod_categoria) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La categoría con el código proporcionado no existe.';
    END IF;
    UPDATE Categorias SET descripcion = p_nueva_descripcion WHERE cod_categoria = p_cod_categoria;
END$$
DELIMITER ;

-- ELIMINAR:
-- Eliminar una Categoria
DELIMITER $$
CREATE PROCEDURE EliminarCategoria(
    IN p_cod_categoria INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Categorias WHERE cod_categoria = p_cod_categoria) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La categoría con el código proporcionado no existe.';
    END IF;
    DELETE FROM Categorias WHERE cod_categoria = p_cod_categoria;
END$$
DELIMITER ;

-- MOSTRAR: