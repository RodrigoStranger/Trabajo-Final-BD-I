USE FabiaNatura;
-- Total de procedimientos : 

-- CREACIÓN: 
-- Creación de un proveedor
DELIMITER $$
CREATE PROCEDURE CrearProveedor(
    IN p_ruc VARCHAR(15),
    IN p_nombre VARCHAR(50),
    IN p_telefono VARCHAR(15)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error al crear el proveedor. Operación revertida.';
    END;
    START TRANSACTION;
    IF EXISTS (SELECT 1 FROM Proveedores WHERE ruc = p_ruc) THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ya existe un proveedor con el mismo RUC.';
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





CALL CrearProveedor(
    '22512345542', 
    'unique', 
    '926172222'
);
select * from Telefonos_Proveedor;
