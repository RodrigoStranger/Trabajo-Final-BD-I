USE FabiaNatura;
-- Total de procedimientos : 10

-- CREACIÓN:
-- Insertar un Cliente
-- Insertar un Asesor
-- Insertar un Vendedor 
DELIMITER $$
CREATE PROCEDURE AgregarCliente(
    IN p_dni VARCHAR(8),
    IN p_nombre VARCHAR(20),
    IN p_apellido_paterno VARCHAR(20),
    IN p_apellido_materno VARCHAR(20),
    IN p_fecha_nacimiento DATE,
    IN p_telefono VARCHAR(9),
    IN p_direccion VARCHAR(100)
)
BEGIN
    START TRANSACTION;
    INSERT INTO Personas (dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento) VALUES (p_dni, p_nombre, p_apellido_paterno, p_apellido_materno, p_fecha_nacimiento);
    INSERT INTO Telefonos_Personas (telefono, dni) VALUES (p_telefono, p_dni);
    INSERT INTO Direcciones_Personas (dni, direccion) VALUES (p_dni, p_direccion);
    INSERT INTO Clientes (dni, tipo_cliente) VALUES (p_dni, 'regular');
    COMMIT;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE AgregarVendedor(
    IN p_dni VARCHAR(8),
    IN p_nombre VARCHAR(20),
    IN p_apellido_paterno VARCHAR(20),
    IN p_apellido_materno VARCHAR(20),
    IN p_fecha_nacimiento DATE,
    IN p_telefono VARCHAR(9),
    IN p_direccion VARCHAR(100),
    IN p_rol VARCHAR(20)
)
BEGIN
    DECLARE empleado_id INT;
    START TRANSACTION;
    INSERT INTO Personas (dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento) VALUES (p_dni, p_nombre, p_apellido_paterno, p_apellido_materno, p_fecha_nacimiento);
    INSERT INTO Telefonos_Personas (telefono, dni) VALUES (p_telefono, p_dni);
    INSERT INTO Direcciones_Personas (dni, direccion) VALUES (p_dni, p_direccion);
    INSERT INTO Empleados (dni, estado) VALUES (p_dni, 'activo');
    SET empleado_id = LAST_INSERT_ID();
    INSERT INTO Vendedores (cod_empleado, rol) VALUES (empleado_id, p_rol);
    COMMIT;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE AgregarAsesor(
    IN p_dni VARCHAR(8),
    IN p_nombre VARCHAR(20),
    IN p_apellido_paterno VARCHAR(20),
    IN p_apellido_materno VARCHAR(20),
    IN p_fecha_nacimiento DATE,
    IN p_telefono VARCHAR(9),
    IN p_direccion VARCHAR(100),
    IN p_experiencia INT,
    IN p_especialidad VARCHAR(20)
)
BEGIN
    DECLARE empleado_id INT;
    START TRANSACTION;
    INSERT INTO Personas (dni, nombre, apellido_paterno, apellido_materno, fecha_nacimiento) VALUES (p_dni, p_nombre, p_apellido_paterno, p_apellido_materno, p_fecha_nacimiento);
    INSERT INTO Telefonos_Personas (telefono, dni) VALUES (p_telefono, p_dni);
    INSERT INTO Direcciones_Personas (dni, direccion) VALUES (p_dni, p_direccion);
    INSERT INTO Empleados (dni, estado) VALUES (p_dni, 'activo');
    SET empleado_id = LAST_INSERT_ID();
    INSERT INTO Asesores (cod_empleado, experiencia, especialidad) VALUES (empleado_id, p_experiencia, p_especialidad);
    COMMIT;
END$$
DELIMITER ;

-- EDICIÓN:
-- Editar el telefono de un Cliente, Asesor, Vendedor
-- Editar la direccion de un Cliente, Asesor, Vendedor
-- Editar la especialidad de un Asesor
-- Editar la experiencia de un Asesor
-- Editar el rol de un Vendedor
DELIMITER $$
CREATE PROCEDURE EditarTelefono(
    IN p_dni VARCHAR(8),
    IN p_telefono_nuevo VARCHAR(9)
)
BEGIN
    UPDATE Telefonos_Personas SET telefono = p_telefono_nuevo WHERE dni = p_dni;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarDireccion(
    IN p_dni VARCHAR(8),
    IN p_direccion_nueva VARCHAR(100)
)
BEGIN
    UPDATE Direcciones_Personas SET direccion = p_direccion_nueva WHERE dni = p_dni;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarEspecialidadAsesor(
    IN p_dni VARCHAR(8),
    IN p_especialidad_nueva VARCHAR(20)
)
BEGIN
    DECLARE asesor_id INT; 
    SELECT cod_asesor INTO asesor_id FROM Asesores JOIN Empleados ON Asesores.cod_empleado = Empleados.cod_empleado WHERE Empleados.dni = p_dni;
    UPDATE Asesores SET especialidad = p_especialidad_nueva WHERE cod_asesor = asesor_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarExperienciaAsesor(
    IN p_dni VARCHAR(8),
    IN p_experiencia_nueva INT
)
BEGIN
    DECLARE asesor_id INT;
    SELECT cod_asesor INTO asesor_id FROM Asesores JOIN Empleados ON Asesores.cod_empleado = Empleados.cod_empleado WHERE Empleados.dni = p_dni;
    UPDATE Asesores SET experiencia = p_experiencia_nueva WHERE cod_asesor = asesor_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarRolVendedor(
    IN p_dni VARCHAR(8),
    IN p_rol_nuevo VARCHAR(20)
)
BEGIN
    DECLARE vendedor_id INT;
    SELECT cod_vendedor INTO vendedor_id FROM Vendedores JOIN Empleados ON Vendedores.cod_empleado = Empleados.cod_empleado WHERE Empleados.dni = p_dni;
    UPDATE Vendedores SET rol = p_rol_nuevo WHERE cod_vendedor = vendedor_id;
END$$
DELIMITER ;

-- DESACTIVACIÓN O ACTIVACIÓN:
DELIMITER $$
CREATE PROCEDURE CambiarEstadoAsesor(
    IN p_dni VARCHAR(8),
    IN p_nuevo_estado ENUM('activo', 'inactivo')
)
BEGIN
    DECLARE empleado_id INT;
    DECLARE contrato_count INT;
    SELECT cod_empleado INTO empleado_id FROM Empleados WHERE dni = p_dni;
    IF empleado_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El asesor con el dni proporcionado no existe.';
    END IF;
    SELECT COUNT(*) INTO contrato_count FROM Contratos WHERE cod_empleado = empleado_id;
    IF contrato_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El asesor no tiene contratos asociados.';
    END IF;
    UPDATE Empleados SET estado = p_nuevo_estado WHERE cod_empleado = empleado_id;
    UPDATE Contratos SET estado = p_nuevo_estado WHERE cod_empleado = empleado_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE CambiarEstadoVendedor(
    IN p_dni VARCHAR(8),
    IN p_nuevo_estado ENUM('activo', 'inactivo')
)
BEGIN
    DECLARE empleado_id INT;
    DECLARE contrato_count INT;
    SELECT cod_empleado INTO empleado_id FROM Empleados WHERE dni = p_dni;
    IF empleado_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El vendedor con el dni proporcionado no existe.';
    END IF;
    SELECT COUNT(*) INTO contrato_count FROM Contratos WHERE cod_empleado = empleado_id;
    IF contrato_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El vendedor no tiene contratos asociados.';
    END IF;
    UPDATE Empleados SET estado = p_nuevo_estado WHERE cod_empleado = empleado_id;
    UPDATE Contratos SET estado = p_nuevo_estado WHERE cod_empleado = empleado_id;
END$$
DELIMITER ;