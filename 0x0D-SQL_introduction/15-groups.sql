-- a script that list number of records with same acore in thetable second_table of the database


SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;
