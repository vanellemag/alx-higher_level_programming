-- Not my genre
-- Script that uses the database to list all genres not linked tot the show Dexter.
SELECT g.name FROM tv_genres AS g, tv_shows AS s, tv_show_genres AS sg WHERE(g.id = sg.genre_id AND s.title <> "Dexter" AND s.id <> sg.show_id) GROUP BY g.name ORDER BY g.name ASC;
