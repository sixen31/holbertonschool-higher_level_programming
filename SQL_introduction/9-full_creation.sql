-- Create table 'second_table' in db 'hbtn_0c_0'
-- Add descriptions (id INT), (name VARCHAR(256)), (score INT)
-- db name will be passed as arg to mysql cmd
-- Not allowed to use SELECT or SHOW
CREATE TABLE IF NOT EXISTS hbtn_0c_0.second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- insert line on the table

INSERT INTO hbtn_0c_0.second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
