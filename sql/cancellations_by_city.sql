-- Cancellation rate by city
SELECT
    city,
    COUNT(*) FILTER (WHERE status = 'cancelled') AS cancelled_rides,
    COUNT(*) AS total_rides,
    ROUND(COUNT(*) FILTER (WHERE status = 'cancelled') * 100.0 / COUNT(*), 2) AS cancellation_rate_pct
FROM rides
GROUP BY city
ORDER BY cancellation_rate_pct DESC;
