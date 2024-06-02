import csv
import time
import random

# Simulate reading data from a sensor
def read_sensor_data():
    
    # Simulate sensor data (e.g., temperature and humidity)
    sensor_data = {
        'temperature': round(random.uniform(20.0, 30.0), 2),  # Temperature in Celsius
        'humidity': round(random.uniform(30.0, 60.0), 2)      # Humidity in percentage
    }
    return sensor_data

# Log sensor data to a CSV file.
def log_data_to_csv(filename, data):
    
    # Check if the file exists
    file_exists = False
    try:
        with open(filename, 'r'):
            file_exists = True
    except FileNotFoundError:
        file_exists = False
    
    # Open the CSV file in append mode
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['timestamp', 'temperature', 'humidity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header only if the file does not exist
        if not file_exists:
            writer.writeheader()
        
        # Write the sensor data to the CSV file
        writer.writerow({
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),  # Current timestamp
            'temperature': data['temperature'],               # Temperature data
            'humidity': data['humidity']                      # Humidity data
        })

# Main function to simulate data logging.
def main():

    filename = 'sensor_data.csv'  # Name of the CSV file to log data
    
    try:
        while True:
            sensor_data = read_sensor_data()  # Read data from the sensor
            log_data_to_csv(filename, sensor_data)  # Log the data to the CSV file
            print(f"Logged data: {sensor_data}")
            time.sleep(5)  # Wait for 5 seconds before logging the next data point
    except KeyboardInterrupt:
        print("Data logging stopped by user.")

if __name__ == "__main__":
    main()
