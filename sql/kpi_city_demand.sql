-- Total rides and average rides per user by city
SELECT
    city,
    COUNT(*) AS total_rides,
    COUNT(DISTINCT user_id) AS unique_users,
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT user_id), 2) AS avg_rides_per_user
FROM rides
WHERE status = 'completed'
GROUP BY city
ORDER BY total_rides DESC;
