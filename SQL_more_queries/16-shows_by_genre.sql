-- Cette requête SQL récupère le titre des émissions (shows) ainsi que les genres associés à chaque émission.
-- Elle utilise LEFT JOIN pour inclure toutes les émissions, même celles sans genre associé.
-- Les résultats sont regroupés par titre d'émission et triés par ordre alphabétique du titre et du nom de genre.
SELECT tv_shows.title AS title, tv_genres.name AS name 
FROM tv_shows
LEFT JOIN tv_show_genres 
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres 
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_shows.title
ORDER BY tv_shows.title, name;
