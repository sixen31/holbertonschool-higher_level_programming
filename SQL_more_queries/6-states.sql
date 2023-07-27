-- Créer la base de données hbtn_0d_usa s'il elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utiliser la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- Créer la table states avec deux colonnes : id de type INT auto-générée, non NULL, unique et clé primaire, et name de type VARCHAR(256) non NULL
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
