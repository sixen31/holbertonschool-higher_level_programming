-- Créer la table unique_id avec deux colonnes : id de type INT avec valeur par défaut 1 et contrainte d'unicité, et name de type VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
