-- Utiliser la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- Sélectionner les villes de Californie en utilisant une sous-requête pour obtenir le state_id pour California
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;
