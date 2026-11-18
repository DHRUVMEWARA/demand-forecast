SELECT strftime('%Y', date) AS year,
       ROUND(SUM(sales), 2) AS total_sales
FROM train
GROUP BY year
ORDER BY year;