CREATE USER 'rodrigo'@'localhost' IDENTIFIED BY 'ubnt'; -- Crear el usuario 'rodrigo' con la contraseña 'ubnt' para acceso local
GRANT ALL PRIVILEGES ON *.* TO 'rodrigo'@'localhost' WITH GRANT OPTION; -- Otorgar todos los privilegios al usuario 'rodrigo' en todas las bases de datos, solo desde localhost
FLUSH PRIVILEGES; -- Aplicar los cambios de privilegios