-- This SQL script lists the number of records with the same score in the "second_table."
-- It displays the score and the number of records for each score, sorted by the number of records in descending order.

SELECT score, COUNT(*) AS number
FROM second_table
GROUPE BY score
ORDER BY number DESC;
