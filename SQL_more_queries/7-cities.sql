-- Créer la base de données hbtn_0d_usa s'il elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utiliser la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- Créer la table cities avec trois colonnes :
-- id de type INT auto-générée, non NULL, unique et clé primaire
-- state_id de type INT, non NULL, faisant référence à id de la table states en tant que clé étrangère
-- name de type VARCHAR(256), non NULL
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
