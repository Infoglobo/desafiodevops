CREATE DATABASE IF NOT EXISTS desafio;
USE desafio;

CREATE TABLE revistas (
    ID int NOT NULL AUTO_INCREMENT,
    message VARCHAR(20),
    PRIMARY KEY (ID)
);

INSERT INTO revistas(message) values ('marieclaire');
INSERT INTO revistas(message) values ('glamour');
INSERT INTO revistas(message) values ('epoca');
INSERT INTO revistas(message) values ('extra');
INSERT INTO revistas(message) values ('globo');
INSERT INTO revistas(message) values ('valor');
INSERT INTO revistas(message) values ('autoesporte');
INSERT INTO revistas(message) values ('pegn');

commit;
