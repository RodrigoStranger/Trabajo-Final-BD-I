Use FabiaNatura;

-- CREACIÓN
-- Creación de un producto
DELIMITER $$
CREATE PROCEDURE AgregarProducto(
    IN p_cod_categoria INT,
    IN p_ruc VARCHAR(15),
    IN p_nombre VARCHAR(100),
    IN p_linea VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio_compra FLOAT,
    IN p_precio_venta FLOAT,
    IN p_stock INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error al agregar el producto.';
    END;
    IF p_precio_compra <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El precio de compra debe ser mayor a 0.';
    END IF;
    IF p_precio_venta <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El precio de venta debe ser mayor a 0.';
    END IF;
    IF p_precio_venta <= p_precio_compra THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El precio de venta debe ser mayor al precio de compra.';
    END IF;
    IF p_stock < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El stock no puede ser negativo.';
    END IF;
    START TRANSACTION;
    INSERT INTO Productos (
        cod_categoria, ruc, nombre, linea, descripcion, 
        precio_compra, precio_venta, stock, estado, fecha_registro
    )
    VALUES (
        p_cod_categoria, p_ruc, p_nombre, p_linea, p_descripcion, 
        p_precio_compra, p_precio_venta, p_stock, 
        IF(p_stock > 0, 'disponible', 'agotado'), 
        CURRENT_TIMESTAMP
    );
    COMMIT;
END$$
DELIMITER ;

-- EDITAR:
-- Editar el precio de compra
-- Editar el precio de venta
-- Editar la descripción
-- Editar la linea
-- Editar el stock
DELIMITER $$
CREATE PROCEDURE EditarPrecioCompraProducto(
    IN p_cod_producto INT,
    IN p_precio_compra FLOAT
)
BEGIN
    IF p_precio_compra <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El precio de compra debe ser mayor a 0.';
    END IF;
    UPDATE Productos SET precio_compra = p_precio_compra WHERE cod_producto = p_cod_producto;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarPrecioVentaProducto(
    IN p_cod_producto INT,
    IN p_precio_venta FLOAT
)
BEGIN
    DECLARE precio_compra_actual FLOAT;
    IF p_precio_venta <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El precio de venta debe ser mayor a 0.';
    END IF;
    SELECT precio_compra INTO precio_compra_actual  FROM Productos WHERE cod_producto = p_cod_producto;
    IF p_precio_venta <= precio_compra_actual THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El precio de venta debe ser mayor al precio de compra actual.';
    END IF;
    UPDATE Productos SET precio_venta = p_precio_venta WHERE cod_producto = p_cod_producto;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarDescripcionProducto(
    IN p_cod_producto INT,
    IN p_descripcion TEXT
)
BEGIN
    IF p_descripcion IS NULL OR TRIM(p_descripcion) = '' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La descripción no puede estar vacía.';
    END IF;
    UPDATE Productos SET descripcion = p_descripcion WHERE cod_producto = p_cod_producto;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarLineaProducto(
    IN p_cod_producto INT,
    IN p_linea VARCHAR(100)
)
BEGIN
    IF p_linea IS NULL OR TRIM(p_linea) = '' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La línea no puede estar vacía.';
    END IF;
    UPDATE Productos SET linea = p_linea WHERE cod_producto = p_cod_producto;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE EditarStockProducto(
    IN p_cod_producto INT,
    IN p_stock INT
)
BEGIN
    IF p_stock < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El stock no puede ser negativo.';
    END IF;
    UPDATE Productos
    SET stock = p_stock,
        estado = IF(p_stock > 0, 'disponible', 'agotado')
    WHERE cod_producto = p_cod_producto;
END$$
DELIMITER ;

-- CAMBIAR ESTADO:
-- si queremos cambiar de disponible a agotado, debemos pasar el stock como 0
-- si queremos cambiar de agotado a disponible, debemos pasar algun tipo de stock mayor a 0
DELIMITER $$
CREATE PROCEDURE CambiarEstadoProducto(
    IN p_cod_producto INT,       -- Código del producto
    IN p_estado ENUM('disponible', 'agotado'), -- Estado deseado
    IN p_stock INT               -- Stock a asignar
)
BEGIN
    IF p_estado NOT IN ('disponible', 'agotado') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El estado debe ser "disponible" o "agotado".';
    END IF;
    IF p_stock < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El stock no puede ser negativo.';
    END IF;
    IF p_estado = 'disponible' THEN
        IF p_stock = 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El stock debe ser mayor a 0 para cambiar el estado a "disponible".';
        END IF;
        UPDATE Productos SET stock = p_stock, estado = 'disponible' WHERE cod_producto = p_cod_producto;
    ELSE
        IF p_stock > 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El stock debe ser 0 para cambiar el estado a "agotado".';
        END IF;
        UPDATE Productos SET stock = p_stock, estado = 'agotado' WHERE cod_producto = p_cod_producto;
    END IF;
    -- SELECT CONCAT('El producto con código ', p_cod_producto, ' ahora tiene estado "', p_estado, '" y stock ', p_stock, '.') AS mensaje;
END$$
DELIMITER ;

-- MOSTRAR: