-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

SELECT s.title
FROM tv_shows s
WHERE s.id NOT IN (
  SELECT sg.show_id
  FROM tv_show_genres sg
  INNER JOIN tv_genres g ON sg.genre_id = g.id
  WHERE g.name = 'Comedy'
)
ORDER BY s.title ASC;
