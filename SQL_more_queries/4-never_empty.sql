-- Créer la table id_not_null avec deux colonnes : id de type INT avec valeur par défaut 1 et name de type VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
