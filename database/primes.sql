/* Create & Drop */
CREATE TABLE ints(n UNIQUE, prime DEFAULT 1);  -- DEFAULT 1 means this int is a prime, 1 represent True, 0 represent False.

/* Insert */
INSERT INTO ints VALUES (2, 1), (3, 1);
INSERT INTO ints(n) VALUES (4), (5), (6), (7), (8);
INSERT INTO ints(n) SELECT n+7 FROM ints;
INSERT INTO ints(n) SELECT n+14 FROM ints;
SELECT * FROM ints;

/* Update */
UPDATE ints SET prime=0 WHERE n > 2 AND n % 2 = 0;
UPDATE ints SET prime=0 WHERE n > 3 AND n % 3 = 0;
UPDATE ints SET prime=0 WHERE n > 5 AND n % 5 = 0;
SELECT * FROM ints;

/* Delete */
DELETE FROM ints WHERE prime=0;
SELECT n FROM ints;

.exit
