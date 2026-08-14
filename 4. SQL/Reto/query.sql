DROP DATABASE IF EXISTS heroes;

CREATE DATABASE heroes;

USE heroes;

CREATE TABLE publisher(
    publisher_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    publisher_name VARCHAR(100) NOT NULL
);
DESCRIBE publisher;

CREATE TABLE race(
    race_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    race_name VARCHAR(100) NOT NULL
);
DESCRIBE race;

CREATE TABLE hero (
    hero_id INTEGER PRIMARY KEY,
    hero_name VARCHAR(100),
    gender VARCHAR(20),
    eye_color VARCHAR(50),
    hair_color VARCHAR(50),
    skin_color VARCHAR(50),
    height FLOAT,
    weight FLOAT,
    alignment VARCHAR(20),

    publisher_id INTEGER,
    race_id INTEGER,

    FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id),

    FOREIGN KEY (race_id) REFERENCES race(race_id)
);
DESCRIBE hero;

INSERT INTO publisher VALUES (1,'Marvel Comics'),
	(2,'Dark Horse Comics'),
	(3,'DC Comics'),
	(4,'NBC - Heroes'),
	(5,'Wildstorm');

INSERT INTO race VALUES (1,'Human'),
	(2,'Icthyo Sapien'),
	(3,'Ungaran'),
	(4,'Human / Radiation'),
	(5,'Cosmic Entity'),
	(6,'-'),
	(7,'Cyborg'),
	(8,'Xenomorph XX121'),
	(9,'Android');


INSERT INTO hero VALUES 
(1,'A-Bomb','Male','yellow','No Hair','-',203,441,'good',1,1),
(2,'Abe Sapien','Male','blue','No Hair','blue',191,65,'good',2,2),
(3,'Abin Sur','Male','blue','No Hair','red',185,90,'good',3,3),
(4,'Abomination','Male','green','No Hair','-',203,441,'bad',1,4),
(5,'Abraxas','Male','blue','Black','-',-99.0,NULL,'bad',1,5),
(6,'Absorbing Man','Male','blue','No Hair','-',193,122,'bad',1,1),
(7,'Adam Monroe','Male','blue','Blond','-',-99.0,NULL,'good',4,6),
(8,'Adam Strange','Male','blue','Blond','-',185,88,'good',3,1),
(9,'Agent 13','Female','blue','Blond','-',173,61,'good',1,6),
(10,'Agent Bob','Male','brown','Brown','-',178,81,'good',1,1),
(11,'Agent Zero','Male','-','-','-',191,104,'good',1,6),
(12,'Air-Walker','Male','blue','White','-',188,108,'bad',1,6),
(13,'Ajax','Male','brown','Black','-',193,90,'bad',1,7),
(14,'Alan Scott','Male','blue','Blond','-',180,90,'good',3,6),
(15,'Alex Mercer','Male','-','-','-',-99.0,NULL,'bad',5,1),
(16,'Alex Woolsly','Male','-','-','-',-99.0,NULL,'good',4,6),
(17,'Alfred Pennyworth','Male','blue','Black','-',178,72,'good',3,1),
(18,'Alien','Male','-','No Hair','black',244,169,'bad',2,8),
(19,'Allan Quatermain','Male','-','-','-',-99.0,NULL,'good',5,6),
(20,'Amazo','Male','red','-','-',257,173,'bad',3,9);

UPDATE hero SET weight = NULL
	WHERE weight = -99.0;

SELECT weight FROM hero;

SELECT
    h.hero_id,
    h.hero_name,
    h.gender,
    h.eye_color,
    r.race_name,
    h.hair_color,
    h.height,
    p.publisher_name,
    h.skin_color,
    h.alignment,
    h.weight
FROM hero h
JOIN publisher p
    ON h.publisher_id = p.publisher_id
JOIN race r
    ON h.race_id = r.race_id
ORDER BY h.hero_id;

CREATE VIEW superhero AS
SELECT
    h.hero_id,
    h.hero_name,
    h.gender,
    h.eye_color,
    r.race_name,
    h.hair_color,
    h.height,
    p.publisher_name,
    h.skin_color,
    h.alignment,
    h.weight
FROM hero h
JOIN publisher p
    ON h.publisher_id = p.publisher_id
JOIN race r
    ON h.race_id = r.race_id
ORDER BY h.hero_id;

SELECT * FROM superhero;

SELECT *, MAX(height) FROM hero;

SELECT * FROM hero
	WHERE weight > (
		SELECT AVG(weight) FROM hero
        );
        
SELECT publisher_name, AVG(height) FROM superhero
	GROUP BY publisher_name;
	