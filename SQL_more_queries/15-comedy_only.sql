-- Cette requête SQL récupère tous les genres de la série "Dexter" à partir de la base de données "hbtn_0d_tvshows" et les trie par nom de genre

-- Sélectionne le titre des émissions de télévision en utilisant un alias "title"
SELECT tv_shows.title AS title
FROM tv_shows
-- Joindre la table "tv_shows" avec la table "tv_genres" en utilisant la clause JOIN
-- La condition de jointure est que la colonne "genre_id" de "tv_shows" doit être égale à la colonne "id" de "tv_genres"
JOIN tv_genres ON tv_shows.genre_id = tv_genres.id

-- Filtrer les résultats en utilisant la clause WHERE pour ne sélectionner que les émissions de genre "Comedy"
WHERE tv_genres.name = 'Comedy'

-- Trier les résultats en fonction du titre de l'émission, dans l'ordre croissant (par ordre alphabétique)
ORDER BY tv_shows.title;
