CREATE TABLE animals(
    animal_name TEXT NOT NULL,
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    age INTEGER NOT NULL
);

ALTER TABLE animals ADD meal TEXT;

.schema animals

ALTER TABLE animals RENAME TO zoo;

.table

DROP TABLE zoo;