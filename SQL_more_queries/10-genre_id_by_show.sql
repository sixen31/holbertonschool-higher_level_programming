-- Utiliser la base de données hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- Sélectionner les émissions avec leur genre_id en utilisant une jointure entre tv_shows et tv_show_genres
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
