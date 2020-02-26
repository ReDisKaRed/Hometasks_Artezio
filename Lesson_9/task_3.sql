CREATE TABLE IF NOT EXISTS communication (
chief_id INT,
inferior_id INT
);
INSERT INTO communication(chief_id, inferior_id) VALUES (1, 2), (1, 3), (3, 1), (4, 3);
SELECT chief.first_name AS chief_name, chief.last_name, inf.first_name AS inferior_name, inf.last_name
FROM people AS chief
INNER JOIN communication ON chief.id = communication.chief_id
INNER JOIN people AS inf ON inf.id = communication.inferior_id
WHERE chief.id=(1);