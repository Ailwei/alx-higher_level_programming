-- MySQL script to list all cities in the hbtn_0d_usa database with corresponding state names
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
