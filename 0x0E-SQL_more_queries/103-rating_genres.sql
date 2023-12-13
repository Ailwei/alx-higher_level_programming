-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

SELECT
    tv_genres.name,
    SUM(tv_show_genres_ratings.rating) AS rating_sum
FROM
    tv_genres
JOIN
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN
    tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN
    tv_show_genres_ratings ON tv_show_genres.id = tv_show_genres_ratings.show_genre_id
GROUP BY
    tv_genres.id, tv_genres.name
ORDER BY
    rating_sum DESC;

