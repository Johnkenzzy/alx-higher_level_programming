--  Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

SELECT genres.name
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;
