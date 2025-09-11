CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    capital VARCHAR(100),
    flag VARCHAR(300),
    subregion VARCHAR(100),
    population BIGINT
);