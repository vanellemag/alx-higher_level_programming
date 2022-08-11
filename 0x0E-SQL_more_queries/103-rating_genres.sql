-- Best genre
-- Script that list all genres in the database by their rating.
SELECT g.name, SUM(sr.rate) AS rating FROM tv_shows AS s, tv_show_ratings AS sr, tv_genres As g, tv_show_genres AS sg WHERE( g.id = sg.genre_id  AND sg.show_id = s.id AND s.id = sr.show_id ) GROUP BY g.name ORDER BY rating DESC;
