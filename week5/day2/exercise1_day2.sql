-- CREATE TABLE FOR ITEMS 

CREATE TABLE items (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	price INT
);

-- CREATE TABLE FOR CUSTOMERS
CREATE TABLE customers (
	id SERIAL PRIMARY KEY
	firstname VARCHAR(50)
	lastname VARCHAR(50)
);

-- Insert items
INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

-- Insert customers
INSERT INTO customers (firstname, lastname) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

SELECT * FROM items;
SELECT * FROM items
WHERE price > 80;
SELECT * FROM items
WHERE price <= 300;
SELECT * FROM customers
WHERE lastname = 'Smith';
SELECT * FROM customers
WHERE lastname = 'Jones';
SELECT * FROM customers
WHERE firstname <> 'Scott';





