import psycopg2
import pandas as pd
import os
import environ

# Load environment variables from .env
env = environ.Env()
environ.Env.read_env(os.path.join(os.path.dirname(__file__), "../parking_backend/.env"))

# Database connection parameters from .env
DB_NAME = env("DB_NAME")
DB_USER = env("DB_USER")
DB_PASSWORD = env("DB_PASSWORD")
DB_HOST = env("DB_HOST")
DB_PORT = env("DB_PORT")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cursor = conn.cursor()

# Load the CSV file
csv_file_path = os.path.join(os.path.dirname(
    __file__), "murray_avenue_parking_spots.csv")
df = pd.read_csv(csv_file_path)

# Insert data into the ParkingSpot table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reservations_parkingspot (location, latitude, longitude, price_per_hour, is_available)
        VALUES (%s, %s, %s, %s, %s)
    """, (row['Location'], row['Latitude'], row['Longitude'], row['Price_per_Hour'], row['Availability'] == 'Available'))

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("Data successfully inserted into the database!")
