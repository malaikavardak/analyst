-- Top cities by total and average revenue
SELECT
    r.city,
    ROUND(SUM(p.amount), 2) AS total_revenue,
    ROUND(AVG(p.amount), 2) AS avg_revenue_per_ride
FROM payments p
JOIN rides r ON p.ride_id = r.ride_id
WHERE r.status = 'completed'
GROUP BY r.city
ORDER BY total_revenue DESC;
