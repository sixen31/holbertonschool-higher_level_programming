-- This SQL script lists all records from the "second_table" with a name value.
-- It displays the score and the name in that order.
-- Records are listed in descending order based on the score.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
