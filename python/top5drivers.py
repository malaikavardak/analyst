# Merge rides with drivers
rides_with_driver = recent_rides.merge(drivers, on='driver_id', how='left')

# Top 5 drivers by ride count
top_drivers = rides_with_driver.groupby(['driver_id', 'city']).agg(
    Rides_Completed=('ride_id', 'count'),
    Avg_Ride_Duration_Min=('start_time', lambda x: (rides_with_driver.loc[x.index, 'end_time'] - x).dt.total_seconds().mean() / 60),
    Avg_Rating=('rating', 'mean'),
    Vehicle_Type=('vehicle_type', 'first')
).reset_index().sort_values(by='Rides_Completed', ascending=False).head(5)

top_drivers = top_drivers.round(2)
