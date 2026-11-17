SELECT strftime('%Y-%m', date) AS month,
       ROUND(SUM(sales), 2) AS total_sales
FROM train
GROUP BY month
ORDER BY month;