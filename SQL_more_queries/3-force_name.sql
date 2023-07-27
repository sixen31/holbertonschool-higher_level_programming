-- Créer la table force_name avec deux colonnes : id de type INT et name de type VARCHAR(256)
-- La contrainte NOT NULL est appliquée sur la colonne name pour s'assurer qu'elle ne peut pas être NULL
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
