-- Rotten tomatoes
-- Script that lists all shows from databases by their rating.
SELECT s.title, SUM(sr.rate) AS rating FROM tv_shows AS s, tv_show_ratings AS sr WHERE s.id = sr.show_id GROUP BY s.title ORDER BY rating DESC;
