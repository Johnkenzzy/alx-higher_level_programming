-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
USE hbtn_0c_0;
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
