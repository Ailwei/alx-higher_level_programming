-- First, get the genre IDs linked to Dexter
SET @dexter_genre_ids = (SELECT GROUP_CONCAT(DISTINCT genre_id) FROM tv_show_genres WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter'));

-- List all genres not linked to Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (@dexter_genre_ids)
ORDER BY tv_genres.name ASC;

