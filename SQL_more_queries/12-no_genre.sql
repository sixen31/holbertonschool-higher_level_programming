-- Utiliser la base de données hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- Sélectionner les émissions sans genre en utilisant une jointure LEFT JOIN entre tv_shows et tv_show_genres et un WHERE clause
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
