-- MySQL script to list cities in California without using JOIN

USE hbtn_0d_usa; -- Replace with your actual database name

-- Query to list cities in California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;


