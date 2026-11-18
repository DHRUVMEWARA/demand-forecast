SELECT s.type AS store_type,
       COUNT(DISTINCT s.store_nbr) AS n_stores,
       ROUND(SUM(t.sales), 2) AS total_sales,
       ROUND(SUM(t.sales) / COUNT(DISTINCT s.store_nbr), 2) AS sales_per_store
FROM train t
JOIN stores s ON t.store_nbr = s.store_nbr
GROUP BY s.type
ORDER BY total_sales DESC;