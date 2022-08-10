-- Temperatures #2
-- Script that displays the max temperature of each state.
SELECT state, MAX(value) AS max_temp FROM temperatures ORDER BY state DESC;
