from com.prestonsproductions.sourcecode.ThemePark2019 import ThemePark2019A as TP

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
    
    print('QUESTION 0 OBJECTIVE A (2): '+str(TP.getThemeParkName())) # Bath High School 7 Wonderland
    print('QUESTION 1 OBJECTIVE A (2): '+str(TP.getRideDescription('Roller Coaster','The Screaming Eagle', 10))) # Roller Coaster - The Screaming Eagle - 10
    print('QUESTION 2 OBJECTIVE A (2): '+str(TP.getRidePrice(960, 1445))) # 1.51 or $1.51
    print('QUESTION 2 OBJECTIVE B (2): '+str(TP.getRidePrice(960, 1445))) # $1.51
    print('QUESTION 3 OBJECTIVE A (3): '+str(TP.isFit(200000, 123832)) + ', ' + str(TP.isFit(123832, 200000))) # 76168, -1
    print('QUESTION 4 OBJECTIVE A (3): '+str(TP.getAttractionsCount(attractions))) # 48
    print('QUESTION 5 OBJECTIVE A (4): '+str(TP.getAttractionsCountOrganized(attractions))) # {'Roller Coaster': 9, 'Transport Ride': 3, 'Shop': 9, 'Water Ride': 4, 'Thrill Ride': 11, 'Gentle Ride': 12}
    print('QUESTION 6 OBJECTIVE A (4): '+str(TP.getRideCost('Gravitron', attractions))) # 653200
    print('QUESTION 7 OBJECTIVE A (4): '+str(TP.getFunPercentage(attractions))) #  0.5641025641025641 or 56%
    print('QUESTION 7 OBJECTIVE B (2): '+str(TP.getFunPercentage(attractions))) # 56%
    print('QUESTION 8 OBJECTIVE A (5): '+str(TP.getProfitCostRatio(attractions))) # ['Souvenir Shop', 'Sunglass Shop']
    print('QUESTION 9 OBJECTIVE A (5): '+str(TP.getFunRating8Profit(attractions))) # 44796 
    print('QUESTION 10 OBJECTIVE A (5): '+str(TP.getRemainingProfit(3600))) #  BASED ON CURRENT TIME 43200 to 60
    print('QUESTION 11 OBJECTIVE A (6): '+str(TP.getMaxNumberOfRides(attractions, 12000000))) # 38
    print('QUESTION 12 OBJECTIVE A (6): '+str(TP.getAvgFunCharacters(attractions))) # 52
    print('QUESTION 13 OBJECTIVE A (6): '+str(TP.getThrillRidesRidden(attractions, 50.00))) # 27 
    print('QUESTION 14 OBJECTIVE A (6): '+str(TP.getTheBestPark(attractions, 170424))) # ['Steam Train', 'Monorail', 'Mine Train Coaster', 'Paratrooper']
    print('QUESTION 14 OBJECTIVE B (2): '+str(TP.getTheBestPark(attractions, 170424))) # ['Mine Train Coaster', 'Monorail', 'Paratrooper', 'Steam Train']

    print('Question 15 OBJECTIVE A (2): '+str(TP.getStatistics(attractions)))
    print('QUESTION 15 OBJECTIVE B (1): '+'Check for comment explaining function.')
    print('QUESTION 15 OBJECTIVE C (1): '+'Check if previous function in file was called.')
    print('QUESTION 15 OBJECTIVE D (1): '+'Check if import statement was used.')
    
main()