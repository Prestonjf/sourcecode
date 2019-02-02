# TEAM NAME:
# TEAM NUMBER:
# PARTICIPANT NAMES:

# SOURCE CODE
# 2019 - Theme Park - Park Builder
# DIVISION B/C

''' INSTRUCTIONS

SCENARIO: Theme Park - Park Builder
DESCRIPTION: You have inherited a large piece of land, a large sum of money, and have decided to 
build a theme park! The functions below will simulate tasks and calculations needed to build the
optimal park. Optimal meaning, generating the largest profit based on the size of your land, 
available funds, and list of rides and attractions you can build. Note: Sizes and values are not to scale.

1. For each question, write your code to solve each objective. (return the answer programmatically. ie via variables)
2. Each objective is worth a designated number of points. 74 Points Total.
3. Highest number of points wins. Question 15 is a tie breaker. If there is still a tie, question 14, 13 and so on will break the tie.
4. The main function will call and run all of the question objectives and print the answers. Do not modify this function.
5. Programs that do not run/compile will not be eligible to receive full points as determined by the Source Code rules.
6. Run your program often to test and check for errors. View the main function to see what values are passed as parameters.

INFORMATION: Some questions will use a list of dictionaries. Each dictionary will represent a ride or attraction.
The structure will be:
[ 
    {
        'TYPE':'Roller Coaster',       # Type of ride/attraction (String)
        'SUBTYPE':'Hyper Coaster',     # SubType of the ride/attraction (String)
        'COST':2000,                   # Cost (in dollars) to build (Number)
        'SIZE':100,                    # Size (in Square Feet) required to build (Number)
        'CAPACITY':50,                 # How many park guests can use the ride/attraction per hour (Number)
        'PROFIT':5,                    # Profit (in dollars) per guest using the ride/attraction (Number)
        'FUNRATING':10                 # A 'fun' rating where 1 is the lowest and 10 is highest. (Number)
    },
    ... 
] 

GOOD LUCK! '''

# QUESTION 0: THEME PARK NAME
# OBJECTIVE A (2): Create a name for your theme park which includes your team name
# and number and return the name from this function.
# ex) Bath High School 7 Wonderland
def getThemeParkName():
    
    return 'Bath High School 7 Wonderland'

# QUESTION 1: RIDE DESCRIPTION
# OBJECTIVE A (2): Three parameters are passed into the function below. 
# A String, String, and Number (rideType, name, funrating). Append the string together to return
# the ride description. ex) Roller Coaster - The Screaming Eagle - 10
def getRideDescription(rideType, name, funRating):
    
    return rideType + ' - ' + name + ' - ' + str(funRating)

# QUESTION 2: RIDE PRICE
# OBJECTIVE A (2): The total capacity (capacity) per hour and total
# profit (profit) per hour are passed into the function below. Calculate and return
# the price for one ride.
# OBJECTIVE B (2): Format the result into the following format: $0.00. 
# Rounded to the nearest hundredth.
def getRidePrice(capacity, profit):
    
    return '$' + format(profit / capacity,'.2f')

# QUESTION 3: DOES IT FIT?
# OBJECTIVE A (3): The function below has two parameters representing the
# total area (totalArea) and the area used (areaUsed). Determine if the 
# total area is still greater than the area used. If the total area is greater
# than the area used, return the difference between totalArea and areaUsed,
# otherwise return -1  
def isFit(totalArea, areaUsed):
    if (totalArea > areaUsed): return totalArea - areaUsed
    else: return -1
    
# QUESTION 4: RIDES AND ATTRACTION COUNT 
# OBJECTIVE A (3): A list of dictionaries (attractions) representing the rides
# and attractions data, as described above, is passed into the function below.
# count how many items are in the list and return the number.
def getAttractionsCount(attractions):

    return len(attractions)

# QUESTION 5: RIDES AND ATTRACTION COUNT ORGANIZED
# OBJECTIVE A (4): Again, the list of attractions is passed into the function
# below. Count how many attractions of each TYPE there are, and return the counts
# in a dictionary. ex): {'Roller Coaster':2, 'Thrill Ride':2...}
def getAttractionsCountOrganized(attractions):
    counts = {}
    for a in attractions:
        if a['TYPE'] in counts:
            counts[a['TYPE']] = counts[a['TYPE']] + 1
        else:
            counts[a['TYPE']] = 1
    return counts

# QUESTION 6: RIDE COST
# OBJECTIVE A (4): The list of attractions is passed into the function below as well as
# a subtype for a ride. Find the ride in the list and return the cost to build that ride.
# If the ride is not found, return 0
def getRideCost(subtype, attractions):
    for a in attractions:
        if a['SUBTYPE'] == subtype:
            return a['COST']
    return 0

# QUESTION 7: FUN RATING PERCENTAGE
# OBJECTIVE A (4): The list of attractions is passed in to the function below.
# What percentage of the attractions have a FUNRATING greater than 5. Do not count
# TYPEs of 'SHOP' in the calculations. Return the percentage.
# OBJECTIVE B (2): Round the percentage to the nearest hundredth, and return
# the value formated like: 76%
def getFunPercentage(attractions):
    count = 0
    ratingsAbove5 = 0
    for a in attractions:
        if a['TYPE'] != 'Shop':
            count += 1
            if a['FUNRATING'] > 5:
                ratingsAbove5 += 1
    return format(ratingsAbove5 / count * 100,'.0f') + '%'

# QUESTION 8: PROFIT VS COST
# OBJECTIVE A (5): Before your theme park is open, you want to determine what the best ride to 
# build is. That is, which ride has the highest profit to cost ratio. (profit divided by cost).
# Return the SUBTYPE, or SUBTYPEs of the attractions in a list. The list of attractions is passed
# into the function below.
def getProfitCostRatio(attractions):
    highest = 0
    rides = []
    for a in attractions:
        if a['PROFIT'] / a['COST'] > highest:
            highest = a['PROFIT'] / a['COST']
            rides = [a['SUBTYPE']]
        elif a['PROFIT'] / a['COST'] == highest:
            rides.append(a['SUBTYPE'])
    return rides

# QUESTION 9: FUN RATING 8 ANALYSIS
# OBJECTIVE A (5): If you were to build all rides and attractions with a FUNRATING of 8 
# (just once), and your park is open for 12 hours, what is the profit you would earn for
# one day. Use the list of attractions passed in to the function and return the total.
def getFunRating8Profit(attractions):
    total = 0
    for a in attractions:
        if a['FUNRATING'] == 8:
            total = a['PROFIT'] * 12
    return total

# QUESTION 10: REMAINING PROFIT
# OBJECTIVE A (5): Using the datetime library. The profit per hour for a ride
# is passed into the function below (profitPerHour). Closing time is 10:00PM. If the current
# time is between 10:00AM and 10:00PM, determine and return how much profit will be earned for
# the ride between now and closing time. Otherwise return 0. Do not round. Only consider hours and minutes.
def getRemainingProfit(profitPerHour):
    import datetime
    if ((datetime.datetime.now().hour >= 10) and (datetime.datetime.now().hour < 22)):
        totalHours = 22 - datetime.datetime.now().hour - 1
        totalMinutes = 60 - datetime.datetime.now().minute      
        return (totalHours * profitPerHour) + ((profitPerHour / 60) * totalMinutes)
    else: return 0
    
# QUESTION 11: MAX RIDES WITH FUNDS
# OBJECTIVE A (6): Given the list of rides and attractions (attractions) and a sum of money (funds)
# determine the maximum numbers of attractions you can build (without building any attraction twice).
# Return the number of rides/attractions. HINT: Make a new function to sort the attractions.
def getMaxNumberOfRides(attractions, funds):
    cost = 0
    count = 0
    attractions.sort(key=getAttractionCost)
    for a in attractions:
        if (cost + a['COST'] > funds):
            break
        else:
            cost += a['COST']
            count += 1
    return count
def getAttractionCost(a):
    return a['COST']

# QUESTION 12: AVG FUN RATING RIDES
# OBJECTIVE A (6): Given the list of rides and attractions (attractions), determine the average fun rating.
# Rounded to the nearest Integer. Do not consider TYPE of 'Shop'. Then find the rides with 
# that fun rating and count the number of letters in their SUBTYPE field. Return the total
# count of all the letters.
def getAvgFunCharacters(attractions):
    avg = 0
    count = 0
    totalChars = 0
    for a in attractions:
        if (a['TYPE'] != 'Shop'):
            count += 1
            avg += a['FUNRATING']
    avg = round(avg / count)
    for a in attractions:
        if (a['FUNRATING'] == avg):
            totalChars += len(a['SUBTYPE'])
    return totalChars

# QUESTION 13: I'M A THRILL RIDER
# OBJECTIVE A (6): A tourist goes to your theme park where you have only built rides
# of TYPE 'Thrill Ride'. The full list of attractions is passed into
# the function below, along with an amount of money (money) the tourist
# brings to the park. Determine and return the maximum number of thrill rides they can
# ride with their money. The tourist must ride each ride once, before they 
# can ride any rides again. (I.E. No ride can be ridden more than one time
# higher than any other ride. Price should be rounded to nearest cent per ride)
def getThrillRidesRidden(attractions, money):
    rides = []
    spent = 0
    count = 0
    complete = False
    for a in attractions:
        if a['TYPE'] == 'Thrill Ride':
            rides.append(a)
    rides.sort(key=getAttractionPrice)
    while spent < money:
        for r in rides:
            if (spent + round(r['PROFIT'] / r['CAPACITY'],2) <= money):       
                spent += round(r['PROFIT'] / r['CAPACITY'],2)
                count += 1
            else:
                complete = True
                break
        if complete:
            break
    return count
def getAttractionPrice(a):
    return round((a['PROFIT'] / a['CAPACITY']),2)

# QUESTION 14: THE BIGGEST PARK
# OBJECTIVE A (6): Given your list of attractions (attractions), area of land in square feet (area),
# determine the smallest number of rides you can build to fill up the park.
# Return the ride SUBTYPES in a list 
# OBJECTIVE A (2): Sort the Rides Alphabetically
def getTheBestPark(attractions, area):
    areaUsed = 0
    rides = []
    attractions.sort(key=getAttractionSize, reverse=True)
    for a in attractions:
        if (areaUsed + a['SIZE'] < area):
            areaUsed += a['SIZE']
            rides.append(a['SUBTYPE'])
            rides.sort()
    return rides
def getAttractionSize(a):
    return a['SIZE']

# QUESTION 15: THEME PARK FREESTYLE
# OBJECTIVE A (2): The function below has one parameter, attractions, which is a list of dictionaries. (as used earlier). 
# Write your own code to calculate a statistic or generate useful data. Return your results in any format.
# OBJECTIVE B (1): Write a two sentence comment explaining what your function does.
# OBJECTIVE C (1): Use at least one previous function from this test in your function.
# OBJECTIVE D (1): Use an import statement to include and use a library
def getStatistics(attractions):

    return ''



###############################
# MAIN FUNCTION
# NOTE: It is in your best interest to not modify values in this function.
# Input for the programming questions is test data. The supervisor will use 
# different values to grade your program.
###############################
def main():
    
    # Rides and Attractions
    attractions = [
        {'TYPE':'Roller Coaster','SUBTYPE':'Hyper Coaster','COST':8000000,'SIZE':20424,'CAPACITY':1851,'PROFIT':3702,'FUNRATING':9},
        {'TYPE':'Roller Coaster','SUBTYPE':'Giga Coaster','COST':12000000,'SIZE':24408,'CAPACITY':1440,'PROFIT':4320,'FUNRATING':10},
        {'TYPE':'Roller Coaster','SUBTYPE':'Wooden Coaster','COST':3000000,'SIZE':32024,'CAPACITY':1751,'PROFIT':3502,'FUNRATING':8},
        {'TYPE':'Roller Coaster','SUBTYPE':'Corkscrew Coaster','COST':4500000,'SIZE':8060,'CAPACITY':1920,'PROFIT':2880,'FUNRATING':7},
        {'TYPE':'Roller Coaster','SUBTYPE':'Wild Mouse Coaster','COST':2303000,'SIZE':5200,'CAPACITY':1263,'PROFIT':1894,'FUNRATING':7},
        {'TYPE':'Roller Coaster','SUBTYPE':'Steel Mini Coaster','COST':1303000,'SIZE':5612,'CAPACITY':2181,'PROFIT':2181,'FUNRATING':5},
        {'TYPE':'Roller Coaster','SUBTYPE':'Inverted Coaster','COST':9700000,'SIZE':17208,'CAPACITY':1705,'PROFIT':5115,'FUNRATING':10},
        {'TYPE':'Roller Coaster','SUBTYPE':'Bobsleigh Coaster','COST':5520000,'SIZE':19332,'CAPACITY':1384,'PROFIT':3600,'FUNRATING':8},
        {'TYPE':'Thrill Ride','SUBTYPE':'Scrambler','COST':300000,'SIZE':900,'CAPACITY':576,'PROFIT':576,'FUNRATING':6},
        {'TYPE':'Thrill Ride','SUBTYPE':'Pirate Ship','COST':450000,'SIZE':800,'CAPACITY':600,'PROFIT':900,'FUNRATING':7},
        {'TYPE':'Thrill Ride','SUBTYPE':'Go Karts','COST':760000,'SIZE':14000,'CAPACITY':450,'PROFIT':1800,'FUNRATING':7},
        {'TYPE':'Thrill Ride','SUBTYPE':'Launched Freefall','COST':2760000,'SIZE':10000,'CAPACITY':2880,'PROFIT':6623,'FUNRATING':8},
        {'TYPE':'Thrill Ride','SUBTYPE':'Top Spin','COST':1160000,'SIZE':2500,'CAPACITY':2400,'PROFIT':7200,'FUNRATING':8},
        {'TYPE':'Thrill Ride','SUBTYPE':'Enterprise','COST':900100,'SIZE':2500,'CAPACITY':1714,'PROFIT':3428,'FUNRATING':7},
        {'TYPE':'Thrill Ride','SUBTYPE':'Swinging Disc','COST':1900100,'SIZE':3600,'CAPACITY':1000,'PROFIT':2000,'FUNRATING':8},
        {'TYPE':'Thrill Ride','SUBTYPE':'Zipper','COST':700100,'SIZE':900,'CAPACITY':960,'PROFIT':1440,'FUNRATING':6},
        {'TYPE':'Thrill Ride','SUBTYPE':'Orbiter','COST':622200,'SIZE':625,'CAPACITY':654,'PROFIT':654,'FUNRATING':6},
        {'TYPE':'Thrill Ride','SUBTYPE':'Gravitron','COST':653200,'SIZE':625,'CAPACITY':782,'PROFIT':1173,'FUNRATING':6},
        {'TYPE':'Gentle Ride','SUBTYPE':'Carousel','COST':800000,'SIZE':2025,'CAPACITY':1200,'PROFIT':1200,'FUNRATING':3},
        {'TYPE':'Gentle Ride','SUBTYPE':'Ferris Wheel','COST':721000,'SIZE':450,'CAPACITY':800,'PROFIT':800,'FUNRATING':4},
        {'TYPE':'Gentle Ride','SUBTYPE':'Super Slide','COST':100100,'SIZE':1050,'CAPACITY':300,'PROFIT':300,'FUNRATING':2},
        {'TYPE':'Gentle Ride','SUBTYPE':'Bumper Cars','COST':203200,'SIZE':2500,'CAPACITY':1200,'PROFIT':1800,'FUNRATING':5},
        {'TYPE':'Gentle Ride','SUBTYPE':'Observation Tower','COST':510200,'SIZE':2500,'CAPACITY':360,'PROFIT':540,'FUNRATING':3},
        {'TYPE':'Gentle Ride','SUBTYPE':'Classic Cars','COST':97200,'SIZE':14000,'CAPACITY':640,'PROFIT':960,'FUNRATING':4},
        {'TYPE':'Gentle Ride','SUBTYPE':'Fun House','COST':97200,'SIZE':2020,'CAPACITY':200,'PROFIT':200,'FUNRATING':3},
        {'TYPE':'Gentle Ride','SUBTYPE':'Mini Golf','COST':56000,'SIZE':5625,'CAPACITY':144,'PROFIT':720,'FUNRATING':4},
        {'TYPE':'Gentle Ride','SUBTYPE':'Circus','COST':80000,'SIZE':5625,'CAPACITY':600,'PROFIT':2400,'FUNRATING':2},
        {'TYPE':'Gentle Ride','SUBTYPE':'Pedal Railway','COST':44000,'SIZE':560,'CAPACITY':750,'PROFIT':750,'FUNRATING':3},
        {'TYPE':'Gentle Ride','SUBTYPE':'Spinning Dragons','COST':25000,'SIZE':400,'CAPACITY':384,'PROFIT':384,'FUNRATING':4},
        {'TYPE':'Water Ride','SUBTYPE':'Log Flume','COST':100500,'SIZE':4024,'CAPACITY':837,'PROFIT':1674,'FUNRATING':6},
        {'TYPE':'Water Ride','SUBTYPE':'River Rapids','COST':203100,'SIZE':4300,'CAPACITY':585,'PROFIT':1170,'FUNRATING':7},
        {'TYPE':'Water Ride','SUBTYPE':'Dinghy Slide','COST':150200,'SIZE':4228,'CAPACITY':2142,'PROFIT':3214,'FUNRATING':7},
        {'TYPE':'Transport Ride','SUBTYPE':'Chairlift','COST':300233,'SIZE':17500,'CAPACITY':1028,'PROFIT':1028,'FUNRATING':4},
        {'TYPE':'Transport Ride','SUBTYPE':'Monorail','COST':410000,'SIZE':56016,'CAPACITY':600,'PROFIT':300,'FUNRATING':2},
        {'TYPE':'Shop','SUBTYPE':'Burger Bar','COST':14000,'SIZE':400,'CAPACITY':60,'PROFIT':240,'FUNRATING':1},
        {'TYPE':'Shop','SUBTYPE':'Drink Stand','COST':11000,'SIZE':400,'CAPACITY':480,'PROFIT':1440,'FUNRATING':1},
        {'TYPE':'Shop','SUBTYPE':'Ice Cream Stand','COST':18000,'SIZE':400,'CAPACITY':240,'PROFIT':480,'FUNRATING':1},
        {'TYPE':'Shop','SUBTYPE':'Fries Stand','COST':14000,'SIZE':400,'CAPACITY':240,'PROFIT':840,'FUNRATING':1},
        {'TYPE':'Shop','SUBTYPE':'Souvenir Shop','COST':20000,'SIZE':400,'CAPACITY':300,'PROFIT':3000,'FUNRATING':1},
        {'TYPE':'Shop','SUBTYPE':'Fried Chicken Stand','COST':15000,'SIZE':400,'CAPACITY':120,'PROFIT':840,'FUNRATING':1},
               
        {'TYPE':'Roller Coaster','SUBTYPE':'Mine Train Coaster','COST':3520000,'SIZE':32848,'CAPACITY':1244,'PROFIT':3733,'FUNRATING':8},
        {'TYPE':'Thrill Ride','SUBTYPE':'Tilt-A-Whirl','COST':70000,'SIZE':900,'CAPACITY':540,'PROFIT':810,'FUNRATING':6},
        {'TYPE':'Gentle Ride','SUBTYPE':'Paratrooper','COST':45000,'SIZE':1225,'CAPACITY':579,'PROFIT':579,'FUNRATING':5},
        {'TYPE':'Water Ride','SUBTYPE':'Bumper Boats','COST':56900,'SIZE':2500,'CAPACITY':480,'PROFIT':720,'FUNRATING':5},
        {'TYPE':'Transport Ride','SUBTYPE':'Steam Train','COST':282100,'SIZE':80000,'CAPACITY':1200,'PROFIT':1200,'FUNRATING':3},
        {'TYPE':'Shop','SUBTYPE':'Cookie Shop','COST':10000,'SIZE':400,'CAPACITY':120,'PROFIT':360,'FUNRATING':1},
        {'TYPE':'Shop','SUBTYPE':'Sandwich Shop','COST':11000,'SIZE':400,'CAPACITY':180,'PROFIT':1080,'FUNRATING':1},
        {'TYPE':'Shop','SUBTYPE':'Sunglass Shop','COST':10000,'SIZE':400,'CAPACITY':180,'PROFIT':1500,'FUNRATING':1}
    ]
    
    # Print Question Answer 74 Points Total
    print('Source Code - Division B/C - Theme Park - Park Builder')
    
    print('QUESTION 0 OBJECTIVE A (2): '+str(getThemeParkName())) # Bath High School 7 Wonderland
    print('QUESTION 1 OBJECTIVE A (2): '+str(getRideDescription('Roller Coaster','The Screaming Eagle', 10))) # Roller Coaster - The Screaming Eagle - 10
    print('QUESTION 2 OBJECTIVE A (2): '+str(getRidePrice(960, 1445))) # 1.51 or $1.51
    print('QUESTION 2 OBJECTIVE B (2): '+str(getRidePrice(960, 1445))) # $1.51
    print('QUESTION 3 OBJECTIVE A (3): '+str(isFit(200000, 123832)) + ', ' + str(isFit(123832, 200000))) # 76168, -1
    print('QUESTION 4 OBJECTIVE A (3): '+str(getAttractionsCount(attractions))) # 48
    print('QUESTION 5 OBJECTIVE A (4): '+str(getAttractionsCountOrganized(attractions))) # {'Roller Coaster': 9, 'Transport Ride': 3, 'Shop': 9, 'Water Ride': 4, 'Thrill Ride': 11, 'Gentle Ride': 12}
    print('QUESTION 6 OBJECTIVE A (4): '+str(getRideCost('Gravitron', attractions))) # 653200
    print('QUESTION 7 OBJECTIVE A (4): '+str(getFunPercentage(attractions))) #  0.5641025641025641 or 56%
    print('QUESTION 7 OBJECTIVE B (2): '+str(getFunPercentage(attractions))) # 56%
    print('QUESTION 8 OBJECTIVE A (5): '+str(getProfitCostRatio(attractions))) # ['Souvenir Shop', 'Sunglass Shop']
    print('QUESTION 9 OBJECTIVE A (5): '+str(getFunRating8Profit(attractions))) # 44796 
    print('QUESTION 10 OBJECTIVE A (5): '+str(getRemainingProfit(3600))) #  BASED ON CURRENT TIME 43200 to 60
    print('QUESTION 11 OBJECTIVE A (6): '+str(getMaxNumberOfRides(attractions, 12000000))) # 38
    print('QUESTION 12 OBJECTIVE A (6): '+str(getAvgFunCharacters(attractions))) # 52
    print('QUESTION 13 OBJECTIVE A (6): '+str(getThrillRidesRidden(attractions, 50.00))) # 27 
    print('QUESTION 14 OBJECTIVE A (6): '+str(getTheBestPark(attractions, 170424))) # ['Steam Train', 'Monorail', 'Mine Train Coaster', 'Paratrooper']
    print('QUESTION 14 OBJECTIVE B (2): '+str(getTheBestPark(attractions, 170424))) # ['Mine Train Coaster', 'Monorail', 'Paratrooper', 'Steam Train']

    print('Question 15 OBJECTIVE A (2): '+str(getStatistics(attractions)))
    print('QUESTION 15 OBJECTIVE B (1): '+'Check for comment explaining function.')
    print('QUESTION 15 OBJECTIVE C (1): '+'Check if previous function in file was called.')
    print('QUESTION 15 OBJECTIVE D (1): '+'Check if import statement was used.')
    
main()