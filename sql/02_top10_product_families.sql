SELECT family,
       ROUND(SUM(sales), 2) AS total_sales
FROM train
GROUP BY family
ORDER BY total_sales DESC
LIMIT 10;