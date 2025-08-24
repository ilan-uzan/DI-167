-- create the table 

CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	last_name VARCHAR(50),
	first_name VARCHAR(50)
	birthdate DATE 
);

-- insert data into the table 

INSERT INTO students (first_name, last_name, birthdate) VALUES
('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-10-03'),
('Ilan', 'Uzan', '2002-10-12');

-- fetch all data
SELECT * FROM students;
-- fetch first and last name
SELECT first_name, last_name FROM students;
-- fetch student with id = 2
SELECT first_name, last_name FROM students WHERE id = 2;
--fetch marc benichou
SELECT first_name, last_name FROM students
WHERE last_name = 'Benichou' AND first_name = 'Marc';
-- fertch benichou or marc
SELECT first_name, last_name FROM students
WHERE last_name = 'Benichou' OR first_name = 'Marc';
-- first name that has the letter 'a'
SELECT first_name FROM students
WHERE first_name LIKE '%a%';
-- first name starts with 'a'
SELECT first_name FROM students
WHERE first_name LIKE 'a%';
-- first name ends with 'a'
SELECT first_name FROM students
WHERE first_name LIKE '%a';



