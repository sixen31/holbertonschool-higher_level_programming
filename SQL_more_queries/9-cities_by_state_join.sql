-- Utiliser la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- Sélectionner les villes avec leur nom d'état en utilisant une jointure entre cities et states
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
