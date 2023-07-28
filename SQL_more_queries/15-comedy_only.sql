-- Cette requête SQL récupère tous les genres de la série "Dexter" à partir de la base de données "hbtn_0d_tvshows" et les trie par nom de genre
SELECT tv_shows.title
FROM tv_shows
JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
