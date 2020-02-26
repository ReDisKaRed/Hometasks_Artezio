CREATE DATABASE IF NOT EXISTS employees;
USE employees;
CREATE TABLE IF NOT EXISTS people(
id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
money INT NOT NULL
);
INSERT INTO people(id, first_name, last_name, money) VALUES(null, 'Anton', 'Petrov', 20000);
INSERT INTO people(id, first_name, last_name, money) VALUES(null, 'Vladislav', 'Ivanov', 40000);
INSERT INTO people(id, first_name, last_name, money) VALUES(null, 'Maxim', 'Egorov', 30000);
INSERT INTO people(id, first_name, last_name, money) VALUES(null, 'Nikita', 'Sokolov', 32000);
INSERT INTO people(id, first_name, last_name, money) VALUES(null, 'Irina', 'Ivanova', 27000);
CREATE TABLE IF NOT EXISTS positions(
id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
position VARCHAR(30) NOT NULL
);
INSERT INTO positions(id, position) VALUES(null, 'engineer');
INSERT INTO positions(id, position) VALUES(null, 'manager');
INSERT INTO positions(id, position) VALUES(null, 'accountant');
INSERT INTO positions(id, position) VALUES(null, 'estimator');
ALTER TABLE people ADD position_id INTEGER NOT NULL;
UPDATE people SET position_id=2 WHERE id IN (1, 4);
UPDATE people SET position_id=1 WHERE id IN (3);
UPDATE people SET position_id=3 WHERE id IN (2);
UPDATE people SET position_id=4 WHERE id IN (5);
SELECT people.first_name, people.last_name, money FROM people WHERE money < 30000;
SELECT people.first_name, people.last_name, job.position, money 
FROM people 
INNER JOIN positions job ON people.position_id=job.id 
WHERE money < 30000;