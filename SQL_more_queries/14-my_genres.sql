-- Ce script SQL récupère tous les genres de la série "Dexter" à partir de la base de données "hbtn_0d_tvshows".
SELECT tv_genres.name AS name
FROM tv_genres
JOIN tv_show_genres
     ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
     ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
