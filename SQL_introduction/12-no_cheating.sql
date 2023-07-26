-- This SQL script updates the score of Bob to 10 in the table "second_table."
-- It identifies Bob using his name field, as the id value is not allowed to be use.

UPDATE second_table
SET score = 10
WHERE name = 'bob';
