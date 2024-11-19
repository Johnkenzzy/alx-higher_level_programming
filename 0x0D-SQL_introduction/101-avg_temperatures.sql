-- Import in hbtn_0c_0 database this table dump: download
USE hbtn_0c_0;
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
