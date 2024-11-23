USE FabiaNatura;

-- verificar si un telefono existe
DELIMITER $$
CREATE FUNCTION VerificarTelefonoExisteProveedores(p_telefono VARCHAR(9))
RETURNS TINYINT
DETERMINISTIC
BEGIN
    DECLARE existe INT;
    SELECT COUNT(*) INTO existe
		FROM Telefonos_Proveedores
		WHERE telefono = p_telefono;
    RETURN IF(existe > 0, 1, 0);
END$$
DELIMITER ;