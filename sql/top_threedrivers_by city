--Top 3 drivers by City

WITH recent_rides AS (
    SELECT *
    FROM rides
    WHERE start_time >= CURRENT_DATE - INTERVAL '30 days'
      AND status = 'completed'
),
driver_stats AS (
    SELECT
        d.driver_id,
        d.city,
        d.rating,
        d.vehicle_type,
        COUNT(r.ride_id) AS total_rides,
        ROUND(SUM(r.fare), 2) AS total_revenue,
        ROUND(AVG(r.distance_km), 2) AS avg_distance,
        ROUND(AVG(EXTRACT(EPOCH FROM (r.end_time - r.start_time)) / 60), 2) AS avg_duration_min
    FROM recent_rides r
    JOIN drivers d ON r.driver_id = d.driver_id
    GROUP BY d.driver_id, d.city, d.rating, d.vehicle_type
),
ranked_drivers AS (
    SELECT *,
           RANK() OVER (PARTITION BY city ORDER BY total_revenue DESC) AS revenue_rank
    FROM driver_stats
)
SELECT
    city,
    driver_id,
    vehicle_type,
    rating,
    total_rides,
    total_revenue,
    avg_distance,
    avg_duration_min,
    revenue_rank
FROM ranked_drivers
WHERE revenue_rank <= 3
ORDER BY city, revenue_rank;
