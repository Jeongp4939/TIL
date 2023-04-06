CREATE TABLE users (
    name TEXT NOT NULL,
    phoneNumber TEXT NOT NULL,
    blance TEXT NOT NULL,
    age INTEGER,
    gender TEXT
);

SELECT name, age, balance
FROM users
ORDER BY age ASC, balance DESC;