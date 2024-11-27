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

-- Insertar DetalleFactura
DELIMITER $$
CREATE PROCEDURE InsertarDetalleFactura(
    IN p_cod_factura INT,
    IN p_cod_producto INT,
    IN p_cantidad INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Facturas WHERE cod_factura = p_cod_factura) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La factura con el código proporcionado no existe.';
    END IF;
    IF NOT EXISTS (SELECT 1 FROM Productos WHERE cod_producto = p_cod_producto) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El producto con el código proporcionado no existe.';
    END IF;
    IF p_cantidad <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La cantidad debe ser un número mayor que 0.';
    END IF;
    INSERT INTO Detalle_Facturas (cod_factura, cod_producto, cantidad) VALUES (p_cod_factura, p_cod_producto, p_cantidad);
END$$
DELIMITER ;

-- CancelarFactura
DELIMITER $$
CREATE PROCEDURE CancelarFactura(
    IN p_cod_factura INT
)
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE cod_producto INT;
    DECLARE cantidad INT;
    DECLARE cur CURSOR FOR
        SELECT cod_producto, cantidad
        FROM Detalle_Facturas
        WHERE cod_factura = p_cod_factura;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    IF NOT EXISTS (SELECT 1 FROM Facturas WHERE cod_factura = p_cod_factura) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La factura con el código proporcionado no existe.';
    END IF;
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO cod_producto, cantidad;
        IF done THEN
            LEAVE read_loop;
        END IF;
        UPDATE Productos
        SET stock = stock + cantidad
        WHERE cod_producto = cod_producto;
        IF (SELECT stock FROM Productos WHERE cod_producto = cod_producto) > 0 THEN
            UPDATE Productos
            SET estado = 'disponible'
            WHERE cod_producto = cod_producto;
        END IF;
    END LOOP;
    CLOSE cur;
    DELETE FROM Detalle_Facturas WHERE cod_factura = p_cod_factura;
    DELETE FROM Facturas WHERE cod_factura = p_cod_factura;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE MostrarBoletaVenta(
    IN p_cod_factura INT
)
BEGIN
    SELECT 
        p.nombre AS Producto,
        df.cantidad AS Cantidad,
        ROUND(p.precio_venta, 2) AS PrecioUnitario,
        ROUND(p.precio_venta * df.cantidad, 2) AS TotalProducto
    FROM 
        Detalle_Facturas df
    JOIN 
        Productos p ON df.cod_producto = p.cod_producto
    WHERE 
        df.cod_factura = p_cod_factura;

END$$
DELIMITER ;