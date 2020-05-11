# TEAM NAME:
# TEAM NUMBER:
# PARTICIPANT NAMES:

# SOURCE CODE
# 2019 - Climatology - Weather Analyzer
# DIVISION B/C

''' INSTRUCTIONS

SCENARIO: Climatology - Weather Analyzer
DESCRIPTION: Analyzing historic climate data can be used to generate trends, and predict future weather in specific areas.
Your tasks will inlcude solving problems related to the weather. During the test, you will be asked to load daily weather
statistics from JAN 1, 1960 to APR 1, 2019 for the Detroit Metro Airport weather station and answer questions based on that data set. Your code
will be tested against a similar data set from Chicago OHare Airport.
Climate data taken from https://www.ncdc.noaa.gov/cdo-web/

1. TASK: For each question, write your code to solve each objective. (return the answer programmatically. ie. via variables)
2. TOTAL POINTS: 103
3. WINNER: High Score
4. TIE BREAKER: Question 18. If there is still a tie, question 17, 16 and so on will break the tie.

TIPS: 
* Some questions may ask you to call functions from previous questions.
* The main function (at bottom) will call and run all of the questions and print the answers. Do not modify this function.
* Programs that do not run/compile will not be eligible to receive full points as determined by the Source Code rules.
* Run your program often to test and check for errors.

INFORMATION: The majority of questions will use a list of dictionaries (weather) which you will load from a file 
in one of the questions. Each line of the file will represent weather attributes for one day. The structure for each
day (dictionary( is listed below: 

[
    {
        'DATE':'1960-01-01',     # (STRING) Date in format year-month-day 
        'TAVG':-4.8,             # (NUMBER) Average Temperature (celsius)
        'TMAX':1.1,              # (NUMBER) Maximum Temperature (celsis us)
        'TMIN':-10.6,            # (NUMBER) Minimum Temperature (celsisus)
        'PRCP':0.0,              # (NUMBER) Percipitation Total (millimeters)
        'SNOW':0.0,              # (NUMBER) Snow Fall Total (millimeters)
        'SNWD':25.0,             # (NUMBER) Snow Depth (millimeters)
        'AWND':0,                # (NUMBER) Average Wind Speed (meters per second))
    },
    ...
]

GOOD LUCK! '''

# QUESTION 0: WEATHER TEAM NAME
# OBJECTIVE A (2): Build a string for the name of your weather team. 
# Include your school name followed by any text you like. Append the 
# parameter date to the end of your string. Return the string.
# Output example: Bath High School Weather Warriors 04/27/2019
def getName(date):
    
    return ''

# QUESTION 1: AVERAGE CALCULATOR
# OBJECTIVE A (2): A list of numbers is passed into the function below. Calculate
# the average of the numbers and return the result.
#OBJECTIVE B (2): Format/round the number to two decimal places.
def getAverage(numbers):
    total = 0;

    return total

# QUESTION 2: CELSISUS TO FAHRENHEIT CONVERSION
# OBJECTIVE A (2): A number temp, is passed into the function below
# representing a temperature. If the other parameter conversion equals 'F'
# convert the temperature from Celsius to Fahrenheit.
# OBJECTIVE B (2): If conversion equals 'C' convert the temperature from
# Fahrenheit to Celisus.
# OBJECTIVE C (2) If conversion equals neither 'F' or 'C' return None (Python's null type)
# Do not round.
def convertTemp(temp, conversion):
    
    return ''
    
# QUESTION 3: DATE COMPARATOR
# OBJECTIVE A (2): Two dates are passed into the function below.
# Import the datetime library. If date1 is before date2 return -1.
# OBJECTIVE B (2): If date1 equals date2 return 0.
# OBJECTIVE C (2): If date1 is after date2 return 1.
def compareDates(date1, date2):

    return ''

# QUESTION 4: LOAD WEATHER DATA
# OBJECTIVE A (4): Using the given text file name, where each line represents
# a dictionary containing weather data for one day, convert each line to a 
# dictionary and add the dictionary as an item in the list weather. The count
# of items in the list will be output. (It should be 21641).
# The resulting list of this function will be used in later questions.
# HINT: Uncomment the JSON library that has been imported. For each line in the file, it
# can be converted to a dictionary with the code: json.loads(line)
def loadWeatherData(fileName):
    #import json
    #json.loads(line)
    weather = []

    return weather

# QUESTION 5: RETURN THE WEATHER
# OBJECTIVE A (5): Using the data set, weather, passed into the function below,
# find the dictionary in the weather list for the date given by the parameter date. 
# (format is year-month-day YYYY-mm-dd). Return the dictionary
def getWeather(weather, date):

    return ''

# QUESTION 6: AVERAGE TEMP 1960 - 2019
# OBJECTIVE A (4): Using the data set you loaded in question 4, which is passed into the
# function below as the parameter, weather, calculate and return the average temperature
# for the entire data set. (ie. Detroit Metro's average temperature) Do not round. 
# Use the dictionary keys in the instructions to determine what each value means.
def getAverageTemperature(weather):
    total = 0;

    return total

# QUESTION 7: TOTAL PERCIPITATION FOR A YEAR
# OBJECTIVE A (5): Using the data set, weather, passed into the function below,
# calculate and return the total percipitation for the given year, year (a String).
# Do not round your answer.
# The data weather is ordered by date. Oldest to Newest
def getYearlyPercipitation(weather, year):
    total = 0;

    return total

# QUESTION 8: DAYS WITH SNOW
# OBJECTIVE A (5): Using the data set, weather, calculate how many days in the data 
# set had snow on the ground. Return the count.
# HINT: Use 'SNWD'
def getDaysWithSnow(weather):
    total = 0

    return total

# QUESTION 9: WINDY DAYS
# OBJECTIVE A (5): Using the data set, weather, find the days that had a
# wind speed greater than or equal to 12 meters per second. Add each date to a list and return
# the list of dates.
def getWindyDays(weather):
    days = []

    return days

# QUESTION 10: METRIC CONVERSION
# OBJECTIVE A (6): The below function accepts three parameters. number is a
# metric number. fromType is the unit of number. toType is the metric unit
# you are converting to. This function should be able to handle
# units (mm,cm,dcm,m,dkm,hm,km) Return the reuslt. Do not round.
def convertMetric(number, fromType, toType):

    return ''

# QUESTION 11: HIGHEST SNOW FALL YEAR
# OBJECTIVE A (7): Using the data set, weather, passed into the function below,
# determine which year had the highest snowfall (using 'SNOW' per day). If 2 or
# more years have the same, return both years in a last. Otherwise return the 
# highest year as the first index of a list.
def getHighestSnowFallYear(weather):
    highestYears = []
    
    return highestYears

# QUESTION 12: HIGHEST AVERAGE TEMP
# OBJECTIVE A (6): Using the data set, weather, determine which year since
# 1960 had the highest average temperature. Return multiple if two or more 
# years had the same amount. Put each year in an index of a list and return
# the list.
# HINT: Some years have 366 days.
def getHighestAverageTemp(weather):
    highestYears = []

    return highestYears

# QUESTION 13: TEMPERATURE RANGE
# OBJECTIVE A (6): Given the data set weather, count how many days had a temperature
# range greater than or equal to 15 celsius (min to max) return the count
def getTempRangeCount(weather):
    total = 0

    return total

# QUESTION 14: TOTAL PERCIPITATION
# OBJECTIVE A (6): Given a start date, end date, and the weather
# data set, calculate the total percipiation between and including
# the dates.
# OBJECTIVE B (2): Round your answer to the nearest whole number.
def getTotalPercipitation(startDate, endDate, weather):
    total = 0.0
      
    return total

# QUESTION 15: THE RIGHT CONDITIONS
# OBJECTIVE A (7): Using the data set, weather, count how many days
# meet the following criteria: Wind Speed  = 0, Average Temperature is above 
# 20, percipitation = 0 and the date is a Friday. Return the count.
def getTheRightConditionsCount(weather):
    total = 0;

    return total

# QUESTION 16: PERFECT SQUARE AVERAGE TEMPS
# OBJECTIVE A (7): A perfect square is the product of two equal integers.
# For every day in the weather data, determine how many days had an
# average temperature that was a perfect square.
def getPerfectSqaures(weather):
    total = 0

    return total

# QUESTION 17: MEDIAN SNOW DEPTH
# OBJECTIVE A (8): Given a start date and end date parameter,
# and the weather data,
# calculate the median snow depth for the days between and including
# the given dates.
def getMedianSnowDepth(startDate, endDate, weather):
            
    return ''
    
    
# QUESTION 18: FREESTYLE
# OBJECTIVE A (2): Using the weather data, calculate a statistic that has 
# not already been calculated in the before questions. Return the result.
# OBJECTIVE B (1): Write at least 2 lines of comments explaining the function.
# OBJECTIVE C (1): Do not use any math/statistical analysis libraries.
def freestyle(weather):
    
    return ''

###############################
# MAIN FUNCTION
# NOTE: It is in your best interest to not modify values in this function.
# Input for the programming questions is test data. The supervisor will use 
# different values to grade your program.
###############################
def main():
    
    # Print Question Answer
    print('Source Code (MAIN) - Division B/C - Climatology - Weather Analyzer')
    
    print('QUESTION 0 A (2): '+getName('04/27/2019'))
    print('QUESTION 1 A (2): '+str(getAverage([10,12.5,-1.34,11,22.23456,7,-9.3,1.113])))
    print('QUESTION 1 B (2): '+str(getAverage([10,12.5,-1.34,11,22.23456,7,-9.3,1.113])))
    print('QUESTION 2 A (2): '+str(convertTemp(33, 'F')))
    print('QUESTION 2 B (2): '+str(convertTemp(127, 'C')))
    print('QUESTION 2 C (2): '+str(convertTemp(33, 'Z'))) 
    print('QUESTION 3 A (2): '+str(compareDates('2018-04-28', '2019-04-27')))  
    print('QUESTION 3 B (2): '+str(compareDates('2019-04-27', '2019-04-27'))) 
    print('QUESTION 3 C (2): '+str(compareDates('2019-05-27', '2019-04-27')))        
    
    # List containing weather information per day since 1960
    weather = loadWeatherData('DetroitMetroData.txt')
    print('QUESTION 4 A (4): '+str(len(weather)))
    print('QUESTION 5 A (4): '+str(getWeather(weather, '1977-07-07')))
    print('QUESTION 6 A (4): '+str(getAverageTemperature(weather)))
    print('QUESTION 7 A (5): '+str(getYearlyPercipitation(weather, '1976')))
    print('QUESTION 8 A (5): '+str(getDaysWithSnow(weather)))
    print('QUESTION 9 A (5): '+str(getWindyDays(weather))) 
    print('QUESTION 10 A (6): '+str(convertMetric(437.377, 'km', 'cm')))
    print('QUESTION 11 A (6): '+str(getHighestSnowFallYear(weather)))
    print('QUESTION 12 A (6): '+str(getHighestAverageTemp(weather)))
    print('QUESTION 13 A (6): '+str(getTempRangeCount(weather)))

    print('QUESTION 14 A (6): '+str(getTotalPercipitation('1990-03-02', '1994-05-10', weather)))
    print('QUESTION 14 B (2): '+str(getTotalPercipitation('1990-03-02', '1994-05-10', weather)))
    
    print('QUESTION 15 A (7): '+str(getTheRightConditionsCount(weather)))
    print('QUESTION 16 A (7): '+str(getPerfectSqaures(weather))) 
    print('QUESTION 17 A (8): '+str(getMedianSnowDepth('2008-12-01', '2009-03-01', weather)))
   
    print('QUESTION 18 A (2): '+str(freestyle(weather))) 
    print('QUESTION 18 B (1): '+'')
    print('QUESTION 18 C (1): '+'')

main()