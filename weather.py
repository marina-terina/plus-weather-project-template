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

#print(format_temperature(120))


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

#print(convert_date("2021-07-05T07:00:00+08:00"))

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

#print(convert_f_to_c(49))

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # weather_data = [float(item)]
    # # for item in weather_data:
        
    # total = sum(weather_data)
    # mean_value = total / len(weather_data)
    
    # return mean_value
    weather_data = [float(item) for item in weather_data]

    total = sum(weather_data)  # Calculate the sum of the list
    mean_value = total / len(weather_data)  # Calculate the mean value

    return mean_value

#print(calculate_mean([10, 20, 30, 40]))



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
        next(reader, None)    #skip the header??? 
        for row in reader:
            if row:
                row[1] = int(row[1])  
                row[2] = int(row[2])  
                data.append(row)
    return data
                
        
print(load_data_from_csv('tests/data/example_one.csv'))

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()  # Return an empty tuple for an empty list
    weather_data = [float(item) for item in weather_data] # Convert all inputs to float
    minimum_val = weather_data[0] #set the min value for the first element (list count starts with 0)
    min_index = 0                    #index 

    for i in range(1, len(weather_data)):
        if weather_data[i] < minimum_val:
            minimum_val = weather_data[i]
            min_index = i
        elif weather_data[i] == minimum_val:
            min_index = i
    
    return minimum_val, min_index
            

#print(find_min([1,2,3]))

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
    print(f'this is weather_data --> {weather_data}')
    max_temp = []
    min_temp = []
    date = []
    for row in weather_data:
        #print(row)
        max_temp.append(row[2])
        min_temp.append(row[1])
        date.append(row[0])
        length_of_list = len(weather_data)
        #print(f'-----> this is lenght of list{length_of_list}')
        #print(f'----> this is date row {date}')
        #print(type(date))
        for date_row in date:
            #print(f'----> this is a date row in date list{date_row}')
            
            #print(f'----> this is formatted date{formatted_date}')

            max_temp_value = find_max(max_temp)[0]
    
    # print(f'------> this is max_temp_date {max_temp_date}')
    # print(f'------>this is max temp {max_temp_value}')
        min_temp_value = find_min(min_temp)[0]
        #print(f'---->this is min temp{min_temp_value}') 
        min_temp_date = date[find_min(min_temp)[1]]
        formatted_min_temp_date = convert_date(min_temp_date)
        #print(f'----> this is formatted min_temp_data{formatted_min_temp_date}')
        min_temp_celcium = convert_f_to_c(min_temp_value)
        #print(f'--->this is the min temp in C {min_temp_celcium}')
    
    max_temp_date = date[find_max(max_temp)[1]]
    formatted_max_temp_date = convert_date(max_temp_date)
    max_temp_celcium = convert_f_to_c(max_temp_value)
    #print(f'---> this is max in C {max_temp_celcium}')
    #print(f'----> this is max min value {max_mean_value}')
    min_mean_value = calculate_mean(min_temp)
    #print(f'----> this is min mean value {min_mean_value}')
    min_mean_celcium = convert_f_to_c(min_mean_value)
    #print(f'---> this is mean min C {min_mean_celcium}')
    max_mean_value = calculate_mean(max_temp)
    
    max_mean_celcium = convert_f_to_c(max_mean_value)
    
    
    summary = f'{length_of_list} Day Overview\n  The lowest temperature will be {min_temp_celcium}°C, and will occur on {formatted_min_temp_date}.\n  The highest temperature will be {max_temp_celcium}°C, and will occur on {formatted_max_temp_date}.\n  The average low this week is {min_mean_celcium}°C.\n  The average high this week is {max_mean_celcium}°C.\n'

    return summary

print(generate_summary([
            ["2020-06-19T07:00:00+08:00", -47, -46],
            ["2020-06-20T07:00:00+08:00", -51, 67],
            ["2020-06-21T07:00:00+08:00", 58, 72],
            ["2020-06-22T07:00:00+08:00", 59, 71],
            ["2020-06-23T07:00:00+08:00", -52, 71],
            ["2020-06-24T07:00:00+08:00", 52, 67],
            ["2020-06-25T07:00:00+08:00", -48, 66],
            ["2020-06-26T07:00:00+08:00", 53, 66]
        ]))

            
            




def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #print(f'this is weather_data --> {weather_data}')
    daily_summary = []
    for row in weather_data:
        date = convert_date(row [0])
        min_temp = row[1]
        min_temp_celcium = convert_f_to_c(min_temp)
        max_temp = row[2]
        max_temp_celcium = convert_f_to_c(max_temp)
        summary = f'---- {date} ----\n  Minimum Temperature: {min_temp_celcium}°C\n  Maximum Temperature: {max_temp_celcium}°C\n\n'
        daily_summary.append(summary)

    return "".join(daily_summary).rstrip()

# print(generate_daily_summary([
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62]]))

