# Crear la tabla marca
CREATE TABLE marca(
    id_marca SMALLINT NOT NULL,
    nombre_marca VARCHAR(30) NOT NULL,
    PRIMARY KEY (id_marca)
);

# Crear la tabla auto
CREATE TABLE auto(
    vin VARCHAR(17) NOT NULL,
    id_marca SMALLINT,
    submarca VARCHAR(30),
    modelo YEAR,
    color VARCHAR(20),
    transmision ENUM('manual', 'automatica'),
    recorrido INT,
    FOREIGN KEY (id_marca) REFERENCES marca(id_marca)
        ON DELETE RESTRICT
        ON UPDATE CASCADE  
);

DESCRIBE empleado;

#Insertar un solo registro en la tabla empleado
INSERT INTO empleado VALUES (1, 'Diego Rodriguez');

# Insertar multiples registros en la tabla empleado
INSERT INTO empleado VALUES
    (2, 'Maria Gomez'),
    (3, 'Juan Perez'),
    (4, 'Ana Martinez'),
    (5, 'Carlos Sanchez');

# Consultar datos de la tabla empleado
SELECT * FROM empleado;

# Consultar solo el nombre del empleado
SELECT nombre FROM empleado;

# Insertamos valores para las tablas marca y auto
INSERT INTO marca VALUES
    (1,'VOLKSWAGEN'), 
    (2, 'HONDA'), 
    (3, 'TOYOTA');
INSERT INTO auto VALUES
  ('3VWU67FR7RE3', 1, 'POLO', 2015, 'gris platino',   'MANUAL',    125000),        
  ('HDG6JBSD7FDT', 2, 'CIVIC', 2020, 'PLATA DIAMANTE', 'AUTOMÁTICA', 40000),       
  ('3VWGCISDS7D7', 1, 'TIGUAN', 2012, 'BLANCO', 'AUTOMÁTICA', 132000),            
  ('6TDG675E54GY', 3, 'COROLLA', 2022, 'ROJO', 'MANUAL', 30000) ;

#Filtrar y proyectar datos
SELECT submarca, color, modelo FROM auto WHERE modelo >= 2020;

#Diferente de
SELECT * FROM auto WHERE id_marca != 1;

# Actualizar datos
UPDATE auto SET modelo = 2021, transmision = 'Manual'
WHERE vin = 'HDG6JBSD7FDT';

# Eliminar datos
DELETE FROM auto WHERE submarca = 'COROLLA';

# Producto entre 2 tablas
SELECT * FROM auto, marca WHERE auto.id_marca = marca.id_marca;

# JOIN
SELECT * FROM auto JOIN marca ON auto.id_marca = marca.id_marca;

#Natural Join busca columnas con el mismo nombre en ambas tablas y las une
SELECT * FROM auto NATURAL JOIN marca;

#Agregamos mas datos a las tablas
INSERT INTO marca VALUES
    (4, 'FORD'),
    (5, 'MAZDA');

INSERT INTO auto VALUES
    ('3VWU67FR7RE3', NULL, 'VITARA', 2016, 'BLANCO', 'AUTOMATICA', 213000),
    ('3VWGCISDS7D7', NULL, 'WRX', 2020, 'BLANCO', 'MANUAL', 50000);

# Ya que insertamos autos sin marca, el resultado no los mostrara ya que es un INNER JOIN
#Para mostrar todos los autos aunque no tengan marca, usamos un LEFT JOIN
SELECT * FROM auto LEFT JOIN marca ON auto.id_marca = marca.id_marca;

#Ahora un RIGHT JOIN para mostrar todas las marcas aunque no tengan autos
SELECT * FROM auto RIGHT JOIN marca ON auto.id_marca = marca.id_marca;

