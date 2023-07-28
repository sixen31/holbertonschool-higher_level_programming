-- Cette requête SQL récupère tous les genres de la série "Dexter" à partir de la base de données "hbtn_0d_tvshows" et les trie par nom de genre
-- Joindre la table "tv_shows" avec la table "tv_genres" en utilisant la clause JOIN
-- La condition de jointure est que la colonne "genre_id" de "tv_shows" doit être égale à la colonne "id" de "tv_genres"
-- Sélectionne le titre des émissions de télévision en utilisant un alias "title"
SELECT tv_shows.title AS title
FROM tv_shows
JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
