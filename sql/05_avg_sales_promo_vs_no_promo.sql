SELECT CASE WHEN onpromotion > 0 THEN 'with_promo' ELSE 'no_promo' END AS promo_flag,
       COUNT(*) AS n_rows,
       ROUND(AVG(sales), 2) AS avg_sales
FROM train
GROUP BY promo_flag;