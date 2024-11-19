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
