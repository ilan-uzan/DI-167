CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	last_name VARCHAR(50),
	first_name VARCHAR(50)
	birthdate DATE 
);

INSERT INTO students (first_name, last_name, birthdate) VALUES
('Marc', 'Benichou', '1998-11-02')
('Yoan', 'Cohen', '2010-12-03')
('Lea', 'Benichou', '1987-07-27')
('Amelia', 'Dux', '1996-04-07')
('David', 'Grez', '2003-06-14')
('Omer', 'Simpson', '1980-10-03')

