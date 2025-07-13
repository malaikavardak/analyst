# Calculate utilization (rides per active day per driver)
rides_with_driver['ride_date'] = rides_with_driver['start_time'].dt.date
driver_utilization = rides_with_driver.groupby('driver_id').agg(
    Active_Days=('ride_date', 'nunique'),
    Rides_Completed=('ride_id', 'count'),
    City=('city', 'first'),
    Avg_Rating=('rating', 'mean')
).reset_index()

driver_utilization['Utilization_Score'] = (driver_utilization['Rides_Completed'] / driver_utilization['Active_Days']).round(2)
driver_utilization = driver_utilization.sort_values(by='Utilization_Score', ascending=False)
