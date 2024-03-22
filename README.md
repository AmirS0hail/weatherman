
# Weather Man

## Introduction
Weather Man is a command-line application designed to generate various reports based on weather data provided in files. The application can produce reports such as displaying the highest and lowest temperatures, the most humid day, and more.

## Features
- Display the highest and lowest temperatures for a given year.
- Display the average highest and lowest temperatures, and average humidity for a given month.
- Draw horizontal bar charts for the highest and lowest temperatures on each day of a given month.

## Usage
To use Weather Man, follow the instructions below:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/weather-man.git
   ```

2. Navigate to the project directory:
   ```bash
   cd weather-man
   ```

3. Run the application with the desired command-line options:
   - Display highest, lowest, and most humid day for a given year:
     ```bash
     python weatherman.py -e <year> /path/to/filesFolder
     ```
   - Display average highest, lowest temperatures, and average humidity for a given month:
     ```bash
     python weatherman.py -a <year>/<month> /path/to/filesFolder
     ```
   - Draw horizontal bar charts for highest and lowest temperatures for each day of a given month:
     ```bash
     python weatherman.py -c <year>/<month> /path/to/filesFolder
     ```

## Example
```bash
# Display highest, lowest, and most humid day for the year 2000
python weatherman.py -e 2000 data/lahore_weather

# Display average highest, lowest temperatures, and average humidity for January 2000
python weatherman.py -a 2000/01 data/lahore_weather

# Draw horizontal bar charts for highest and lowest temperatures for each day of January 2000
python weatherman.py -c 2000/01 data/lahore_weather
```

## Requirements
- Python 3.11.7
