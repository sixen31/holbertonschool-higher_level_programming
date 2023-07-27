-- List all shows in db 'hbtn_0d_tvshows'
-- Each record show display tv_shows.title, tv_show_genres.genre_id
-- If show doesn't have genre, display NULL
-- You can use only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id -- Query to join cities and states
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
