USE FabiaNatura;
-- Total de procedimientos : 3

-- CREACIÓN: 
-- Creación de un proveedor
DELIMITER $$
CREATE PROCEDURE AgregarProveedor(
    IN p_ruc VARCHAR(11),
    IN p_nombre VARCHAR(50),
    IN p_telefono VARCHAR(15)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error al crear el proveedor.';
    END;
    START TRANSACTION;
    IF EXISTS (SELECT 1 FROM Proveedores WHERE ruc = p_ruc) THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ya existe un proveedor con el mismo ruc.';
    END IF;
    IF EXISTS (SELECT 1 FROM Proveedores WHERE nombre = p_nombre) THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ya existe un proveedor con el mismo nombre.';
    END IF;
    INSERT INTO Proveedores (ruc, nombre, fecha_registro)
    VALUES (p_ruc, p_nombre, CURRENT_TIMESTAMP);
    INSERT INTO Telefonos_Proveedores (ruc, telefono)
    VALUES (p_ruc, p_telefono);
    COMMIT;
END$$
DELIMITER ;

-- EDICIÓN:
-- Modificar el telefono de un proveedor
DELIMITER $$
CREATE PROCEDURE EditarTelefonoProveedor(
    IN p_ruc VARCHAR(11),
    IN p_nuevo_telefono VARCHAR(15)
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Proveedores WHERE ruc = p_ruc) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El proveedor con el ruc proporcionado no existe.';
    END IF;
    UPDATE Telefonos_Proveedores SET telefono = p_nuevo_telefono WHERE ruc = p_ruc;
END$$
DELIMITER ;

-- ELIMINAR:
-- Eliminar un proveedor
DELIMITER $$
CREATE PROCEDURE EliminarProveedor(
    IN p_ruc VARCHAR(11)
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Proveedores WHERE ruc = p_ruc) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El proveedor con el ruc proporcionado no existe.';
    END IF;
    DELETE FROM Proveedores WHERE ruc = p_ruc;
END$$
DELIMITER ;

-- MOSTRAR