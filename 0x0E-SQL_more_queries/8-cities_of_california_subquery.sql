-- Cities of california
-- Script that lists all the cities of california that can be found in the database hbtn_0d_usa
-- SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'Califonia');
SELECT cities.id, cities.name FROM cities, states WHERE cities.state_id = states.id AND states.name = 'California' ORDER BY cities.id ASC;
