USE FabiaNatura;

DELIMITER $
CREATE TRIGGER ActualizarTipoClienteFrecuente
AFTER INSERT ON Facturas
FOR EACH ROW
BEGIN
    DECLARE total_facturas INT;
    SELECT COUNT(*) INTO total_facturas
    FROM Facturas
    WHERE dni = NEW.dni;
    IF total_facturas >= 30 THEN
        UPDATE Clientes
        SET tipo_cliente = 'frecuente'
        WHERE dni = NEW.dni;
    END IF;
END $$
DELIMITER ;

-- SHOW TRIGGERS;
