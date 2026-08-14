DROP DATABASE IF EXISTS `agencia`;
CREATE DATABASE `agencia`;

use `agencia`;

DROP TABLE IF EXISTS `marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marca` (
  `id_marca` smallint NOT NULL,
  `marca` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id_marca`)
);
/*!40101 SET character_set_client = @saved_cs_client */;


LOCK TABLES `marca` WRITE;
/*!40000 ALTER TABLE `marca` DISABLE KEYS */;
INSERT INTO `marca` VALUES
(1,'VOLKSWAGEN'),
(2,'HONDA'),
(3,'TOYOTA'),
(4,'FORD'),
(5,'MAZDA'),
(6,'SUZUKI'),
(7,'SUBARU');
/*!40000 ALTER TABLE `marca` ENABLE KEYS */;
UNLOCK TABLES;



DROP TABLE IF EXISTS `submarca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `submarca` (
  `submarca` varchar(30) NOT NULL,
  `id_marca` smallint DEFAULT NULL,
  PRIMARY KEY (`submarca`),
  KEY `id_marca` (`id_marca`),
  CONSTRAINT `submarca_ibfk_1` FOREIGN KEY (`id_marca`) REFERENCES `marca` (`id_marca`)
  ON DELETE RESTRICT ON UPDATE CASCADE
);
/*!40101 SET character_set_client = @saved_cs_client */;


LOCK TABLES `submarca` WRITE;
/*!40000 ALTER TABLE `submarca` DISABLE KEYS */;
INSERT INTO `submarca` VALUES
('POLO',1),
('TIGUAN',1),
('CIVIC',2),
('CR-V',2),
('FIT',2),
('COROLLA',3),
('SIENNA',3),
('VITARA',6),
('FORESTER',7),
('WRX',7);
/*!40000 ALTER TABLE `submarca` ENABLE KEYS */;
UNLOCK TABLES;



DROP TABLE IF EXISTS `auto`;

CREATE TABLE `auto` (
  `vin` varchar(17) DEFAULT NULL,
  `submarca` varchar(30) DEFAULT NULL,
  `modelo` year DEFAULT NULL,
  `color` varchar(30) DEFAULT NULL,
  `transmision` enum('MANUAL','AUTOMATICA') DEFAULT NULL,
  `recorrido` int DEFAULT NULL,
  KEY `submarca` (`submarca`),
  CONSTRAINT `auto_ibfk_1` FOREIGN KEY (`submarca`) REFERENCES `submarca` (`submarca`) ON DELETE RESTRICT ON UPDATE CASCADE
);


LOCK TABLES `auto` WRITE;
/*!40000 ALTER TABLE `auto` DISABLE KEYS */;
INSERT INTO `auto` VALUES
('3VWU67FR7RE3','POLO',2015,'GRIS PLATINO','MANUAL',125000),
('HDG6JBSD7FDT','CIVIC',2020,'PLATA DIAMANTE','AUTOMATICA',42000),
('3VWGCISDS7D7','TIGUAN',2012,'BLANCO','AUTOMATICA',132000),
('6TDG675E54GY','COROLLA',2022,'ROJO','MANUAL',30000),
('JD76F6SDF7DF','VITARA',2016,'BLANCO','AUTOMATICA',213000),
('9DTF6S5SG5G5','WRX',2020,'BLANCO','MANUAL',50000),
('3VWHUIHU4535','POLO',2019,'ROJO FLASH','MANUAL',63000),
('H787N7T34GNG','FIT',2018,'BLANCO','MANUAL',125000),
('HVNDUD778QER','CR-V',2022,'NEGRO','AUTOMATICA',75800),
('3VWUIHFUHDSF','POLO',2012,'BLANCO','AUTOMATICA',132000),
('6TDPOKDQ44O6','SIENNA',2023,'BLANCO PERLADO','AUTOMATICA',18500),
('JDRGERG54564','VITARA',2021,'ROJO','AUTOMATICA',213000),
('9D896GFG9DFG','WRX',2022,'AZUL METALICO','AUTOMATICA',41500),
('9DTHRUIHIEU8','FORESTER',2024,'AZUL METALICO','AUTOMATICA',37000);
/*!40000 ALTER TABLE `auto` ENABLE KEYS */;
UNLOCK TABLES;



CREATE VIEW `autos_disponibles` AS
select `auto`.`vin` AS `vin`,
  `auto`.`submarca` AS `submarca`,
  `marca`.`marca` AS `marca`,
  `auto`.`modelo` AS `modelo`,
  `auto`.`color` AS `color`,
  `auto`.`transmision` AS `transmision`,
  `auto`.`recorrido` AS `recorrido`
from ((`submarca` left join `auto` on((`auto`.`submarca` = `submarca`.`submarca`)))
join `marca` on((`submarca`.`id_marca` = `marca`.`id_marca`))) ;


select * FROM autos_disponibles


# Funciones agregadas
# Count
SELECT COUNT(*) FROM autos_disponibles;

# Sum
SELECT SUM(recorrido) FROM autos_disponibles;

# Promedio AVG
SELECT AVG(recorrido) FROM autos_disponibles;

# Minimo
SELECT MIN(modelo) FROM autos_disponibles;

# Maximo
SELECT MAX(modelo) FROM autos_disponibles;


# Agrupacion
SELECT marca,
       COUNT(*)
FROM autos_disponibles
GROUP BY marca;

# Order by sobre agregacion
SELECT marca,
       COUNT(*)
FROM autos_disponibles
GROUP BY marca
ORDER BY COUNT(*);

# Having que es un filtro where sobre una agrupacion
SELECT marca,
       COUNT(*)
FROM autos_disponibles
GROUP BY marca
HAVING COUNT(*) > 2;

/* El Orden que siempre se debe seguir para una consulta es:
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
*/

