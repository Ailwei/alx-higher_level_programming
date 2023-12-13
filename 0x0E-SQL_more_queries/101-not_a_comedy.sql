--  script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

-- First, get the genre ID for Comedy
SET @comedy_genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy');

-- List all shows without the Comedy genre
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id = @comedy_genre_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC;

