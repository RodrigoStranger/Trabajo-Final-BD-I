USE FabiaNatura;

-- Agregar una factura
DELIMITER $$
CREATE PROCEDURE AgregarFactura(
    IN p_dni VARCHAR(8),
    IN p_cod_vendedor INT,
    IN p_cod_asesor INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Clientes WHERE dni = p_dni) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El cliente con el DNI proporcionado no existe.';
    END IF;
    IF NOT EXISTS (SELECT 1 FROM Vendedores WHERE cod_vendedor = p_cod_vendedor) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El vendedor con el código proporcionado no existe.';
    END IF;
    IF p_cod_asesor IS NOT NULL AND NOT EXISTS (SELECT 1 FROM Asesores WHERE cod_asesor = p_cod_asesor) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El asesor con el código proporcionado no existe.';
    END IF;
    INSERT INTO Facturas (dni, cod_vendedor, cod_asesor) VALUES (p_dni, p_cod_vendedor, p_cod_asesor);
END$$
DELIMITER ;
   
-- Eliminar una factura:
DELIMITER $$
CREATE PROCEDURE EliminarFactura(
    IN p_cod_factura INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Facturas WHERE cod_factura = p_cod_factura) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La factura con el código proporcionado no existe.';
    END IF;
    DELETE FROM Facturas WHERE cod_factura = p_cod_factura;
END$$
DELIMITER ;

