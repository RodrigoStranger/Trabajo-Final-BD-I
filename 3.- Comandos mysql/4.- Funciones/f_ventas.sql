USE FabiaNatura;

-- devolver la ultima factura creada
DELIMITER $$
CREATE FUNCTION ObtenerUltimaFactura()
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE ultimo_id INT;
    SELECT MAX(cod_factura) INTO ultimo_id FROM Facturas;
    RETURN ultimo_id;
END$$
DELIMITER ;