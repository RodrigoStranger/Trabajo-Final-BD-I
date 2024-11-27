USE FabiaNatura

-- Verificar si una persona existe
DELIMITER $$
CREATE FUNCTION VerificarPersonaExiste(p_dni VARCHAR(8))
RETURNS BOOLEAN
DETERMINISTIC
BEGIN
    DECLARE existe INT;
    SELECT COUNT(*) INTO existe
		FROM Personas
		WHERE dni = p_dni;
    RETURN existe > 0;
END$$
DELIMITER ;

-- verificar si un telefono existe
DELIMITER $$
CREATE FUNCTION VerificarTelefonoExiste(p_telefono VARCHAR(9))
RETURNS TINYINT
DETERMINISTIC
BEGIN
    DECLARE existe INT;
    SELECT COUNT(*) INTO existe
		FROM Telefonos_Personas
		WHERE telefono = p_telefono;
    RETURN IF(existe > 0, 1, 0);
END$$
DELIMITER ;

-- Obtener el codigo de un empleado sabiendo su dni
DELIMITER $$
CREATE FUNCTION ObtenerCodEmpleado(p_dni VARCHAR(8))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE cod_empleado INT;
    SELECT e.cod_empleado 
    INTO cod_empleado
    FROM Personas p
		JOIN Empleados e ON p.dni = e.dni
		WHERE p.dni = p_dni
    LIMIT 1;
    RETURN cod_empleado;
END$$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION VerificarVendedor(
    p_cod_vendedor INT
)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE vendedor_existente INT;
    SELECT COUNT(*) INTO vendedor_existente
    FROM Vendedores
    WHERE cod_vendedor = p_cod_vendedor;
    IF vendedor_existente > 0 THEN
        RETURN 1;
    ELSE
        RETURN 0;
    END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION VerificarAsesor(
    p_cod_asesor INT
)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE resultado INT;
    IF EXISTS (SELECT 1 FROM Asesores WHERE cod_asesor = p_cod_asesor) THEN
        SET resultado = 1;
    ELSE
        SET resultado = 0;
    END IF;
    RETURN resultado;
END$$
DELIMITER ;
