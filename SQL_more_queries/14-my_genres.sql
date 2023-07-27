-- Ce script SQL récupère tous les genres de la série "Dexter" à partir de la base de données "hbtn_0d_tvshows".
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
