-- MySQL script to list all cities in the hbtn_0d_usa database with corresponding state names
USE hbtn_0d_usa; -- Switch to the hbtn_0d_usa database

-- Select the required columns and join the cities and states tables
-- Display cities.id, cities.name, and states.name for each record
-- Order the results by cities.id in ascending order
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

