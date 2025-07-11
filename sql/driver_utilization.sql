-- Driver utilization: rides per driver and average ride distance
SELECT
    d.city,
    r.driver_id,
    COUNT(*) AS total_rides,
    ROUND(AVG(r.distance_km), 2) AS avg_distance_km,
    ROUND(AVG(EXTRACT(EPOCH FROM (r.end_time::timestamp - r.start_time::timestamp)) / 60), 2) AS avg_duration_min
FROM rides r
JOIN drivers d ON r.driver_id = d.driver_id
WHERE r.status = 'completed'
GROUP BY d.city, r.driver_id
ORDER BY total_rides DESC;
