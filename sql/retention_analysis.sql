-- Monthly user retention: users who rode again in a later month
WITH first_ride AS (
    SELECT user_id, MIN(start_time::date) AS first_ride_date
    FROM rides
    GROUP BY user_id
),
repeat_riders AS (
    SELECT r.user_id, DATE_TRUNC('month', r.start_time::timestamp) AS ride_month
    FROM rides r
    JOIN first_ride f ON r.user_id = f.user_id
    WHERE r.start_time::date > f.first_ride_date
)
SELECT
    ride_month,
    COUNT(DISTINCT user_id) AS retained_users
FROM repeat_riders
GROUP BY ride_month
ORDER BY ride_month;
