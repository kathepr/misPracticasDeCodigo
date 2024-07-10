-- Crea la base de datos 'hello_mysql' si no existe
CREATE DATABASE IF NOT EXISTS `hello_mysql`;

-- Usa la base de datos 'hello_mysql'
USE `hello_mysql`;

-- Crea una tabla llamada 'users' con las siguientes columnas
CREATE TABLE `users` (
    -- Define una columna 'user_id' de tipo entero (INT)
    -- La columna no puede tener valores NULL (NOT NULL)
    -- Los valores se incrementarán automáticamente (AUTO_INCREMENT)
    `user_id` INT NOT NULL AUTO_INCREMENT,

    -- Define una columna 'name' de tipo cadena de texto variable (VARCHAR)
    -- La longitud máxima de la cadena es 50 caracteres
    -- La columna no puede tener valores NULL (NOT NULL)
    `name` VARCHAR(50) NOT NULL,

    -- Define una columna 'surname' de tipo cadena de texto variable (VARCHAR)
    -- La longitud máxima de la cadena es 100 caracteres
    -- La columna puede tener valores NULL
    `surname` VARCHAR(100) NULL,

    -- Define una columna 'age' de tipo entero (INT)
    -- La columna puede tener valores NULL
    `age` INT NULL,

    -- Define una columna 'init_date' de tipo fecha (DATE)
    -- La columna puede tener valores NULL
    `init_date` DATE NULL,

    -- Define una columna 'email' de tipo cadena de texto variable (VARCHAR)
    -- La longitud máxima de la cadena es 100 caracteres
    -- La columna puede tener valores NULL
    `email` VARCHAR(100) NULL,

    -- Establece la columna 'user_id' como la clave primaria de la tabla
    -- Esto asegura que cada valor en 'user_id' sea único y no NULL
    PRIMARY KEY (`user_id`)
);







--********************************************
-- Añadir VALORES A LA TABLA

-- Insertar un registro en la tabla 'users'
INSERT INTO `users` (`name`, `surname`, `age`, `init_date`, `email`)
VALUES ('John', 'Doe', 30, '2024-07-09', 'john.doe@example.com');


-- Insertar otro registro en la tabla 'users'
--OJO:Es importante usar comillas inversas en INSERT INTO

INSERT INTO `users` (`name`, `surname`, `age`, `init_date`, `email`)
VALUES ('Hermione', 'Granger', 44, '2024-07-09', 'hermione@example.com');

