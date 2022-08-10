-- GENRE id BY SHOW
-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows, tv_shows_genres ORDER BY tv_shows.title AND tv_show_genres.genre_id;
