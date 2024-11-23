USE FabiaNatura;

-- funcion que calcula los subtotales de una factura
DELIMITER $$
CREATE FUNCTION CalcularSubtotal(cod_factura INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE subtotal FLOAT;
    SELECT SUM(p.precio_venta * df.cantidad) INTO subtotal
		FROM Detalle_Facturas df
		JOIN Productos p ON df.cod_producto = p.cod_producto
		WHERE df.cod_factura = cod_factura;
    RETURN IFNULL(subtotal, 0);
END$$
DELIMITER ;