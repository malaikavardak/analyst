import pandas as pd
from datetime import datetime, timedelta
import os

# Define paths
data_dir = 'data'
output_dir = 'python'
output_file = os.path.join(output_dir, f'weekly_report_{datetime.today().date()}.xlsx')

# Load datasets
users = pd.read_csv(os.path.join(data_dir, 'users.csv'), parse_dates=['signup_date'])
drivers = pd.read_csv(os.path.join(data_dir, 'drivers.csv'), parse_dates=['join_date'])
rides = pd.read_csv(os.path.join(data_dir, 'rides.csv'), parse_dates=['start_time', 'end_time'])
payments = pd.read_csv(os.path.join(data_dir, 'payments.csv'), parse_dates=['timestamp'])

# Define the 7-day window
end_date = max(rides['start_time'].max(), payments['timestamp'].max())
start_date = end_date - timedelta(days=7)

# Filter data for the last 7 days
recent_rides = rides[(rides['start_time'] >= start_date) & (rides['start_time'] <= end_date) & (rides['status'] == 'completed')]
recent_payments = payments[(payments['timestamp'] >= start_date) & (payments['timestamp'] <= end_date)]

# Calculate KPIs
total_rides = len(recent_rides)
total_revenue = recent_payments['amount'].sum()
active_users = recent_rides['user_id'].nunique()
active_drivers = recent_rides['driver_id'].nunique()
avg_distance = recent_rides['distance_km'].mean()
avg_fare = recent_rides['fare'].mean()

# Create a summary DataFrame
summary = pd.DataFrame({
    'Metric': [
        'Total Rides',
        'Total Revenue',
        'Active Users',
        'Active Drivers',
        'Average Ride Distance (km)',
        'Average Fare (currency)'
    ],
    'Value': [
        total_rides,
        round(total_revenue, 2),
        active_users,
        active_drivers,
        round(avg_distance, 2),
        round(avg_fare, 2)
    ]
})

# Save to Excel
summary.to_excel(output_file, index=False, engine='openpyxl')
print(f"Weekly report saved to {output_file}")
