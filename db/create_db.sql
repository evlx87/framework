PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS person;
CREATE TABLE person (IDPERSON INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, FIRSTNAME VARCHAR (32), LASTNAME VARCHAR (32));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;