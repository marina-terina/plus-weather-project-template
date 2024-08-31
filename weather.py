import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_object = datetime.fromisoformat(iso_string)
    formatted_date = date_object.strftime("%A %d %B %Y")
    
    return formatted_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    if isinstance(temp_in_fahrenheit, str):
        temp_in_fahrenheit = float(temp_in_fahrenheit)
    temp_in_celcius = (temp_in_fahrenheit - 32) * 5/9
    
    return round(temp_in_celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data = [float(item) for item in weather_data]
    total = sum(weather_data)  
    mean_value = total / len(weather_data) 
    
    return mean_value


def load_data_from_csv(csv_file):
    
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file) as file:
        reader = csv.reader(file)
        data = []
        next(reader, None)    

        for row in reader:
            if row:
                row[1] = int(row[1])  
                row[2] = int(row[2])  
                data.append(row)
    return data
                

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return () 
    weather_data = [float(item) for item in weather_data] 
    minimum_val = weather_data[0] 
    min_index = 0                   
    
    for i in range(1, len(weather_data)):
        if weather_data[i] < minimum_val:
            minimum_val = weather_data[i]
            min_index = i
        elif weather_data[i] == minimum_val:
            min_index = i
    
    return minimum_val, min_index
            

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    weather_data = [float(item) for item in weather_data]
    max_val = weather_data[0]
    max_index = 0

    for i in range(1, len(weather_data)):
        if weather_data[i] >= max_val:  
            max_val = weather_data[i]
            max_index = i

    return max_val, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    max_temp = []
    min_temp = []
    date = []

    for row in weather_data:
        max_temp.append(row[2])
        min_temp.append(row[1])
        date.append(row[0])
        length_of_list = len(weather_data)

        for date_row in date:
            max_temp_value = find_max(max_temp)[0]
            min_temp_value = find_min(min_temp)[0]
            min_temp_date = date[find_min(min_temp)[1]]
            formatted_min_temp_date = convert_date(min_temp_date)
            min_temp_celcium = convert_f_to_c(min_temp_value)
            max_temp_date = date[find_max(max_temp)[1]]
            formatted_max_temp_date = convert_date(max_temp_date)
            max_temp_celcium = convert_f_to_c(max_temp_value)
            min_mean_value = calculate_mean(min_temp)
            min_mean_celcium = convert_f_to_c(min_mean_value)
            max_mean_value = calculate_mean(max_temp)
            max_mean_celcium = convert_f_to_c(max_mean_value)
            summary = f'{length_of_list} Day Overview\n  The lowest temperature will be {format_temperature(min_temp_celcium)}, and will occur on {formatted_min_temp_date}.\n  The highest temperature will be {format_temperature(max_temp_celcium)}, and will occur on {formatted_max_temp_date}.\n  The average low this week is {format_temperature(min_mean_celcium)}.\n  The average high this week is {format_temperature(max_mean_celcium)}.\n'

    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary = []

    for row in weather_data:
        date = convert_date(row [0])
        min_temp = row[1]
        min_temp_celcium = convert_f_to_c(min_temp)
        max_temp = row[2]
        max_temp_celcium = convert_f_to_c(max_temp)
        summary = f'---- {date} ----\n  Minimum Temperature: {min_temp_celcium}°C\n  Maximum Temperature: {max_temp_celcium}°C'
        daily_summary.append(summary)

    return "\n\n".join(daily_summary) + "\n\n"

