-- Lists all cities contained in the database hbtn_0d_usa.

SELECT cities.id, cities.name,
       (SELECT name FROM states WHERE id = cities.state_id) AS state_name
FROM cities;
