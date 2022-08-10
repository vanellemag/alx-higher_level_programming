-- Temperature #1
-- Script that displays the top 3 of cities temperature during july and August.
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 0,4;
