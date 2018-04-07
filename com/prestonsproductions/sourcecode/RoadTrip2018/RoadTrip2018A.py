# TEAM NAME:
# TEAM NUMBER:
# PARTICIPANT NAMES:

# SOURCE CODE
# 2018 - Road Trip - Travel Log
# DIVISION B/C

''' INSTRUCTIONS

SCENARIO: Road Trip - Travel Log
DESCRIPTION: There are many aspects of a road trip where software can be used to generate reports
or calculate statistics. One task is generating a travel Log. Each of the questions below will break
down this large task into smaller (more manageable) tasks. By completing the questions, you will be able
to generate a custom travel log. The main function will call your questions (using your logic) and
print out the travel log. Some of your questions may require you to call previous functions.

1. For each question, write your code to solve each objective. (return the answer programmatically. ie via variables)
2. Each objective is worth a designated number of points. 105 Points Total.
3. Highest number of points wins. Question 19 is a tie breaker. If there is still a tie, question 18, 17 and so on will break the tie.
4. The main function will call and run all of the questions and print the travel log. Do not modify this function.
5. Programs that do not run/compile will not be eligible to receive full points as determined by the Source Code rules.
6. Run your program often to test and check for errors.

INFORMATION: Many questions will deal with a list of dictionaries. Each item in the list (a dictionary) will contain
data about a city on the trip. An explanation of each field is below:
'NAME'        : name of the city
'DISTANCE'    : distance to reach that city (from the previous city)
'DURATION'    : the time it takes to reach that city (from the previous city)
'GASPRICE'    : the price of fuel per gallon in that city

GOOD LUCK! '''

# QUESTION 0: LOG TITLE
# OBJECTIVE A (2): A name, number, and date are passed into the function below. (All strings) 
# Return the name, number, and date concatenated, each separated by a space and hyphen. ex) "Log - 01 - 01/01/2018"
def getTravelLogTitle(name, number, date):
    
    return name + ' - ' + number + ' - ' + date

# QUESTION 1: DISTANCE BETWEEN
# OBJECTIVE A (2): Two distances, dist1 and dist2 are passed into the function below. (Both Numbers)
# Return the difference between dist2 and dist1.
# OBJECTIVE B (2): Make your function more versatile and return the absolute value of the difference so it
# does not matter what order the values are passed in.
def getDistanceBetween(dist1, dist2):
    
    return abs(dist2 -dist1)

# QUESTION 2: FUEL COST
# OBJECTIVE A (2): A distance (in miles) and a price (per gallon of fuel) and fuelmileage (miles the vehicle can go per gallon)
# are passed into the function below. Return the cost (a float 0.00) to go the given distance.
# OBJECTIVE B (2): Round the answer to the nearest cent.
def getFuelCost(distance, price, fuelmileage):
    
    return format((distance / fuelmileage) * price, '.2f')

# QUESTION 3: AVERAGE SPEED
# OBJECTIVE A (3): A distance (in miles) and a duration in minutes is passed into the function below. Calculate the average
# speed in miles per hour and return the answer. Do not round.
def getAverageSpeed(distance, duration):
    
    return distance / (duration / 60)

# QUESTION 4: FIRST CAPITAL
# OBJECTIVE A (3): The function below takes in a string. Characters in the string may be upper or lower case.
# Return the string with the first character capitalized and the rest lower case. Use string.lower and string.upper.
def firstCapital(s):
    s = s.lower() 
   
    return s[0].upper() + s[1:]

# QUESTION 5: CONVERT TO CENTS
# OBJECTIVE A (3): The function below takes in a number dollar amount (a float). Convert the number to cents and
# return the number as an INTEGER.
def getCents(money): 
    
    return int(money * 100)

# QUESTION 6: FUEL STOP
# OBJECTIVE A (4): Before we travel to the next city, we need to make sure we have enough fuel to get there. Calculate 
# how much fuel is needed to get to the next city with the parameters nextdistance (miles) and fuelmileage (miles our vehicle 
# can travel per gallon). Compare that value with parameter currentfuel (gallons). Return False if we have more fuel than
# needed for the distance. If our current fuel exactly equals the fuel needed, return True. (We still need fuel to get to
# the gas station.)
def isFuelNeeded(currentfuel, nextdistance, fuelmileage):
    neededfuel = nextdistance / fuelmileage;
    if (neededfuel < currentfuel): return False
    return True

# QUESTION 7: PRIME NUMBERS
# OBJECTIVE A (4): A number is passed into this function. Determine if it is a prime number. Return True is the number is prime
# otherwise return False
def isPrimeNumber(nbr):
    for i in range(2, nbr):
        if (nbr % i == 0): return False
    return True

# QUESTION 8: UNIT CONVERTER
# OBJECTIVE A (4): The function below takes in three parameters. A value (a number) , a from unit and to unit. Write
# your code to convert the value from miles to kilometers or kilometers to miles based on the supplied parameters.
# Possible values for fromUnit and toUnity are: MILES = 'MI', KILOMETERS = 'KM'
# OBJECTIVE B (2): Return -1 if the conversion cannot be calculated.
def convertUnits(value, fromUnit, toUnit):
    if (fromUnit == 'MI'):
        if (toUnit == 'KM'):
            return value / .62 
    elif(fromUnit == 'KM'):
        if (toUnit == 'MI'):
            return value * .62 
    return -1

# QUESTION 9: TOTAL DISTANCE
# OBJECTIVE A (4): A list of trip data is passed into the function below (see comments for structure of each item).
# Each key (a city) in the dictionary has a dictionary as the value containing travel data. 
# 'DISTANCE' (to the city), 'TIME' (to the city), 'GASPRICE' (in the city), etc. Calculate the sum of the distances.
# HINT: Loop through the dictionary for each city and get the distance city['DISTANCE']
def getTotalDistance(tripdata):
    total = 0
    for city in tripdata:
        total += city['DISTANCE']
    return total

# QUESTION 10: SHORTEST TRIP
# OBJECTIVE A (5): Two different lists of 'tripdata' are passed into the function below. Determine which list has the shorter
# total distance. Call your function getTotalDistance from question 6 to determine a trips total distance. Return a list with 
# the first city name, last city name, and difference in miles of the two trips.
# OBJECTIVE B (2): If the trips are the same length, return an empty list.
def getShortestTrip(tripdata1, tripdata2):
    cities = []
    trip1 = getTotalDistance(tripdata1)
    trip2 = getTotalDistance(tripdata2)
    if (trip1 > trip2):
        cities.append(tripdata2[0]['NAME'])
        cities.append(tripdata2[len(tripdata2)-1]['NAME'])
        cities.append(trip1-trip2)
    elif (trip1 < trip2):
        cities.append(tripdata1[0]['NAME'])
        cities.append(tripdata1[len(tripdata1)-1]['NAME'])
        cities.append(trip2-trip1)
        
    return cities

# QUESTION 11: FASTEST SPEED
# OBJECTIVE A (5): The tripdata list is passed into the function below. Calculate the  average speed of the trip (MPH) between each 
# city and return the two cities in a list where the speed was the fastest. Use the getAverageSpeed function to calculate
# the speed
def getFastestSpeed(tripdata):
    cities = []
    fastest = 0
    count = 0
    for city in tripdata:
        if (count > 0):
            tmp = getAverageSpeed(city['DISTANCE'], city['DURATION'])
            if (tmp > fastest):
                fastest = tmp
                cities = [city['NAME'], tripdata[count-1]['NAME']]
        count += 1
    return cities

# QUESTION 12: TOTAL AVERAGE SPEED
# OBJECTIVE A (4): Trip data is passed into the function below. Using your function from question 3 'getAverageSpeed',
# Calculate the average speed for the entire trip. (Skip the first city as this is where we start). Return the speed.
# OBJECTIVE B (2): Add a condition to return -1 if the size of trip data is less than or equal to 1.
def getTotalAverageSpeed(tripdata):
    speed = 0
    cities = 0
    if (len(tripdata) <= 1): return -1
    for city in tripdata:
        if (cities > 0):
            speed += getAverageSpeed(city['DISTANCE'], city['DURATION'])
        cities += 1
    return speed / cities-1

# QUESTION 13: DISTANT CITIES
# OBJECTIVE A (4): The list of trip data is again passed into the function.
# Return a LIST of city names where the DURATION to them was greater than 50 minutes.
# OBJECTUVE B (2): Return the list sorted alphabetically.
def getDistantCities(tripdata):
    cities = []
    for city in tripdata:
        if (city['DURATION'] > 50):
            cities.append(city['NAME'])
    cities.sort()
    return cities

# QUESTION 14: LANDMARKS
# OBJECTIVE A (5): A landmark is an object between two cities. There could be multiple landmarks between
# two cities. Below, the names of two cities are passed into the function. The third parameter 'landmarks'
# is a list of tuples with structure: (landmark name, first city name, second city name). First city an second
# city are the cities the landmark is between. Return a list of landmark names between the first city and second city.
def getLandMarks(firstcity, secondcity, landmarks):
    items = []
    for i in landmarks:
        if (i[1] == firstcity and i[2] == secondcity):
            items.append(i[0])
    return items

# QUESTION 15: LANDMARKS SEEN
# OBJECTIVE A (5): The trip data list and landmark list are passed into the function below. Count how many landmarks
# are seen throughout the trip and return the number. Use the function getLandMarks from question 8 to determine if
# landmarks exist between two cities. (size of the list indicates how many landmarks between cities.
#
def getLandMarksSeen(tripdata, landmarks):
    count = 0
    cities = 0
    for city in tripdata:
        if (cities < len(tripdata)-1):
            count += len(getLandMarks(city['NAME'], tripdata[cities+1]['NAME'], landmarks))
        cities += 1
    return count

# QUESTION 16: STANDARD DEVIATION - GAS PRICES
# OBJECTIVE A (8): Calculate the population standard deviation of the gas prices based on the trip data 
# passed into the function. Use the following algorithm to calculate and return the correct value:
# 1. Calculate the Average of the GASRICES.
# 2. Calculate the deviations of each Gas Price by the formula:
#    deviation = (GASPRICE - AVERAGE) * (GASPRICE - AVERAGE)
# 3. Calculate the average of the deviations values. This is the variance.
# 4. Finally, return the square root of the variance. This is the population standard deviation.
def getFuelStandardDeviation(tripdata):
    import math
    variance = 0
    count = 0
    avg = 0
    for city in tripdata:
        avg += city['GASPRICE']
        count += 1
    avg = avg / count
    
    for city in tripdata: 
        variance += (city['GASPRICE'] - avg)**2
        
    return math.sqrt((variance / count))

# QUESTION 17: TOTAL FUEL PRICE
# OBJECTIVE A (4): A dictionary of trip data is passed into the function below. Using the 'isFuelNeeded' function 
# from Question 3, calculate how much money will be needed for fuel for the entire trip. Your vehicle holds 20 gallons
# of fuel and can go 24 miles per gallon. You must fill up the tank each time you need fuel. 
# OBJECTIVE B (2): The cities 'Grand Rapids' and 'Alpena' give a $0.50 discount on fuel per gallon if you traveled 
# more than 20 miles from your previous city.
# OBJECTIVE C (2): The cities 'Detroit' and 'Saginaw' give a $0.25 discount on fuel per gallon if your trip from the
# previous city took more than 20 minutes.
def getTotalFuelCost(tripdata):
    total = 0.00
    currentfuel = 20
    citynbr = 0
    for city in tripdata:
        if (citynbr < len(tripdata)-1):
            if isFuelNeeded(currentfuel, tripdata[citynbr+1]['DISTANCE'], 24):
                if (('Grand Rapids'==city['NAME'] or 'Alpena'==city['NAME']) and tripdata[citynbr]['DISTANCE'] > 20):
                    total =+ (city['GASPRICE']-.50) * 20
                elif (('Detroit'==city['NAME'] or 'Saginaw'==city['NAME']) and tripdata[citynbr]['DURATION'] > 20):
                    total =+ (city['GASPRICE']-.25) * 20 
                else:
                    total += city['GASPRICE'] * 20 
                currentfuel = 20
            currentfuel -= tripdata[citynbr+1]['DISTANCE'] / 24
        citynbr += 1
    return total

# QUESTION 18: MEDIAN DISTANCE
# OBJECTIVE A (8): The median is the middle number in a set. If there is an even amount of
# numbers, you average the two middle numbers. Find the Median Distance in the travel data
# and return the median distance. Assume more than 1 city will be in tripdata.
# HINT: Sort the list using the key parameter. Use the function getDistance as the key value.  
# Use Integer Division when searching for the middle index.
def getMedianDistance(tripdata):
    median = 0
    tripdata.sort(key=getDistance)
    if (len(tripdata) % 2 != 0):
        median = tripdata[len(tripdata)//2]['DISTANCE']
    else:
        median = (tripdata[len(tripdata)//2]['DISTANCE'] + tripdata[(len(tripdata)//2)-1]['DISTANCE']) / 2
    return median

def getDistance(city):
    return city['DISTANCE']

# QUESTION 19: FREE STYLE
# OBJECTIVE A (4): Write a custom function that calculates a statistic with the tripdata and returns a string
# OBJECTIVE B (2): Write a comment that explains what statistic you are calculating.
# OBJECTIVE C (2): Call a previous function within your calculation.
# Objective D (2): Import a library within the function.
def getStatistic(tripdata):
    x = 0

    return x

###############################
# MAIN FUNCTION
# NOTE: It is in your best interest to not modify values in this function.
# Input for the programming questions is test data. The supervisor will use 
# different values to grade your program.
###############################
def main():
    # Trip Data
    tripdata = [{'NAME':'Bath', 'DISTANCE':0, 'DURATION':0, 'GASPRICE':2.51},
                {'NAME':'Lansing', 'DISTANCE':10, 'DURATION':12, 'GASPRICE':2.50}, 
                {'NAME':'Detroit', 'DISTANCE':150, 'DURATION':43, 'GASPRICE':2.60}, 
                {'NAME':'Saginaw', 'DISTANCE':100, 'DURATION':51, 'GASPRICE':2.60},
                {'NAME':'Alpena', 'DISTANCE':219, 'DURATION':89, 'GASPRICE':3.10},
                {'NAME':'Albion', 'DISTANCE':300, 'DURATION':70, 'GASPRICE':2.80},
                {'NAME':'Muskegon', 'DISTANCE':140, 'DURATION':80, 'GASPRICE':2.99},
                {'NAME':'Traverse City', 'DISTANCE':50, 'DURATION':50, 'GASPRICE':3.14},
                {'NAME':'Kalamazoo', 'DISTANCE':120, 'DURATION':50, 'GASPRICE':3.00},
                {'NAME':'Jackson', 'DISTANCE':43, 'DURATION':45, 'GASPRICE':2.78},
                {'NAME':'Marshall', 'DISTANCE':32, 'DURATION':33, 'GASPRICE':2.78},
                {'NAME':'Three Rivers', 'DISTANCE':51, 'DURATION':59, 'GASPRICE':2.75},
                {'NAME':'Holland', 'DISTANCE':74, 'DURATION':84, 'GASPRICE':3.05},
                {'NAME':'Ludington', 'DISTANCE':102, 'DURATION':104, 'GASPRICE':3.25},
                {'NAME':'Cadillac', 'DISTANCE':71, 'DURATION':84, 'GASPRICE':3.01},
                {'NAME':'Mount Pleasant', 'DISTANCE':65, 'DURATION':65, 'GASPRICE':2.99},
                {'NAME':'Flint', 'DISTANCE':90, 'DURATION':87, 'GASPRICE':2.59},
                {'NAME':'Clio', 'DISTANCE':15, 'DURATION':18, 'GASPRICE':2.66},
                ]
    
    tripdata2 = [{'NAME':'Bath', 'DISTANCE':0, 'DURATION':0, 'GASPRICE':2.51},                 
                {'NAME':'Detroit', 'DISTANCE':130, 'DURATION':43, 'GASPRICE':2.60},
                {'NAME':'Jackson', 'DISTANCE':43, 'DURATION':45, 'GASPRICE':2.78}, 
                {'NAME':'Saginaw', 'DISTANCE':100, 'DURATION':51, 'GASPRICE':2.60},
                {'NAME':'Muskegon', 'DISTANCE':200, 'DURATION':80, 'GASPRICE':2.99},
                {'NAME':'Alpena', 'DISTANCE':160, 'DURATION':89, 'GASPRICE':3.10},
                {'NAME':'Albion', 'DISTANCE':300, 'DURATION':70, 'GASPRICE':2.80},
                {'NAME':'Lansing', 'DISTANCE':10, 'DURATION':12, 'GASPRICE':2.50},                
                {'NAME':'Traverse City', 'DISTANCE':109, 'DURATION':50, 'GASPRICE':3.14},
                {'NAME':'Kalamazoo', 'DISTANCE':22, 'DURATION':50, 'GASPRICE':3.00},
                {'NAME':'Ann Arbor', 'DISTANCE':98, 'DURATION':92, 'GASPRICE':3.10},
                {'NAME':'Brighton', 'DISTANCE':19, 'DURATION':24, 'GASPRICE':2.96},
                {'NAME':'Flint', 'DISTANCE':38, 'DURATION':36, 'GASPRICE':2.99},
                {'NAME':'Bay City', 'DISTANCE':50, 'DURATION':45, 'GASPRICE':2.89},
                {'NAME':'Tawas City', 'DISTANCE':69, 'DURATION':70, 'GASPRICE':2.89},
                {'NAME':'Mackinaw City', 'DISTANCE':165, 'DURATION':152, 'GASPRICE':3.30},
                {'NAME':'St. Ignace', 'DISTANCE':12, 'DURATION':25, 'GASPRICE':3.20},
                {'NAME':'Sault Ste Marie', 'DISTANCE':60, 'DURATION':56, 'GASPRICE':3.44},
                ]
    
    landmarks = [('Blue Chair','Alpena','Lansing'),
                 ('Tallest Sign','Alpena','Albion'),
                 ('Waffle House','Detroit','Jackson'),
                 ('Candy Factory','Kalamazoo','Grand Rapids'),
                 ('Pencil Factory','Jackson','Lansing'),
                 ('Michigan\'s Smallest House','Alpena','Albion'),
                 ('Famous Steve''s','Kalamazoo','Jackson'),
                 ('Mystery Spot','Mackinaw City','Sault Ste Marie'),
                 ('The Big Tire','Ann Arbor','Detroit'),
                 ('I94 Scenic View','Jackson','Marshall'),
                 ('Sky Resort','Ludington','Traverse City'),
                 ('The Bay Bridge','Bay City','Saginaw'),
                 ('Nothing','Bath','St. Johns'),
                 ('Nothing','Flint','Clio'),
                ]
    
    # Print Question Answer
    print('Source Code (MAIN) - Division B/C - Road Trip - Travel Log')
    
    print('QUESTION 0 A (2): '+getTravelLogTitle('The Source Code Travel Log', '10001', '03/03/2018')) # The Source Code Travel Log - 10001 - 03/03/2018
    
    print('QUESTION 1 A (2): '+str(getDistanceBetween(800,600))) # 200 or -200
    print('QUESTION 1 B (2): '+str(getDistanceBetween(600,800))) # 200
    
    print('QUESTION 2 A (2): '+str(getFuelCost(501,2.59,24))) # 54.07 or 54.07777777
    print('QUESTION 2 B (2): '+str(getFuelCost(501,2.59,24))) # 54.07
    
    print('QUESTION 3 A (3): '+str(getAverageSpeed(600, 500))) # 72.0
    
    print('QUESTION 4 A (3): '+str(firstCapital('sAGINaW'))) # Saginaw
    
    print('QUESTION 5 A (3): '+str(getCents(1.377))) # 137
    
    print('QUESTION 6 A (4): '+str(isFuelNeeded(20, 479, 24)) + ', ' + str(isFuelNeeded(15, 600, 24))) # False, True
    
    print('QUESTION 7 A (4): '+str(isPrimeNumber(199)) +', ' + str(isPrimeNumber(8335))) # True, False
    
    print('QUESTION 8 A (4): '+str(convertUnits(20, 'MI','KM'))) # 32.25806451612903
    print('QUESTION 8 B (2): '+str(convertUnits(20, 'MI','CE'))) # -1
    
    print('QUESTION 9 A (4): '+str(getTotalDistance(tripdata))) # 1632
    
    print('QUESTION 10 A (5): '+str(getShortestTrip(tripdata,tripdata2))) # ['Bath', 'Sault Ste Marie', 47]
    print('QUESTION 10 B (2): '+str(getShortestTrip(tripdata2,tripdata2))) # []
    
    print('QUESTION 11 A (5): '+str(getFastestSpeed(tripdata))) # ['Albion', 'Alpena']
    
    print('QUESTION 12 A (4): '+str(getTotalAverageSpeed(tripdata))) # 87.47771095642337
    print('QUESTION 12 B (2): '+str(getTotalAverageSpeed([]))) # -1
    
    print('QUESTION 13 A (4): '+str(getDistantCities(tripdata))) # ['Albion', 'Alpena', 'Cadillac', 'Flint', 'Holland', 'Ludington', 'Mount Pleasant', 'Muskegon', 'Saginaw', 'Three Rivers']
    print('QUESTION 13 B (2): '+str(getDistantCities(tripdata))) # ['Albion', 'Alpena', 'Cadillac', 'Flint', 'Holland', 'Ludington', 'Mount Pleasant', 'Muskegon', 'Saginaw', 'Three Rivers']
    
    print('QUESTION 14 A (5): '+str(getLandMarks('Alpena','Albion', landmarks))) # ['Tallest Sign', "Michigan's Smallest House"]
    
    print('QUESTION 15 A (5): '+str(getLandMarksSeen(tripdata, landmarks))) # 5
     
    print('QUESTION 16 A (8): '+str(getFuelStandardDeviation(tripdata))) # 0.22617321014579586
    
    print('QUESTION 17 A (8): '+str(getTotalFuelCost(tripdata))) # 176.8
    
    print('QUESTION 18 A (8): '+str(getMedianDistance(tripdata))) # 72.5
      
    print('QUESTION 19 A (4): '+str(getStatistic(tripdata))) # Check for Answer
    print('QUESTION 19 A (2): '+'Check for comment explaining function.')
    print('QUESTION 19 A (2): '+'Check if previous function in file was called.')
    print('QUESTION 19 A (2): '+'Check if import statement was used.')

    # Print Trip Log
    
#main()