CREATE DATABASE testdb;

USE testdb;

CREATE TABLE region (
  id INT PRIMARY KEY,
  name TEXT
);

INSERT INTO region (id,name)
  VALUES(1,"North America"),
  (2,"Latin America"),
  (3,"Europe"),
  (4,"Middle East"),
  (5,"Sub-Saharan Africa"),
  (6,"Central Asia"),
  (7,"South Asia"),
  (8,"East Asia"),
  (9,"Southeast Asia"),
  (10,"Caribbean");