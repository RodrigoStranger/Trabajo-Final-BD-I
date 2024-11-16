USE FabiaNatura;

-- CREACIÓN:
-- Creación de un Contrato: se debe de asignar al empleado con dni
DELIMITER $$
CREATE PROCEDURE AgregarContrato(
    IN p_dni VARCHAR(8),
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_salario_mensual FLOAT,
    IN p_observaciones TEXT
)
BEGIN
    DECLARE empleado_id INT;
    SELECT cod_empleado INTO empleado_id FROM Empleados WHERE dni = p_dni;
    IF empleado_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El empleado con el dni proporcionado no existe.';
    END IF;
    INSERT INTO Contratos (cod_empleado, fecha_inicio, fecha_fin, salario_men, observaciones, estado) VALUES (empleado_id, p_fecha_inicio, p_fecha_fin, p_salario_mensual, p_observaciones, 'activo');
END$$
DELIMITER ;

-- EDICIÓN:
-- Edición de un contrato de sueldo
-- Edicion de un contrato de fecha_inicio, fecha_fin
-- Edicion de un contrato de la observación
DELIMITER $$
CREATE PROCEDURE EditarContratoSueldo(
    IN p_dni VARCHAR(8),
    IN p_nuevo_sueldo FLOAT
)
BEGIN
    DECLARE empleado_id INT;
    SELECT cod_empleado INTO empleado_id FROM Empleados WHERE dni = p_dni;
    IF empleado_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El empleado con el dni proporcionado no existe.';
    END IF;
    UPDATE Contratos SET salario_men = p_nuevo_sueldo WHERE cod_empleado = empleado_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarContratoFechas(
    IN p_dni VARCHAR(8),
    IN p_nueva_fecha_inicio DATE,
    IN p_nueva_fecha_fin DATE
)
BEGIN
    DECLARE empleado_id INT;
    SELECT cod_empleado INTO empleado_id FROM Empleados WHERE dni = p_dni;
    IF empleado_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El empleado con el DNI proporcionado no existe.';
    END IF;
    UPDATE Contratos SET fecha_inicio = p_nueva_fecha_inicio, fecha_fin = p_nueva_fecha_fin WHERE cod_empleado = empleado_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarContratoObservacion(
    IN p_dni VARCHAR(8),
    IN p_nueva_observacion TEXT
)
BEGIN
    DECLARE empleado_id INT;
    SELECT cod_empleado INTO empleado_id FROM Empleados WHERE dni = p_dni;
    IF empleado_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El empleado con el DNI proporcionado no existe.';
    END IF;
    UPDATE Contratos SET observaciones = p_nueva_observacion WHERE cod_empleado = empleado_id;
END$$
DELIMITER ;

-- DESACTIVACIÓN O ACTIVACIÓN:
DELIMITER $$
CREATE PROCEDURE CambiarEstadoContrato(
    IN p_dni VARCHAR(8),
    IN p_nuevo_estado ENUM('activo', 'inactivo')
)
BEGIN
    DECLARE empleado_id INT;
    SELECT cod_empleado INTO empleado_id FROM Empleados WHERE dni = p_dni
    LIMIT 1;
    IF empleado_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El empleado con el dni proporcionado no existe.';
    END IF;
    IF p_nuevo_estado NOT IN ('activo', 'inactivo') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Estado inválido. Solo se permiten "activo" o "inactivo".';
    END IF;
    UPDATE Contratos SET estado = p_nuevo_estado WHERE cod_empleado = empleado_id;
    UPDATE Empleados SET estado = p_nuevo_estado WHERE cod_empleado = empleado_id;
END$$
DELIMITER ;

-- MOSTRAR