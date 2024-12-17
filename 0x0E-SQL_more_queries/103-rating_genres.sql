-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.

SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres g
INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
INNER JOIN tv_shows s ON s.id = sg.show_id
INNER JOIN tv_show_ratings r ON r.show_id = s.id
GROUP BY g.name
ORDER BY rating DESC;
