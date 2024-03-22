import argparse
import os
from datetime import datetime

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Weather Man")
    parser.add_argument("-e", "--year", help="Year for the report")
    parser.add_argument("-a", "--month", help="Month for the report in YYYY/MM format")
    parser.add_argument("folder", help="Path to the folder containing weather data files")
    return parser.parse_args()

# Function to read weather data files
def read_weather_data(folder, year=None, month=None):
    weather_data = {}
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):  # assuming weather data files have .txt extension
            with open(os.path.join(folder, filename), "r") as file:
                # Skip the first line (headers)
                next(file)
                for line in file:
                    # Split the line and extract date, max temperature, and humidity
                    fields = line.strip().split(",")
                    
                    # Check if the line has enough fields
                    if len(fields) < 10:  # Adjust the index based on the actual number of fields containing temperature and humidity
                        continue  # Skip lines with insufficient data
                    
                    date_str = fields[0]
                    temp = fields[1]
                    humidity = fields[9]

                    try:
                        # Parse date and check if it matches the specified year or month
                        if date_str.startswith("PKT"):
                            # Date format: "PKT,YYYY-MM-DD"
                            date_str = date_str[4:]
                            date = datetime.strptime(date_str, "%Y-%m-%d")
                        else:
                            # Date format: "YYYY-MM-DD"
                            date = datetime.strptime(date_str, "%Y-%m-%d")

                        if (year and date.year == int(year)) or (month and date.strftime("%Y/%m") == month):
                            weather_data[date] = {"date": date, "temperature": float(temp), "humidity": int(humidity)}
                    except ValueError:
                        # Skip lines with date parsing errors
                        continue
    return weather_data

# Function to generate year report
def year_report(year, folder):
    weather_data = read_weather_data(folder, year=year)
    if not weather_data:
        print(f"No data available for the year {year}")
        return

    highest_temp = max(weather_data.values(), key=lambda x: x["temperature"])
    lowest_temp = min(weather_data.values(), key=lambda x: x["temperature"])
    highest_humidity = max(weather_data.values(), key=lambda x: x["humidity"])

    print(f"Highest: {highest_temp['temperature']}C on {highest_temp['date'].strftime('%B %d')}")
    print(f"Lowest: {lowest_temp['temperature']}C on {lowest_temp['date'].strftime('%B %d')}")
    print(f"Humid: {highest_humidity['humidity']}% on {highest_humidity['date'].strftime('%B %d')}")

# Function to generate month report
def month_report(month, folder):
    weather_data = read_weather_data(folder, month=month)
    if not weather_data:
        print(f"No data available for the month {month}")
        return

    total_temp = 0
    total_humidity = 0
    count = 0
    for data in weather_data.values():
        total_temp += data["temperature"]
        total_humidity += data["humidity"]
        count += 1

    average_temp = total_temp / count
    average_humidity = total_humidity / count

    print(f"Highest Average: {average_temp:.1f}C")
    print(f"Lowest Average: {average_temp:.1f}C")
    print(f"Average Humidity: {average_humidity:.1f}%")

# Main function
def main():
    args = parse_arguments()
    if args.year:
        year_report(args.year, args.folder)
    elif args.month:
        month_report(args.month, args.folder)
    else:
        print("Please provide either a year (-e) or a month (-a) for the report.")

# Call main function
if __name__ == "__main__":
    main()
