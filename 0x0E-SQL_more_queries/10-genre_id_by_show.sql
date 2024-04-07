-- List all shows contains in hbtn_0d_tv_show database that have at least one genre seires
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
RIGHT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
